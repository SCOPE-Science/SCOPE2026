"""Exact tests for the lecture-hall coefficient threshold theorem.

All arithmetic uses the Python standard library; finite tests supplement the
proof based on an exact Bernoulli/Faulhaber coefficient identity.
"""
from fractions import Fraction
from math import comb, factorial


def elementary_upto_four(m):
    e = [1, 0, 0, 0, 0]
    for j in range(1, m + 1):
        for k in range(4, 0, -1):
            e[k] += j * e[k - 1]
    return e


def quartic_coefficients(n):
    """Coefficients of Q_n in increasing powers of a."""
    assert n >= 5
    e = elementary_upto_four(n - 1)
    return (
        Fraction(e[4], n - 4),
        Fraction(e[4], n) + Fraction(e[3], 2),
        Fraction((n - 3) * e[2], 12),
        Fraction(0),
        -Fraction((n - 1) * (n - 2) * (n - 3), 720),
    )


def evaluate(cs, a):
    return sum((z * (a ** k) for k, z in enumerate(cs)), Fraction(0))


def ehrhart_count_direct(n, a, t):
    """Count dilate lattice points by conditioning on the last coordinate."""
    return sum(comb(a * y // (a + 1) + n - 1, n - 1)
               for y in range((a + 1) * t + 1))


def ehrhart_count_formula(n, a, t):
    return comb(a * t + n, n) + sum(comb(a * j + n - 1, n - 1)
                                   for j in range(t))


def poly_mul_linear(poly, offset):
    ans = [Fraction(0)] * (len(poly) + 1)
    for i, v in enumerate(poly):
        ans[i] += offset * v
        ans[i + 1] += v
    return ans


def interpolate_monomials_from_values(values):
    """Newton forward interpolation using falling-factorial polynomials."""
    diffs = list(map(Fraction, values))
    out = [Fraction(0)] * len(values)
    falling = [Fraction(1)]
    for j in range(len(values)):
        scale = diffs[0] / factorial(j)
        for k, coeff in enumerate(falling):
            out[k] += coeff * scale
        diffs = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]
        falling = poly_mul_linear(falling, -j)
    return out


def first_negative(n):
    q = quartic_coefficients(n)
    a = 1
    while evaluate(q, a) >= 0:
        a += 1
    return a


def main():
    trials = 0
    for n in range(5, 10):
        q = quartic_coefficients(n)
        assert all(q[k] > 0 for k in (0, 1, 2)) and q[3] == 0 and q[4] < 0
        for a in (1, 2, 3, 5, 8, 16):
            values = []
            for t in range(n + 1):
                direct = ehrhart_count_direct(n, a, t)
                assert direct == ehrhart_count_formula(n, a, t)
                values.append(direct)
                trials += 1
            coefficients = interpolate_monomials_from_values(values)
            predicted = Fraction(a ** (n - 5), factorial(n - 1)) * evaluate(q, a)
            assert coefficients[n - 4] == predicted, (n, a)
        expected_beta = {5: 16, 6: 19, 7: 23, 8: 27, 9: 31}[n]
        assert first_negative(n) == expected_beta
        assert evaluate(q, expected_beta - 1) >= 0 > evaluate(q, expected_beta)
    for n in (10, 20, 50, 100, 250):
        q = quartic_coefficients(n)
        assert all(q[i] > 0 for i in (0, 1, 2)) and q[3] == 0 and q[4] < 0
        beta = first_negative(n)
        assert evaluate(q, beta - 1) >= 0 and evaluate(q, beta) < 0
    print('VERIFY_OK exact_counts=%d dim5to9_a6 beta5to9=16,19,23,27,31 sign_pattern_n5to250' % trials)


if __name__ == '__main__':
    main()
