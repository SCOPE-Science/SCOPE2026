#!/usr/bin/env python3
"""Exact finite replay for the LCM prime-increment doubling theorem."""
from math import isqrt

N = 200_000
spf = list(range(N + 2))
for i in range(2, isqrt(N + 1) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 2, i):
            if spf[j] == j:
                spf[j] = i

def factor(n):
    out = {}
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out[p] = e
    return out

# va[p] is v_p(a_n) after the current step.  Initially a_1=1.
va = {}
b = [0] * (N + 1)
for n in range(2, N + 1):
    fn = factor(n)
    g = 1
    for p, e in fn.items():
        g *= p ** min(e, va.get(p, 0))
    bn = n // g
    b[n] = bn
    for p, e in factor(1 + bn).items():
        va[p] = va.get(p, 0) + e

primes = [p for p in range(5, N // 2 + 1) if spf[p] == p]
equivalence_mismatches = []
prime_pair_mismatches = []
forced_ones = 0
for p in primes:
    left = b[2 * p] == 1
    right = b[2 * p - 1] == 2 * p - 1
    if left != right:
        equivalence_mismatches.append((p, b[2 * p - 1], b[2 * p]))
    if left:
        forced_ones += 1
    q = 2 * p - 1
    q_is_prime = spf[q] == q
    if left != q_is_prime:
        prime_pair_mismatches.append((p, q, b[2 * p - 1], b[2 * p]))

assert not equivalence_mismatches
assert not prime_pair_mismatches
print(
    "VERIFY_OK",
    f"N={N}",
    f"primes={len(primes)}",
    f"equivalence_mismatches={len(equivalence_mismatches)}",
    f"prime_pair_mismatches={len(prime_pair_mismatches)}",
    f"forced_ones={forced_ones}",
)
