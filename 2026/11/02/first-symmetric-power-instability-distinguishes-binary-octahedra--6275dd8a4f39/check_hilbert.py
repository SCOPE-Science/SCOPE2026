#!/usr/bin/env python3
"""Reproduce graded Hilbert-series and hypersurface-weight consistency checks."""
from fractions import Fraction

def coeffs(weights,rel,N=32):
    v=[0]*(N+1);v[0]=1
    for w in weights:
        for i in range(w,N+1):v[i]+=v[i-w]
    return [v[i]-(v[i-rel] if i>=rel else 0) for i in range(N+1)]

for weights,rel,first,order in [((4,6,9),18,4,48),((6,10,15),30,6,120)]:
    assert rel == 2*weights[2]
    if weights==(4,6,9):assert rel==3*weights[1]==weights[1]+3*weights[0]
    else:assert rel==3*weights[1]==5*weights[0]
    c=coeffs(weights,rel)
    assert c[0]==1 and c[first]==1 and all(c[i]==0 for i in range(1,first))
    # H(t) ~ rel / (product(weights) * (1-t)^2); degree halving of binary-polynomial invariants
    assert Fraction(rel,weights[0]*weights[1]*weights[2])==Fraction(4,order)
    assert all(n>=0 for n in c)
print('VERIFY_OK')
