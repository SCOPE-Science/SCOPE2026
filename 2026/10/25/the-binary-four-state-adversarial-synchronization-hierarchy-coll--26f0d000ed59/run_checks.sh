#!/bin/sh
# Reproduce complete game and symmetry counts using standard Python and a C++17 compiler.
set -eu
c++ -O2 -std=c++17 verify_alicefirst.cpp -o ./verify_alicefirst
./verify_alicefirst
python3 verify_bobfirst.py
python3 verify_orbits.py
