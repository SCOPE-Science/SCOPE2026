#!/usr/bin/env python3
"""Exact and floating tests for three-band, common-emissivity thermal mixtures.

Requires Python 3 and SymPy. Finite tests corroborate, but do not replace,
the all-temperature convexity and intermediate-value proofs.
"""
from fractions import Fraction as F
import random
import sympy as sp

x = sp.symbols('x', positive=True)
f = x**3 / (1 - 2*x + 2*x**2)
assert sp.simplify(sp.diff(f, x, 2) - (2*x*(2*x**2-6*x+3)/(1-2*x+2*x*x)**3)) == 0
assert sp.simplify((x/sp.Integer(2) - f) - x*(1-2*x)/(2*(1-2*x+2*x*x))) == 0
assert sp.simplify((f/x**2) - (x/(1-2*x+2*x*x))) == 0
print('Symbolic: three curvature/endpoint identities verified')

rng = random.Random(314159)
assertions = 3

def curve(u):
    return u**3/(1-2*u+2*u*u)

def model(r, s, c, d):
    arr = [c/F(r**k-1)+d/F(s**k-1) for k in (1, 2, 4)]
    return arr[1]/arr[0], arr[2]/arr[0], arr

# Exact rational tests for each two-temperature finite mixture, including single-T cases.
for i in range(1200):
    r = F(rng.randint(11, 200), rng.randint(2, 10))
    s = F(rng.randint(11, 200), rng.randint(2, 10))
    if r <= 1 or s <= 1:
        continue
    c = F(rng.randint(1, 60), rng.randint(1, 40))
    d = F(rng.randint(1, 60), rng.randint(1, 40))
    u, v, arr = model(r, s, c, d)
    assert 0 < u < F(1, 2)
    assertions += 1
    assert curve(u) <= v < u/2
    assertions += 1
    assert (v == curve(u)) == (r == s)
    assertions += 1
    if r == s:
        assert u == F(1,r+1)
        assertions += 1

# One-parameter constructive approximation of all interior points.
# Proof is the IVT; these floating checks only stress-test the implementation.
def float_curve(t):
    return t**3/(1-2*t+2*t*t)
def chord_value(u, e):
    a = e
    b = .5-e
    if b-a <= 1e-14:
        return float_curve(u)
    lam = (b-u)/(b-a)
    return lam*float_curve(a)+(1-lam)*float_curve(b)
for i in range(400):
    u = rng.uniform(.005, .495)
    base = float_curve(u)
    top = u/2
    vtarget = base+(top-base)*rng.uniform(.002,.998)
    lower = 0.0
    upper = min(u,.5-u)
    for _ in range(85):
        mid=(lower+upper)/2
        if chord_value(u,mid) > vtarget:
            lower=mid
        else:
            upper=mid
    est=chord_value(u,(lower+upper)/2)
    assert abs(est-vtarget) < 2e-13
    assertions += 1

r,s,c,d=F(16),F(3,2),F(1),F(1,20)
u,v,_=model(r,s,c,d)
assert u == F(112,425)
assert v == F(104986,1419925)
assert v/u**2 == F(3187075,2993536)
assert v/u**2 > 1
assertions += 4
print('Finite reproducibility assertions:', assertions, 'passed')
