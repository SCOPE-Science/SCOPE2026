#!/usr/bin/env python3
"""Independent finite verification of a four-primitive-root theorem at safe primes.

Run: python3 verify_safe_prime.py [upper_bound]
The proof of the unrestricted result is in RESULT.md; this is a finite check.
"""
import sys
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True


def primitive_flags(p):
    """Primitive-root criterion from orders dividing p-1=2q (q prime)."""
    q = (p - 1) // 2
    return [False] + [pow(x, 2, p) != 1 and pow(x, q, p) != 1
                      for x in range(1, p)]


def check(limit=50000):
    counts = {3: 0, 7: 0}
    for p in range(5, limit + 1, 2):
        if not (is_prime(p) and is_prime((p - 1) // 2)):
            continue
        root = primitive_flags(p)
        if p in (5, 7):
            witnesses = [(a, b) for a in range(1, p)
                         for b in range(a+1, p-a)
                         if all(root[z % p] for z in (a, b, a+b, a*b*(a+b)))]
            assert not witnesses, (p, witnesses)
            continue
        assert p >= 11 and p % 8 in (3, 7)
        if p % 8 == 3:
            actual = sum(
                all(root[z % p] for z in (2, b, b+2, 2*b*(b+2)))
                for b in range(1, p-2) if b != 2
            )
            assert actual == (p - 7) // 4, (p, actual)
            counts[3] += 1
        else:
            a = (p - 1) // 2
            b = (p - 3) // 2
            assert a != b and a + b < p
            assert all(root[z % p] for z in (a, b, a+b, a*b*(a+b))), (p, a, b)
            counts[7] += 1
    print(f"VERIFY_OK: safe primes <= {limit}, {counts[3]} in 3 mod 8 and {counts[7]} in 7 mod 8; 5,7 excluded")


if __name__ == '__main__':
    check(int(sys.argv[1]) if len(sys.argv) > 1 else 50000)
