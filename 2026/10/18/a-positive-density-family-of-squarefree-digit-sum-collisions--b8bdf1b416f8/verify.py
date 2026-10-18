#!/usr/bin/env python3
"""Independent finite checks of a squarefree base-digit-sum witness theorem."""
from math import isqrt


def digit_sum(n, base):
    total = 0
    while n:
        total += n % base
        n //= base
    return total


def squarefree(n):
    for p in range(2, isqrt(n) + 1):
        if n % (p * p) == 0:
            return False
    return True


def witnesses(base):
    return base * (2 * base - 3), (base - 2) * (2 * base - 3)


def run():
    # Full unrestricted collision identity and actual base-b digit sums.
    for b in range(7, 30001):
        x, y = witnesses(b)
        assert x > y > 0
        assert digit_sum(x, b) == b - 2
        assert digit_sum(y, b) == b
        assert x * digit_sum(x, b) == y * digit_sum(y, b)

    # Actual squarefreeness of both witnesses versus the prime-factor criterion.
    qualifying = []
    for b in range(7, 2001):
        x, y = witnesses(b)
        actual = squarefree(x) and squarefree(y)
        criterion = (b % 3 != 0 and squarefree(b) and
                     squarefree(b - 2) and squarefree(2 * b - 3))
        assert actual == criterion, (b, actual, criterion)
        if b >= 11 and actual:
            qualifying.append(b)
    assert qualifying[:10] == [13, 17, 19, 23, 31, 35, 37, 41, 43, 53]

    # Local prime-square restrictions, including the exceptional primes 2 and 3.
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        modulus = p * p
        allowed = [b for b in range(modulus) if
                   witnesses(b)[0] % modulus != 0 and
                   witnesses(b)[1] % modulus != 0]
        expected = 2 if p == 2 else (5 if p == 3 else modulus - 3)
        assert len(allowed) == expected, (p, len(allowed), expected)

    print('PASS: 29,994 bases checked for the digit-sum identity.')
    print('PASS: 1,994 bases checked for exact squarefreeness equivalence.')
    print('PASS: 11 prime-square local residue counts checked.')
    print('PASS: first ten witness bases are', qualifying[:10])
    print('Finite tests are not proofs of the infinite density statement.')


if __name__ == '__main__':
    run()
