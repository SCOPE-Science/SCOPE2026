"""Supplementary numerical checks for Gaussian Fock local-limit constants.
Run: python CHECK.py   (requires numpy, scipy).
Finite calculations below do not prove the theorem's infinite-dimensional claims.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
from scipy.special import gammaln

checks = 0

def verify(condition, message):
    global checks
    assert condition, message
    checks += 1


def log_kernel(z, w, alpha, p):
    """Logarithm of the exact reproducing-kernel power series."""
    zcw = z * np.conjugate(w)
    peak = p * alpha * abs(zcw)**p
    count = int(max(180, peak + 24 * math.sqrt(peak + 1) + 110))
    n = np.arange(count + 1, dtype=float)
    terms = n * np.log(zcw) + (n / p) * np.log(alpha) - gammaln((n + 1) / p)
    center = terms.real.max()
    return gammaln(1 / p) + center + np.log(np.exp(terms - center).sum())


def local_kernel(R, alpha, p, u, v):
    delta = R**(1 - p)
    z, w = R + delta * u, R + delta * v
    k_zz = log_kernel(z, z, alpha, p)
    k_zw = log_kernel(z, w, alpha, p)
    log_kappa = math.log(p / math.pi) + math.log(alpha) / p - gammaln(1 / p)
    return math.exp(2 * math.log(delta) + log_kappa - alpha * abs(w)**(2 * p)
                    + 2 * k_zw.real - k_zz.real)


for p in (1.5, 2.0, 3.0):
    for alpha in (0.8, 1.7):
        # The normalized radial measure has total mass one and the stated moments.
        for n in (0, 1, 2, 3):
            integrand = lambda r: 2 * p * alpha**(1/p) / math.gamma(1/p) * r**(2*n+1) * math.exp(-alpha * r**(2*p))
            observed = quad(integrand, 0, np.inf, limit=200)[0]
            expected = alpha**(-n / p) * math.gamma((n + 1) / p) / math.gamma(1 / p)
            verify(abs(observed - expected) <= 4e-9 * max(1, expected),
                   f'moment failed: {p=}, {alpha=}, {n=}')
        u, v = 0.2 + 0.3j, -0.4 + 0.1j
        target = alpha * p*p / math.pi * math.exp(-alpha * p*p * abs(u-v)**2)
        early = local_kernel(2.5, alpha, p, u, v)
        later = local_kernel(4.0, alpha, p, u, v)
        verify(abs(later / target - 1) < 0.055,
               f'local Gaussian kernel constant failed: {p=}, {alpha=}')
        verify(abs(later / target - 1) < abs(early / target - 1),
               f'local asymptotics did not improve: {p=}, {alpha=}')
        rate = alpha * p*p
        for freq in (0.0, 0.7, 1.5, 2.3):
            one_dim = math.sqrt(rate / math.pi) * quad(
                lambda x: math.exp(-rate*x*x)*math.cos(freq*x), -np.inf, np.inf,
                limit=200)[0]
            verify(abs(one_dim - math.exp(-freq*freq/(4*rate))) < 1e-10,
                   f'Gaussian Fourier multiplier failed: {p=}, {alpha=}, {freq=}')

# Optimize the difference of the two limit heat multipliers independently.
for r in (0.4, 0.5, 0.8, 1.5, 2.0, 3.0, 4.0):
    alpha, beta = r, 1.0
    objective = lambda s: -abs(math.exp(-s/alpha) - math.exp(-s/beta))
    opt = minimize_scalar(objective, bounds=(0, 40), method='bounded',
                          options={'xatol': 1e-12})
    predicted = abs(r-1) * r**(-r/(r-1))
    verify(abs(-opt.fun - predicted) < 1e-9,
           f'wrong exact two-parameter multiplier maximum: {r=}')

print(f'CHECK_OK {checks}')
