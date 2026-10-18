#!/usr/bin/env python3
"""Independent finite verifier for the five-support exclusion.

This checker uses an Eratosthenes sieve, product-of-prime-subsets pair
construction, and integer-bitset reachability rather than trial-division,
divisor enumeration, and a dictionary subset-sum search.
"""
from itertools import combinations
from math import prod

LIMIT = 384
sieve = [True] * (LIMIT + 1)
sieve[0] = sieve[1] = False
for p in range(2, int(LIMIT ** 0.5) + 1):
    if sieve[p]:
        for q in range(p*p, LIMIT + 1, p):
            sieve[q] = False
primes = [p for p in range(LIMIT + 1) if sieve[p]]
limits = {11:384,13:64,17:30,19:25}
counts, counts_mod4 = {}, {}
for r, upper in limits.items():
    found = 0
    examined = 0
    for s in primes:
        if not r < s <= upper:
            continue
        found += 1
        prime_factors = (3,5,7,r,s)
        n = prod(prime_factors)
        if n % 4 != 1:
            continue
        examined += 1
        delta = prod(p+1 for p in prime_factors) - 2*n
        assert delta >= 0
        divisors = [prod(t) for size in range(6)
                    for t in combinations(prime_factors,size)]
        assert len(divisors) == 32 and len(set(divisors)) == 32
        pair_sums = [d+n//d for d in divisors if d < n//d]
        assert len(pair_sums) == 16
        mask = (1 << (delta + 1)) - 1
        possible_sums = 1
        for weight in pair_sums:
            possible_sums = (possible_sums | (possible_sums << weight)) & mask
        assert not (possible_sums & (1 << delta)), (r,s)
    counts[r] = found
    counts_mod4[r] = examined
assert counts == {11:71,13:12,17:3,19:1}, counts
assert counts_mod4 == {11:37,13:6,17:1,19:1}, counts_mod4

n = 937365
assert n == prod((3,5,11,13,19,23))
ps = ((55,17043),(57,16445),(65,14421),(143,6555),(165,5681))
assert all(a*b == n for a,b in ps)
assert len(set(x for pair in ps for x in pair)) == 10
assert sum(sum(pair) for pair in ps) == prod(p+1 for p in (3,5,11,13,19,23)) - 2*n
print('Independent sieve, subset-divisor enumeration, bitset checks: PASS')
print('candidate counts:', counts)
print('modulo-four survivor counts:', counts_mod4)
print('six-support witness omitted pairs: PASS')
