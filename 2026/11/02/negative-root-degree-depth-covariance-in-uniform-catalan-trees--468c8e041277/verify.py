"""Exact reproducibility checks for root-degree/total-depth dependence in plane trees."""
from collections import defaultdict
from fractions import Fraction
from math import comb


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def moment_recursions(max_n):
    """Unrestricted sequences of primitive Dyck excursions, using integer moments."""
    c = [catalan(n) for n in range(max_n + 1)]
    a = [0] * (max_n + 1)  # area (sum of heights before up-steps)
    r = [0] * (max_n + 1)  # primitive-component count
    m = [0] * (max_n + 1)  # product area * component count
    for n in range(1, max_n + 1):
        for i in range(1, n + 1):
            p = c[i - 1]
            ap = a[i - 1] + (i - 1) * c[i - 1]
            j = n - i
            a[n] += ap * c[j] + p * a[j]
            r[n] += p * (c[j] + r[j])
            m[n] += ap * (c[j] + r[j]) + p * (a[j] + m[j])
    return c, a, r, m


def exact_dyck_statistics(n):
    """Directly enumerate all balanced paths; independent from GF recursions."""
    result = defaultdict(lambda: [0, 0, 0])  # r: count, total area, total depth
    def walk(up, down, height, returns, area):
        if up == down == n:
            # Tree contour ascent at height h reaches a child at depth h+1.
            rec = result[returns]
            rec[0] += 1
            rec[1] += area
            rec[2] += area + n
            return
        if up < n:
            walk(up + 1, down, height + 1, returns, area + height)
        if down < up:
            h = height - 1
            walk(up, down + 1, h, returns + int(h == 0), area)
    walk(0, 0, 0, 0, 0)
    return result


def conditional_area_coefficient(n, degree):
    """[z^n] r z^(r+1) C(z)^r/(1-4z) divided by [z^n](z C)^r."""
    if degree == n:
        return Fraction(0)
    j = n - degree
    def coeff_c_power(t):
        return degree * comb(2 * t + degree, t) // (2 * t + degree)
    denominator = coeff_c_power(j)
    numerator = degree * sum(4 ** (j - 1 - t) * coeff_c_power(t) for t in range(j))
    return Fraction(numerator, denominator)


def run():
    tests = 0
    c, a, r, m = moment_recursions(100)
    for n in range(1, 101):
        b = comb(2 * n, n)
        expected_a = c[n] - Fraction(3, 2) * b + Fraction(4 ** n, 2)
        expected_r = catalan(n + 1) - c[n]
        expected_m = 3 * c[n] + 2 * catalan(n + 1) - Fraction(13, 2) * b + Fraction(3 * 4 ** n, 2)
        assert a[n] == expected_a
        assert r[n] == expected_r
        assert m[n] == expected_m
        tests += 3
        exact_cov = Fraction(m[n] * c[n] - a[n] * r[n], c[n] ** 2)
        stated_cov = Fraction(3 * 4 ** n, c[n] * (n + 2)) - Fraction((2 * n + 1) * (n + 3), n + 2)
        assert exact_cov == stated_cov
        assert exact_cov < 0 if n >= 2 else exact_cov == 0
        tests += 2

    for n in range(1, 11):
        distribution = exact_dyck_statistics(n)
        assert sum(v[0] for v in distribution.values()) == c[n]
        assert sum(v[1] for v in distribution.values()) == a[n]
        assert sum(k * v[0] for k, v in distribution.items()) == r[n]
        assert sum(k * v[1] for k, v in distribution.items()) == m[n]
        assert sum(v[2] for v in distribution.values()) == a[n] + n * c[n]
        tests += 5
        for degree in range(1, n + 1):
            count, area, depth = distribution[degree]
            assert area + n * count == depth
            assert Fraction(area, count) == conditional_area_coefficient(n, degree)
            tests += 2
    # Convex/asymptotic sign certificate ratio: ratio of differences is positive.
    for n in range(1, 101):
        b_n = Fraction(comb(2*n,n), 4**n)
        b_next = Fraction(comb(2*n+2,n+1),4**(n+1))
        t_n = Fraction(3*(n+1),(2*n+1)*(n+3))
        t_next = Fraction(3*(n+2),(2*n+3)*(n+4))
        actual = b_next/b_n - t_next/t_n
        stated = Fraction(n*(2*n+1),2*(n+1)*(n+4)*(2*n+3))
        assert actual == stated and stated > 0
        tests += 1
    print('PASS: %d exact integer/rational assertions; direct enumeration through n=10 edges (16,796 Dyck paths); symbolic recurrence comparisons through n=100.' % tests)

if __name__ == '__main__':
    run()
