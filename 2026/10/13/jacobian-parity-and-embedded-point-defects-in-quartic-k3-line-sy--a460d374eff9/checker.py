#!/usr/bin/env python3
"""Finite smoke test of the stated Jacobian formulas; not an infinite certificate."""
from sympy import symbols, diff, expand
u,v=symbols("u v")
for r in range(1,13):
    f=u**r*v
    assert expand(diff(f,u)-r*u**(r-1)*v)==0
    assert expand(diff(f,v)-u**r)==0
    assert expand(diff(u**r,u)-r*u**(r-1))==0
for m in range(2,22):
    for k in range(1,2*m):
        a=k//2; r=m-a
        assert r>=1 and k-2*a in (0,1)
        assert k-2*(m-(r-1))<0
        assert (4*k*k+2*k*a-2*a*a)%2==0
print('QUARTIC_LINE_JACOBIAN_SANITY_OK')
