#!/usr/bin/env python3
"""Finite diagnostic checks for the positive constrained boundary Hessian.

The all-radius stationary-phase theorem requires the analytic proof and is not
certified by these finite calculations.
"""
import math
import sympy as s

b=s.symbols('b',positive=True,real=True)
H=(1+s.coth(b))*(s.coth(b)-1)
assert s.simplify(H-1/s.sinh(b)**2)==0
checks=1
for n in (2,3,4,7):
    for radius in (0.1,0.4,1.0,3.0,8.0):
        bb=radius/math.sqrt(2)
        c=math.cosh(bb)/math.sinh(bb)
        eig=[2/(1-math.exp(-2*bb)),2/math.expm1(2*bb)]+[1/bb]*(2*n-3)
        assert len(eig)==2*n-1
        assert all(x>0 for x in eig)
        determinant=math.prod(eig)
        exact=(1/math.sinh(bb)**2)*(bb**(-(2*n-3)))
        assert math.isclose(determinant,exact,rel_tol=2e-12)
        coef=math.sqrt(2)*(2*math.pi)**(n-0.5)*(bb**(n-1.5))*math.sinh(bb)
        assert coef>0 and math.isfinite(coef)
        checks+=4
for n in (2,3,4,5,8):
    radius=1e-5
    bb=radius/math.sqrt(2)
    coef=math.sqrt(2)*(2*math.pi)**(n-.5)*(bb**(n-1.5))*math.sinh(bb)
    euclid=(2*math.pi)**(n-.5)*(2**(.75-n/2))*radius**(n-.5)
    assert math.isclose(coef/euclid,1.0,rel_tol=1e-10)
    checks+=1
print('PASS',checks,'finite algebraic/positivity assertions')
