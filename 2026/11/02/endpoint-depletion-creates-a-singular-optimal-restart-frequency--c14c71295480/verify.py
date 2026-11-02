"""Finite numerical cross-checks for Brownian resetting to a symmetric beta law.

Run: python verify.py
Dependencies: numpy, scipy
These tests do not replace the analytic proof for arbitrary parameters.
"""

import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
from scipy.special import beta, gamma, hyp1f1
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

CHECKS = 0

def check(condition, message):
    global CHECKS
    if not condition:
        raise AssertionError(message)
    CHECKS += 1


def success(alpha, k):
    """Laplace transform of the absorption time before reset, L=D=1."""
    return 2.0 * hyp1f1(alpha+1, 2*alpha+2, -k) / (1.0 + math.exp(-k))


def mean(alpha, k):
    if k == 0:
        p = alpha+1
        return p / (4 * (2*p+1))
    F = success(alpha, k)
    return (1.0 - F) / (k*k*F)


def high_rate(alpha, k):
    return gamma(alpha+1) / (2*gamma(2*alpha+2)) * k**(alpha-1)


def small_rate_coefficient(alpha):
    p = alpha+1
    return p*(2*p*p-p-7)/(96*(2*p+1)**2*(2*p+3))


# Direct integration of the one-particle boundary-value solution.
for alpha in [0., .5, 1., 1.05, 1.5, 2.]:
    B = beta(alpha+1, alpha+1)
    for k in [.25, 1., 4., 12., 40.]:
        q, _ = quad(lambda x: math.exp(-k*x)*x**alpha*(1-x)**alpha,
                    0., 1., epsabs=1e-13, epsrel=1e-12)
        direct = 2*q / (B*(1+math.exp(-k)))
        check(abs(success(alpha,k)-direct) < 8e-11,
              f'integral vs Kummer: alpha={alpha}, k={k}')

# Exact critical beta-shape expression and the unattained sharp infimum.
for k in [.4, .8, 1.5, 3., 5., 10., 25., 100., 500.]:
    exact = 12*(k-2*math.tanh(k/2))/k**3
    check(abs(success(1.,k)-exact) < 8e-10*max(1.,exact),
          f'exact critical formula at k={k}')
    check(mean(1., k) > 1/12, f'critical strict bound at k={k}')

# Small-reset-rate derivative from the independent first two exit moments.
for alpha in [0., .6, 1., 1.08, 1.2, 2.]:
    h = .005
    num_slope = (mean(alpha,math.sqrt(2*h))-mean(alpha,math.sqrt(h)))/h
    check(abs(num_slope-small_rate_coefficient(alpha)) < 2.5e-5,
          f'low-rate derivative at alpha={alpha}')

# Large resetting regimes, including each side of the alpha=1 boundary.
for alpha in [-.5, 0., .5, 1., 1.5, 2.]:
    for k in [100., 500., 1500.]:
        val = mean(alpha,k)
        asym = high_rate(alpha,k)
        check(abs(val/asym-1) < .13, f'high rate at {alpha},{k}')

# Independent finite-state absorbing diffusion, plus complete resetting.
def lattice_mean(alpha,k,n=360):
    sites = np.arange(1,n)/n
    weights = (sites*(1-sites))**alpha
    weights /= weights.sum()
    r = k*k
    lap = diags([-n*n*np.ones(n-2),
                 (2*n*n+r)*np.ones(n-1),
                 -n*n*np.ones(n-2)], [-1,0,1], format='csc')
    u = spsolve(lap, np.ones(n-1))
    averaged = float(weights@u)
    return averaged/(1-r*averaged)

for alpha in [0., 1., 1.1, 2.]:
    for k in [.8, 2., 5., 8.]:
        approximation=lattice_mean(alpha,k)
        check(abs(approximation/mean(alpha,k)-1)<.015,
              f'independent discretized process at {alpha},{k}')

# Singular optimizer: these numerical tests only illustrate the proven limit.
previous_error=1.
for eps in [.08,.04,.02,.01,.005]:
    opt=minimize_scalar(lambda z: mean(1+eps,math.exp(z)),
                        bounds=(math.log(.3),math.log(10000)),
                        method='bounded', options={'xatol':1e-10})
    k=math.exp(opt.x)
    error=abs(eps*k/2-1)
    check(opt.success, f'optimization numerical failure at {eps}')
    check(error < previous_error, f'nonconvergent numerical scaling at {eps}')
    previous_error=error
    check(opt.fun < mean(1+eps,0),f'optimizer not improving at {eps}')

print(f'PASS: {CHECKS} finite assertions; analytic theorem not inferred from numerical samples.')
