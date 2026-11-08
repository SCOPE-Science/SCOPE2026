#!/usr/bin/env python3
"""Finite diagnostic checks for a time-inhomogeneous Friedman urn proof."""
from fractions import Fraction as Q
from math import sqrt, isfinite

checks = 0

def check(b):
    global checks
    assert b
    checks += 1

# Exact finite-state law, urn probabilities, and unconditional moments.
dist = {0: Q(1)}
for n in range(1, 24):
    nxt = {}
    for x, probability in dist.items():
        right = Q(n + 1 - x, 2 * n)
        check(Q(0) <= right <= Q(1))
        for y, chance in ((x + 1, right), (x - 1, 1 - right)):
            nxt[y] = nxt.get(y, Q(0)) + probability * chance
    dist = nxt
    check(sum(dist.values()) == 1)
    check(sum(Q(x)*p for x, p in dist.items()) == 1)
    if n >= 2:
        check(sum(Q(x*x)*p for x, p in dist.items()) == Q(n+4, 3))

# F(z) - (3/2)zF'(z) + (1/2)F''(z) identity, using exact rationals.
for k in range(0, 121):
    z = Q(k, 17)
    F = 48*z + Q(16)*z/(1+z)
    Fp = 48 + Q(16)/(1+z)**2
    Fpp = -Q(32)/(1+z)**3
    L = F - Q(3, 2)*z*Fp + Q(1, 2)*Fpp
    explicit = -24*z + 16*(z-1)*(z*z+Q(3,2)*z+1)/(1+z)**3
    check(L == explicit)
    check(L <= -Q(64,27))

# Exact one-step urn transition against the actual potential.
def F(x):
    return 48*x + 16*x/(1+x)

def V(t,x):
    return t*F(x/sqrt(t))
for t in (10000,10001,25000,100000,1000000):
    for x in (1, 2, 3, int(sqrt(t)), t//2, t-1):
        right = (t+1-x)/(2*t)
        check(0<=right<=1)
        lhs = right*V(t+1,x+1)+(1-right)*V(t+1,x-1)-V(t,x)
        envelope = -64/27+130/sqrt(t)
        check(lhs <= envelope + 1e-8)
        check(envelope < -1)

check(9999 + 6400*sqrt(10003/3) < 380000)
print(f"PASS: {checks} finite exact-rational and floating-point diagnostic checks")
