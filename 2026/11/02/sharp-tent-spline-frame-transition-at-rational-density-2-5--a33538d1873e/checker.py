#!/usr/bin/env python3
"""Symbolic verification of the exact two determinant identities in RESULT.md."""
from sympy import symbols, Rational, expand
u,eps,z=symbols('u eps z', real=True)
h=Rational(2,5); b=2+eps;v=u+h
Eleft=b-u+(eps+u)*z**2+(eps-u)/z**2
Oleft=(1+eps-u)/z+(1+eps+u)*z
Ecentral=b-v+(eps+v)*z**2
Ocentral=(1+eps-v)/z+(1+eps+v)*z
P=expand(z**3*(Eleft*Ocentral-Ecentral*Oleft))
assert expand(P-(-h*z**2*(z**2-1)**2+(eps-u)*((1+eps-v)+(1+eps+v)*z**2)))==0
Esecondleft=Ecentral+(eps-v)/z**2
assert expand(z**3*(Eleft*Ocentral-Esecondleft*Oleft)-h*(-z**6+2*z**4+2*eps*z**2+1))==0
# At t in [eps,1-eps], z=-1 makes even and odd sum equal.
t=symbols('t', real=True)
assert expand((b-t+eps+t)-((1+eps-t)+(1+eps+t)))==0
print('PASS: exact determinant identities and central zero-row identity')
