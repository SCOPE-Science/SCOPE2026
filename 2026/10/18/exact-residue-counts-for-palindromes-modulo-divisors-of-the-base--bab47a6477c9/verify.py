"""Exact finite regression for palindromes modulo divisors of base plus one.

Uses only standard-library integer and rational operations.
"""
from fractions import Fraction
from itertools import product


def delta(r, s, q):
    return int((r - s) % q == 0)


def formula(b, q, length, r):
    assert b >= 2 and q >= 2 and (b + 1) % q == 0
    assert length >= 1 and 0 <= r < q
    if length == 1:
        return Fraction(b + 1, q) - delta(r, 0, q) - delta(r, -1, q)
    if length % 2 == 0:
        k = length // 2
        return Fraction((b - 1) * b ** (k - 1) * delta(r, 0, q))
    k = (length - 1) // 2
    eps = int(q % 2 == 0)
    sgn = (-1) ** r
    total = (b - 1) * b ** k
    alt = (b - 1) * b ** (k - 1)
    return (Fraction(total + eps * sgn * alt, q)
            + (-1) ** (k + 1) * (delta(r, 1, q) + delta(r, -1, q)
                                     - Fraction(2, q)
                                     + Fraction(2 * eps * sgn, q)))


def enumerated_residues(b, q, length):
    counts = [0] * q
    half = (length + 1) // 2
    for leading in range(1, b):
        for trailing in product(range(b), repeat=half - 1):
            free = (leading,) + trailing
            digits = free + (free[-2::-1] if length % 2 else free[::-1])
            value = 0
            for digit in digits:
                value = b * value + digit
            counts[value % q] += 1
    return counts


def main():
    checks = 0
    for b in range(2, 15):
        for q in range(2, b + 2):
            if (b + 1) % q:
                continue
            for length in range(1, 8):
                counts = enumerated_residues(b, q, length)
                total = (b - 1) * b ** ((length - 1) // 2)
                assert sum(counts) == total
                for r in range(q):
                    exact = formula(b, q, length, r)
                    assert exact.denominator == 1
                    assert counts[r] == exact.numerator, (b, q, length, r, counts[r], exact)
                    if length >= 3 and length % 2:
                        k = (length - 1) // 2
                        bias = int(q % 2 == 0) * (-1) ** r * (b - 1) * b ** (k - 1)
                        assert abs(Fraction(counts[r]) - Fraction(total + bias, q)) < 1
                    checks += 1
    print('PALINDROME_BASE_PLUS_ONE_EXACT_OK', 'residue_checks=', checks)


if __name__ == '__main__':
    main()
