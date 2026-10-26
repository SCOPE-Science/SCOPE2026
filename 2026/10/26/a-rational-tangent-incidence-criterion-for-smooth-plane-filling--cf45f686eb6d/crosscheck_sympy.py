#!/usr/bin/env python3
"""Independent symbolic verification of the eighteen algebraic-closure tests.
Requires SymPy (tested using its GF(2) Groebner implementation).
"""
from pathlib import Path
import sympy as sp
X,Y,Z=sp.symbols('X Y Z')
mons=[(a,b,5-a-b) for a in range(6) for b in range(6-a)]
reps=[]
for line in Path(__file__).with_name('orbit_table.tsv').read_text().splitlines():
    mask,size,prof,concur,good=line.split('\t')
    reps.append((int(mask),int(size),prof,int(concur),bool(int(good))))
assert len(reps)==18
for mask,size,prof,concur,good in reps:
    f=sum(X**a*Y**b*Z**c for j,(a,b,c) in enumerate(mons) if mask>>j&1)
    smooth=True
    for chart,free in [(X,(Y,Z)),(Y,(X,Z)),(Z,(X,Y))]:
        gb=sp.groebner([sp.diff(f,v).subs(chart,1) for v in (X,Y,Z)],*free,modulus=2)
        if not (len(gb.polys)==1 and gb.polys[0].total_degree()==0):smooth=False
    assert smooth==good,(mask,smooth,good)
print('INDEPENDENT_GROEBNER_CROSSCHECK_18_ORBITS_OK')
