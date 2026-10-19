"""Numerical corroboration of two-annulus Hermite spectral mode asymptotics.
Scientific proof is analytic; tests cover finitely many examples only.
"""
import math
import numpy as np
from scipy.special import gammaln
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss

nodes, weights = leggauss(16)

def eigenvalue(a, n, d, w=1.0):
    total = 0.0
    for c in (a - d * math.sqrt(a), a + d * math.sqrt(a)):
        t = c + 0.5 * w * nodes
        p = np.exp(-t + n * np.log(t) - gammaln(n + 1))
        total += 0.5 * w * float(np.dot(weights, p))
    return total

def argmax(a, d, w=1.0):
    radius = int(4 * max(d, 1.0) * math.sqrt(a) + 12)
    return max(range(max(0, int(a) - radius), int(a) + radius + 1),
               key=lambda n: eigenvalue(a, n, d, w))

checks = 0
for a in (2500., 10000., 40000.):
    n = argmax(a, 1.)
    err = abs((a - n) / (a ** (1. / 3.)) - 2 ** (1. / 3.))
    assert err < 0.06, (a, n, err)
    checks += 1
for a in (2500., 10000.):
    n = argmax(a, 0.7)
    assert abs(n - a) <= 5
    checks += 1
for d in (1.4, 2.):
    xd = brentq(lambda x: x - d * math.tanh(d * x), 0.1, d)
    for a in (2500., 10000.):
        n = argmax(a, d)
        assert abs((n - a) / math.sqrt(a) + xd) < 0.12
        checks += 1
assert abs(2 ** (1.0 / 3.0) - 1.2599210498948732) < 1e-12
checks += 1
print('PASS:', checks, 'numerical checks (not an infinite-degree proof)')
