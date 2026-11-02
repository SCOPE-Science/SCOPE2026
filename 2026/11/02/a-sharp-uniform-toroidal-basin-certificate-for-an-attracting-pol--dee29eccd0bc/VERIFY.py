#!/usr/bin/env python3
"""Exact identities for the sharp positive-invariance rectangle."""
import sympy as sp
q,w,delta,mu=sp.symbols('q w delta mu', real=True)
P=21*q*q-125*q+400*w*w+100
a=4-delta; b=4+delta; c=a/10; d=b/10
assert sp.expand(P.subs({q:a,w:d})-delta*(25*delta-11))==0
assert sp.expand(P.subs({q:b,w:c})-delta*(25*delta+11))==0
assert sp.expand(P.subs(w,q/10)-25*(q-1)*(q-4))==0
Q=-2*mu*q*P
W=q/10-w
J=sp.Matrix([Q,W]).jacobian([q,w]).subs({q:4,w:sp.Rational(2,5)})
assert sp.simplify(J.trace()+344*mu+1)==0
assert sp.simplify(J.det()-600*mu)==0
E=sp.expand(P+q*sp.diff(P,q))
assert sp.expand(E-(63*q*q-250*q+400*w*w+100))==0
assert sp.expand(E.subs({q:a,w:c})-(67*delta**2-286*delta+172))==0
assert sp.simplify((67*delta**2-286*delta+172).subs(delta,sp.Rational(11,25))-sp.Rational(36957,625))==0
assert sp.simplify((-2*mu*a*P.subs({q:a,w:d})).subs({delta:sp.Rational(1,2),mu:1}))<0
print('PASS: 9 exact boundary/equilibrium/Jacobian/divergence/sharpness checks')
