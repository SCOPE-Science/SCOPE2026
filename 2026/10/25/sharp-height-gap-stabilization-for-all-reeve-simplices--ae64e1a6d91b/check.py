"""Exact integer verification of the projected-height theorem for Reeve simplices.

Finite tests supplement, rather than replace, the all-parameter barycentric proof.
Run with Python 3: python check.py
"""
from itertools import product
from math import gcd

def predicted(d, m, n):
    heights = set(range(0, m*n+1, m))
    for s in range(1, m):
        qmax = n-d+1 + ((d-2)*s)//m
        heights.update(m*q+s for q in range(max(0, qmax+1)))
    return heights

def enumerated(d, m, n):
    observed = set()
    for x in product(range(n+1), repeat=d-1):
        tot = sum(x)
        for z in range(m*n+1):
            if all(m*xi >= z for xi in x) and m*tot-(d-2)*z <= m*n:
                observed.add(z)
    return observed

def holes(d, m):
    return {m*j-s for s in range(1, m)
            for j in range(1, d-1-((d-2)*s)//m)}

def bound(d, m):
    return d-1-(d-2)//m

finite = 0
for d in (3,4,5):
    for m in range(2,7):
        for n in range(0,5):
            A=enumerated(d,m,n)
            B=predicted(d,m,n)
            assert A == B, (d,m,n,A^B)
            finite += 1
structure = 0
for d in range(3,15):
    for m in range(2,25):
        start = bound(d,m)
        assert start >= 2
        assert min(((d-2)*s)//m for s in range(1,m)) == (d-2)//m
        H=holes(d,m)
        expected=((d-1)*(m-1)-gcd(d-2,m)+1)//2
        assert len(H)==expected, (d,m,len(H),expected)
        assert all(z>0 for z in H)
        for n in range(start,start+4):
            p=predicted(d,m,n)
            assert set(range(m*n+1))-p == {m*n-z for z in H}
        # Precisely one residue s=1 still absent at the preceding dilation.
        assert 1 not in predicted(d,m,start-1)
        assert 1 in predicted(d,m,start)
        structure += 1
print('REEVE_RANGE_OK exhaustive_instances=', finite,
      'symbolic_template_parameter_pairs=', structure)
