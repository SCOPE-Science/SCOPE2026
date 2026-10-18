"""Finite consistency tests for the cyclic-group sentential modal invariant.

The general theorem relies on Baur--Monk and Smith normal form, not on sampling.
This script checks representative finite quotient back/forth constructions.
"""
from itertools import product
from math import gcd

PRIMES = (2, 3, 5, 7)
CAPS = (4, 3, 2, 2)
BOUND = 9


def valuation(n, p):
    r = 0
    while n % p == 0:
        n //= p
        r += 1
    return r


def signature(n):
    return (tuple(min(valuation(n, p), e) for p, e in zip(PRIMES, CAPS)), int(n >= BOUND))


def le(a, b):
    return a[1] <= b[1] and all(x <= y for x, y in zip(a[0], b[0]))


def fresh_prime(n):
    q = 11
    while n % q == 0:
        q += 1
        while any(q % d == 0 for d in range(2, int(q**0.5) + 1)):
            q += 1
    return q


def lift(n, target):
    assert le(signature(n), target)
    if target[1] == 0:
        m = next(x for x in range(1, BOUND) if signature(x) == target)
        assert m % n == 0
        return m
    m = n
    for p, e, b in zip(PRIMES, CAPS, target[0]):
        old = valuation(m, p)
        if old < b:
            m *= p ** (b - old)
        if b < e:
            assert valuation(m, p) == b
    if m < BOUND:
        m *= fresh_prime(m)
    assert m % n == 0 and signature(m) == target, (n, target, m)
    return m


all_sigs = {(v, 1) for v in product(*(range(e + 1) for e in CAPS))}
all_sigs.update(signature(n) for n in range(1, BOUND))
assert len(all_sigs) == 8 + 5 * 4 * 3 * 3
assert all(signature(n)[1] == 0 for n in range(1, BOUND))
count_back = 0
for n in range(1, 121):
    s = signature(n)
    assert s in all_sigs
    for t in all_sigs:
        if le(s, t):
            lift(n, t)
            count_back += 1

count_cube = 0
for k in range(1, 5):
    ps = PRIMES[:k]
    for n in range(1, 121):
        old = {i for i, p in enumerate(ps) if n % p == 0}
        for bits in product((0, 1), repeat=k):
            target = {i for i in range(k) if bits[i]}
            if old <= target:
                m = n
                for i in target - old:
                    m *= ps[i]
                assert m % n == 0
                assert {i for i, p in enumerate(ps) if m % p == 0} == target
                count_cube += 1

# The Smith identities for one homogeneous equation and image of multiplication.
count_smith = 0
for n in range(1, 101):
    for a in range(-9, 10):
        roots = sum((a * x) % n == 0 for x in range(n))
        image = len({(a * x) % n for x in range(n)})
        assert roots == gcd(n, a)
        assert image == n // gcd(n, a)
        count_smith += 1

print(f'CYCLIC_MODAL_VERIFY_OK finite_signatures={len(all_sigs)} back_lifts={count_back} boolean_cube_lifts={count_cube} smith_checks={count_smith}')
