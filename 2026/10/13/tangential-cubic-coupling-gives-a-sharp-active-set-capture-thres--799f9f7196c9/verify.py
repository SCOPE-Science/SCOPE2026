#!/usr/bin/env python3
"""Reproduce finite symbolic and numerical checks for a two-dimensional SOS-convex Taylor model."""
from fractions import Fraction as F
from math import sqrt
import random
import sympy as s
from scipy.optimize import brentq

h, v, p, q, c, t = s.symbols('h v p q c t', real=True)
psi_hessian=s.Matrix([[1+12*t*h*h+4*t*v*v, 8*t*h*v],
                       [8*t*h*v, 1+6*c*v+4*t*h*h+12*t*v*v]])
T=3*c*c/4
qform=s.factor((s.Matrix([p,q]).T*psi_hessian*s.Matrix([p,q]))[0].subs(t,T))
expected=p*p+q*q+6*c*v*q*q+3*c*c*(h*h+v*v)*(p*p+q*q)+6*c*c*(h*p+v*q)**2
assert s.expand(qform-expected)==0
assert s.factor((1-3*q**4+2*q**6)-(1-q*q)**2*(1+2*q*q))==0
assert s.factor((1+6*c*v+12*t*v*v).subs(t,T)-(1+3*c*v)**2)==0

# Two-dimensional Hessian certificate: normalize (p,q) to unit length; completing
# the square in (h,v) gives (1-q^2)^2(1+2q^2), strictly nonnegative.
for numerator in range(-100,101):
    beta=numerator/100
    alpha=sqrt(max(0,1-beta*beta))
    cc=1.7
    ww=[alpha,beta]
    import numpy as np
    M=3*cc*cc*np.eye(2)+6*cc*cc*np.outer(ww,ww)
    linear=np.array([0,6*cc*beta*beta])
    z=-np.linalg.solve(M,linear)/2
    lower=1+linear@z+z@M@z
    exact=(1-beta**2)**2*(1+2*beta**2)
    assert abs(lower-exact)<1e-11

# Exact rational Hessian determinants and 1D model derivatives.
for cc in [F(1,2),F(1),F(2)]:
    tt=F(3,4)*cc**2
    for hh in [F(-2),F(-1,3),F(0),F(1,7),F(1),F(3)]:
      for vv in [F(-2),F(-1,3),F(0),F(1,7),F(1),F(3)]:
        aa=1+12*tt*hh**2+4*tt*vv**2
        bb=1+6*cc*vv+4*tt*hh**2+12*tt*vv**2
        dd=8*tt*hh*vv
        assert aa>0 and aa*bb-dd**2>=0

# The exact boundary derivative is lambda-3*c^2*x^3.
u,x,lam=s.symbols('u x lam', real=True,nonnegative=True)
obj=lam*u+s.Rational(1,2)*u**2+T*(u-x)**4
assert s.factor(s.diff(obj,u).subs(u,0)-(lam-3*c*c*x**3))==0
assert s.factor(s.diff(obj,u,2)-(1+12*T*(u-x)**2))==0

# Interior solution for lambda below threshold and exact cubic limit.
for cc in [0.5,1.,2.]:
  tt=.75*cc*cc
  for xx in [.01,.1,.6,1.5]:
    cutoff=4*tt*xx**3
    for l in [0., cutoff*.25, cutoff*.75, cutoff, cutoff*2]:
      if l>=cutoff: uu=0.
      else: uu=brentq(lambda z:l+z+4*tt*(z-xx)**3,0,xx,xtol=1e-15)
      assert 0<=uu<xx or (l>=cutoff and uu==0.)
      if l<cutoff: assert abs(l+uu+4*tt*(uu-xx)**3)<1e-10
    z=xx
    for step in range(5):
      if z**3 < 1e-11: break
      nz=brentq(lambda w:w+4*tt*(w-z)**3,0,z,xtol=1e-16)
      assert 0<nz<z
      ratio=nz/z**3
      assert 0<ratio<4*tt+1e-10
      z=nz
      if z<1e-6: break
print('VERIFY_OK: symbolic Hessian, exact-rational PSD, 201 analytic minimizations, multiplier thresholds, cubic iterations')
