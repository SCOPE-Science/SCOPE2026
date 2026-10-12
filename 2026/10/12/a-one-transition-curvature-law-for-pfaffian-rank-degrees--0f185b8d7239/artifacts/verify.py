from fractions import Fraction
from math import factorial, comb

def catalan(m):
    return comb(2*m, m) // (m + 1)

def degree(n, s):
    if s in (-1, 0):
        return 1
    out = Fraction(1, 1)
    for i in range(1, s + 1):
        for j in range(i, s + 1):
            out *= Fraction(n - s - 1 + i + j, i + j)
    assert out.denominator == 1
    return out.numerator

def adjacent_ratio_closed(n, s):
    num = 1
    for k in range(-(s - 1), s):
        num *= n + k
    den = factorial(2*s) * catalan(s - 1)
    return Fraction(num, den)

def curvature_closed(n, s):
    return Fraction(
        (n*n - s*s) * (n*n - (s + 1)*(s + 1)),
        16 * (2*s - 1) * (2*s + 1)**2 * (2*s + 3)
    )

def Q(n, s):
    return (
        (n*n - s*s) * (n*n - (s + 1)*(s + 1))
        - 16 * (2*s - 1) * (2*s + 1)**2 * (2*s + 3)
    )

degree_checks = ratio_checks = curvature_checks = monotone_checks = 0

for n in range(4, 121):
    start = 1 if n % 2 == 0 else 2
    endpoint = -1 if n % 2 == 0 else 0
    ss = list(range(start, n - 2, 2))

    for s in ss:
        d = degree(n, s)
        assert d > 0
        degree_checks += 1

        prev = endpoint if s == start else s - 2
        lhs = Fraction(d, degree(n, prev))
        rhs = adjacent_ratio_closed(n, s)
        assert lhs == rhs, (n, s, lhs, rhs)
        ratio_checks += 1

    for s in range(start, n - 4, 2):
        prev = endpoint if s == start else s - 2
        curv = Fraction(degree(n, s + 2) * degree(n, prev), degree(n, s) ** 2)
        closed = curvature_closed(n, s)
        assert curv == closed, (n, s, curv, closed)

        q = Q(n, s)
        assert (curv > 1) == (q > 0)
        assert (curv < 1) == (q < 0)
        assert (curv == 1) == (q == 0)
        curvature_checks += 1

        if s + 2 <= n - 5:
            diff = Q(n, s + 2) - Q(n, s)
            expected = -4 * (2*s + 3) * (n*n + 255*s*s + 765*s + 701)
            assert diff == expected
            assert diff < 0
            monotone_checks += 1

print("VERIFY_OK", degree_checks, ratio_checks, curvature_checks, monotone_checks)
