#!/usr/bin/env python3
"""Exact bounded search and a divisor-pair witness for a near-perfect/strongly pseudoperfect intersection."""
from math import isqrt

LIMIT = 174592
TARGET = 174592
OMITTED = 43648
# Each ordered entry (d, TARGET//d) is a complete complementary divisor orbit.
INCLUDED_PAIRS = (
    (1, 174592), (2, 87296), (4, 43648),
    (8, 21824), (22, 7936), (31, 5632),
    (32, 5456), (124, 1408), (176, 992),
)

def divisors(n):
    lo, hi = [], []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            lo.append(d)
            if d*d != n:
                hi.append(n // d)
    return lo + hi[::-1]

def strongly_pseudoperfect(n, ds):
    # Every subset closed under d <-> n/d consists of complete disjoint
    # complementary orbits; the only singleton orbit can be sqrt(n).
    weights = [d + n // d if d*d < n else d for d in ds if d*d <= n]
    possible = 1
    cap = (1 << (2*n + 1)) - 1
    for weight in weights:
        possible = (possible | (possible << weight)) & cap
    return bool((possible >> (2*n)) & 1)

def independent_sigma(n):
    return sum(divisors(n))

def main():
    # Complete divisor-sum sieve: each d is added to exactly those multiples
    # that it divides. Both the divisor 1 and the divisor n are included.
    sigma = [0] * (LIMIT + 1)
    for d in range(1, LIMIT + 1):
        for multiple in range(d, LIMIT + 1, d):
            sigma[multiple] += d
    near = []
    overlaps = []
    for n in range(2, LIMIT + 1):
        delta = sigma[n] - 2*n
        if delta <= 0 or delta >= n or n % delta:
            continue
        near.append(n)
        ds = divisors(n)
        assert sum(ds) == sigma[n]  # Independent divisor traversal.
        if strongly_pseudoperfect(n, ds):
            overlaps.append(n)
    assert len(near) == 37, (len(near), near)
    assert overlaps == [TARGET], overlaps
    ds = divisors(TARGET)
    assert len(ds) == 40
    assert independent_sigma(TARGET) == sigma[TARGET] == 392832
    assert sigma[TARGET] == 2 * TARGET + OMITTED
    assert OMITTED in ds and OMITTED < TARGET
    paired = set()
    for a, b in INCLUDED_PAIRS:
        assert a in ds and b in ds and a*b == TARGET
        assert a != b
        assert a not in paired and b not in paired
        paired.update((a, b))
    assert sum(paired) == 2*TARGET
    assert all((TARGET//x) in paired for x in paired)
    assert strongly_pseudoperfect(TARGET, ds)
    print('VERIFY_OK limit=%d near_candidates=%d intersection=%s '
          'factorization=2^9*11*31 sigma=%d redundant_divisor=%d '
          'included_orbits=%d included_divisors=%d' %
          (LIMIT,len(near),overlaps,sigma[TARGET],OMITTED,len(INCLUDED_PAIRS),len(paired)))

if __name__ == '__main__':
    main()
