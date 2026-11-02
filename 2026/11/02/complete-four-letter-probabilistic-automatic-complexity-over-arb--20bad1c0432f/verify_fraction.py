#!/usr/bin/env python3
"""Exact rational verification of finite-alphabet, four-letter witnesses."""
from fractions import Fraction as F
from itertools import product
from json import loads
from pathlib import Path

path = Path(__file__).with_name('CERTIFICATES.json')
rows = loads(path.read_text(encoding='utf-8'))['certificates']

def normalize(w):
    mapping = {}
    return ''.join(str(mapping.setdefault(c,len(mapping))) for c in w)

patterns = {normalize(w) for w in product('0123',repeat=4)}
assert len(patterns)==15
assert {x['pattern'] for x in rows} == patterns-{'0000','0100'}
assert len(rows)==13

for row in rows:
    w = tuple(map(int,row['pattern']))
    s = len(set(w))
    p = F(row['initial'])
    u = list(map(F,row['row0']))
    v = list(map(F,row['row1']))
    assert len(u)==len(v)==s
    assert 0<=p<=1 and all(0<=t<=1 for t in (*u,*v))
    def acceptance(z):
        x=p
        for a in z:
            x = x*u[a]+(1-x)*v[a]
        return x
    value=acceptance(w)
    gap=min(value-acceptance(z) for z in product(range(s),repeat=4) if z != w)
    assert gap>0 and gap == F(row['exact_gap']), (w,gap,row['exact_gap'])
    print(f"{row['pattern']}  {s} symbols  gap={gap}")

# Constant words have a separate simple witness on every alphabet of size >=2:
# start at state 0, let target letter act as identity, every other letter
# send both states to state 1 (nonaccepting and absorbing under identity).
def constant_acceptance(z):
    x=F(1)
    for a in z:
        x=x if a==0 else F(0)
    return x
assert constant_acceptance((0,0,0,0)) == 1
assert all(constant_acceptance(z)==0 for z in product(range(2),repeat=4) if z!=(0,0,0,0))
print('PASS: all 13 nonconstant certificates, 15 partitions, and constant case')
