#!/usr/bin/env python3
"""Exact symbolic identities and optional rational diagnostic orbits.
Scientific content only; requires Python 3 and SymPy.
"""
import sympy as S
x,t,k,L = S.symbols('x t k L', positive=True)
assert S.factor((k*x**2*(1-x)-L).subs(k,1/(L*(1-L))) + (x-L)*(x**2+(L-1)*x-L*(1-L))/(L*(1-L))) == 0
P=t**3+t**2+t+1
X=(t*t+t+1)/P
Y=t*X
K=P**2/(t*t*(t*t+t+1))
assert S.factor(K*X**2*(1-X)-Y)==0
assert S.factor(K*Y**2*(1-Y)-X)==0
assert S.factor(3*P**2-16*t*t*(t*t+t+1))==(t-1)**2*(3*t**4+12*t**3+14*t*t+12*t+3)
for kval in (S.Rational(41,10),S.Rational(9,2),S.Integer(5),S.Rational(16,3)):
    ell = (1-S.sqrt(1-4/kval))/2
    upper = 1-ell
    right=(1-ell+S.sqrt((1-ell)*(1+3*ell)))/2
    F=lambda a: kval*a*a*(1-a)
    assert abs(float(F(ell)-ell))<1e-13
    assert abs(float(F(upper)-upper))<1e-13
    assert abs(float(F(right)-ell))<1e-13
    assert float(right)>0.8
    assert float(4*kval/27)<0.8
    for n in range(1,100):
        z=S.Rational(n,100)
        v=float(z)
        if abs(v-float(ell))<1e-8 or abs(v-float(right))<1e-8:continue
        # Numerical orbit avoids enormous exact rational iterates.
        z=float(S.Rational(n,100))
        for _ in range(1000):z=float(kval)*z*z*(1-z)
        if v<float(ell) or v>float(right): assert z<0.002
        else: assert abs(z-float(upper))<0.004
print('PASS: exact identities, threshold factorization, and four finite diagnostic grids')
