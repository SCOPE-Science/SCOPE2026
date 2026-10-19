"""Numerical cross-checks for the reset-age mixed two-time edge law.

Run: python check.py. Requires numpy and scipy. This verifies finite integrals
and Gaussian probabilities; the asymptotic theorem is proved analytically.
"""
from math import exp, log, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.special import erf, erfc, ndtr
from scipy.stats import norm
from numpy.polynomial.laguerre import laggauss

checks = 0

def near(x, y, eps=2e-7):
    global checks
    assert np.isfinite(x) and abs(x - y) < eps, (x, y, eps)
    checks += 1

def hu(x, y, s, a):
    lam = sqrt(s / (2.0 * a))
    h = exp(-x) * ndtr(lam + (y - x) / (2 * lam))
    h += exp(-y) * ndtr(lam + (x - y) / (2 * lam))
    return exp(-h)

def limit_cdf(x, y, s):
    return quad(lambda a: exp(-a) * hu(x, y, s, a), 0, np.inf,
                epsabs=1e-11, epsrel=1e-11)[0]

def limit_cdf_laguerre(x, y, s):
    nodes, weights = laggauss(100)
    return sum(w * hu(x, y, s, a) for a, w in zip(nodes, weights))

def bvn_union(u, v, rho):
    # P(Z1>u or Z2>v) evaluated independently as a 1D Gaussian integral.
    # P(Z2>v) + P(Z1>u,Z2<=v).
    sd = sqrt(1 - rho * rho)
    exclusive = quad(lambda z: norm.pdf(z) * norm.cdf((v - rho * z) / sd),
                     u, np.inf, epsabs=1e-13, epsrel=2e-11)[0]
    return norm.sf(v) + exclusive

# Identity yielding the explicit stretched-exponential tail-dependence law.
for s in [0.01, 0.1, 0.25, 1., 2., 4., 9., 16.]:
    chi = quad(lambda a: exp(-a) * erfc(sqrt(s / (4 * a))),
               0, np.inf, epsabs=2e-12, epsrel=2e-12)[0]
    near(chi, exp(-sqrt(s)), 1e-9)
    mean_coefficient = quad(lambda a: exp(-a) * 2 * ndtr(sqrt(s / (2*a))),
                            0, np.inf, epsabs=1e-11)[0]
    near(mean_coefficient, 2-exp(-sqrt(s)), 1e-9)

# Independent quadrature strategies for the mixed Huesler--Reiss CDF.
for s in [0.05, 0.25, 1., 3., 9.]:
    for x, y in [(-0.6, 0.4), (0., 0.), (0.5, -0.2), (1.2, 1.2)]:
        near(limit_cdf(x, y, s), limit_cdf_laguerre(x, y, s), 2e-4)
        near(limit_cdf(x, y, s), limit_cdf(y, x, s), 1e-10)

# Non-max-stability: mixing over the random age is genuinely nontrivial.
for s in [0.15, 1.0, 5.0]:
    p = limit_cdf(0.0, 0.0, s)
    shifted_squared = limit_cdf(log(2), log(2), s)**2
    assert shifted_squared < p - 1e-7, (s, shifted_squared, p)
    checks += 1

# Conditional finite-N Gaussian probabilities tend toward the HR law.
# Rates are logarithmic; test convergence after stepping N to the large range.
for s, a, x, y in [(0.25, 1.0, 0., 0.), (1.0, 1.0, 0.2, -0.4),
                    (3.0, 0.5, 0.3, 0.6), (0.7, 2.0, -0.3, 0.7)]:
    target = hu(x,y,s,a)
    errors = []
    for N in [300, 10000, 1000000]:
        b = norm.isf(1/N)
        rho = sqrt(a / (a + s / log(N)))
        union = bvn_union(b + x/b, b + y/b, rho)
        assert 0 < union < 1
        cdf = exp(N * np.log1p(-union))
        errors.append(abs(cdf-target))
        checks += 1
    assert errors[-1] < errors[0] and errors[-1] < 0.09, (s,a,errors)
    checks += 1

# At zero lag the two maxima coincide; at very long log-scaled lag
# the limiting Gumbel residuals become independent.
for x,y in [(0.,0.),(-0.3,0.7),(0.2,1.1)]:
    near(limit_cdf(x,y,1e-7), exp(-exp(-min(x,y))), 2e-3)
    near(limit_cdf(x,y,1000), exp(-exp(-x)-exp(-y)), 2e-5)

# A direct Monte Carlo check of empirical-variance normalization under no reset.
# Conditional on A and no reset this is an iid bivariate Gaussian sample.
rng = np.random.default_rng(91753)
N = 1600
s = 1.0
A = 1.25
replicates = 3500
b = norm.isf(1/N)
rho = sqrt(A / (A + s / log(N)))
first = rng.normal(size=(replicates,N))
second = rho*first + sqrt(1-rho*rho)*rng.normal(size=(replicates,N))
Y1 = b * (first.max(axis=1)/np.sqrt(np.mean(first**2,axis=1))-b)
Y2 = b * (second.max(axis=1)/np.sqrt(np.mean(second**2,axis=1))-b)
empirical = np.mean((Y1<=0) & (Y2<=0))
union = bvn_union(b,b,rho)
oracle = exp(N*np.log1p(-union))
assert abs(empirical-oracle)<0.037, (empirical,oracle)
checks += 1

print(f'PASS {checks} cross-check assertions')
print('Monte Carlo joint probability (self-normalized):', round(float(empirical),6))
print('Finite-N oracle-normalized probability:', round(float(oracle),6))
print('Limiting joint CDF s=1 x=y=0:', round(float(limit_cdf(0,0,1)),9))
print('Upper-tail dependence chi(1):', round(float(exp(-1)),9))
