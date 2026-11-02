"""Numerical corroboration of finite convolution caustic formulas, not a proof."""
from math import comb, gamma, pi, sqrt, log
import numpy as np
from scipy.integrate import quad
from scipy.signal import fftconvolve
from scipy.special import betainc


def b(a):
    return 2 ** (a - 1) * gamma(a + .5) / sqrt(pi)


def predicted(n, a, k, side, q):
    if k == 0 or k == n:
        return b(a) ** n / gamma(n * a) * q ** (n * a - 1)
    exponent = (n - k if side == '+' else k) * a
    return comb(n, k) * b(a) ** n * gamma(1 - n * a) / (gamma(exponent) * gamma(1 - exponent)) * q ** (n * a - 1)


def discretized(n, a, power=13):
    h = 2. / (2 ** power)
    edges = np.linspace(-1, 1, 2 ** power + 1)
    mass = np.diff(betainc(a, a, (edges + 1) / 2))
    v = mass.copy()
    for _ in range(n - 1):
        v = np.maximum(fftconvolve(v, mass), 0)
    assert abs(sum(v) - 1) < 2e-10
    centers_start = -n + n * h / 2
    return h, centers_start, v


def verify_n3():
    n, a = 3, .2
    h, start, masses = discretized(n, a)
    for k in (1, 2):
        for side in ('+', '-'):
            for q in (.01, .02, .04):
                x = (2 * k - n) + (q if side == '+' else -q)
                j = round((x - start) / h)
                observed = masses[j] / h
                theoretical = predicted(n, a, k, side, q)
                assert abs(observed / theoretical - 1) < .08, (k, side, q, observed, theoretical)
    # Exact internal-amplitude ratio is generically not 1.
    assert abs(predicted(3, a, 1, '+', .01) / predicted(3, a, 1, '-', .01) - 1) > .1
    print('N=3: normalization, 12 two-sided asymptotic comparisons and asymmetry passed')


def verify_n2_critical():
    # Cross-check critical log coefficient against a direct, independent
    # quadrature of the convolution of two symmetric beta densities at alpha=.5.
    a = .5
    c = gamma(a + .5) / (sqrt(pi) * gamma(a))
    def f(x):
        return c * (1 - x * x) ** (a - 1) if abs(x) < 1 else 0.
    def d(q):
        # Split integrable edge singularities; quadrature is finite for q!=0.
        lo = max(-1., q - 1.)
        hi = min(1., q + 1.)
        x, _ = quad(lambda t: f(t) * f(q - t), lo, hi, epsabs=2e-9, limit=800, points=[lo, hi])
        return x
    q1, q2 = 1e-3, 1e-4
    observed = (d(q2) - d(q1)) / log(q1 / q2)
    coeff = comb(2, 1) * b(a) ** 2 / (gamma(a) ** 2)
    assert abs(observed / coeff - 1) < .01, (observed, coeff)
    print('N=2: independent critical logarithmic slope corroborated')


if __name__ == '__main__':
    verify_n3()
    verify_n2_critical()
    print('All corroboration checks passed; analytical proof remains essential.')
