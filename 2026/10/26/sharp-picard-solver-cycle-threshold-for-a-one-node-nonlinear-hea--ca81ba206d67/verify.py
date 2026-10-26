#!/usr/bin/env python3
"""Self-contained algebraic and finite trajectory cross-checks for the one-node heat map."""
import sympy as s
x,t,v=s.symbols('x t v',positive=True)
F=lambda z:1/(1+t*z*z)
assert s.simplify(F(F(x))-x+(t*x*x-t*x+1)*(t*x**3+x-1)/(t*t*x**4+2*t*x*x+t+1))==0
H=s.factor(F(F(x)).subs(t,4)-x)
assert s.factor(H+(2*x-1)**3*(2*x*x+x+1)/(16*x**4+8*x*x+5))==0
vv=s.symbols('v')
series=s.series(F(F(x)).subs(t,4).subs(x,s.Rational(1,2)+vv)-s.Rational(1,2),vv,0,4).removeO()
assert s.expand(series)==vv-2*vv**3
for T in [s.Rational(5),s.Rational(8),s.Rational(100)]:
  p=(1+s.sqrt(1-4/T))/2; q=1-p
  assert s.simplify(F(p).subs(t,T)-q)==0
  assert s.simplify(F(q).subs(t,T)-p)==0
  fp=lambda z:-2*T*z/(1+T*z*z)**2
  assert s.simplify(fp(p)*fp(q)-4/T)==0
for T in [2.0,3.99,4.0,4.01,5.0,8.0,100.0]:
  z=1.0
  for k in range(300000): z=1/(1+T*z*z)
  if T<4: assert abs(z+T*z**3-1)<5e-8
  if T>4:
    pp=(1+(1-4/T)**.5)/2;pm=1-pp
    assert min(abs(z-pp),abs(z-pm))<1e-8
  if T==4: assert abs(300000*(z-.5)**2-.5)<.004
print('PASS: exact factorization, critical jet, exact cycles/multipliers and 7 trajectories')
