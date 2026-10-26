#!/usr/bin/env python3
"""Reproducible symbolic and numerical checks for an exponential SDE step."""
from fractions import Fraction
import math
import sympy as sp
import mpmath as mp

x, sigma, h, p = sp.symbols('x sigma h p', positive=True)
f = sigma*x/(1+x)
g = sigma*x*x/(1+x)
q = sp.cancel(sp.diff(f,x)*g)
assert sp.simplify(q - sigma**2*x*x/(1+x)**3)==0
assert sp.factor(sp.diff(q,x)) == -sigma**2*x*(x-2)/(x+1)**4
assert sp.simplify(q.subs(x,2)-4*sigma**2/27)==0
assert sp.simplify(sp.diff(q,x,2).subs(x,2)+2*sigma**2/81)==0
hc = sp.Rational(27,4)/(p*sigma**2)
delta=sp.factor(1-p*hc*q)
assert sp.simplify(delta.subs(x,2))==0
assert sp.simplify(sp.diff(delta,x).subs(x,2))==0
assert sp.simplify(sp.diff(delta,x,2).subs(x,2)-sp.Rational(1,6))==0
assert sp.simplify(f**2/q-(x+1))==0
xmin=x*sp.exp(-(1+x)/2)
assert sp.simplify(sp.diff(xmin,x).subs(x,2))==0
assert sp.simplify(sp.diff(xmin,x,2).subs(x,2))<0
# Exact bound x exp(-(x+1)/2) <= 2e^-3/2 follows sign of derivative.
assert sp.simplify(sp.factor(sp.diff(xmin,x)/sp.exp(-(1+x)/2))-(2-x)/2)==0

mp.mp.dps=50
count=0
for x0 in (mp.mpf('0.35'), mp.mpf('1'), mp.mpf('2'), mp.mpf('5')):
  for sig in (mp.mpf('0.7'), mp.mpf('2')):
    for pp in (1,2,3):
      qq=sig**2*x0**2/(1+x0)**3
      ff=sig*x0/(1+x0)
      for rel in (mp.mpf('0.15'),mp.mpf('0.6')):
        hh=rel/(pp*qq)
        # Integrate the full Gaussian density, not the Gaussian MGF identity.
        A=pp*ff*mp.sqrt(hh)
        B=pp*qq*hh/2
        integ=mp.quad(lambda z: mp.exp(A*z+B*z*z-z*z/2)/mp.sqrt(2*mp.pi), [-mp.inf,0,mp.inf])
        predicted=1/mp.sqrt(1-pp*qq*hh)*mp.exp(A*A/(2*(1-pp*qq*hh)))
        assert abs(integ/predicted-1)<mp.mpf('1e-36'), (x0,sig,pp,rel)
        count+=1
# Exact-rational global inequality witnesses around critical point.
for xx in [Fraction(j,8) for j in range(1,129)]:
  rr=xx**2/(1+xx)**3
  assert rr<=Fraction(4,27)
  count+=1
# Critical coefficient of delta is exactly 1/12; see symbolic assertions.
print('verification passed: symbolic identities; %d numeric/exact-rational checks' % count)
