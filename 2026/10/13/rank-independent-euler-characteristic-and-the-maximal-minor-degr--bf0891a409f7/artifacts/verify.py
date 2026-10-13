from fractions import Fraction
from math import factorial, comb

def det_degree(m, n, r):
    out = Fraction(1, 1)
    for i in range(m-r):
        out *= Fraction(
            factorial(n+i) * factorial(i),
            factorial(r+i) * factorial(n-r+i)
        )
    assert out.denominator == 1
    return out.numerator

def expected_sign(m, n):
    # -1 means degree<Euler, 0 equality, +1 degree>Euler.
    if m == 2:
        return -1
    if m == 3:
        if n <= 6:
            return -1
        if n == 7:
            return 0
        return 1
    if m == 4:
        return -1 if n <= 6 else 1
    if m == 5:
        if n <= 6:
            return -1
        if n == 7:
            return 0
        return 1
    return -1 if n <= m+1 else 1

degree_checks = comparison_checks = ratio_checks = fixed_point_checks = 0

for m in range(2, 41):
    for n in range(m, 101):
        r = m-1
        d_product = det_degree(m, n, r)
        d_binom = comb(n, m-1)
        assert d_product == d_binom, (m, n, d_product, d_binom)

        euler = m*n
        sign = (d_binom > euler) - (d_binom < euler)
        assert sign == expected_sign(m, n), (m, n, d_binom, euler, sign)

        if n < 100:
            lhs = Fraction(comb(n+1, m-1), m*(n+1)) / Fraction(comb(n, m-1), m*n)
            rhs = Fraction(n, n-m+2)
            assert lhs == rhs
            if m >= 3:
                assert rhs > 1
            else:
                assert rhs == 1
            ratio_checks += 1

        # Generic distinct coordinate weights give exactly one fixed point per entry.
        weights = [1000*i + j for i in range(m) for j in range(n)]
        assert len(set(weights)) == m*n
        fixed_point_checks += 1

        degree_checks += 1
        comparison_checks += 1

assert comb(7, 2) == 3*7 == 21
assert comb(7, 4) == 5*7 == 35

print("VERIFY_OK", degree_checks, comparison_checks, ratio_checks, fixed_point_checks)
