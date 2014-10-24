# Copyright 2014 Cloudbase Solutions Srl
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

VSWITCH_PRIVATE = "private"
VSWITCH_INTERNAL = "internal"
VSWITCH_EXTERNAL = "external"

UDP = "UDP"
TCP = "TCP"


class BaseDriver(object):
    def create_vm(self, vm_name, vm_path, max_disk_size, max_memory_mb,
              min_memory_mb, vcpus_num, vmnic_info, vfd_path):
        raise NotImplementedError()

    def vswitch_exists(self, vswitch_name):
        raise NotImplementedError()

    def create_vswitch(self, vswitch_name, vswitch_type=VSWITCH_PRIVATE):
        raise NotImplementedError()

    def add_vswitch_host_firewall_rule(self, vswitch_name, rule_name,
                                       local_ports, protocol=TCP, allow=True,
                                       description=""):
        raise NotImplementedError()