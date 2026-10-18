"""Numerical diagnostics for affine Hardy-Sobolev composition power laws.

This finite computation is not a proof of the spectral assertions.
"""
from cmath import exp as cexp
from math import exp, log, sqrt


def poly(order, s):
    return sum(s ** (2 * j) for j in range(order + 1))


def grid_max(func, low=0.0, high=200.0, count=40001):
    step = (high - low) / (count - 1)
    return max((func(low + i * step), low + i * step) for i in range(count))


def power_norm_sq(order, a, b, power):
    q = a ** (-power)
    damping = 2 * b * (1 - q) / (a - 1)
    upper = max(200.0, 40.0 / max(damping, 0.05)) if b > 0 else 300.0
    return a ** (-power) * grid_max(
        lambda s: exp(-damping * s) * poly(order, s) / poly(order, q * s),
        0.0, upper
    )[0]


def limiting_prefactor(order, a, b):
    c = 2 * b / (a - 1)
    upper = max(200., 40.0 / c)
    return sqrt(grid_max(lambda s: exp(-c * s) * poly(order, s), 0.0, upper)[0])


def check():
    for n, a, b in [(1, 2.0, 0.12), (2, 1.6, 0.23), (3, 2.5, 0.5)]:
        prefactor = limiting_prefactor(n, a, b)
        measured = sqrt(power_norm_sq(n, a, b, 22)) * a ** 11
        assert abs(measured - prefactor) / prefactor < 0.002, (measured, prefactor)
        assert sqrt(power_norm_sq(n, a, 0.0, 1)) < a ** (n - 0.5)
        assert abs(sqrt(power_norm_sq(n, a, 0.0, 1)) - a ** (n - 0.5)) < 0.05

        gamma = complex(0.23, 0.71)
        for t in [0.05, 0.4, 1., 4., 15.]:
            def f(s):
                return cexp(gamma * log(s) - b * s / (a - 1))
            transformed = a ** -1 * exp(-b * t / a) * f(t / a)
            eigen = cexp(-(gamma + 1) * log(a)) * f(t)
            assert abs(transformed - eigen) < 1e-12 * max(1, abs(eigen))
    print('PASS: finite power diagnostics and pointwise eigenfunction identity')

if __name__ == '__main__':
    check()
