"""Exact symbolic identities and reproducible examples for three-band Cauchy zero geometry.

Requires sympy and mpmath. Execute: python three_band_cauchy_verification.py
This checker supplements the analytic theorem in RESULT.md.
"""
from __future__ import annotations
import sympy as sp
import mpmath as mp

r, s, w, z = sp.symbols('r s w z', real=True)
A = 1-r+s
B = (1-r)*(r-s*s)-s*(r*r+1)
C = r*s*(r-(1-r)*s)
N = sp.expand((1-r)*(w+r)*(w-s*s)+s*(w-r*r)*(w-1))
assert sp.expand(N-(A*w*w+B*w+C)) == 0
Q = (1-r)*s*s+(r*r+6*r+1)*s-r*(1-r)
assert sp.factor((B*B-4*A*C)+(1-r)*(r-s)*(1+s)*Q) == 0
assert sp.simplify(Q.subs(s,r)-8*r*r) == 0

# Two disjoint intervals cannot exhibit this upper-zero collision.
u, v, h, k = sp.symbols('u v h k', real=True)
P2 = (v-u)*(z-h)*(z-k)+(k-h)*(z-u)*(z-v)
assert sp.factor(sp.discriminant(P2,z) + 4*(k-u)*(u-v)*(v-h)*(k-h)) == 0

# The exact collision at r=2/5, s=1/15 and sharp splitting constant.
r0=sp.Rational(2,5)
s0=sp.Rational(1,15)
assert sp.simplify(Q.subs({r:r0,s:s0})) == 0
assert sp.factor(N.subs({r:r0,s:s0})-sp.Rational(2,3)*(w+sp.Rational(3,25))**2) == 0
H=(1-r)*(r-s)*(1+s)*sp.diff(Q,s)
y2=B/(2*A)
assert sp.simplify((H/(16*A*A*y2)).subs({r:r0,s:s0})-sp.Rational(91,100)) == 0

# Check the rational formula directly against the six endpoints.
R = sp.expand(N.subs(w,z*z))
F_by_endpoints = (1/(z-1)-1/(z-r)) + (1/(z+r)-1/(z+1)) + (1/(z-s)-1/(z+s))
F_by_polynomial = 2*R/((z*z-r*r)*(z*z-1)*(z*z-s*s))
assert sp.factor(F_by_endpoints-F_by_polynomial) == 0

mp.mp.dps = 45
rv=mp.mpf('0.4')
q=lambda sv: (1-rv)*sv**2+(rv**2+6*rv+1)*sv-rv*(1-rv)
sc=mp.findroot(q, (mp.mpf('.01'),mp.mpf('.12')))
assert mp.mpf('0') < sc < rv
for sv, expected in [(mp.mpf('.02'),'two_imaginary'),(sc,'collision'),(mp.mpf('.20'),'off_axis')]:
 a=1-rv+sv
 b=(1-rv)*(rv-sv**2)-sv*(rv**2+1)
 c=rv*sv*(rv-(1-rv)*sv)
 delta=b*b-4*a*c
 if expected=='two_imaginary':
  assert delta>0 and b>0
 elif expected=='off_axis':
  assert delta<0
 else:
  assert abs(delta)<mp.mpf('1e-36')
 rootsw=mp.polyroots([a,b,c],maxsteps=500,error=False) if expected!='collision' else [-b/(2*a)]
 for ww in rootsw:
  zz=mp.sqrt(ww)
  if mp.im(zz)<0: zz=-zz
  if abs(zz)<mp.mpf('1e-40'): continue
  # Rational evaluation should vanish. At collision, the upper root is double.
  FF=(1/(zz-1)-1/(zz-rv))+(1/(zz+rv)-1/(zz+1))+(1/(zz-sv)-1/(zz+sv))
  assert abs(FF)<mp.mpf('1e-22')
  if expected!='collision':
   # A direct integral, not only a symbolic rearrangement.
   II=mp.quad(lambda x: (zz-x)**(-2),[-1,-rv])+mp.quad(lambda x: (zz-x)**(-2),[-sv,sv])+mp.quad(lambda x: (zz-x)**(-2),[rv,1])
   assert abs(II)<mp.mpf('1e-20')
  print(expected,'s=',mp.nstr(sv,12),'zero=',mp.nstr(zz,15))
print('threshold=',mp.nstr(sc,25),'all checks passed')
