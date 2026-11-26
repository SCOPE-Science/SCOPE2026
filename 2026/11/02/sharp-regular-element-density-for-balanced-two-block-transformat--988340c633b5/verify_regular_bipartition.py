"""Bounded checks of the regular count and sharp correction for two equal blocks."""

from fractions import Fraction
from itertools import product
from math import comb, exp, factorial, sqrt


def direct_count(m):
    targets = [tuple(range(m)), tuple(range(m, 2 * m))]
    maps = [f for a, b in product(targets, repeat=2)
            for f in product(*([a] * m + [b] * m))]
    total = 0
    for f in maps:
        image = tuple(set(f))
        for g in maps:
            if all(f[g[y]] == y for y in image):
                total += 1
                break
    return total, len(maps)


def inclusion_and_equality_counts(m):
    row = [1] + [0] * m
    for _ in range(m):
        row = [0] + [row[s - 1] + s * row[s] for s in range(1, m + 1)]
    a, b = 0, 0
    for s in range(1, m + 1):
        onto = factorial(s) * row[s]
        a += comb(m, s) * onto * s**m
        b += comb(m, s) * onto**2
    return a, b


def correction(m):
    a, b = inclusion_and_equality_counts(m)
    return Fraction(2*a - b, 2*m**(2*m))


def saddle():
    lo, hi = 0.1, 1.0
    for _ in range(55):
        x = (lo + hi) / 2
        y = x / (1 - exp(-x))
        if exp(-y) > 1 + (x - 1) * exp(x):
            lo = x
        else:
            hi = x
    x = (lo + hi) / 2
    y = x / (1 - exp(-x))
    rho = (1 + (exp(x) - 1)*exp(y)) / (exp(2)*x*y)
    prefactor = 1 / sqrt(x*y - (y - 1)**2)
    return rho, prefactor


if __name__ == '__main__':
    for m, expected in enumerate((4, 60, 2400), start=1):
        count, total = direct_count(m)
        assert count == expected
        assert Fraction(count, total) == Fraction(1, 2) + correction(m)
        print('direct', m, count, total)
    assert abs(float(Fraction(1, 2) + correction(12)) - 0.5156703857) < 1e-10
    rho, prefactor = saddle()
    print('rho', rho, 'prefactor', prefactor)
    assert abs(rho - 0.696742956572524) < 1e-13
    assert abs(prefactor - 1.210700991285293) < 1e-13
    for m in (40, 80):
        ratio = float(correction(m)) / (prefactor * rho**m)
        assert abs(ratio - 1) < 0.01
        print('asymptotic_ratio', m, ratio)
    print('VERIFY_OK')
