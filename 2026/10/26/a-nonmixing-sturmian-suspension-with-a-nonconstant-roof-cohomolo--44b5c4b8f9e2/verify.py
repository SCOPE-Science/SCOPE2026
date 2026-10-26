"""Finite arithmetic checks for the factorial-denominator Sturmian roof.

The infinite theorem is proved analytically in RESULT.md. This program tests
finite rational instances of its number-theoretic estimates.
"""
from fractions import Fraction


def Q(k):
    import math
    return 10 ** math.factorial(k)


def check():
    checks = 0
    for k in range(1, 7):
        q, qnext = Q(k), Q(k + 1)
        assert qnext == q ** (k + 1)
        checks += 1
        # Sum two positive tail terms; the actual infinite tail is larger.
        dlow = Fraction(q, qnext)
        dpartial = Fraction(q, qnext) + Fraction(q, Q(k + 2))
        assert dlow < dpartial < 2 * dlow < Fraction(1, 2)
        checks += 1
        assert qnext >= q ** 2
        checks += 1
        if k >= 2:
            # The analytic proof uses pi < 22/7, and a tail bound of 2/q^2.
            bound = Fraction(22, 7 * 50) * Fraction(q * q, qnext) + Fraction(2, q)
            assert bound < Fraction(3, q)
            checks += 1
        if k >= 3:
            # Lower bound for a hypothetical transfer Fourier coefficient:
            # Q_{k+1}/(8*pi*Q_k^3) > Q_{k+1}/((176/7)*Q_k^3).
            lower = Fraction(7 * qnext, 176 * q ** 3)
            assert lower > k
            checks += 1
    assert sum(Fraction(1, Q(k) ** 2) for k in range(1, 7)) < Fraction(1, 50)
    checks += 1
    print(f"VERIFY_OK: {checks} exact rational arithmetic assertions")


if __name__ == "__main__":
    check()
