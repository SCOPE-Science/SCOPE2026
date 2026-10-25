"""Supplementary algebraic checks for the inellipse stochastic-dominance theorem.
Run: python CHECK.py. Requires SymPy for symbolic identities. These checks do not prove global novelty.
"""
import sympy as S
x,c,h,q,r,k=S.symbols('x c h q r k',real=True)
f=lambda z:(1-z*z)*(1+q*z)
odd=S.expand((f(c+h)-f(c-h))/(2*h))
assert S.factor(odd-(q-2*c-3*q*c*c-q*h*h))==0
avg=S.expand((f(c+h)+f(c-h))/2)
assert S.factor(avg-(f(c)-h*h*(1+3*q*c)))==0
assert S.factor((1-h*h)*f(c)-avg-h*h*(c*c+2*q*c+q*c**3))==0
# Direct trapezoid contacts for center (c,1/2), top half-base r, bottom 1.
k=1-r
q11=r+c*c
q12=-(1+r)*c/(2*k)
det=S.factor(q11/S.Integer(4)-q12**2)
assert S.simplify(det-r/S.Integer(4)*(1-4*c*c/k**2))==0
# A handful of exact rational level inequalities; the theorem is analytic.
for p in [S.Rational(1,10),S.Rational(1,3),S.Rational(3,5)]:
    import numpy as np
    xx=np.linspace(-1,1,20001)
    y=(1-xx**2)*(1+float(p)*xx)
    y/=max(y)
    for u in [0.1,0.25,0.5,0.75,0.9]:
        assert np.mean(y>u*u)<(1-u*u)**.5+0.0002
print('Algebraic identities and finite diagnostic comparisons passed')
