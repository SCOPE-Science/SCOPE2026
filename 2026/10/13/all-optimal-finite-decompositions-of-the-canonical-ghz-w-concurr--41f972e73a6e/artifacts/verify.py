#!/usr/bin/env python3
import cmath
import math


def close(a, b, tol=1e-11):
    return abs(a-b) <= tol


def det_reduced_A(q, theta):
    # State: sqrt(q) GHZ + exp(i theta) sqrt(1-q) W.
    a = math.sqrt(q)
    b = cmath.exp(1j*theta)*math.sqrt(1-q)
    p0 = abs(a)**2/2 + 2*abs(b)**2/3
    p1 = abs(a)**2/2 + abs(b)**2/3
    off = a*b.conjugate()/math.sqrt(6)
    return p0*p1 - abs(off)**2


def g(lam, r):
    return (5*lam*lam*r*r - 4*lam*r + 8)/9

# Phase independence and the closed pure-state formula.
for q in [0.0, 0.07, 0.4, 0.73, 1.0]:
    target = (5*q*q - 4*q + 8)/9
    for theta in [0.0, 0.37, 1.9, math.pi]:
        assert close(4*det_reduced_A(q, theta), target)

# The minimal two-state phase polygon.
for lam in [0.1, 0.4, 0.83]:
    p = [0.5, 0.5]
    z = [1+0j, -1+0j]
    assert abs(sum(pi*zi for pi, zi in zip(p, z))) < 1e-14
    assert close(sum(pi*g(lam, 1.0) for pi in p), g(lam, 1.0))

# The source's four-column co-isometry is just duplicated +/- states.
row1 = [0.5, 0.5, 0.5, 0.5]
row2 = [0.5, 0.5, -0.5, -0.5]
assert close(sum(x*x for x in row1), 1.0)
assert close(sum(x*x for x in row2), 1.0)
assert close(sum(x*y for x, y in zip(row1, row2)), 0.0)
for lam in [0.2, 0.6]:
    probs = [lam*x*x + (1-lam)*y*y for x, y in zip(row1, row2)]
    assert all(close(p, 0.25) for p in probs)
    rs = [x*x/p for x, p in zip(row1, probs)]
    assert all(close(r, 1.0) for r in rs)

# Strict Jensen gap for a nonconstant admissible weighted r profile with mean one.
for lam in [0.15, 0.4, 0.9]:
    p = [0.5, 0.5]
    r = [0.6, 1.4]
    avg = sum(pi*g(lam, ri) for pi, ri in zip(p, r))
    assert avg > g(lam, 1.0) + 1e-12

print('VERIFY_OK')
