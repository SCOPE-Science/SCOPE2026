#!/usr/bin/env python3
"""Exact trial-division confirmation of a three-prime divisibility theorem."""
from math import gcd, isqrt, lcm


def prime(n):
    if n < 2:
        return False
    for k in range(2, isqrt(n) + 1):
        if n % k == 0:
            return False
    return True


def sieve(p):
    result = []
    preliminary = []
    table = []
    for d in range(1, p):
        candidates = []
        hits = []
        K = (p + 1) * (p + d)
        for q in range(p + 2, 2 * p * p + p + 1):
            if not prime(q) or K % (q - 1):
                continue
            if (p * q + 1) % d:
                continue
            r = 1 + (p * q + 1) // d
            if r <= q or not prime(r):
                continue
            candidates.append((q, r))
            if (q * r + 1) % (p - 1) == 0 and (p * r + 1) % (q - 1) == 0:
                hits.append((q, r))
                result.append((p, q, r))
        table.append((d, K, candidates, hits))
        preliminary.extend(candidates)
    return sorted(set(result)), table


def direct(p):
    hits = []
    for q in range(p + 2, 2 * p * p + p + 1):
        if not prime(q):
            continue
        for r in range(q + 2, p * q + 3):
            if prime(r) and ((p * q * r + 1) % lcm(p - 1, q - 1, r - 1) == 0):
                hits.append((p, q, r))
    return sorted(hits)


EXPECTED = {
    3: [(3, 5, 17), (3, 17, 53)],
    5: [(5, 7, 13), (5, 7, 37), (5, 13, 67), (5, 19, 97), (5, 43, 109)],
}
for p in (3, 5):
    hits, table = sieve(p)
    brute = direct(p)
    assert hits == brute == EXPECTED[p], (hits, brute, EXPECTED[p])
    for _, q, r in hits:
        assert (p * q + 1) % (r - 1) == 0
        d = (p * q + 1) // (r - 1)
        assert 1 <= d < p
        assert ((p + 1) * (p + d)) % (q - 1) == 0
        assert q <= 2 * p * p + p
    print("PRIME", p, "BOUND_Q", 2 * p * p + p, "HITS", hits)
    print("PARAMETER_ROWS", table)
print("VERIFY_OK sieve_equals_independent_direct_search")
