#!/usr/bin/env python3
"""Exact Groebner-basis agreement on all orbit representatives of cubic cone sections."""
from sympy import symbols,groebner
from cone_census import MON,CHART,matrix_maps,apply_map,smooth
seen=set();maps=matrix_maps();reps=[]
for mask in range(1<<15,1<<16):
    if mask in seen:continue
    orb={apply_map(mask,x) for x in maps}
    assert not orb.intersection(seen)
    seen.update(orb);reps.append(mask)
assert len(seen)==32768 and len(reps)==752
y,w=symbols('y w')
n_smooth=0
for mask in reps:
    passes=True
    for ch in (0,1):
        f=sum(y**e*w**l for idx in range(16) if (mask>>idx)&1 for e,l in [CHART[idx][ch]])
        G=groebner([f,f.diff(y),f.diff(w)],y,w,modulus=2)
        passes &= (len(G.polys)==1 and G.polys[0].is_one)
    assert passes==smooth(mask),mask
    n_smooth+=passes
assert n_smooth==274
print(f'PASS: {len(reps)} orbits, {n_smooth} geometrically smooth; no Groebner/gcd disagreements.')
