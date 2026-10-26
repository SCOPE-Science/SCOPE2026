"""Finite-degree numerical cross-checks for sharp endpoint projection errors.

Requires scipy and numpy. Numerical checks do not prove large-degree limits.
"""
import math
import numpy as np
from scipy.special import eval_jacobi, roots_jacobi
from scipy.integrate import quad


def legendre_error(n):
    if n == 0:
        return 1.0
    zeros = roots_jacobi(n, 0, 1)[0]
    bounds = [-1.0] + list(zeros) + [1.0]
    return 0.5 * sum(
        quad(lambda t: (1.0 + t) * abs(eval_jacobi(n, 0, 1, t)), a, b,
             epsabs=1e-11, limit=150)[0]
        for a, b in zip(bounds[:-1], bounds[1:])
    )


def chebyshev_error(n):
    def integrand(u):
        k = np.arange(1, n + 1, dtype=float)
        a = math.pi - u - 2 * np.sum(np.sin(k * u) / k)
        return math.sin(u) * abs(a) / math.pi
    # Each cell is shorter than one oscillation; quad handles zero crossings.
    grid = np.linspace(0, math.pi, 6 * (n + 1) + 1)
    return sum(quad(integrand, float(a), float(b), epsabs=1e-11,
                    limit=80)[0] for a, b in zip(grid[:-1], grid[1:]))


if __name__ == '__main__':
    target_l = math.sqrt(2.0 / math.pi)
    target_c = 8.0 / math.pi ** 2
    for n in [0, 1, 2, 5, 10, 20, 50, 100]:
        l, c = legendre_error(n), chebyshev_error(n)
        assert l > 0 and c > 0
        if n == 0:
            assert abs(l - 1) < 1e-10 and abs(c - 1) < 1e-10
        if n == 2:
            assert abs(l - 24 * math.sqrt(6) / 125) < 1e-10
        if n > 0:
            print(n, format(l, '.12g'), format(c, '.12g'),
                  format(math.sqrt(n) * l, '.9g'), format(n * c, '.9g'))
        if n == 100:
            assert abs(math.sqrt(n) * l - target_l) < 0.004
            assert abs(n * c - target_c) < 0.012
    print('PASS finite-degree consistency checks; limits require analytic proof')
