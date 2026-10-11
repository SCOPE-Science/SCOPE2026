#!/usr/bin/env python3
"""Exact algebraic sanity checks for a coupled-radius angular system."""
import sympy as S
s,u,v,q=S.symbols('s u v q',real=True)
base=2*s*(1-s)*u/(s*u-v)
factor=2*u/(s*u-v)
assert S.simplify(S.diff(factor,s)+2*u*u/(s*u-v)**2)==0
A=-2*u/(u-v)
series=S.series(base.subs(s,1+q),q,0,3).removeO().expand()
assert S.simplify(series.coeff(q,1)-A)==0
assert S.simplify(series.coeff(q,2)-A-A*A/2)==0
# A neutral angular profile, U=2-sqrt(5)+cos(theta), V=2.
a=2-S.sqrt(5)
assert S.simplify((2-a)**2-1-4)==0
assert S.simplify(2*(a+1)-2)<0
# An inner-cycle example, U=-1/10+3*cos(theta)/2, V=2.
a2=-S.Rational(1,10)
b=S.Rational(3,2)
assert S.simplify(S.Rational(11,10)*(a2+b)-2)<0
assert S.simplify((2-a2)**2-b*b-4)<0
print('CHECK_OK')
