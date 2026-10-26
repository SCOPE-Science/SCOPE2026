#!/usr/bin/env python3
"""Exact finite checks of a Dedekind-sum prime-cube fiber (stdlib only)."""
from fractions import Fraction
from math import gcd


def normalized(a, b):
    a %= b
    if a == 1:
        return Fraction((b - 1) * (b - 2), b)
    if a == 0:
        raise ValueError("nonunit residue")
    return (Fraction(a * a + b * b + 1, a * b) - 3
            - normalized(b % a, a))


def check(p):
    assert all(p % d for d in range(2, int(p**0.5) + 1))
    modulus = p**3
    target = 3 - Fraction(p*p + 2, modulus)
    lhs = {a for a in range(1, modulus)
           if a % p and normalized(a, modulus) == target}
    first = {p - 1 + j*p*p for j in range(1, p - 1)}
    second = {p*p - p - 1 + j*p*p for j in range(p - 2)}
    rhs = first | second
    assert not first & second
    assert len(rhs) == 2*p-4
    assert lhs == rhs, (p, lhs ^ rhs)
    e0 = p - 1
    e1 = p**3 - p*p + p - 1
    assert normalized(e0, modulus) - target == p*p - 1
    assert normalized(e1, modulus) - target == 1 - p*p
    assert {a for a in range(1, modulus) if a % p and
            ((a - (p-1+p*p))*(a*(p-1+p*p)-1)) % modulus == 0} - rhs == {
                e0, e1, pow(e0, -1, modulus), pow(e1, -1, modulus)}


if __name__ == '__main__':
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        check(p)
    print('VERIFY_OK')
