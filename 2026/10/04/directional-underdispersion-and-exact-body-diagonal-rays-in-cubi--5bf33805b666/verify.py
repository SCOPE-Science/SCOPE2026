#!/usr/bin/env python3
import math


def energy(ell, p):
    nu = len(p)
    c = sum(math.cos(ell*x) for x in p) / nu
    c = max(-1.0, min(1.0, c))
    return nu * math.acos(c)**2 / (ell*ell)


def continuum(p):
    return sum(x*x for x in p)


def variance_sq(p):
    vals = [x*x for x in p]
    m = sum(vals)/len(vals)
    return sum((x-m)**2 for x in vals)/len(vals)

checks = 0
ell = 0.73
for nu in range(2, 6):
    lim = math.pi/ell
    vals = [-0.92*lim, -0.45*lim, 0.0, 0.37*lim, 0.81*lim]
    # Deterministic structured paths rather than a combinatorial full grid.
    for a in vals:
        for b in vals:
            p = [a, b] + [0.23*lim*((j % 3)-1) for j in range(nu-2)]
            e = energy(ell, p)
            c = continuum(p)
            assert e <= c + 5e-12*max(1.0, c), (nu, p, e, c)
            checks += 1

for nu in range(2, 7):
    lim = math.pi/ell
    r = 0.61*lim
    p = [r if j % 2 == 0 else -r for j in range(nu)]
    e = energy(ell, p)
    c = continuum(p)
    assert abs(e-c) <= 2e-12*max(1.0, c), (nu, e, c)
    checks += 1

cases = [
    [1.2, 0.3],
    [1.1, -0.4, 0.7],
    [0.2, 0.8, -1.0, 0.5],
]
ell2 = 0.01
for p in cases:
    nu = len(p)
    observed = (energy(ell2, p) - continuum(p))/(ell2*ell2)
    predicted = -nu*variance_sq(p)/12.0
    assert abs(observed-predicted) < 2e-6, (p, observed, predicted)
    checks += 1

print(f'VERIFY_OK checks={checks} dimensions=2..6 coefficient_cases={len(cases)}')
