#!/usr/bin/env python3
"""Reproducible finite and numerical checks of the signed-antichain join angular law.

Needs numpy and scipy. Finite tests are not proof of the asymptotic assertions.
"""
from itertools import product
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar, brentq
from scipy.special import log_ndtr, erf, ndtri
from scipy.stats import qmc

rng = np.random.default_rng(20261017)

def vertices(p, q):
    return np.array(
        [list(s) + [0] * q for s in product((-1, 1), repeat=p)]
        + [[0] * p + list(s) for s in product((-1, 1), repeat=q)],
        dtype=float,
    )

def log_mgf_half(s):
    return math.log(2.0) + 0.5 * s * s + float(log_ndtr(s))

def rate(alpha):
    f = lambda s: alpha * log_mgf_half(-s) + (1-alpha) * log_mgf_half(s)
    opt = minimize_scalar(f, bounds=(0.0, 50.0), method='bounded',
                          options={'xatol': 1e-12})
    assert opt.success
    return -f(opt.x)

def crossing(alpha):
    return 2 * rate(alpha) - (2 * alpha - 1) * math.log(2.0)

# Direct support function: vertices generated independently from signed antichains.
for p in range(1, 5):
    for q in range(1, 5):
        V = vertices(p, q)
        assert len(V) == 2**p + 2**q
        for _ in range(100):
            x = rng.normal(size=p+q)
            direct = np.max(V @ x)
            formula = max(np.abs(x[:p]).sum(), np.abs(x[p:]).sum())
            assert abs(direct-formula) < 1e-12
print('SUPPORT_OK: 1600 direct polytope comparisons')

# At p=q=1 all four normal cones have probability 1/4, so C2=1/4.
assert abs((2**-1) * (0.5**2) * 2 - 0.25) < 1e-15

# At (p,q)=(2,1), an exact trivariate Gaussian orthant identity
# gives the smaller-block mass 1-4 arcsin(1/sqrt(3))/pi.
small_exact = 1.0 - 4.0 / math.pi * math.asin(1/math.sqrt(3))
# The sum of two independent folded normals has density
# (2/sqrt(pi))*exp(-s^2/4)*erf(s/2).
density_sum2 = lambda s: 2 / math.sqrt(math.pi) * math.exp(-s*s/4) * erf(s/2)
small_quad, err = quad(lambda s: density_sum2(s)*math.erfc(s/math.sqrt(2)),
                       0, np.inf, epsabs=5e-13, epsrel=5e-13)
assert err < 1e-11
assert abs(small_quad-small_exact) < 2e-12
coll = 0.25*(1-small_exact)**2 + 0.5*small_exact**2
assert 0.17 < coll < 0.18
print('EXACT_ANGLE_OK: orthant identity and independent 1D integral', small_exact, coll)

# Reproducible quasi-Monte-Carlo geometric normal-cone exposure frequencies.
p, q = 2, 1
points = qmc.Sobol(d=p+q, scramble=True, seed=371).random_base2(17)
z = ndtri(points)
V = vertices(p, q)
winning_vertex = np.argmax(z @ V.T, axis=1)
counts = np.bincount(winning_vertex, minlength=len(V)) / len(points)
assert max(abs(counts[:4]-(1-small_exact)/4)) < 0.005
assert max(abs(counts[4:]-small_exact/2)) < 0.005
print('NORMAL_CONES_OK: 131072 quasi-random exposures')

# Separate stationary-equation evaluation for the exponential tilt.
def halfnormal_tilt_mean(s):
    return s + math.exp(-0.5*s*s - 0.5*math.log(2*math.pi) - float(log_ndtr(s)))

def rate_from_stationarity(alpha):
    stationary = lambda s: (1-alpha)*halfnormal_tilt_mean(s) - alpha*halfnormal_tilt_mean(-s)
    root_s = brentq(stationary, 0.0, 45.0, xtol=1e-12)
    return -alpha*log_mgf_half(-root_s) - (1-alpha)*log_mgf_half(root_s)

for alpha in (0.55, 0.60, 0.70, 0.85):
    assert abs(rate(alpha)-rate_from_stationarity(alpha)) < 3e-10
print('TILT_STATIONARITY_OK: independent saddle-point equations')

# Two computational expressions for the half-normal rate.
for alpha in (0.55, 0.60, 0.70, 0.85):
    val = rate(alpha)
    assert val > 0
    assert math.isfinite(val)
assert crossing(0.60) < -0.06
assert crossing(0.70) > 0.015
root = brentq(crossing, 0.60, 0.70, xtol=1e-13)
assert 0.68863 < root < 0.68864
assert abs(crossing(root)) < 2e-12
print('RATE_OK: unique-root numerical cross-check', root)
print('ALL_CHECKS_PASS')
