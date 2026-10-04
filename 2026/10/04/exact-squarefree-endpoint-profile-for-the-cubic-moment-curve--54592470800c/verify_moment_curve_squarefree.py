#!/usr/bin/env python3
from collections import Counter
from itertools import product
from math import prod

def signature(t, p):
    return tuple(sum(pow(x, k, p) for x in t) % p for k in (1, 2, 3))

def brute_J(p):
    fibers = Counter(signature(t, p) for t in product(range(p), repeat=3))
    return sum(v*v for v in fibers.values()), Counter(fibers.values())

def local_formula(p):
    return p * (6*p*p - 9*p + 4)

for p in (5, 7, 11):
    got, sizes = brute_J(p)
    want = local_formula(p)
    assert got == want, (p, got, want)
    # Multiset fibers have sizes 1 (aaa), 3 (aab), or 6 (abc).
    assert set(sizes) == {1, 3, 6}, (p, sizes)
    assert sizes[1] == p
    assert sizes[3] == p*(p-1)
    assert sizes[6] == p*(p-1)*(p-2)//6

for primes in ((5, 7), (5, 11), (5, 7, 11)):
    N = prod(primes)
    local_product = prod(local_formula(p) for p in primes)
    normalized = N**3 * prod((6*p*p - 9*p + 4) for p in primes) // prod(p*p for p in primes)
    assert local_product == normalized
    # Equivalent exact integer form of N^3 * product(6 - 9/p + 4/p^2).
    direct_integer = prod(p*(6*p*p - 9*p + 4) for p in primes)
    assert local_product == direct_integer

print("VERIFY_OK")
