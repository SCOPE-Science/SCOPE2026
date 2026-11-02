"""Reproducible exact parameter arithmetic and numerical small-hole diagnostics.

Requires Python 3 and NumPy. Numerical spectra corroborate, but do not prove,
the limiting escape-rate theorem.
"""

from fractions import Fraction
from math import log, sqrt
import numpy as np


def cusp_parameters(theta):
    k = (1.0 - theta / 2.0) / sqrt(2.0)
    lam = 1.0 + theta / 2.0
    return k, lam


def inverse_data(y, theta):
    k, lam = cusp_parameters(theta)
    u = (np.sqrt(k * k + theta * (1.0 - y)) - k) / theta
    weight = u / (k + theta * u)
    left, right = 0.5 - u * u, 0.5 + u * u
    return left, right, weight


def forward(x, theta):
    k, lam = cusp_parameters(theta)
    t = np.abs(x - 0.5)
    return 1.0 - theta * t - 2.0 * k * np.sqrt(t)


def check_inverse():
    sample = np.linspace(0.0, 1.0, 5001)
    for theta in (1.5, 1.75):
        left, right, w = inverse_data(sample, theta)
        assert np.max(np.abs(forward(left, theta) - sample)) < 1e-12
        assert np.max(np.abs(forward(right, theta) - sample)) < 1e-12
        assert abs(left[0]) < 1e-12 and abs(right[0] - 1) < 1e-12
        assert abs(left[-1] - 0.5) < 1e-12
        assert abs(right[-1] - 0.5) < 1e-12
        assert abs(w[0] - cusp_parameters(theta)[1] ** (-1)) < 1e-12
        assert abs(w[-1]) < 1e-12


def check_exact_sample():
    p = Fraction(2, 3)
    a = (1 - p) * Fraction(32) + p * Fraction(128)
    b = (1 - p) * Fraction(16, 49) + p * Fraction(64, 225)
    assert a == 96
    assert b == Fraction(9872, 33075)
    assert 0 < b < 1
    assert (1 - b) * (b / (1 - b)) == b
    print('Exact mixture A =', a, '; B =', b, '=', float(b))
    return float(b)


def check_numerical_escape(target):
    grid = np.linspace(0.0, 1.0, 32769)
    theta = (1.5, 1.75)
    prob = (1 / 3, 2 / 3)
    branches = [inverse_data(grid, t) for t in theta]

    def killed_operator(phi, eps, side):
        out = np.zeros_like(phi)
        for mass, (g0, g1, w) in zip(prob, branches):
            a = np.interp(g0, grid, phi)
            b = np.interp(g1, grid, phi)
            if side == 0:
                a *= g0 > eps
                b *= g1 > eps
            else:
                a *= g0 < 1.0 - eps
                b *= g1 < 1.0 - eps
            out += mass * w * (a + b)
        return out

    observed = []
    for eps in (0.006, 0.003, 0.0015):
        rates = []
        for side in (0, 1):
            phi = np.ones_like(grid)
            for iteration in range(250):
                next_phi = killed_operator(phi, eps, side)
                lam = float(np.trapezoid(next_phi, grid))
                assert 0.0 < lam < 1.0
                next_phi /= lam
                change = float(np.max(np.abs(next_phi - phi)))
                phi = next_phi
                if change < 1e-10 and iteration > 30:
                    break
            rates.append(-log(lam))
        ratio = rates[0] / rates[1]
        observed.append(ratio)
        print(f'hole={eps:.4g}  rate_left={rates[0]:.12g} '
              f'rate_right={rates[1]:.12g} ratio={ratio:.10f}')

    assert observed[0] > observed[1] > observed[2] > target
    assert abs(observed[-1] - target) < 0.04
    print('Limiting ratio predicted by the theorem =', target)


if __name__ == '__main__':
    check_inverse()
    b = check_exact_sample()
    check_numerical_escape(b)
    print('All reproducibility checks passed.')
