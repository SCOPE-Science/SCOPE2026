"""Exact arithmetic checks for the simplex-frustum mixed-volume coefficient formula.

Run with Python 3. Uses only the standard library. The independent calculation
sums contributions of the sign-orthant integration, not the closed formula.
"""
from fractions import Fraction
from math import comb, factorial


def orthant_coefficient(n, m, t):
    z = Fraction((-1) ** m * comb(n, m), factorial(n)) * (t ** m - t ** (n - m))
    for j in range(1, n):
        s = m - (n - j)
        if s < 0 or s > j:
            continue
        if s == 0:
            z += Fraction(comb(n, j), factorial(j) * factorial(n - j)) * (1 - t ** j)
        else:
            z += Fraction((-1) ** s * comb(n, j), factorial(j - s) * factorial(n - j + s)) * (
                t ** (n - j + s) - t ** (j - s)
            )
    return z


def claimed_coefficient(n, m, t):
    return Fraction(comb(n, m) ** 2, factorial(n)) * (
        1 - Fraction(m, n) * t ** m - Fraction(n - m, n) * t ** (n - m)
    )


def main():
    samples = (Fraction(1, 11), Fraction(2, 7), Fraction(3, 4), Fraction(9, 10))
    checked = 0
    for n in range(2, 19):
        for t in samples:
            for m in range(n + 1):
                a = orthant_coefficient(n, m, t)
                b = claimed_coefficient(n, m, t)
                assert a == b, (n, m, t, a, b)
                assert a == claimed_coefficient(n, n - m, t)
                checked += 1
            for m in range(1, n):
                v = claimed_coefficient(n, m, t) / comb(n, m)
                vol = (1 - t ** n) / factorial(n)
                assert 0 < v < comb(n, m) * vol
                if n % 2 == 0 and m == n // 2:
                    assert v / (comb(n, m) * vol) == 1 / (1 + t ** m)
    print(f'VERIFY_OK exact orthant coefficients: {checked}; n=2..18; 4 rational t samples')


if __name__ == '__main__':
    main()
