#!/usr/bin/env python3
"""Elementary reproducibility checks for the exact bisector-section theorem."""
import math
from fractions import Fraction


def simpson(f, a, b, n=2000):
    if n % 2:
        raise ValueError('even number of panels needed')
    h = (b - a) / n
    total = f(a) + f(b)
    total += 4 * sum(f(a + h * j) for j in range(1, n, 2))
    total += 2 * sum(f(a + h * j) for j in range(2, n, 2))
    return total * h / 3


def kappa(k):
    return math.pi ** (k / 2) / math.gamma(1 + k / 2)


def exact_slice(d, t):
    if abs(t) >= 1 / math.sqrt(2):
        return 0.0
    return 2 * math.sqrt(2) * kappa(d - 2) / d * (1 - 2 * t * t) ** ((d - 2) / 2)


def coordinate_slice(d, t):
    bound = 1 / math.sqrt(2)
    p = (d - 2) / 2
    left = simpson(lambda v: max(0.0, (1 - math.sqrt(2) * t) * (1 + math.sqrt(2) * v)) ** p, -bound, t, 8000)
    right = simpson(lambda v: max(0.0, (1 + math.sqrt(2) * t) * (1 - math.sqrt(2) * v)) ** p, t, bound, 8000)
    return kappa(d - 2) * (left + right)


def beta(a, b):
    return math.exp(math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b))


def directional(d):
    a = (d - 2) / (d - 1)
    bound = 1 / math.sqrt(2)
    integ = simpson(lambda t: exact_slice(d, t) ** a, -bound, bound, 12000)
    vol = 2 * kappa(d - 1) / d
    return integ ** (d - 1) / (bound * vol ** (d - 2))


def beta_formula(d):
    return (kappa(d - 2) / kappa(d - 1)) ** (d - 2) * beta(.5, 1 + (d - 2) ** 2 / (2 * (d - 1))) ** (d - 1)


def check():
    checks = 0
    for d in range(3, 8):
        for t in [-0.6, -0.3, 0.0, 0.15, 0.55]:
            a = coordinate_slice(d, t)
            b = exact_slice(d, t)
            assert abs(a - b) < 1e-6 * max(1.0, abs(b)), (d, t, a, b)
            checks += 1
        a, b = directional(d), beta_formula(d)
        assert abs(a - b) < 1e-5 * max(1.0, abs(b)), (d, a, b)
        checks += 1

    b3 = beta_formula(3)
    assert abs(b3 - 2 * (math.gamma(1.25) / math.gamma(1.75)) ** 2) < 1e-13
    assert abs(b3 - 1.9452796579790903) < 1e-12
    checks += 2

    s = Fraction(8939, 8192)
    cert = Fraction(157, 100) * (s * s - Fraction(33, 28))
    assert cert == Fraction(893631283, 46976204800)
    assert cert > Fraction(1, 100)
    assert Fraction(157, 50) < Fraction(22, 7)
    checks += 3
    # Independent axial volume calculation: area(z)=pi*(1-|z|)^2 and h=1.
    axial_integral = 2 * math.sqrt(math.pi) * 0.5
    axial_value = axial_integral ** 2 / (2 * math.pi / 3)
    assert abs(axial_value - 1.5) < 1e-14
    checks += 1
    print('VERIFY_OK', checks, 'F3=', format(b3, '.15f'))


if __name__ == '__main__':
    check()
