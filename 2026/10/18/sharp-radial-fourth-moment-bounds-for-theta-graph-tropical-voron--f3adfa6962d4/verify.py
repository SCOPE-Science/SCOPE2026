#!/usr/bin/env python3
"""Exact symbolic checker for Euclidean moments of the genus-two theta Voronoi cell.
Requires sympy (pip install sympy); no numerical finite sampling is used for the identities.
"""
from fractions import Fraction
import itertools
import sympy as s

a,b,c=s.symbols('a b c',positive=True)
T=a+b+c; S=a*b+a*c+b*c; P=a*b*c; h=P/S
R2=(T-h)/4
w=[v*(T-v)/(2*S) for v in (a,b,c)]
ct=[(T+h-2*v)/(T-h) for v in (a,b,c)]
assert s.factor(sum(w)-1)==0
I_direct=s.factor(sum(wi*R2*(2+ci)/6 for wi,ci in zip(w,ct)))
J_direct=s.factor(sum(wi*R2**2*(7+6*ci+2*ci**2)/45 for wi,ci in zip(w,ct)))
I=(S*T+P)/(12*S)
J=(9*S**2*T**2+18*P*S*T-3*P**2-8*S**3)/(720*S**2)
assert s.factor(I_direct-I)==0, 'second moment formula'
assert s.factor(J_direct-J)==0, 'fourth moment formula'
Q=s.factor(J/I**2)
assert s.factor(Q-(9*S**2*T**2+18*P*S*T-3*P**2-8*S**3)/(5*(S*T+P)**2))==0
assert s.factor(s.Rational(9,5)-Q-4*(3*P**2+2*S**3)/(5*(S*T+P)**2))==0
N=57*S**2*T**2+114*P*S*T-243*P**2-200*S**3
assert s.factor(Q-s.Rational(168,125)-N/(125*(S*T+P)**2))==0
x,y,z=s.symbols('x y z',nonnegative=True)
certificate=(480*x**4*(y*y+y*z+z*z)
+20*x**3*(2*y+z)*(31*y*y+31*y*z+34*z*z)
+12*x**2*(89*y**4+178*y**3*z+212*y*y*z*z+123*y*z**3+19*z**4)
+12*x*y*(y+z)*(2*y+z)*(14*y*y+14*y*z+19*z*z)
+y*y*(y+z)**2*(28*y*y+28*y*z+57*z*z))
assert s.expand(N.subs({a:x,b:x+y,c:x+y+z})-certificate)==0, 'positivity identity'
assert all(coef>0 for coef in s.Poly(certificate,x,y,z).coeffs())
assert s.factor(Q.subs({a:x,b:x,c:x})-s.Rational(168,125))==0
assert s.limit(Q.subs({a:2,b:2,c:z}),z,s.oo)==s.Rational(9,5)
for aa,bb,cc in itertools.product(range(2,13),repeat=3):
    expr=(Q.subs({a:aa,b:bb,c:cc}))
    assert s.Rational(168,125)<=expr<s.Rational(9,5)
    assert (expr==s.Rational(168,125))==(aa==bb==cc)
print('MOMENT_PROOF_CHECK_OK symbolic fourth integral, source second moment, sharp inequalities, positivity certificate, 1331 rational profiles, equality and supremum')
