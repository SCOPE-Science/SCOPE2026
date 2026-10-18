#!/bin/sh
set -eu
cd "$(dirname "$0")"
python verify_geometry.py smooth_masks.txt
g++ -std=c++17 -O2 -Wall -Wextra -o verify_nets verify_nets.cpp
./verify_nets smooth_masks.txt
