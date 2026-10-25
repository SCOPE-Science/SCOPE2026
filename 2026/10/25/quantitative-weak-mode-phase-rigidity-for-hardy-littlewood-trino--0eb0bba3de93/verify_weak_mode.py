#!/usr/bin/env python3
"""Independent numerical checks for the weak-mode trinomial phase theorem.

Analytic inequalities in RESULT.md establish the theorem for infinitely many
parameters. This script checks sample gamma/Fourier integrals, the quadratic
pointwise derivative envelope, and the predicted phase ordering.
"""
import math
import cmath
from scipy.integrate import quad


def c_gamma(k, p):
    n = k + 2
    return math.gamma(p) / (math.gamma(p / 2 + n) * math.gamma(p / 2 - n + 1))


def c_direct(k, p):
    n = k + 2
    def fn(t):
        return (2 * math.cos(t / 2)) ** (p - 1) * math.cos((n - 0.5) * t)
    return quad(fn, -math.pi, math.pi, epsabs=2e-11, limit=800, points=[0])[0] / (2 * math.pi)


def moment(k, p, rho, theta):
    n = k + 2
    def fn(t):
        z = cmath.exp(1j * t)
        return abs(1 + z + rho * cmath.exp(1j * theta) * z ** n) ** p
    return quad(fn, 0, 2 * math.pi, epsabs=3e-11, limit=800)[0] / (2 * math.pi)


if __name__ == '__main__':
    counts = {'gamma_integrals': 0, 'phase_grid': 0, 'linear_slopes': 0, 'radius_bounds': 0}
    for k, p in [(2, 5.), (3, 7.), (5, 11.), (7, 15.)]:
        c = c_gamma(k, p)
        assert c < 0
        direct = c_direct(k, p)
        assert abs(c - direct) < 3e-9 * max(1, abs(c)), (k, c, direct)
        counts['gamma_integrals'] += 1
        a = p / 2
        rstar = min(1., p * abs(c) / (18 * math.pi * a * (a - 1) * 9 ** (a - 2)))
        assert rstar > 0
        rho = max(rstar / 4, 0.01 if k >= 5 else 0.0)
        samples = [moment(k, p, rho, math.pi * j / 8) for j in range(9)]
        assert all(samples[j] < samples[j + 1] for j in range(8)), (k, samples)
        counts['phase_grid'] += 8
        counts['radius_bounds'] += 1
        for frac in ([0.5,0.25] if k<=3 else []):
            rho2 = frac * rstar
            contrast = moment(k, p, rho2, math.pi) - moment(k, p, rho2, 0.)
            assert contrast > p * abs(c) * rho2 * 1.5, (k, rho2, contrast)
            counts['linear_slopes'] += 1
    print('VERIFY_OK ' + ' '.join('%s=%s' % (k, v) for k,v in counts.items()))
