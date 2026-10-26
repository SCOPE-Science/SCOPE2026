#!/usr/bin/env python3
"""Independent algebraic and benchmark-inequality checks for the stated SIR theorem.
This finite checker does not prove the universal Pontryagin/Rolle argument.
"""
from fractions import Fraction
from math import exp, sqrt
try:
    import sympy as sy
except ImportError as exc:
    raise SystemExit('sympy is required for derivative checks') from exc
S,I=sy.symbols('S I', real=True)
eps=sy.Rational(1,10**8)
B=48*sy.exp(3*I-sy.Rational(3,2)*S)
C=32*(1+2*I)*(1-sy.Rational(67,100)*S)
gamma=5+2*I
assert sy.simplify(sy.diff(B*S-gamma,S)-B*(1-sy.Rational(3,2)*S))==0
assert sy.simplify(sy.diff(C*S-gamma,S)-32*(1+2*I)*(1-sy.Rational(134,100)*S))==0
assert sy.simplify((B+I*sy.diff(B,I))/B-(1+3*I))==0
assert sy.simplify((C+I*sy.diff(C,I))/(32*(1-sy.Rational(67,100)*S))-(1+4*I))==0
assert sy.simplify(sy.Rational(64,11)-5-2*eps)>0
assert sy.simplify(sy.Rational(132,25)-5-2*eps)>0
assert sy.simplify(sy.Rational(99,100)-sy.Rational(2,3))>0
assert sy.simplify(sy.Rational(99,100)-sy.Rational(50,67))>0
assert exp(1.5)<11/2
# Rational proof skeleton for the e-bound: e<3 => e^(3/2)<3sqrt(3)<11/2.
assert 3*sqrt(3)<11/2
print('PASS: two exact sensitivities, incidence positivity, benchmark bounds, thresholds')
