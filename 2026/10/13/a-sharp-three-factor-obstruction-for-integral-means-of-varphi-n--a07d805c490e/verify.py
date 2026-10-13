#!/usr/bin/env python3
"""Exact finite corroboration of the low-multiplicity integer-means theorem."""
from math import isqrt

LIMIT = 1_000_000
PAIR_LIMIT = 1200

smallest = list(range(LIMIT + 1))
smallest[0] = 0
smallest[1] = 1
for p in range(2, isqrt(LIMIT) + 1):
    if smallest[p] == p:
        for m in range(p*p, LIMIT+1, p):
            if smallest[m] == m:
                smallest[m] = p

def factor(n):
    result = []
    while n > 1:
        p = smallest[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        result.append((p, e))
    return result

def phi_sigma(factors):
    ph = 1
    sg = 1
    for p, e in factors:
        ph *= (p-1)*p**(e-1)
        sg *= (p**(e+1)-1)//(p-1)
    return ph, sg

def integral_means(u, v):
    if (u + v) % 2:
        return False
    product = u*v
    if isqrt(product)**2 != product:
        return False
    return (2*product) % (u+v) == 0

pair_cases = 0
for x in range(2, PAIR_LIMIT+1):
    for y in range(x, PAIR_LIMIT+1):
        pair_cases += 1
        assert not integral_means((x-1)*(y-1), (x+1)*(y+1)), (x, y)

omega_le_two = 0
min_omega = None
min_examples = []
all_hits = []
for n in range(2, LIMIT+1):
    fac = factor(n)
    ph, sg = phi_sigma(fac)
    if sum(e for p, e in fac) <= 2:
        omega_le_two += 1
        assert not integral_means(ph, sg), (n, fac, ph, sg)
    if integral_means(ph, sg):
        all_hits.append(n)
        k = sum(e for p, e in fac)
        if min_omega is None or k < min_omega:
            min_omega = k
            min_examples = [n]
        elif k == min_omega:
            min_examples.append(n)

assert all_hits[0] == 248 and 418 in all_hits and 477 in all_hits
assert min_omega == 3
assert integral_means(180, 720)
assert integral_means(312, 702)
assert 1 + len(all_hits) == 67

print("VERIFY_OK", f"limit={LIMIT}", f"pair_limit={PAIR_LIMIT}",
      f"pair_cases={pair_cases}", f"omega_le2_checked={omega_le_two}",
      f"mean_integral_count_including_1={1+len(all_hits)}",
      f"least_omega={min_omega}",f"sharp_examples={min_examples[:8]}")
