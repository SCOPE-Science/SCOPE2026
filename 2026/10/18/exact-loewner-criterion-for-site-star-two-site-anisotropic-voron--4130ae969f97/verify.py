#!/usr/bin/env python3
"""Exact rational regression checks for the global quadratic two-site cell criterion.

A finite computation is not a proof of the universal equivalence; see RESULT.md.
"""
from fractions import Fraction as F

def q(x,y,A):
    return sum(x[i]*A[i][j]*y[j] for i in range(len(x)) for j in range(len(x)))

def g(y,v,A,B):
    x=tuple(y[i]-v[i] for i in range(len(v)))
    return q(y,y,A)-q(x,x,B)

v=(F(1),F(0)); A=((F(2),F(0)),(F(0),F(1)))
B=((F(1),F(0)),(F(0),F(2)))
u=(F(10),F(11))
for t,expected in ((F(0),F(-1)),(F(1,2),F(15,4)),(F(1),F(-2))):
    value=g(tuple(t*z for z in u),v,A,B)
    assert value==expected,(t,value,expected)

# An exact, non-exhaustive regression for a PSD difference.
A2=((F(3),F(1)),(F(1),F(2)))
B2=((F(2),F(1)),(F(1),F(1)))
assert all(q((F(i),F(j)),(F(i),F(j)),((A2[0][0]-B2[0][0],F(0)),(F(0),A2[1][1]-B2[1][1]))) >= 0 for i in range(-3,4) for j in range(-3,4))
# A convex quadratic is convex on any chord; test exact rational sublevels.
points=[(F(i,2),F(j,2)) for i in range(-6,7) for j in range(-6,7)]
inside=[x for x in points if g(x,v,A2,B2)<=0]
for x in inside:
    for y in inside:
        for t in (F(0),F(1,3),F(1,2),F(2,3),F(1)):
            z=tuple(t*a+(1-t)*b for a,b in zip(x,y))
            assert g(z,v,A2,B2)<=0,(x,y,t)
print('TWO_SITE_ANISOTROPIC_STAR_CRITERION_RATIONAL_CHECKS_OK')
