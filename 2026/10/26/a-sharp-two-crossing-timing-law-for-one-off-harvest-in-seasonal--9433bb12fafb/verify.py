"""Independent numerical and exact-rational spot checks for a two-season Ricker-map identity.

Standard-library only. Finite tests supplement, not replace, the analytical proof.
"""
from fractions import Fraction
from math import exp, log, sqrt
from random import Random


def recruit(x, multiplier, crowding):
    return multiplier * x * exp(-crowding * x)


def early(x, R1, a1, R2, a2, survival):
    return recruit(recruit(survival * x, R1, a1), R2, a2)


def late(x, R1, a1, R2, a2, survival):
    return recruit(survival * recruit(x, R1, a1), R2, a2)


def log_ratio_formula(x, R1, a1, a2, survival):
    z = a1 * x
    rho = a2 * R1 / a1
    return z * ((1 - survival) - survival * rho *
                (exp(-survival * z) - exp(-z)))


def bisect(fun, left, right, iterations=90):
    vl = fun(left)
    vr = fun(right)
    assert vl * vr < 0
    for _ in range(iterations):
        middle = (left + right) / 2
        vm = fun(middle)
        if vl * vm > 0:
            left, vl = middle, vm
        else:
            right = middle
    return (left + right) / 2


def main():
    rng = Random(20261022)
    pairs = 8000
    roots_checked = 0
    for _ in range(pairs):
        s = rng.uniform(0.05, 0.96)
        R1 = exp(rng.uniform(-1.3, 2.5))
        R2 = exp(rng.uniform(-0.8, 1.6))
        a1 = exp(rng.uniform(-1, 1))
        a2 = exp(rng.uniform(-1, 1))
        x = rng.uniform(0.002, 3 / a1)
        e = early(x, R1, a1, R2, a2, s)
        l = late(x, R1, a1, R2, a2, s)
        assert e > 0 and l > 0
        assert abs(log(e / l) - log_ratio_formula(x, R1, a1, a2, s)) < 1e-10
        rho = a2 * R1 / a1
        rho_c = s ** (-1 / (1 - s))
        zm = -log(s) / (1 - s)
        if rho > rho_c + 1e-7:
            target = (1 - s) / (s * rho)
            fun = lambda z: exp(-s * z) - exp(-z) - target
            z1 = bisect(fun, 0, zm)
            z2 = bisect(fun, zm, zm + 200 / s)
            assert 0 < z1 < zm < z2
            assert log_ratio_formula(z1 / (2 * a1), R1, a1, a2, s) > 0
            assert log_ratio_formula((z1 + z2) / (2 * a1), R1, a1, a2, s) < 0
            assert log_ratio_formula((z2 + 1) / a1, R1, a1, a2, s) > 0
            roots_checked += 1
        else:
            assert log_ratio_formula(zm / a1, R1, a1, a2, s) > -1e-10
    s = Fraction(1, 2)
    rho = Fraction(5, 1)
    checks = [(Fraction(3, 4), Fraction(1, 32)),
              (Fraction(1, 2), Fraction(-1, 8)),
              (Fraction(1, 4), Fraction(1, 32))]
    for y, expected in checks:
        bracket = (1 - s) - s * rho * (y - y * y)
        assert bracket == expected
    assert abs((0.8 ** (-1 / (1 - 0.8))) - (5 / 4)**5) < 1e-12
    assert log(4) < 2
    print('PASS: 8,000 two-season composition and logarithmic-ratio identities')
    print('PASS:', roots_checked, 'root-bracketing and three-region sign cases')
    print('PASS: exact-rational three-point witness, threshold, stable-map example')
    print('Finite tests are not a proof of the universal classification.')


if __name__ == '__main__':
    main()
