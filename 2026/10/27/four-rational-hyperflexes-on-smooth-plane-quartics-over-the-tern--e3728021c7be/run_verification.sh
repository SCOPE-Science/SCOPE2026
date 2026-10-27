#!/bin/sh
set -eu
python hyperflex_prep.py
python hyperflex_orbit_prep.py
g++ -O3 -std=c++17 hyperflex_enum.cpp -o hyperflex_enum
g++ -O3 -std=c++17 hyperflex_orbits.cpp -o hyperflex_orbits
./hyperflex_enum > enumeration.txt 2> enumeration.err
python hyperflex_filter.py > rational_smoothness.txt 2>&1
python independent_rational_smoothness.py > independent_rational_smoothness.txt
./hyperflex_orbits > orbits_summary.txt 2> orbits.err
python hyperflex_smooth.py > geometric_smoothness.txt
python hyperflex_reps.py > representatives.txt
python contact_table.py > contacts_summary.txt
python - <<'PY'
import json
x=json.load(open('hyperflex_orbits.json'))
assert len(x)==18 and sum(o['size'] for o in x)==52884
assert {o['rep']:o['size'] for o in x if o['rep'] in {83262,78741,78754}}=={83262:1872,78741:234,78754:234}
f=open('geometric_smoothness.txt').read().splitlines()
assert len([s for s in f if 'SMOOTH' in s and 'SINGULAR' not in s])==3
assert {int(s.split()[1]) for s in f if 'SMOOTH' in s and 'SINGULAR' not in s}=={83262,78741,78754}
print('ALL verification assertions satisfied')
PY
