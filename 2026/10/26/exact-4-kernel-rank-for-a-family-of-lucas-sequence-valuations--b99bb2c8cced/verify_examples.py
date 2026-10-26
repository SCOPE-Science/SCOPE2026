#!/usr/bin/env python3
"""Finite exact-integer sanity checks for the Lucas valuation formula.

This script checks examples only; the infinite rank proof is in RESULT.md.
"""

def v2(n):
    n = abs(n)
    if n == 0:
        raise ValueError("valuation of zero is not used here")
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def v4(n):
    n = abs(n)
    if n == 0:
        raise ValueError("valuation of zero is not used here")
    e = 0
    while n % 4 == 0:
        n //= 4
        e += 1
    return e


def check_pair(a, b, terms=500):
    if a == 0 or a % 2 != 0 or b == 0 or b % 2 != 1:
        raise ValueError("requires nonzero even a and odd nonzero b")
    U = [0, 1]
    for _ in range(terms - 1):
        U.append(a * U[-1] + b * U[-2])
    t = v2(a)
    for n in range(1, terms + 1):
        expected = 0 if n % 2 else (v2(n) + t - 1) // 2
        actual = v4(U[n])
        if actual != expected:
            raise AssertionError((a, b, n, actual, expected))


def main():
    pairs = [(a, b) for a in (2, 4, 8, 16, 32) for b in (1, 3, 5)]
    for a, b in pairs:
        check_pair(a, b)
    print(f"PASS: {len(pairs)} coefficient pairs, 500 terms each; exact integers only")


if __name__ == "__main__":
    main()
