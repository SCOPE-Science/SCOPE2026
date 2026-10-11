"""Reproducibility checks for the complex Janowski symmetric Toeplitz bound.

Only algebraic symbolic identities are certified by this script. Finite numerical
checks are supplementary and do not establish universal inequalities.
"""
from __future__ import annotations
import cmath
import math
import random
import sympy as sp

A, B, t, R, eta = sp.symbols('A B t R eta')
d = A-B
k = d*(A-3*B)/8
m = d*(3*A-B)/8
ell = d/4
S = d*d/2
K = k*m
p1 = d*(A-3*B)
p2 = d*(3*A-B)

# Exact two-coefficient Janowski reconstruction, using t = u^2,
# R = |u|^2 and eta in the unit disk.
a3_sq = d*d*t/4
a5 = k*t + ell*(1-R)*eta
D_from_coefficients = (1-a5)*(1+a5-2*a3_sq)
D_factor = (1-k*t-ell*(1-R)*eta)*(1-m*t+ell*(1-R)*eta)
D_poly = 1-S*t+K*t*t + ell*(m-k)*t*(1-R)*eta-ell**2*(1-R)**2*eta**2
assert sp.simplify(D_from_coefficients-D_factor) == 0
assert sp.simplify(D_from_coefficients-D_poly) == 0
assert sp.simplify(k+m-S) == 0
assert sp.simplify(k*m-d*d*(4*d*d-(A+B)**2)/64) == 0
assert sp.simplify((1+k)*(1+m)-(8+p1)*(8+p2)/64) == 0
assert sp.simplify((1+k)*(1+m)-(1+S+K)) == 0
print('SYMBOLIC_IDENTITIES_OK')

# Rational stress tests of the analytic inequality's gap bracket.
from fractions import Fraction as F
rf=[F(j,20) for j in range(-20,21)]
tests=0
for bb in rf:
 for aa in rf:
  if aa<=bb: continue
  dd=aa-bb
  kk=dd*(aa-3*bb)/8
  mm=dd*(3*aa-bb)/8
  ss=dd*dd/2
  KK=kk*mm
  ll=dd/4
  for rr in [F(j,10) for j in range(11)]:
   gap=ss+KK*(1+rr)-ll*abs(mm-kk)*rr-ll*ll*(1-rr)
   assert gap >= 3*dd*dd/16
   assert KK >= -ss/8
   assert ss <= 2
   tests+=1
print('RATIONAL_GAP_TESTS_OK',tests)

# Numerical stress tests on the full compact Schur parameter body.
rng=random.Random(20261010)
tests=40000
max_excess=-1e99
for i in range(tests):
 bb=-1+2*rng.random()
 aa=bb+(1-bb)*rng.random()
 if aa==bb: continue
 dd=aa-bb
 kk=dd*(aa-3*bb)/8
 mm=dd*(3*aa-bb)/8
 ll=dd/4
 radius=rng.random()**.5
 phi=rng.random()*2*math.pi
 u=radius*cmath.exp(1j*phi)
 v=cmath.exp(1j*(2*math.pi*rng.random()))*rng.random()**.5
 aa3=dd*u/2
 aa5=kk*u*u+ll*(1-abs(u)**2)*v
 D=(1-aa5)*(1+aa5-2*aa3*aa3)
 target=(1+kk)*(1+mm)
 max_excess=max(max_excess,abs(D)-target)
 assert abs(D)<=target+2e-12
assert max_excess<2e-12
print('SCHUR_BODY_SAMPLING_OK',tests,'maximum_excess',max_excess)

# Check extremizer at u=+i or -i exactly for a rational mesh.
checks=0
for bb in rf:
 for aa in rf:
  if aa<=bb: continue
  dd=aa-bb;kk=dd*(aa-3*bb)/8;mm=dd*(3*aa-bb)/8
  for u in (1j,-1j):
   a3=complex(float(dd))*u/2
   a5=complex(float(kk))*u*u
   dnum=(1-a5)*(1+a5-2*a3*a3)
   assert abs(dnum-float((1+kk)*(1+mm)))<1e-12
   checks+=1
print('EXACT_EXTREMIZER_FORMULAS_OK',checks)
print('VERIFY_OK')
