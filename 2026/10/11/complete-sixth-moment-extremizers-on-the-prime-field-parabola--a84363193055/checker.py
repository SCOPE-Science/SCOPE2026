#!/usr/bin/env python3
"""Exact reproducibility checks for finite-prime-field parabola sixth moments.

Run with Python 3 and no external packages. The general classification
is proved analytically; the finite checks here test the normalizations,
collision geometry, and the quadratic-character construction.
"""
from collections import defaultdict
from itertools import product

PRIMES = (5, 7, 11, 13, 17, 19, 23)
assert sorted(PRIMES) == list(PRIMES)
total_fibers = 0
total_cubic_phase_tests = 0

for p in PRIMES:
    fibers = defaultdict(list)
    for a, b, c in product(range(p), repeat=3):
        key = ((a+b+c) % p, (a*a+b*b+c*c) % p)
        fibers[key].append((a,b,c))
    energy = sum(len(triples)**2 for triples in fibers.values())
    assert energy == p**4 + p**3 - p**2, (p, energy)
    assert len(fibers) == p*p
    total_fibers += len(fibers)

    for t in range(p):
        a = (t, (t+3)%p, (t+3)%p)
        b = ((t+1)%p, (t+1)%p, (t+4)%p)
        assert (sum(a)-sum(b))%p == 0
        assert (sum(x*x for x in a)-sum(x*x for x in b))%p == 0

    # For quadratic phases, products on each three-fold-sum fiber have
    # identical p-th-root-of-unity exponents, for every A and B.
    for A in range(p):
        for B in range(p):
            for key, triples in fibers.items():
                target = (A*key[0]+B*key[1]) % p
                assert all((sum(A*t+B*t*t for t in ts)-target) % p == 0
                           for ts in triples)
            total_cubic_phase_tests += 1

    # The cross-fiber phase of a genuinely cubic polynomial fails
    # for at least one equal-sum/equal-squares triple collision.
    assert any(len({sum(t**3 for t in tri) % p for tri in triples}) > 1
               for triples in fibers.values()), p
    print(f"p={p} fibers={len(fibers)} energy={energy} "
          f"sharp_ratio={p**-4*energy:.12g} characters={p*p}")

print(f"PRIMES={len(PRIMES)} FIBERS={total_fibers} "
      f"QUADRATIC_PHASE_TESTS={total_cubic_phase_tests}")
print('EXACT_CHECKS_PASS')
