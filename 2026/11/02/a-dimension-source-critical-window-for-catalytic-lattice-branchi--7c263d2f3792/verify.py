#!/usr/bin/env python3
"""Finite and symbolic checks for the catalytic-walk resolvent expansion."""
from fractions import Fraction as F
from math import factorial

def moment(n): return factorial(n)
# Integral coefficients of exp(y^2/4d + (y^4/32-u*y/2)/d^2) against exp(-y).
a1=F(moment(2),4)
a2_base=F(moment(4),32)
a2_slope=-F(moment(1),2)
assert a1==F(1,2) and a2_base==F(3,4) and a2_slope==F(-1,2)
# Coefficient of beta_d G_{u/d} at d^{-2}, with beta_d=2d-1+s/d.
for s in range(-9,10):
  for u in range(0,15):
    coefficient=a2_base+a2_slope*u-F(1,2)*a1+F(s,2)
    assert coefficient==F(s+1-u,2)
print('PASS: 3 exact Laplace-moment coefficients and 285 exact critical-window identities')
try:
 import mpmath as mp
 mp.mp.dps=30
 for d in (20,50,100,200):
  # Use transformed Laplace integral; split to make tail control visible.
  f=lambda y: mp.exp(-y)*mp.besseli(0,y/d)**d
  g=mp.quad(f,[0,20,100,mp.inf])
  expn=1+mp.mpf(1)/(2*d)+mp.mpf(3)/(4*d*d)
  err=float(abs(g-expn))
  assert err<30/d**3,(d,err)
  print(f'd={d}: 2d*G0={mp.nstr(g,16)}, expansion={mp.nstr(expn,16)}, remainder={err:.3g}')
 print('PASS: 4 finite-dimension numerical comparisons')
except ImportError:
 print('mpmath unavailable; exact checks passed; numerical comparisons skipped')
