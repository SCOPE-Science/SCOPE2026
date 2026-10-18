#!/usr/bin/env python3
"""Exact rational checks for the squarefree reciprocal-cube band classification.

Requires Python 3 standard library. Infinite prime coverage is proved in RESULT.md
using Nagura's theorem, not by this finite checker.
"""
from fractions import Fraction as Q
from itertools import combinations

SMALL=(2,3,5,7)
FINITE={
    11:(13,17,19),
    13:(17,19,23,29),
    17:(19,23),
    19:(23,29,31),
    23:(29,31,37),
}

def prime(n):
    return n>=2 and all(n%d for d in range(2,int(n**.5)+1))

for p,other in FINITE.items():
    assert prime(p) and all(prime(q) and q>p for q in other)
    rhs=Q(1)
    for q in other:
        rhs*=1+Q(1,q**3)
    assert 1+Q(1,p**3)<rhs, (p,other)

U=Q(1,1331)+Q(1,484)
for p,other in ((7,()),(5,(7,)),(3,(5,7)),(2,(3,5,7))):
    assert Q(1,p**3+1)>sum((Q(1,q**3) for q in other),Q(0))+U

assert Q(125,91)>1+Q(1,29**3)

bands=[]
for mask in range(16):
    included=tuple(p for i,p in enumerate(SMALL) if mask & (1<<i))
    a=Q(1)
    b=Q(1)
    for p in SMALL:
        if p in included:
            a*=1+Q(1,p**3)
            b*=Q(1,p+1)
        else:
            b*=Q(p,p+1)
    bands.append((included,a,b))
assert len(bands)==16
assert len({a for _,a,_ in bands})==16
assert sum((b for _,_,b in bands),Q(0))==1
assert all(b>0 for _,_,b in bands)
print('VERIFY_OK: 16 intervals, 16 conditional masses, finite inequalities exact')
