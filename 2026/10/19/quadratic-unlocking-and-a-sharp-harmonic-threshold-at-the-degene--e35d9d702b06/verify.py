#!/usr/bin/env python3
"""Self-contained consistency checks for a half-turn circle-map theorem.
Finite trajectory observations do not establish asymptotic or global assertions.
"""
import math
from fractions import Fraction

checks=0
def ok(assertion, label):
    global checks
    if not assertion:
        raise AssertionError(label)
    checks+=1

def f(x,a,b):
    return a*(1.0+math.cos(4*math.pi*x))+b*math.sin(2*math.pi*x)

def delta(x,mu,a,b):
    return mu*(f(x,a,b)+f(x+0.5+mu*f(x,a,b),a,b))

def coef(a,b):
    return math.pi*abs(b)*math.sqrt(16*a*a-b*b)/2

# Exact rational identities corresponding to the two local quadratic forms,
# with a common factor pi^2 removed. Fractions avoid roundoff entirely.
for aa in [Fraction(1),Fraction(2),Fraction(3,2)]:
    for bb in [Fraction(1,4),Fraction(1),Fraction(2),Fraction(3),Fraction(9,2),Fraction(-2)]:
        for sgn in (1,-1):
            A=16*aa
            B=sgn*4*bb*(4*aa+sgn*bb)
            C=2*bb*bb*(4*aa+sgn*bb)
            ok(4*A*C-B*B==16*bb*bb*(16*aa*aa-bb*bb),'discriminant')

# Exact b-profile optimization by squaring and completing the square.
for aa in [Fraction(1),Fraction(2),Fraction(3,2)]:
    bb2=8*aa*aa
    ok(bb2*(16*aa*aa-bb2)==64*aa**4,'maximum coefficient square')
    for bb2 in [Fraction(0),Fraction(1),4*aa*aa,8*aa*aa,12*aa*aa,16*aa*aa]:
        ok(bb2*(16*aa*aa-bb2)<=64*aa**4,'coefficient extremum')

# Critical endpoint identity, half-translation conjugacy, exact b=0 orbit.
for aa in (0.4,1.0,2.0):
    for mu in (-.017,-.004,.004,.017):
        true=delta(.75,mu,aa,4*aa)
        exact=-2*aa*mu*(1-math.cos(8*math.pi*aa*mu))**2
        ok(abs(true-exact)<=2e-12,'critical endpoint trigonometric identity')
        ok(abs(delta(.25,mu,aa,-4*aa)-delta(.75,mu,aa,4*aa))<2e-12,'translation symmetry')
        ok(abs(delta(.25,mu,aa,0))<2e-12,'b zero lock')

# Rotational estimates: test finite-time drift with conservative errors only;
# these do not prove the infinite-time limit.
def rotation(mu,a,b,steps=180000):
    x=0.146295
    for _ in range(steps):
        x+=0.5+mu*f(x,a,b)
    return (x-0.146295)/steps

for b in (1.0,2.0,3.0):
    for mu in (0.014,-0.014):
        empirical=rotation(mu,1.,b)
        target=.5+coef(1.,b)*mu*abs(mu)
        ok(abs(empirical-target)<0.00014,'finite numerical rotation comparison')
for b in (0.0,4.1,-4.1,5.0):
    for mu in (0.012,-0.012):
        empirical=rotation(mu,1.,b)
        ok(abs(empirical-.5)<0.000014,'finite locking comparison')

print('PASS',checks,'checks; finite numerics are diagnostic only')
