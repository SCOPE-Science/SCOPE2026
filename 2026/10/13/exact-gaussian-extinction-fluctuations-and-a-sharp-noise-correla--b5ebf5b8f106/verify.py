#!/usr/bin/env python3
"""Exact algebra checks for a mathematical epidemic fluctuation theorem."""
from fractions import Fraction
import sympy as s
L,mu,a,b,c,rho=s.symbols('L mu a b c rho',real=True)
m=L/mu
q=2*L**2/(mu*(2*mu-a*a))
k=c*a/mu
v=k*k*q+b*b+2*k*b*rho*m
floor=k*k*(q-m*m)+(b-k*m)**2
assert s.simplify(v.subs(rho,-1)-floor)==0
assert s.simplify(q-m*m-L*L*a*a/(mu*mu*(2*mu-a*a)))==0
assert s.simplify(q*(2*mu-a*a)-2*L*m)==0
assert s.simplify(k-c*a/mu)==0
vals={L:2,mu:2,a:1,b:s.Rational(1,2),c:2}
assert s.simplify(m.subs(vals))==1
assert s.simplify(q.subs(vals))==s.Rational(4,3)
assert s.simplify(k.subs(vals))==1
assert s.simplify(v.subs(vals).subs(rho,-1))==s.Rational(7,12)
assert s.simplify(v.subs(vals).subs(rho,0))==s.Rational(19,12)
assert s.simplify(v.subs(vals).subs(rho,1))==s.Rational(31,12)
alpha=4
lam=(c*m-alpha-b*b/2).subs(vals)
assert lam==s.Rational(-17,8)
assert max(s.Rational(1,1),s.Rational(1,4),s.Rational(1,4))<4
I=s.symbols('I',positive=True)
f=1+I**2
p=I/f
assert s.simplify(s.diff(p,I)-(1-I**2)/(1+I**2)**2)==0
assert s.simplify(s.diff(f,I)-2*I)==0
print('VERIFY_OK')
