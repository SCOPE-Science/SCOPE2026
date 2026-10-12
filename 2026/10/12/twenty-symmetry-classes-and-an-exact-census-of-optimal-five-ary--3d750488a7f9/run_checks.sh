#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 gens.py
python3 make_mapping.py
c++ -O2 -std=c++17 -o planes planes.cpp
./planes > plane_config.txt
c++ -O2 -std=c++17 -o factor factor.cpp
./factor
c++ -O2 -std=c++17 -o orbits orbits.cpp
./orbits
python3 groupconj.py
c++ -O2 -std=c++17 -o burnside burnside.cpp
./burnside
python3 verify_codes.py
python3 matchings.py
