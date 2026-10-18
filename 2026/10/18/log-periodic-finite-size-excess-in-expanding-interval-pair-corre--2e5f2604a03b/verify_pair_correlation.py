"""Exact rational checks for interval-map collision probabilities and finite-size means.

Requires only Python's standard library. Run: python verify_pair_correlation.py
"""
from fractions import Fraction
from math import floor, log


def probability_branch_sum(bpower, radius):
    """Closed form obtained by summing clipped branch lengths."""
    u = bpower * radius
    m = u.numerator // u.denominator
    return (Fraction(m * (m + 1), bpower)
            + 2 * (bpower - 1 - m) * radius) / (bpower - 1)


def probability_independent_intersections(bpower, radius):
    """Direct intersections on the bpower affine branches."""
    ans = Fraction(0)
    for j in range(bpower):
        left = max(Fraction(j, bpower), (Fraction(j, 1) - radius) / (bpower - 1))
        right = min(Fraction(j + 1, bpower), (Fraction(j, 1) + radius) / (bpower - 1))
        ans += max(Fraction(0), right - left)
    return ans


def probability_fractional_formula(bpower, radius):
    u = bpower * radius
    v = u - (u.numerator // u.denominator)
    return 2 * radius - radius * radius + (u * (1 - radius) - v * (1 - v)) / (bpower * (bpower - 1))


def exact_normalized_mean(n, base, s):
    radius = Fraction(s, n)
    expected = sum((Fraction(2 * (n - k), n) * probability_branch_sum(base ** k, radius)
                    for k in range(1, n)), Fraction(0))
    reference = (n - 1) * (2 * radius - radius * radius)
    return (expected - reference) * Fraction(n * n, 2 * s * s)


def shape(u):
    frac = u - floor(u)
    return (u - frac * (1 - frac)) / (u * u)


def phase(base, t):
    return sum(shape(base ** (j - t)) for j in range(1, 60)) - t


def main():
    checked = 0
    for bpower in range(2, 15):
        for denominator in (13, 19):
            for numerator in (1, 2, 3, 5, 7, 9):
                radius = Fraction(numerator, denominator)
                if radius >= 1:
                    continue
                p1 = probability_branch_sum(bpower, radius)
                p2 = probability_independent_intersections(bpower, radius)
                p3 = probability_fractional_formula(bpower, radius)
                assert p1 == p2 == p3, (bpower, radius, p1, p2, p3)
                assert 0 <= p1 <= 1
                checked += 1
    for base in (2, 3, 5):
        assert abs(phase(base, 0) - 1 / (base - 1)) < 1e-12
        assert abs(phase(base, 1) - phase(base, 0)) < 1e-12
        assert abs(phase(base, 0.2) - phase(base, 0)) > 0.01
    s = 3
    errors = []
    for n in (50, 100, 200, 400):
        finite = float(exact_normalized_mean(n, 2, s))
        z = log(n / s, 2)
        err = abs(finite - (z + phase(2, z % 1)))
        errors.append(err)
        print(f'n={n} normalized={finite:.12f} prediction={(z+phase(2,z%1)):.12f} error={err:.12f}')
    assert all(a > b for a, b in zip(errors, errors[1:]))
    print('PASS: exact branch and fractional identities for', checked, 'rational cases; phase and finite-size checks')


if __name__ == '__main__':
    main()
