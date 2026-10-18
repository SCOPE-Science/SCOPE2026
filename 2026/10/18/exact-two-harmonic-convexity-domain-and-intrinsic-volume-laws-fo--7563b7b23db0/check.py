#!/usr/bin/env python3
"""Reproduce exact algebra and independent bounded numerical checks for a two-mode zonal support family.
Requires Python 3 and SymPy. Use: python check.py
"""
import random
import math
import sympy as s
z,x,a,b=s.symbols('z x a b', real=True)
h=1+a*(3*z**2-1)/2+b*(35*z**4-30*z**2+3)/8
az=s.expand(h-z*s.diff(h,z))
mer=s.expand(az+(1-z*z)*s.diff(h,z,2))
az_poly=1-a*(3*x+1)/2+b*(-105*x*x+30*x+3)/8
mer_poly=1+a*(5-9*x)/2+b*(-525*x*x+510*x-57)/8
assert s.simplify(az-az_poly.subs(x,z*z))==0
assert s.simplify(mer-mer_poly.subs(x,z*z))==0
assert s.simplify(mer_poly-(az_poly-2*(1-x)*s.diff(az_poly,x)))==0
print('EXACT_CURVATURE_EIGENVALUES_AND_INTEGRATING_IDENTITY_OK')

B=-s.Rational(27,217)
C=s.Rational(6,49)
p=s.Rational(-24,679)
q=s.Rational(-1,21)
a_minus=lambda beta: (-55*beta-5*s.sqrt(-14*beta*(27+217*beta)))/27
a_plus=lambda beta: (-55*beta+5*s.sqrt(-14*beta*(27+217*beta)))/27
lowerline=lambda beta:(57*beta-8)/20
upperline=lambda beta:(1-9*beta)/2
assert s.simplify(a_minus(B)-s.Rational(55,217))==0
assert s.simplify(a_plus(B)-s.Rational(55,217))==0
assert s.simplify(a_minus(p)-lowerline(p))==0
assert s.simplify(a_plus(q)-upperline(q))==0
assert s.simplify(lowerline(C)-upperline(C))==0
assert s.simplify(mer_poly.subs(x,s.Rational(5,9))-(1+s.Rational(217,27)*b))==0
assert s.simplify(mer_poly.subs(x,0)-(1+5*a/2-57*b/8))==0
assert s.simplify(mer_poly.subs(x,1)-(1-2*a-9*b))==0
A=s.Poly(mer_poly,x).coeff_monomial(x**2)
BB=s.Poly(mer_poly,x).coeff_monomial(x)
CC=s.Poly(mer_poly,x).coeff_monomial(1)
assert s.simplify(-BB/(2*A)-(85*b-6*a)/(175*b))==0
T=27*a*a+110*a*b+2925*b*b+350*b
assert s.simplify(CC-BB**2/(4*A)-T/(350*b))==0
assert s.factor(T.subs(a,a_minus(b)))==0
assert s.factor(T.subs(a,a_plus(b)))==0
print('EXACT_PHASE_BOUNDARIES_AND_SHARP_EXTREME_PARAMETERS_OK')

surface=s.factor(s.integrate(s.expand(az*mer),(z,-1,1))/2)
volume=s.factor(s.integrate(s.expand(h*az*mer),(z,-1,1))/2)
s_expected=1-2*a*a/5-b*b
v_expected=1-6*a*a/5-3*b*b+4*a**3/7+s.Rational(18,35)*a*a*b+s.Rational(300,77)*a*b*b+s.Rational(2448,1001)*b**3
assert s.simplify(surface-s_expected)==0
assert s.simplify(volume-v_expected)==0
assert s.integrate(h,(z,-1,1))==2
print('EXACT_SURFACE_AREA_VOLUME_AND_MEAN_WIDTH_IDENTITIES_OK')

# Independent check: among all x in [0,1], a quadratic is nonnegative
# iff endpoints and (when applicable) its stationary value are nonnegative.
def qmin(aa,bb):
 def f(y):return 1+aa*(5-9*y)/2+bb*(-525*y*y+510*y-57)/8
 vals=[f(0),f(1)]
 if bb<0:
  xx=(85*bb-6*aa)/(175*bb)
  if 0<xx<1:vals.append(f(xx))
 return min(vals)

def lval(bb):
 return float(a_minus(bb)) if bb<float(p) else float(lowerline(bb))
def uval(bb):
 return float(a_plus(bb)) if bb<float(q) else float(upperline(bb))
rng=random.Random(20261017)
for _ in range(50000):
 bb=rng.uniform(-.17,.17)
 aa=rng.uniform(-.95,.95)
 expected=(float(B)<=bb<=float(C)) and lval(bb)-1e-10<=aa<=uval(bb)+1e-10
 actual=qmin(aa,bb)>=-1e-10
 assert expected==actual,(aa,bb,expected,actual)
print('INDEPENDENT_50000_GLOBAL_QUADRATIC_TESTS_OK')

# Direct Gauss-Legendre integration confirms exact intrinsic formulas;
# mpmath is supplied transitively with SymPy.
import mpmath as mp
mp.mp.dps=40
for aa,bb in [(mp.mpf('0.1'),mp.mpf('-0.05')),(mp.mpf('-0.2'),mp.mpf('0.07')),(mp.mpf('0.4'),mp.mpf('0.0')),(mp.mpf('0.0'),mp.mpf('-0.08'))]:
 def hh(t):return 1+aa*(3*t*t-1)/2+bb*(35*t**4-30*t*t+3)/8
 def ar(t):return 1-aa*(3*t*t+1)/2+bb*(-105*t**4+30*t*t+3)/8
 def mr(t):return 1+aa*(5-9*t*t)/2+bb*(-525*t**4+510*t*t-57)/8
 SS=mp.quad(lambda t: ar(t)*mr(t), [-1,0,1])/2
 VV=mp.quad(lambda t: hh(t)*ar(t)*mr(t),[-1,0,1])/2
 Sp=1-2*aa**2/5-bb**2
 Vp=1-6*aa**2/5-3*bb**2+4*aa**3/7+mp.mpf(18)/35*aa**2*bb+mp.mpf(300)/77*aa*bb**2+mp.mpf(2448)/1001*bb**3
 assert abs(SS-Sp)<mp.mpf('1e-35')
 assert abs(VV-Vp)<mp.mpf('1e-35')
print('INDEPENDENT_HIGH_PRECISION_GEOMETRIC_INTEGRALS_OK')
print('ALL_TWO_MODE_ZONAL_CHECKS_OK')
