#!/usr/bin/env python3
"""Exact finite checks for the index-eight centered-coset theorem.

No third-party modules or precomputed data; finite checks are not the proof
of the asserted infinite-prime or density statements.
"""
from math import gcd

P, G = 41, 6
K = {pow(G, 8*i, P) for i in range(5)}
assert K == {1, 10, 16, 18, 37}
assert pow(G, 20, P) == P-1 and pow(G, 8, P) == 10
C = [{(pow(G, j, P)*k) % P for k in K} for j in range(8)]
assert len(set.union(*C)) == 40
assert all(len(c) == 5 for c in C)
assert all(not (C[i] & C[j]) for i in range(8) for j in range(i))
R = [sum(c) for c in C]
assert R == [82, 82, 123, 123, 123, 123, 82, 82]


def is_prime(n):
    return n >= 2 and all(n % k for k in range(2, int(n**0.5)+1))


def primitive_root(q):
    for a in range(2, q):
        if len({pow(a, i, q) for i in range(1, q)}) == q-1:
            return a
    raise AssertionError('missing primitive root for prime')

expected_witnesses = {0: 23, 2: 53, 4: 5, 6: 3, 8: 37}
counts = {};
for q in range(3, 400):
    if not is_prime(q) or q == P or (q-1) % 5 == 0:
        continue
    m = P*q
    h = next(h for h in range(8) if q % P in C[h])
    order = 5*(q-1)
    midpoint = m*order//2
    H = {x for x in range(1, m) if x % P in K and x % q != 0}
    assert len(H) == order
    root_q = primitive_root(q)
    a = next(x for x in range(1, m) if x % P == 10 and x % q == root_q)
    assert {pow(a, i, m) for i in range(order)} == H
    num_centered = 0
    for j in range(8):
        E = {x for x in range(1, m) if x % P in C[j] and x % q != 0}
        assert len(E) == order
        delta = sum(E)-midpoint
        assert delta == q*(R[j]-R[(j-h) % 8])
        num_centered += (delta == 0)
    assert num_centered == 8-2*min(h, 8-h)
    counts[q] = num_centered
assert len(counts) == 60
for h in range(8):
    admissible = [a for a in range(1, 205) if gcd(a, 205) == 1 and a % 41 in C[h] and a % 5 in (2, 3, 4)]
    assert len(admissible) == 15
assert all(counts[q] == n for n, q in expected_witnesses.items())
print('VERIFY_OK admissible_primes=60 direct_coset_sums=480 witness_counts=5')
