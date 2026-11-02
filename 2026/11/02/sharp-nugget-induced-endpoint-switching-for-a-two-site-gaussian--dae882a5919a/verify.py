#!/usr/bin/env python3
"""Independent numerical and exact-algebra checks for the two-observation likelihood theorem.

Run with Python 3 standard library: python verify.py
The general theorem is proved in the accompanying manuscript, not by these finite tests.
"""
import math
from fractions import Fraction

checks = 0

def test(condition, context):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(context)

def objective(a, z, t):
    return 2.0*z/(a-t) + math.log(a*a-t*t)

def threshold(a):
    return -0.5*a*(a-1)*math.log1p(-1.0/(a*a))

def crossing(a, t):
    return -0.5*a*(a-t)/t * math.log1p(-(t/a)**2)

# Exact polynomial derivative identity, using rational arithmetic rather
# than numerical differentiation.
for ia in range(2, 9):
    A = Fraction(ia, 1)
    for iz in range(0, 18):
        z = Fraction(iz, 13)
        for it in range(0, 10):
            t = Fraction(it, 10)
            derivative_rational = 2*z/(A-t)**2 - 2*t/(A*A-t*t)
            q = t*t+(z-A)*t+A*z
            predicted = 2*q/((A-t)**2*(A+t))
            test(derivative_rational == predicted, ('derivative identity', A,z,t))

# Boundary-law checks over the entire critical high-nugget range.
for A in [2.0, 2.01, 2.2, 2.5, 3.0, 5.0, 10.0, 30.0, 100.0]:
    c = threshold(A)
    test(0<c<0.5, ('critical level range',A,c))
    test(abs(objective(A,c,1)-objective(A,c,0))<1e-11, ('boundary tie',A))
    for k in range(1,101):
        t = k/101.0
        test(crossing(A,t)<c, ('interior crossing below boundary',A,t))
        test(objective(A,c,t)>objective(A,c,0), ('no interior maximum at tie',A,t))
    for z in [0.0,0.25*c,0.99*c,1.01*c,2*c,0.5,1.0,2.0]:
        preferred=1.0 if z<c else 0.0
        for k in range(1,101):
            t=k/101.0
            test(objective(A,z,t)>objective(A,z,preferred)-1e-12,
                 ('global optimizer',A,z,t))
        test(objective(A,z,1-preferred)>objective(A,z,preferred)-1e-12,
             ('correct endpoint',A,z))

# The large-contrast obstruction holds for all positive nuggets.
for A in [1.0001,1.001,1.01,1.1,1.5,1.9,2.0,3.0,5.0,100.0]:
    for z in [0.5,0.5001,0.8,1.5]:
        for k in range(1,102):
            t=k/101.0
            test(objective(A,z,t)>objective(A,z,0),
                 ('large contrast boundary',A,z,t))

# Monotonic threshold; high-noise critical limit 1/2.
last = threshold(2.0)
for i in range(1,2001):
    a = 2.0+i/100.0
    now = threshold(a)
    test(now>last,('increasing threshold',a,now,last))
    last=now
for a in [1e2,1e3,1e4,1e5]:
    test(abs(threshold(a)-0.5) < 1.0/a, ('half limit',a))

# Random finite-difference derivative checks away from machine cancellation.
for A in [2.0,2.5,4.0,10.0]:
    for z in [0.01,0.1,0.3,0.7,2.0]:
        for j in range(1,100):
            t=j/100.0
            eps=1e-5
            fd=(objective(A,z,t+eps)-objective(A,z,t-eps))/(2*eps)
            formula=2*z/(A-t)**2-2*t/(A*A-t*t)
            test(abs(fd-formula)<3e-7, ('finite difference',A,z,t))

print(f'PASS: {checks} assertions; exact rational and numerical checks completed.')
