"""Exact-integer regression checks for the minimum-support totient/divisor equation."""

from fractions import Fraction
from math import prod


def factor_exponents(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            out.append((d, e))
        d += 1 if d == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out


def totient_and_tau(n):
    f = factor_exponents(n)
    phi = n
    tau = 1
    for p, e in f:
        phi = (phi // p) * (p - 1)
        tau *= e + 1
    return phi, tau


def check():
    # Every possible exponent point in the proved finite search box.
    matched = []
    tests = 0
    for p in (7, 11, 13):
        for a in range(1, 5):
            for b in range(1, 4):
                for c in range(1, 3):
                    m = 2**a * 3**b * 5**c * p
                    lhs = (16-p) * 2**a * 3**(b-1) * 5**(c-1)
                    rhs = (a+3)*(b+1)*(c+1)*2
                    phi, tau = totient_and_tau(4*m)
                    assert (lhs == rhs) == (phi + tau == m)
                    tests += 1
                    if lhs == rhs:
                        matched.append((p, a, b, c, m, 4*m, phi, tau))

    expected = [
        (11, 2, 2, 1, 1980, 7920, 1920, 60),
        (13, 2, 1, 2, 3900, 15600, 3840, 60),
        (13, 3, 2, 1, 4680, 18720, 4608, 72),
    ]
    assert matched == expected, (matched, expected)
    assert tests == 72

    # Exact-rational checks of the only numerically decisive bounding constants.
    assert Fraction(16, 15) > 1
    assert 2 * Fraction(4, 5)*Fraction(6, 7)*Fraction(10, 11) > 1
    assert 2 * Fraction(2, 3)*Fraction(6, 7)*Fraction(10, 11) > 1
    assert 2 * Fraction(2, 3)*Fraction(4, 5)*Fraction(16, 17) > 1
    assert all(Fraction(p*(16-p), 24) > 1 for p in (7,11,13))
    assert Fraction(2**5, 5+3)>Fraction(8,3)
    assert Fraction(3**(4-1),4+1)>Fraction(8,3)
    assert Fraction(5**(3-1),3+1)>Fraction(8,3)

    # Direct finite regression only, not an unbounded completeness argument.
    m_limit = 50000
    all_witnesses = []
    for m in range(1, m_limit + 1):
        phi, tau = totient_and_tau(4*m)
        if phi + tau == m:
            all_witnesses.append(m)
    assert all_witnesses == [1980, 3900, 4680], all_witnesses
    print('VERIFY_OK')
    print('finite_box_cases=72; choices=(7,11,13) x (a=1..4,b=1..3,c=1..2)')
    print('finite_box_solutions=' + str([r[4] for r in matched]))
    print('independent_totient_and_tau_checks=' + str(tests))
    print('direct_regression_m_max=' + str(m_limit))
    print('direct_regression_solutions=' + str(all_witnesses))
    print('critical_rational_inequalities=PASS')


if __name__ == '__main__':
    check()
