#!/usr/bin/env python3
"""Finite checks of the five-point split-cone convolution formula."""
import cmath
import math
import random

POINTS = ((0, 0), (1, 0), (2, 0), (0, 1), (0, 2))
W = cmath.exp(2j * math.pi / 3)
R = (math.sqrt(33) - 1) / 4
K = (729 + 33 * math.sqrt(33)) / 296

def energies(values):
    a = {p: values[j] for j, p in enumerate(POINTS)}
    conv = {(u, v): 0j for u in range(3) for v in range(3)}
    for x in POINTS:
        for y in POINTS:
            conv[((x[0]+y[0])%3, (x[1]+y[1])%3)] += a[x]*a[y]
    vconv = sum(abs(z)**2 for z in conv.values())
    efour = 0.0
    for u in range(3):
        for v in range(3):
            z = sum(a[x]*W**(u*x[0]+v*x[1]) for x in POINTS)/3
            efour += abs(z)**4
    p = sum(abs(z)**2 for z in values)
    return vconv, efour, p

rng = random.Random(20261009)
for j in range(2000):
    z = [complex(rng.uniform(-2,2),rng.uniform(-2,2)) for _ in range(5)]
    v,e,p = energies(z)
    assert abs(e-v/9) < 1e-8 * max(1,v/9)
    assert v <= (K+1e-12)*p*p
for j in range(3):
    for k in range(3):
        z = [R,W**j,W**(-j),W**k,W**(-k)]
        v,e,p=energies(z)
        assert abs(v/p**2-K) < 1e-12
        assert abs(e-K*p**2/9)<1e-12
assert abs((R**4+24*R**2+16*R+36)/(R*R+4)**2-K)<1e-12
assert 77/25>3
print('VERIFY_OK: 2000 complex trials, 2000 Plancherel tests, 9 sharp character extremizers, radical constant')
