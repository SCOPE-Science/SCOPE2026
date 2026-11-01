#!/usr/bin/env python3
"""Exact independent finite checks of the Thue--Morse autocorrelation recurrence.

The infinite-domain proof is the integral-matrix parity induction in RESULT.md;
this checker is a finite consistency test, not that proof.
"""
from fractions import Fraction

LIMIT = 1 << 16
eta = [None] * (LIMIT + 1)
eta[0] = Fraction(1)
eta[1] = Fraction(-1, 3)
for n in range(2, LIMIT + 1):
    if n % 2 == 0:
        eta[n] = eta[n // 2]
    else:
        eta[n] = -(eta[n // 2] + eta[n // 2 + 1]) / 2

base = ((-1, 0), (0, 1), (1, 0), (0, -1))
for n in range(4, 8):
    k = n.bit_length() - 1
    assert (3 * 2 ** (k - 2) * eta[n],
            3 * 2 ** (k - 2) * eta[n + 1]) == base[n - 4]

pairs = {n: base[n - 4] for n in range(4, 8)}
for n in range(8, LIMIT):
    a, b = pairs[n // 2]
    pair = (2 * a, -a - b) if n % 2 == 0 else (-a - b, 2 * b)
    pairs[n] = pair
    k = n.bit_length() - 1
    assert Fraction(pair[0], 3 * 2 ** (k - 2)) == eta[n]
    assert Fraction(pair[1], 3 * 2 ** (k - 2)) == eta[n + 1]
    assert (pair[0] + pair[1]) % 2 == 1
    if n % 2:
        assert pair[0] % 2 == 1 and pair[1] % 2 == 0
        assert eta[n] != 0
        assert eta[n].numerator % 2 == 1
        assert (3 * 2 ** (k - 2) * eta[n]).denominator == 1
    else:
        assert pair[0] % 2 == 0 and pair[1] % 2 == 1

for n in range(1, LIMIT):
    odd = n // (n & -n)
    assert (eta[n] == 0) == (odd in (5, 7))
for n in range(4, LIMIT):
    assert eta[n] != eta[n + 1]
    assert eta[n] != -eta[n + 1]
assert eta[1] == eta[2]
assert eta[2] == -eta[3]
assert eta[3] == -eta[4]
for K in range(3, 16):
    assert sum(eta[n] == 0 for n in range(1, 1 << K)) == 2 * (K - 2)

print('THUE_MORSE_DYADIC_ZERO_CERTIFICATE_OK', LIMIT - 1)
