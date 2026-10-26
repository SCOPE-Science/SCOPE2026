"""Finite numerical checks for Gaussian additive ANOVA kernel energy.

Requires Python 3 standard library only. This is not a proof of asymptotic claims.
"""
from math import cos, exp, pi, sqrt, log


def scaled_i0(z):
    """Numerical quadrature of exp(-z) I_0(z), z >= 0."""
    n = max(512, 2 * int(12 * sqrt(max(z, 1.0)) / 2) + 2)
    if n % 2:
        n += 1
    h = pi / n
    acc = 0.0
    for k in range(n + 1):
        weight = 1 if k == 0 or k == n else 4 if k % 2 else 2
        acc += weight * exp(-z * (1 - cos(k * h)))
    return h * acc / (3 * pi)


def energy(sigma):
    z = 2 / (sigma * sigma)
    a = scaled_i0(z)
    return scaled_i0(2 * z) / (a * a) - 1


def kernel(sigma, x):
    z = 2 / (sigma * sigma)
    return exp(z * (cos(2 * pi * x) - 1)) / scaled_i0(z)


def trap(fn, count=4096):
    return sum(fn(j / count) for j in range(count)) / count


for sigma in (0.2, 0.35, 0.6, 1.0):
    assert abs(trap(lambda x: kernel(sigma, x)) - 1) < 5e-7
    direct = trap(lambda x: kernel(sigma, x) ** 2)
    assert abs(direct - 1 - energy(sigma)) < 3e-6
    assert energy(sigma) > 0

# Compare the first two asymptotic powers using finite truncated sums.
c = sqrt(2 * pi)
for exponent in (2.0, 4.0, 8.0):
    t = exponent / 4
    for rho in (0.1, 0.05):
        n = int((1 / rho) ** (1 / t))
        value = sum(energy(rho * j ** t) for j in range(1, n + 1))
        assert value > 0
        if exponent == 4:
            assert 0.6 < rho * value / (c * log(1 / rho)) < 1.5
        if exponent == 8:
            # zeta(2) = pi^2/6.
            assert 0.5 < rho * value / (c * pi * pi / 6) < 1.3
        if exponent == 2:
            # p=2 requires rho^-2 growth, with positive finite limiting coefficient.
            assert 1 < rho * rho * value < 6
print('PASS: exact-kernel numerical normalization and energy; representative scaling tests')
