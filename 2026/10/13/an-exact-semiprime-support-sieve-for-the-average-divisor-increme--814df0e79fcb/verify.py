#!/usr/bin/env python3
"""Exact finite corroboration of the semiprime divisor-mean increment sieve."""
from math import isqrt

LIMIT = 2_000_000
M = LIMIT + 1

sigma = [0] * (M + 1)
for d in range(1, M + 1):
    for multiple in range(d, M + 1, d):
        sigma[multiple] += d

spf = list(range(LIMIT + 1))
spf[0] = 0
spf[1] = 1
for p in range(2, isqrt(LIMIT) + 1):
    if spf[p] == p:
        for x in range(p * p, LIMIT + 1, p):
            if spf[x] == x:
                spf[x] = p

hits = []
checked = 0
p2_hits = []
p3_hits = []
for n in range(6, LIMIT + 1):
    p = spf[n]
    q = n // p
    if p >= q or spf[q] != q:  # squarefree semiprimes only
        continue
    checked += 1
    original = (4 * (sigma[n + 1] - (p + 1) * (q + 1))
                == (p + 1) * (q + 1))
    reduced = 4 * sigma[n + 1] == 5 * (p + 1) * (q + 1)
    assert original == reduced, (n, p, q)
    if p == 3:
        # Exact transformed equation, including the necessary progression.
        odd_branch = (q % 12 == 11 and
                      sigma[(3 * q + 1) // 2] ==
                      20 * ((q - 11) // 12 + 1))
        assert original == odd_branch, (n, p, q)
    if original:
        assert p in (2, 3), (n, p, q)
        if p == 2:
            assert q % 16 == 15, (n, q)
            p2_hits.append(n)
        else:
            assert q % 12 == 11, (n, q)
            p3_hits.append(n)
        hits.append(n)

for p, q in ((7, 11), (7, 13)):
    n = p * q
    assert 4 * sigma[n + 1] != 5 * (p + 1) * (q + 1)

assert 753 in hits and 148173 in hits
assert 4 * sigma[754] == 5 * 4 * 252
assert 4 * sigma[148174] == 5 * 4 * 49392
assert sigma[377] == 420
assert sigma[74087] == 82320
print('VERIFY_OK', 'limit=' + str(LIMIT),
      'squarefree_semiprimes_checked=' + str(checked),
      'semiprime_hits=' + str(hits),
      'p2_hits=' + str(p2_hits),
      'p3_hits=' + str(p3_hits))
