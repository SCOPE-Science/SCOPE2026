"""Finite sanity checks for the gap-four Bergman-numerator identities.

The proof in RESULT.md is symbolic: the displayed Bernstein coefficients are
strictly positive for every integer k >= 1.  This script is only a reproducible
finite cross-check of the coefficient extraction, not an infinite proof.
"""
from math import gcd
from fractions import Fraction


def q_coefficients_from_kernel_formula(n):
    """Return coefficients q[0],...,q[8] of Q_{n+4,n}.

    This is the finite numerator formula obtained after summing the monomial
    kernel series; L and kappa are the integer floor/ceiling data in that
    formula. Coefficients are stored in increasing powers of s.
    """
    m = n + 4
    q = [0] * 9
    q[4] += m * m
    for j in range(m - 1):
        L = (1 + n * (j + 1) + m - 1) // m
        kappa = m + n - 1 + n * j - m * L
        terms = (
            (j + 1 - L, (j + 1) * (kappa + 1)),
            (j + 2 - L, (j + 1) * (m - kappa - 1)),
            (j + 5 - L, (m - j - 1) * (kappa + 1)),
            (j + 6 - L, (m - j - 1) * (m - kappa - 1)),
        )
        for exponent, coefficient in terms:
            if not 0 <= exponent <= 8:
                raise AssertionError((n, j, exponent))
            q[exponent] += coefficient
    return q


def expected_coefficients(n):
    if n % 4 == 1:
        k = (n - 1) // 4
        c0 = (k + 1) * (k + 2) * (4 * k + 3) // 6
        c1 = (k + 1) * (4 * k * k + 11 * k + 8)
        c2 = (k + 1) * (2 * k + 3) * (4 * k + 5)
        c3 = (k + 1) * (12 * k * k + 33 * k + 22)
        c4_num = 44 * k**3 + 165 * k**2 + 217 * k + 99
    elif n % 4 == 3:
        k = (n - 3) // 4
        c0 = (k + 1) * (k + 2) * (4 * k + 9) // 6
        c1 = (k + 2) * (4 * k * k + 13 * k + 11)
        c2 = (k + 2) * (2 * k + 3) * (4 * k + 7)
        c3 = (k + 2) * (12 * k * k + 39 * k + 31)
        c4_num = 44 * k**3 + 231 * k**2 + 415 * k + 255
    else:
        raise ValueError("n must be odd")
    if c4_num % 3:
        raise AssertionError((n, c4_num))
    c4 = c4_num // 3
    return [c0, c1, c2, c3, c4, c3, c2, c1, c0]


def bernstein_coefficients(n, sign):
    """Bernstein coefficients of R(+-2u), degree four, for u in [0,1]."""
    if n % 4 == 1:
        k = (n - 1) // 4
        minus = [4*k+5, 5*k+6,
                 Fraction(32*k**3+120*k**2+208*k+129, 9),
                 Fraction(8*k**3+30*k**2+61*k+42, 3), 4*k+5]
        plus = [4*k+5, 3*k+4,
                (32*k**3+120*k**2+172*k+93)//9,
                ((4*k+5)*(14*k**2+35*k+24))//3,
                (4*k+5)**3]
    else:
        k = (n - 3) // 4
        minus = [4*k+7, 5*k+9,
                 Fraction(32*k**3+168*k**2+352*k+279, 9),
                 Fraction(8*k**3+42*k**2+97*k+87, 3), 4*k+7]
        plus = [4*k+7, 3*k+5,
                Fraction(32*k**3+168*k**2+316*k+207, 9),
                Fraction((4*k+7)*(14*k**2+49*k+45), 3),
                (4*k+7)**3]
    return minus if sign < 0 else plus


def main():
    tested = 0
    for n in range(5, 402):
        if n % 2 == 0:
            continue
        m = n + 4
        assert gcd(m, n) == 1
        q = q_coefficients_from_kernel_formula(n)
        expected = expected_coefficients(n)
        assert q == expected, (n, q, expected)
        assert q == q[::-1] and q[0] > 0
        for sign in (-1, 1):
            b = bernstein_coefficients(n, sign)
            assert all(v > 0 for v in b), (n, sign, b)
        tested += 1
    print(f"PASS: exact coefficient/positivity formulas agree for {tested} odd n in [5,401].")
    print("The all-n conclusion follows from the symbolic Bernstein formulas in RESULT.md, not from this finite test.")

if __name__ == "__main__":
    main()
