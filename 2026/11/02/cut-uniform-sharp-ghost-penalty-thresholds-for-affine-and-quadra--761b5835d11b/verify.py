#!/usr/bin/env python3
"""Exact symbolic checks for the two-cell P1/P2 ghost-penalty theorem."""
import sympy as s
k,g=s.symbols('k g',positive=True)
a,b,c,d=s.symbols('a b c d')
x=s.symbols('x')
inputs={
 1:([a,c], a*a+k*c*c+g*(c-a)**2,c),
 2:([a,b,c,d],s.integrate((a+b*x)**2,(x,-1,0))+s.integrate((c+d*x)**2,(x,0,k))+g*((c-a)**2+(d-b)**2/s.Integer(4)),c+k*d)
}
P=12*g**3*(1+k)**3+g**2*(31*k**3+6*k+24)+g*(11*k**3+3)+k**3
Q=3*g**2*(1+k)**4+g*(7*k**4+4*k**3+3*k)+k**4
N=12*g**2*(1+k)**3+g*(28*k**3+12*k**2+3)+4*k**3
count=0
for p,(v,E,z) in inputs.items():
 H=s.hessian(E,v)/2
 w=s.Matrix([s.diff(z,t) for t in v])
 T=s.factor((w.T*H.inv()*w)[0])
 if p==1: assert s.cancel(T-(1+g)/(k*(1+g)+g))==0
 else:
  assert s.cancel(T-N/Q)==0
  assert s.cancel((4+1/g)-T-k*P/(g*Q))==0
 assert s.cancel(T.subs(k,0)-(p*p+1/g))==0
 for K in [s.Rational(1,1000),s.Rational(1,8),s.Rational(1,2),s.Rational(3,4),s.Rational(99,100)]:
  for G in [s.Rational(1,25),s.Rational(1,5),s.Integer(1),s.Rational(7,2)]:
   M=H.subs({k:K,g:G}); v0=w.subs(k,K);delta=p*p+1/G
   assert s.simplify((v0.T*M.inv()*v0)[0]) < delta
   assert (M-v0*v0.T/delta).is_positive_definite
   count+=1
assert count==40
print('PASS: two symbolic identities, two vanishing-cut limits, 40 exact rational checks')
