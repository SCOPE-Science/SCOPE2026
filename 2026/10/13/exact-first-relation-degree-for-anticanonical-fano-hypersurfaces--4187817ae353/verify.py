#!/usr/bin/env python3
from fractions import Fraction
from math import ceil

def M_value(n,a):
    assert len(n)==len(a) and n
    den=[ni+1-ai for ni,ai in zip(n,a)]
    assert all(d>0 for d in den)
    ratios=[Fraction(ai,d) for ai,d in zip(a,den)]
    r=max(ratios)
    return (r.numerator+r.denominator-1)//r.denominator

cases=[
    ((2,), (1,), 1, 2),
    ((3,), (3,), 3, 3),
    ((4,), (4,), 4, 4),
    ((2,2),(1,1),1,2),
    ((3,4),(2,4),4,4),
    ((5,3),(3,2),1,2),
]
for n,a,m,t in cases:
    got=M_value(n,a)
    assert got==m, (n,a,got,m)
    assert max(2,got)==t

# Exact ceiling identity against direct rational comparison over a broad finite grid.
checked=0
for n1 in range(1,10):
  for n2 in range(1,10):
    for a1 in range(0,n1+1):
      for a2 in range(0,n2+1):
        if a1==a2==0:
            continue
        m=M_value((n1,n2),(a1,a2))
        for k in range(m):
            assert not (Fraction(a1,n1+1-a1)<=k and Fraction(a2,n2+1-a2)<=k)
        assert Fraction(a1,n1+1-a1)<=m and Fraction(a2,n2+1-a2)<=m
        checked+=1
print(f"threshold_cases={checked}")
print("universal_proof=written_algebraic_argument")
print("VERIFY_OK")
