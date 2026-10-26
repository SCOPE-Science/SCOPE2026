#!/usr/bin/env python3
"""Finite diagnostics for the pure-state p-Bures sharp quasi-triangle formula.

These tests check arithmetic and sample cases; they do not replace the proof.
"""
import math
import random

rng = random.Random(601211)
PI2 = math.pi / 2


def f(p, theta):
    if theta <= 0:
        return 0.0
    if theta >= PI2:
        return 1.0
    return math.sqrt(-math.expm1(p * math.log(math.cos(theta))))


def k(p):
    return 1.0 / (2.0 * f(p, math.pi / 4))


def norm(v):
    return math.sqrt(sum(abs(z)**2 for z in v))


def unit(v):
    n = norm(v)
    return tuple(z/n for z in v)


def inner(u, v):
    return sum(a.conjugate()*b for a,b in zip(u,v))


def dist(p, u, v):
    a = min(1.0, abs(inner(u,v)))
    return math.sqrt(2.0 * max(0.0, 1-a**p))


checks = 0
for p in (0.025, 0.1, 0.25, 0.5, 0.6, 2.0/3.0):
    kp = k(p)
    # The orthogonal-endpoint midpoint gives equality.
    u = (1+0j, 0+0j)
    v = (1/math.sqrt(2), 1/math.sqrt(2))
    w = (0+0j, 1+0j)
    assert abs(dist(p,u,w) - kp*(dist(p,u,v)+dist(p,v,w))) < 2e-13
    checks += 1
    # Angular Jensen bound and the monotone-halving envelope.
    for i in range(1,180):
        s = PI2 * i/180
        assert f(p,s)/(2*f(p,s/2)) <= kp + 4e-13
        checks += 1
        for t in (0.1,0.25,0.4,0.5,0.7,0.9):
            x = t*s
            assert f(p,s) <= kp * (f(p,x)+f(p,s-x)) + 4e-13
            checks += 1
    # Complex pure-state triples, including non-geodesic configurations.
    for j in range(1200):
        vecs = []
        for h in range(3):
            vecs.append(unit((complex(rng.gauss(0,1),rng.gauss(0,1)),
                              complex(rng.gauss(0,1),rng.gauss(0,1)))))
        u,v,w = vecs
        assert dist(p,u,w) <= kp * (dist(p,u,v)+dist(p,v,w)) + 3e-12
        checks += 1
    # Critical convexity factorization at p=2/3.
    for j in range(100):
        r = rng.random()
        t = r**(2/3)
        lhs = 1+2*r*r-(2+r*r)*r**(2/3)
        rhs = (1-t)**3*(1+t)
        assert abs(lhs-rhs) < 6e-13
        checks += 1

# Above 2/3 the angular function is concave sufficiently close to zero;
# the exact convexity boundary is determined analytically in the proof.
print(f"PASS: {checks} deterministic finite checks; exact sharp midpoint attained")
