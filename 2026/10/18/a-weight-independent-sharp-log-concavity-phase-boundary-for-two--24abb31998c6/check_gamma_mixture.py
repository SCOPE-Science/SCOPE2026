#!/usr/bin/env python3
"""Exact-rational reproducibility checks for common-rate two-Gamma shape mixtures.

The identities are elementary and the finite computations are NOT substitutes
for the all-parameter proof in RESULT.md.
"""
from fractions import Fraction as F
from math import factorial


def curvature_by_direct_differentiation(a, d, A, B, x):
    # f(x) = exp(-x) * x**(a-1) * (A+B*x**d), integer a,d.
    Q = A + B*x**d
    Qp = B*d*x**(d-1)
    Qpp = B*d*(d-1)*x**(d-2)
    return -F(a-1, 1)/x**2 + (Q*Qpp-Qp*Qp)/Q**2


def curvature_formula(a, d, A, B, x):
    t = B*x**d/A
    return (-F(a-1, 1) + F(d,1)*t*(d-1-t)/(1+t)**2)/x**2


def square_formula(a, d, A, B, x):
    t = B*x**d/A
    return (F((d-1)**2,4)-(a-1)-((d+1)*t-(d-1))**2/(4*(1+t)**2))/x**2


def phi(d,t):
    return F(d,1)*t*(d-1-t)/(1+t)**2


count=0
for a in range(1,10):
    for d in range(1,12):
        for A,B,x in ((F(1,2), F(1,120), F(2)),
                      (F(5,7), F(3,11), F(13,10)),
                      (F(1,17), F(99,13), F(9,7))):
            v=curvature_by_direct_differentiation(a,d,A,B,x)
            assert v==curvature_formula(a,d,A,B,x)
            assert v==square_formula(a,d,A,B,x)
            count+=2
        if d>1:
            tstar=F(d-1,d+1)
            assert phi(d,tstar)==F((d-1)**2,4)
            for t in (F(1,99), F(1,3), F(2), F(8)):
                assert phi(d,t)<=phi(d,tstar)
                count+=1

# Check explicit critical integer-shape cases using exact arithmetic.
# For shape (2,5), d=3, and t=1/2, the normalized curvature is exactly zero.
assert -F(1)+phi(3,F(1,2))==0
# For shape (2,6), d=4, and t=3/5, the normalized curvature is 5/4 > 0.
assert -F(1)+phi(4,F(3,5))==F(5,4)
# At alpha=1, beta=3, t=1/2 gives positive curvature.
assert phi(2,F(1,2))>0
# At alpha=1, beta=2, all t>0 yield negative curvature.
for i in range(1,60):
    assert phi(1,F(i,10))<0
    count+=1
print(f'PASS: {count} exact-rational checks and three sharp analytic examples')
