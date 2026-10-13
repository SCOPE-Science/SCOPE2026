#!/usr/bin/env python3
from fractions import Fraction
from math import comb


def power_sum(k, q):
    e = [Fraction(0) for _ in range(k + 1)]
    e[0] = Fraction(1)
    for j in range(1, min(k, q - 1) + 1):
        if j % 2 == 0:
            e[j] = Fraction(((-1) ** (j // 2)) * comb(q, j + 1), q)
    pows = [Fraction(0) for _ in range(k + 1)]
    for m in range(1, k + 1):
        acc = Fraction(0)
        for j in range(1, m):
            acc += ((-1) ** (j - 1)) * e[j] * pows[m - j]
        pows[m] = acc + ((-1) ** (m + 1)) * m * e[m]
    return pows[k]


def cotangent_block(sig):
    assert sig % 2 == 0
    m = sig // 2
    return ((-1) ** m) * (2 * power_sum(sig, m) - power_sum(sig, sig))


def inv_mod(a, p):
    return pow(a % p, -1, p)


def main():
    # Regression datum: the 2026 source lists denominator 5^5 at n=20.
    c20 = cotangent_block(20)
    assert c20.denominator == 5 ** 5

    c28 = cotangent_block(28)
    expected = Fraction(-34695770811027473098809241186, 49)
    assert c28 == expected
    assert c28.denominator == 49
    assert c28.numerator % 7 == 2

    residue_fraction = Fraction(14, 45)
    assert Fraction(10, 9) - Fraction(4, 5) == residue_fraction

    primes = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    for p in primes:
        c = cotangent_block(4 * p)
        assert c.denominator == p ** 3, (p, c.denominator)
        scaled_num = c.numerator * (p ** 3 // c.denominator)
        lhs = scaled_num % p
        rhs = (14 * inv_mod(45, p)) % p
        assert lhs == rhs, (p, lhs, rhs)

    print(f"VERIFY_OK p7_den={c28.denominator} generic_primes={len(primes)} residue=14/45")


if __name__ == '__main__':
    main()
