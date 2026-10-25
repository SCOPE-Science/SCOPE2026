#!/usr/bin/env python3
"""Exact verification for the odd squarefree strongly pseudoperfect prime-support theorem.

Uses only Python integer arithmetic and the standard library. No numerical
approximations or external datasets are used.
"""
from math import isqrt, prod
from hashlib import sha256


def is_prime(n):
    if n < 2:
        return False
    return all(n % k for k in range(2, isqrt(n) + 1))


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def pair_weights(m, t):
    # Every complementary pair in m*t has exactly one member dividing m.
    return [d + (m // d) * t for d in divisors(m)]


def sqrt_pairs(n):
    return [d + n // d for d in range(1, isqrt(n) + 1) if n % d == 0]


def possible_mitm(weights, target):
    split = len(weights) // 2
    left, right = weights[:split], weights[split:]
    a = {0}
    b = {0}
    for w in left:
        a |= {x + w for x in a}
    for w in right:
        b |= {x + w for x in b}
    return any((target - x) in b for x in a)


def possible_bitset(weights, target):
    # Bit j of bits is 1 exactly when a subset has integer sum j.
    bits = 1
    for w in weights:
        bits |= bits << w
    return bool((bits >> target) & 1)


def main():
    assert prod((p+1 for p in (3, 5, 7, 11))) < 2 * prod((3, 5, 7, 11))
    assert prod((p+1 for p in (5, 7, 11, 13, 17))) < 2 * prod((5, 7, 11, 13, 17))
    assert prod((p+1 for p in (3, 7, 11, 13, 17))) < 2 * prod((3, 7, 11, 13, 17))
    assert prod((p+1 for p in (3, 5, 11, 13, 17))) < 2 * prod((3, 5, 11, 13, 17))
    assert prod((p+1 for p in (3, 5, 7, 23, 29))) < 2 * prod((3, 5, 7, 23, 29))
    expected = {11: (384, 71), 13: (64, 12), 17: (30, 3), 19: (25, 1)}
    count = 0
    record = []
    for s, (bound, expected_count) in expected.items():
        m = 105 * s
        assert bound == 192 * (s+1) // (18*s-192)
        tt = [t for t in range(s+1, bound+1) if is_prime(t)]
        assert len(tt) == expected_count
        for t in tt:
            n = m*t
            weights = pair_weights(m, t)
            assert len(weights) == 16
            assert sorted(weights) == sorted(sqrt_pairs(n))
            sigma = 192*(s+1)*(t+1)
            assert sum(weights) == sigma
            assert sigma >= 2*n
            assert not possible_mitm(weights, 2*n), (s, t)
            assert not possible_bitset(weights, 2*n), (s, t)
            record.append((s, t))
            count += 1
    assert count == 87
    witness_factors = (3, 5, 11, 13, 19, 23)
    n = prod(witness_factors)
    assert n == 937365 and all(is_prime(p) for p in witness_factors)
    omitted = [(55, 17043), (57, 16445), (65, 14421),
               (143, 6555), (165, 5681)]
    assert all(d * e == n for d, e in omitted)
    assert len(set(x for pair in omitted for x in pair)) == 10
    assert sum(d+e for d,e in omitted) == 60630
    sigma = prod(p+1 for p in witness_factors)
    assert sigma == 1935360 and sigma - 60630 == 2*n
    # Independently expand the retained divisor set and test complementation.
    excluded = {v for pair in omitted for v in pair}
    retained = {d for d in divisors(n) if d not in excluded}
    assert all(n//d in retained for d in retained)
    assert sum(retained) == 2*n
    print('VERIFY_OK')
    print('FIVE_PRIME_CANDIDATES', count)
    print('CANDIDATES_BY_FOURTH_PRIME', expected)
    print('CANDIDATE_TABLE_SHA256', sha256(repr(record).encode('utf-8')).hexdigest())
    print('SIX_PRIME_WITNESS', n, 'OMITTED_SUM', sigma - 2*n)

if __name__ == '__main__':
    main()
