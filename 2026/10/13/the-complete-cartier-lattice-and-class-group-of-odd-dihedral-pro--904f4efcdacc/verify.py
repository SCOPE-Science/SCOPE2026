#!/usr/bin/env python3
"""Finite stabilizer-character sanity checks for odd dihedral surface quotients."""
from itertools import product

def conditions(n, a, b, eps):
    h = (n + 1) // 2
    corner = all((u*h*a+v*b) % n == 0 for u,v in product((-1,1),repeat=2))
    reflection = all(((-1 if (u*a+v*b+eps)%2 else 1)==1) for u,v in product((0,1),repeat=2))
    return corner and reflection

for n in (5,7,9,11,15):
    for a,b,eps in product(range(2*n),range(2*n),range(2)):
        expected = a==0 and b==0 and eps==0
        assert conditions(n,a,b,eps)==expected,(n,a,b,eps)
    assert conditions(n,2*n,0,0) and conditions(n,0,2*n,0)
print("VERIFY_OK")
