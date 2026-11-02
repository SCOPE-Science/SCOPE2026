#!/usr/bin/env python3
"""Numerical checks for a field-aligned rotational diffusion hitting-time asymptotic."""
import math
from scipy.integrate import quad
from scipy.special import exp1


def scaled_mean(xi, eta):
    if not (xi > eta / 2 > 0):
        raise ValueError('require xi > eta / 2 > 0')
    def integrand(s):
        if s == 2 * xi:
            return 2 * xi * math.exp(-2 * xi)
        return (math.exp(-s) - math.exp(-2 * xi)) / (s * (1 - s / (2 * xi)))
    return quad(integrand, eta, 2 * xi, epsabs=2e-12, epsrel=2e-12)[0]


def exact_mean(xi, b, D=0.5):
    def integrand(u):
        # Expm1 preserves accuracy at the regular north pole.
        return (math.expm1(xi * (1 - u)) / (1 + u) / (1 - u)
                if u < 1 else xi / 2)
    return quad(integrand, b, 1, epsabs=1e-10, epsrel=1e-11)[0] / (D * xi)


def run():
    checks = 0
    for eta in (0.2, 1., 3.):
        for xi in (10., 20., 50., 100.):
            b = -1 + eta / xi
            direct = exact_mean(xi, b)
            scaled = scaled_mean(xi, eta)
            assert abs(2 * 0.5 * xi * math.exp(-2 * xi) * direct - scaled) < 3e-9
            checks += 1
            two = exp1(eta) + math.exp(-eta) / (2 * xi)
            err = abs(scaled - two)
            # Quadratic remainder, conservative uniform bound at these parameters.
            assert err * xi * xi < 1.0
            checks += 1
        # Leading crossover and second-term coefficient.
        leading = exp1(eta)
        assert abs(scaled_mean(100, eta) - leading - math.exp(-eta) / 200) < 0.00015
        checks += 1
    for b in (-0.8, -0.4, 0.2):
        for xi in (20., 50., 100.):
            exact = exact_mean(xi, b)
            asymp = math.exp(xi * (1 - b)) / (0.5 * xi * xi * (1 - b * b))
            assert 0 < asymp / exact < 1.4
            checks += 1
    print('PASS:', checks, 'deterministic integral and asymptotic checks')


if __name__ == '__main__':
    run()
