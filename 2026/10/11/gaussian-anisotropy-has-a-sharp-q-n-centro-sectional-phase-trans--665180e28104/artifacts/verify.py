#!/usr/bin/env python3
from fractions import Fraction


def check(n, m, q):
    den = n * (n - 1) * (n + 2)
    alpha = Fraction(m * (m * n + m - 2), den)
    beta = Fraction(m * (n - m), den)

    # The two projection trace identities determine alpha and beta.
    assert alpha * n * n + 2 * beta * n == m * m
    assert alpha * n + beta * (n * n + n) == m

    ex2 = 2 * beta
    ey = Fraction(m, n) - alpha - beta
    assert ex2 == Fraction(2 * m * (n - m), den)
    assert ey == Fraction(m * (n - m), (n - 1) * (n + 2))

    hess = Fraction(q * q, 4) * ex2 - Fraction(q, 2) * ey
    target = Fraction(m * (n - m) * q * (q - n), 2 * n * (n - 1) * (n + 2))
    assert hess == target

    q0 = -Fraction(1, 2) * ey
    q0_target = -Fraction(m * (n - m), 2 * (n - 1) * (n + 2))
    assert q0 == q0_target


for n in range(2, 13):
    for m in range(1, n):
        for q in range(-5, n + 6):
            if q != 0:
                check(n, m, q)

print('VERIFY_OK')
