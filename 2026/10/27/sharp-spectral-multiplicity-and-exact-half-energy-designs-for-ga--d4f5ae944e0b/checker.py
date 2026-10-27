"""Independent finite numerical checks for annular Gaussian Fock concentration.

Requires numpy and scipy.  Numerical checks are not substitutes for the
analytic proof and make no assertion about historical priority.
"""
import math
import numpy as np
from scipy.optimize import root
from scipy.special import gammaincc


def modal_values(endpoints, count):
    half_count = len(endpoints) // 2
    return np.array([
        sum(gammaincc(n + 1, endpoints[2*j]) -
            gammaincc(n + 1, endpoints[2*j+1])
            for j in range(half_count))
        for n in range(count)
    ])


def run():
    cases = [
        (1, [0.43, 1.92]),
        (2, [0.25, 1.04, 2.47, 4.86]),
    ]
    moment_checks = 0
    negative_steps = 0
    difference_checks = 0
    for m, guess in cases:
        solve = root(lambda x: modal_values(x, 2*m) - 0.5,
                     guess, tol=1e-12)
        assert solve.success, solve.message
        endpoints = solve.x
        assert np.all(endpoints > 0) and np.all(np.diff(endpoints) > 0)
        modes = modal_values(endpoints, 18)
        assert np.max(np.abs(modes[:2*m] - 0.5)) < 1e-11
        moment_checks += 2*m
        for n in range(2*m-1, 15):
            assert modes[n] > modes[n+1] + 1e-12, (m, n, modes[n:n+2])
            negative_steps += 1
        for n in range(0, 14):
            F = sum(np.exp(-endpoints[2*j]) * endpoints[2*j]**(n+1)
                    - np.exp(-endpoints[2*j+1]) * endpoints[2*j+1]**(n+1)
                    for j in range(m))
            assert abs((n+1) * (modes[n+1] - modes[n]) - F / math.factorial(n)) < 1e-10
            difference_checks += 1
        print('m=',m,'radii_squared=', ', '.join('%.12f'%x for x in endpoints),
              'head=',modes[:2*m+2].round(12).tolist())
    print('VERIFY_OK cases=2 half_moment_checks=%d strict_tail_steps=%d difference_checks=%d'
          % (moment_checks, negative_steps, difference_checks))


if __name__ == '__main__':
    run()
