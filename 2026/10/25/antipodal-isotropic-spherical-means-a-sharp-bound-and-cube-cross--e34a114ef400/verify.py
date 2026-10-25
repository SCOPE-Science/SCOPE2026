"""Reproduce finite checks of antipodal spherical Fréchet mean identities.

This script supports, but does not replace, the analytic all-dimensional proof.
"""
import itertools
import math
import random


def cube(d):
    return [tuple(s / math.sqrt(d) for s in signs)
            for signs in itertools.product((-1, 1), repeat=d)]


def cross(d):
    out = []
    for j in range(d):
        for sign in (-1, 1):
            v = [0.0] * d
            v[j] = float(sign)
            out.append(tuple(v))
    return out


def frechet(x, vertices):
    return sum(math.acos(max(-1., min(1., sum(a*b for a, b in zip(x, v)))))**2
               for v in vertices) / len(vertices)


def unit(x):
    n = math.sqrt(sum(t*t for t in x))
    return [t/n for t in x]


checks = 0
rng = random.Random(802371)
for d in range(2, 9):
    C, X = cube(d), cross(d)
    target = math.pi**2 / 4 + math.asin(1 / math.sqrt(d))**2
    axial = [1.] + [0.] * (d - 1)
    diagonal = [1 / math.sqrt(d)] * d
    assert abs(frechet(axial, C) - target) < 1e-11
    assert abs(frechet(diagonal, X) - target) < 1e-11
    checks += 2
    for _ in range(100):
        x = unit([rng.gauss(0, 1) for _ in range(d)])
        sc4 = sum(v**4 for v in x)
        bound_cube = 2*(1-sc4)/(3*d*d)
        bound_cross = sum((v*v - 1/d)**2 for v in x)/(3*d)
        assert frechet(x, C) >= target + bound_cube - 1e-11
        assert frechet(x, X) >= target + bound_cross - 1e-11
        checks += 2
        fourth_cube = sum(sum(xi * vi for xi,vi in zip(x,v))**4 for v in C)/len(C)
        assert abs(fourth_cube-(3-2*sc4)/(d*d)) < 2e-13
        checks += 1
print('PASS: %d finite numerical identities and bounds, dimensions 2..8.' % checks)
