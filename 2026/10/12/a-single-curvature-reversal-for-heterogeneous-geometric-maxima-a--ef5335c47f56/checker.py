#!/usr/bin/env python3
"""Exact rational and symbolic consistency checks for discrete geometric maxima.

Requires Python 3 and SymPy. The infinite-domain theorem is proved in RESULT.md;
finite cases here are supplementary checks rather than a substitute for proof.
"""
from fractions import Fraction as F
import sympy as S

r, s = S.symbols('r s')
A, B, C = 1-r, 1-s, 1-r*s
p = lambda k: A*r**k + B*s**k - C*(r*s)**k
h = lambda k: -A*B*(r-s)**2 + A*C*r**(k+1)*(1-s)**2 + B*C*s**(k+1)*(1-r)**2
for k in range(1, 7):
    assert S.expand(p(k)**2-p(k-1)*p(k+1)-(r*s)**(k-1)*h(k)) == 0
assert S.factor(h(1) - r*s*(1-r)**2*(1-s)**2*(r+s+2)) == 0
u,v = S.symbols('u v')
q1 = u+v+u*v
q2 = u*u*(1+v+v*v)+v*v*(1+u)
q3 = u**3*(1+v+v*v+v**3)+v**3*(1+u+u*u)
assert S.expand(q1**2-q2-u*v*(u+v+2))==0
assert S.factor(q2**2-q1*q3-u*v*(u*v*(u*u+v*v+u+v+2)-(u*u+v*v)))==0
assert S.factor((q2**2-q1*q3).subs({u:S.Rational(1,10),v:S.Rational(1,5)})) == -S.Rational(3,50000)
for rr,ss in [(F(1,10),F(1,5)),(F(1,2),F(1,3)),(F(3,4),F(1,4)),(F(1,3),F(1,3))]:
    AA,BB,CC=1-rr,1-ss,1-rr*ss
    pp=lambda k:AA*rr**k+BB*ss**k-CC*(rr*ss)**k
    hh=lambda k: -AA*BB*(rr-ss)**2+AA*CC*rr**(k+1)*(1-ss)**2+BB*CC*ss**(k+1)*(1-rr)**2
    vals=[]
    for k in range(1,101):
        delta=pp(k)**2-pp(k-1)*pp(k+1)
        assert delta == (rr*ss)**(k-1)*hh(k)
        vals.append(hh(k))
    assert vals[0]>0 and all(vals[i]>vals[i+1] for i in range(99))
    if rr!=ss:
        assert any(x<0 for x in vals)
        assert all(not (vals[i]<0 and vals[i+1]>0) for i in range(99))
    else: assert all(x>0 for x in vals)
print('PASS: 6 symbolic infinite-index templates, 4 exact identities, 400 exact-rational parameter/index checks')
