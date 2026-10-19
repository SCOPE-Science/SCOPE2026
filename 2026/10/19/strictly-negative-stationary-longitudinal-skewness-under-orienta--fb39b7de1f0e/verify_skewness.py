#!/usr/bin/env python3
"""Exact rational checks for a stationary active-particle moment identity.

No simulation or external dependencies. These checks supplement, but do not
replace, the all-positive-parameter generator proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def compute(beta, rate, speed, diffusion):
    harmonic = lambda n: rate / (rate + n * n)
    m = speed * harmonic(1) / beta
    u = (speed * (1 + harmonic(2)) / 2 + rate * m) / (beta + rate + 1)
    m2 = (speed * u + diffusion) / beta
    k = (speed * (harmonic(1) + harmonic(3)) / 2 + rate * m) / (beta + rate + 4)
    h = (speed * (m + k) + 2 * diffusion * harmonic(1) + rate * m2) / (2 * beta + rate + 1)
    m3 = (speed * h + 2 * diffusion * m) / beta
    central = m3 - 3 * m * m2 + 2 * m**3
    target = -4 * rate * speed**3 * (37 * beta * rate + 13 * beta + 52 * rate**2 + 191 * rate + 67) / (
        beta * (rate + 1)**3 * (rate + 4) * (rate + 9)
        * (beta + rate + 1) * (beta + rate + 4) * (2 * beta + rate + 1)
    )
    assert beta * m == speed * harmonic(1)
    assert (beta + rate + 1) * u == speed * (1 + harmonic(2)) / 2 + rate * m
    assert beta * m2 == speed * u + diffusion
    assert (beta + rate + 4) * k == speed * (harmonic(1) + harmonic(3)) / 2 + rate * m
    assert (2 * beta + rate + 1) * h == speed * (m + k) + 2 * diffusion * harmonic(1) + rate * m2
    assert beta * m3 == speed * h + 2 * diffusion * m
    assert central == target
    assert central < 0
    return central


def main():
    count = 0
    for b, r, v, d in product(
        [F(1, 5), F(1, 2), F(1), F(2), F(5)],
        [F(1, 7), F(1, 2), F(1), F(2), F(7)],
        [F(1, 3), F(1), F(3)],
        [F(0), F(1, 5), F(1), F(4)],
    ):
        ans = compute(b, r, v, d)
        assert ans == compute(b, r, v, F(0))
        count += 1
    print(f'{count} exact rational parameter cases passed; each tests generator identities, negativity, and independence from thermal diffusivity.')


if __name__ == '__main__':
    main()
