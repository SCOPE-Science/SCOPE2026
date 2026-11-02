#!/usr/bin/env python3
"""Exact arithmetic checks for the DGZ seventh-extension vanishing theorem."""
from math import isqrt

FIELDS = (3, 5, 17, 19, 31, 47)

def prime_power(q):
    if q < 2:
        return False
    for p in range(2, isqrt(q) + 2):
        if q % p:
            continue
        n = q
        while n % p == 0:
            n //= p
        return n == 1
    return True  # q prime


def invariants(q):
    g = q * (q - 1) * (q**3 - 2*q - 2) // 2 + 1
    order = q**3 * (q**3 - 1) * (q**2 - 1)
    upper = q**7 + 1 + isqrt(4 * g * g * q**7)
    return g, order, upper


def main():
    candidates = tuple(q for q in range(3, 48)
                       if prime_power(q) and q % 7 in (3, 5))
    assert candidates == FIELDS, candidates
    for q in FIELDS:
        g, order, upper = invariants(q)
        assert q >= 3 and prime_power(q)
        assert pow(q, 6, 7) == 1 and all(pow(q, d, 7) != 1 for d in (1, 2, 3))
        assert order % 7 != 0
        assert order < upper < 7 * order
        assert 7 * order - (q**7 + 1) > 0
        assert (7 * order - q**7 - 1)**2 > 4*g*g*q**7
        print(q, g, order, upper, 7*order-upper)
    print('DGZ_DEGREE_SEVEN_EXACT_BOUNDS_PASS')

if __name__ == '__main__':
    main()
