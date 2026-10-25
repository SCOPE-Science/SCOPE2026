#!/usr/bin/env python3
"""Independent symbolic and numerical checks for the switching-trap covariance theorem.

Requires Python 3, sympy, numpy and scipy. It tests the exact stationary
moment equations, the covariance ODE, the sharp OU-mimicry criterion, and
fourth-cumulant/entropy-production formulas.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.linalg import expm

k0, k1, r, D = sp.symbols('k0 k1 r D', positive=True)
s, p = k0 + k1, k0 * k1
B2 = sp.Matrix([[2*k0+r,-r],[-r,2*k1+r]])
B4 = sp.Matrix([[4*k0+r,-r],[-r,4*k1+r]])
u2 = B2.inv()*sp.Matrix([D,D])
u4 = B4.inv()*(12*D*u2)
C0 = sp.factor(sum(u2)); M4 = sp.factor(sum(u4))
K4 = sp.factor(M4-3*C0**2)
J = 2*p+r*s
L = s+2*r
P = p+r*s
EPR = sp.factor(r*(k0-k1)**2/(4*p+2*r*s))
zero = sp.Integer(0)

def test(expr, desc):
    assert sp.simplify(sp.factor(expr)) == zero, f'{desc}: {sp.factor(expr)}'
    print('PASS:',desc)

test(C0-D*L/J,'stationary variance')
test(sp.factor((u2.T*sp.Matrix([k0,k1]))[0])-D,'stationary initial covariance slope')
test(K4-3*D**2*(k0-k1)**2*(2*r**2+3*r*s+4*p)/(J**2*(r*s+4*p)),
     'unconstrained stationary fourth-cumulant rational expression')
test(sp.expand(J**2-L**2*J+P*L**2)-(p-r**2)*(4*p-s**2),
     'characteristic-polynomial cancellation identity')
test(sp.factor(C0.subs(k1,r**2/k0)-D/r),'OU variance on product condition')
test(sp.factor(P.subs(k1,r**2/k0)-r*(L-r).subs(k1,r**2/k0)),
     'OU eigenvalue on product condition')
test(sp.factor(K4.subs(k1,r**2/k0)-9*D**2*(k0-r)**2/(r**2*(k0**2+4*r*k0+r**2))),
     'fourth cumulant on geometric-mean switching curve')
test(sp.factor(EPR.subs(k1,r**2/k0)-(k0-r)**2/(2*k0)),
     'entropy production on geometric-mean switching curve')
excess = sp.factor(K4.subs(k1,r**2/k0)/C0.subs(k1,r**2/k0)**2)
epr_critical = sp.factor(EPR.subs(k1,r**2/k0))
test(excess-9*epr_critical/(epr_critical+3*r),'fourth cumulant measures entropy production')
test(sp.factor(excess.subs(k0,sp.Integer(1)).subs(r,sp.Integer(2))-sp.Rational(9,13)),
     'illustration has excess kurtosis 9/13')
test(sp.factor(epr_critical.subs(k0,sp.Integer(1)).subs(r,sp.Integer(2))-sp.Rational(1,2)),
     'illustration has entropy production 1/2')

# Numerically independent Feynman-Kac matrix-exponential calculation.
# At product equality, C(t) must match a fixed-stiffness OU process at all lags.
for a,b,rate,noise in [(1.,4.,2.,1.),(0.25,16.,2.,0.7),(0.5,8.,2.,1.3),
                       (0.2,45.,3.,1.2), (2.,18.,6.,1.5)]:
    assert abs(a*b-rate**2)<1.e-11
    C2=np.linalg.solve(np.array([[2*a+rate,-rate],[-rate,2*b+rate]]),
                       np.array([noise,noise]))
    M=np.array([[-a-rate,rate],[rate,-b-rate]])
    for t in [0.,0.03125,0.15,0.5,1.3,3.0]:
        actual=float(C2@expm(M*t)@np.ones(2))
        expected=noise/rate*math.exp(-rate*t)
        assert abs(actual-expected)<2.e-13, (a,b,rate,t,actual,expected)
print('PASS: 30 independent matrix-exponential lag checks (five nonidentical traps)')

# Test the factorization away from the sharp threshold.
for a,b,rate in [(1.,4.,1.9),(1.,4.,2.1),(0.7,5.3,3.1),(2.,6.,0.5)]:
    C2=np.linalg.solve(np.array([[2*a+rate,-rate],[-rate,2*b+rate]]),
                       np.array([1.,1.]))
    M=np.array([[-a-rate,rate],[rate,-b-rate]])
    actual=float(C2@expm(M*0.75)@np.ones(2))
    fake=float(sum(C2)*math.exp(-0.75/sum(C2)))
    assert abs(actual-fake)>1.e-8, (a,b,rate,actual,fake)
print('PASS: four off-threshold counterchecks')

# Markov-switching Gaussian stationarity: at a fixed rate, higher moments of
# the position differ from equilibrium OU despite identical autocovariances.
R = (sp.Integer(1),sp.Integer(4),sp.Integer(2),sp.Integer(1))
u2_example = [z.subs(dict(zip((k0,k1,r,D),R))) for z in u2]
u4_example = [z.subs(dict(zip((k0,k1,r,D),R))) for z in u4]
assert sum(u2_example) == sp.Rational(1,2)
assert sum(u4_example) == sp.Rational(12,13)
assert sum(u4_example)-3*sum(u2_example)**2 == sp.Rational(9,52)
print('PASS: exact rational fourth moment 12/13 vs OU 3/4, cumulant 9/52')
print('ALL CHECKS PASSED')
