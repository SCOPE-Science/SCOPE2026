#!/usr/bin/env python3
"""Finite block check for a sharp symplectic multiplier distortion formula.
This is numerical verification of an illustration, not an infinite-dimensional proof.
"""
from math import isclose, sqrt

p=[1.,2.,.125,4.]
q=[1.,.5,1.,1.]
a=[1.,.7,0.,.5]
b=[0.,.3,1.,.25]
s=[(u/v)**.25 for u,v in zip(p,q)]
R=max(max(u/v,v/u) for u,v in zip(p,q))
for i,(u,v,aa,bb,scale) in enumerate(zip(p,q,a,b,s)):
    assert isclose(scale*(1/scale),1.,abs_tol=1e-13)
    # Symplectic identity for a single position-momentum fiber.
    dA=aa*sqrt(u*v)
    dB=bb*sqrt(u*v)
    for weight,d in ((aa,dA),(bb,dB)):
        assert isclose(scale**2*d,weight*u,abs_tol=1e-13)
        assert isclose((scale**-2)*d,weight*v,abs_tol=1e-13)
    print('fiber',i,'stretch',round(scale,9),'inverse_stretch',round(1/scale,9))
condition=max(max(t,1/t) for t in s)**2
assert isclose(condition,sqrt(R),rel_tol=1e-13)
print('R',R,'sharp_condition_number',condition)
print('FINITE_CHECK_OK')
