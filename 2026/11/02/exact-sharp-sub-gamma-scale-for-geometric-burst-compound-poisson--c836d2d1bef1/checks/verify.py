#!/usr/bin/env python3
"""Reproduce polynomial and finite stop-loss identities for geometric bursts."""
import math
import sympy as s
q,u=s.symbols('q u',positive=True)
c=(1+4*q+q*q)/(3*(1-q*q))
r=1-q
S=1-2*r/(1+q)*u+r*r/(1+q)*u*u
F=c-u+r/(1+q)*u*u-r*r/(3*(1+q))*u**3
checks=0
def check(x):
 global checks
 assert x
 checks+=1
check(s.simplify(F.subs(u,0)-c)==0)
check(s.simplify(F.subs(u,1)-q*c)==0)
check(s.simplify(s.diff(F,u)+S)==0)
check(s.simplify(c*S-F - r*r*u*(u-1)*((1+q)*u-1)/(3*(1+q)**2))==0)
check(s.simplify((1+q)/(1-q)**2 * c - (1+4*q+q*q)/(3*(1-q)**3))==0)
for Q in (s.Rational(1,100),s.Rational(1,5),s.Rational(1,2),s.Rational(4,5),s.Rational(99,100)):
 cv=float(c.subs(q,Q)); qv=float(Q)
 check(-math.log(qv)>1/cv)
 for m in range(8):
  for j in range(101):
   uv=j/100
   fv=float(F.subs({q:Q,u:s.Rational(j,100)})) * qv**m
   target=cv*math.exp(-(m+uv)/cv)
   check(fv<=target+1e-12)
print(f'PASS: {checks} symbolic and numerical assertions')
