#!/usr/bin/env python3
"""Exact checks for the tandem-exclusion optimal-current theorem.

Execute with Python >=3.10 and SymPy >=1.12. Scientific claims about all
parameters also require the analytic arguments in RESULT.md.
"""
import math
import sympy as S

s, q, r, t, x = S.symbols('s q r t x', positive=True)
D = 1 + 2*s + q*s*s
rho = s*(1+q*s)/D
j = q*s*s*(s+2+q*s)/((1+s)*(1+q*s)*D)
P = (q*q*(q+1)*s**5 + 4*q*q*s**4 - 2*(q*q+1)*s**3
     - 2*(q*q+4*q+3)*s**2 - (5*q+9)*s - 4)

assert S.simplify(q*(1-rho)*s*s+(1-2*rho)*s-rho) == 0
assert S.factor(S.diff(rho,s)) == (q*s*s+2*q*s+1)/D**2
j_source = q*rho*s*(s+2+q*s)/((1+s)*(1+q*s)**2)
assert S.simplify(j_source-j) == 0
assert S.simplify(S.diff(j,s) + q*s*P/((1+s)**2*(1+q*s)**2*D**2)) == 0
assert S.simplify(P.subs(q,1)-2*(s-2)*(s+1)**4) == 0
assert S.simplify(rho.subs({q:1,s:2}) - S.Rational(2,3)) == 0
assert S.simplify(j.subs({q:1,s:2}) - S.Rational(8,27)) == 0

high_poly = S.factor(S.limit(t**4*P.subs({q:t**-3,s:t*x}),t,0))
low_poly = S.factor(S.limit(t**3*P.subs({q:t,s:x/t}),t,0))
assert high_poly == x*x*(x**3-2)
assert low_poly == x**3*(x*x-2)
assert S.simplify(S.limit((1-j.subs({q:t**-3,s:t*x}))/t,t,0) -(x+1/x**2)) == 0
assert S.simplify(S.limit((1-rho.subs({q:t**-3,s:t*x}))/t,t,0)-1/x**2) == 0
assert S.simplify(S.limit(rho.subs({q:t,s:x/t}),t,0)-(x+1)/(x+2)) == 0
assert S.simplify(S.limit(j.subs({q:t,s:x/t}),t,0)-x/((x+1)*(x+2))) == 0

# The high-density recovery boundary layer, at rho=1-zeta/q.
z = S.symbols('z', positive=True)
s_boundary = (-(1-2*(1-z/q)) + S.sqrt((1-2*(1-z/q))**2 + 4*q*(z/q)*(1-z/q)))/(2*q*(z/q))
lim_s = S.simplify(S.limit(s_boundary,q,S.oo))
assert S.simplify(lim_s - (1+S.sqrt(1+4*z))/(2*z)) == 0
lim_j = S.simplify(S.limit(j.subs(s,s_boundary),q,S.oo))
assert S.simplify(lim_j - (S.sqrt(1+4*z)-1)/(S.sqrt(1+4*z)+1)) == 0

# Independent numerical bisection of the unique positive root, not a certificate
# of uniqueness (the coefficient-sign proof in RESULT.md supplies that).
def poly(u,Q):
 return Q*Q*(Q+1)*u**5+4*Q*Q*u**4-2*(Q*Q+1)*u**3-2*(Q*Q+4*Q+3)*u**2-(5*Q+9)*u-4

def root(Q):
 lo,hi=0.0,1.0
 while poly(hi,Q)<0: hi*=2
 for _ in range(160):
  m=(lo+hi)/2
  if poly(m,Q)>0: hi=m
  else:lo=m
 return (lo+hi)/2

for Q in [0.001,0.1,1.0,2.0,10.0,100.0,1e4,1e6,1e9]:
 u=root(Q)
 rr=u*(1+Q*u)/(1+2*u+Q*u*u)
 jj=Q*u*u*(u+2+Q*u)/((1+u)*(1+Q*u)*(1+2*u+Q*u*u))
 assert 0<rr<1 and 0<jj<1
 for a in [0.1,0.5,0.9,1.1,2,10]:
  v=u*a
  jv=Q*v*v*(v+2+Q*v)/((1+v)*(1+Q*v)*(1+2*v+Q*v*v))
  assert jj>=jv-1e-13
 if Q==1: assert abs(rr-2/3)<1e-12
 if Q>=1e6:
  assert abs(Q**(1/3)*(1-rr)-2**(-2/3))<0.025
  assert abs(Q**(1/3)*(1-jj)-3*2**(-2/3))<0.03
 if Q<=0.001:
  assert abs(rr-1/math.sqrt(2))<0.001
  assert abs(jj-(3-2*math.sqrt(2)))<0.001
print('VERIFY_OK: symbolic identities, derivative, limit polynomial, both rate extremes, numerical roots')
