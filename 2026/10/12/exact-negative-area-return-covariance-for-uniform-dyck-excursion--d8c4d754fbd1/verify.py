"""Exact rational tests for area and completed-component counts of Dyck paths.

Requires Python 3.9 or later; uses only its standard library.
"""
from fractions import Fraction
from math import comb


def catalan(n):
    assert n >= 0
    return comb(2 * n, n) // (n + 1)


def moments_from_finite_paths(n):
    """Directly enumerate all Catalan objects, independently of generating functions."""
    sums = [0, 0, 0, 0, 0]
    count = 0

    def explore(height, up, down, area, returns):
        nonlocal count
        if up == n and down == n:
            assert height == 0
            count += 1
            sums[0] += area
            sums[1] += returns
            sums[2] += area * returns
            sums[3] += area * area
            sums[4] += returns * returns
            return
        if up < n:
            explore(height + 1, up + 1, down, area + height, returns)
        if down < n and height:
            explore(height - 1, up, down + 1, area + height,
                    returns + int(height == 1))

    explore(0, 0, 0, 0, 0)
    assert count == catalan(n)
    return tuple(Fraction(value, count) for value in sums)


def expected_moments(n):
    """Closed forms derived from the q- and return-marked Catalan series."""
    assert n >= 1
    c = catalan(n)
    x = Fraction(4 ** n, c)
    a = x - 2 * n - 1
    r = Fraction(3 * n, n + 2)
    ar = 3 * x - 10 * n - 5 + 2 * Fraction(catalan(n + 1), c)
    avar = Fraction((n + 1) * (2 * n + 1) * (5 * n + 3), 3) - x * x
    rvar = Fraction(2 * n * (n - 1) * (2 * n + 1), (n + 2) ** 2 * (n + 3))
    return a, r, ar, avar + a * a, rvar + r * r


def series_coefficient_moments(n):
    """Extract from rational expressions in sqrt(1-4z)."""
    c = catalan(n)
    b = comb(2 * n, n)
    r = catalan(n + 1) - c
    a = 4 ** n - 2 * b + c
    ar = 3 * 4 ** n - 10 * b + 5 * c + 2 * catalan(n + 1)
    aa_factorial = Fraction((n + 1) * (2 * n + 1) * (5 * n + 9), 3) * c - (4 * n + 3) * 4 ** n
    rr_factorial = (Fraction(10, 2 * n + 1) * comb(2 * n + 1, n - 2)) if n >= 2 else 0
    return tuple(Fraction(v, c) for v in (a, r, ar, aa_factorial + a, rr_factorial + r))


def main():
    enumerated = 0
    for n in range(1, 12):
        direct = moments_from_finite_paths(n)
        theory = expected_moments(n)
        assert direct == theory, (n, direct, theory)
        enumerated += catalan(n)

    for n in range(1, 151):
        expected = expected_moments(n)
        coeff = series_coefficient_moments(n)
        assert expected == coeff, (n, expected, coeff)
        ea, er, ear, _, _ = expected
        covariance = ear - ea * er
        x = Fraction(4 ** n, catalan(n))
        assert covariance == Fraction(6 * x - 2 * (2*n+1) * (n+3), n+2)
        assert covariance == 0 if n == 1 else covariance < 0
        if n >= 2:
            k_previous = Fraction((2*n-1)*(n+2)*catalan(n-1), 3 * 4 ** (n-1))
            k_current = Fraction((2*n+1)*(n+3)*catalan(n), 3 * 4 ** n)
            assert k_current > k_previous
            assert k_current / k_previous == 1 + Fraction(n - 1, 2*(n+1)*(n+2))
    print(f'VERIFICATION_OK: {enumerated} enumerated paths, 150 exact coefficient/moment identities, sign checks')


if __name__ == '__main__':
    main()
