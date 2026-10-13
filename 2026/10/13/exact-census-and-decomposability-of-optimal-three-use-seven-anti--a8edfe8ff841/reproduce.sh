#!/bin/sh
set -eu
cd "$(dirname "$0")"
c++ -std=c++17 -O2 -Wall -Wextra -o count_ordered count_ordered.cpp
c++ -std=c++17 -O2 -Wall -Wextra -o count_coloring count_coloring.cpp
./count_ordered
./count_coloring
python3 verify_small.py
printf '%s\n' 'VERIFY_OK root8=38259704 root9=0 N3=1640384809 decomposable=35329 indecomposable=1640349480'
