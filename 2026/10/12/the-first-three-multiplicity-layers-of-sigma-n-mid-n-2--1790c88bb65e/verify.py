#!/usr/bin/env python3
from math import isqrt

LIMIT = 1_000_000

spf = list(range(LIMIT + 1))
spf[0] = 0
spf[1] = 1
for p in range(2, isqrt(LIMIT) + 1):
    if spf[p] == p:
        for m in range(p * p, LIMIT + 1, p):
            if spf[m] == m:
                spf[m] = p

def factor_stats(n):
    x = n
    omega = 0
    sigma = 1
    while x > 1:
        p = spf[x]
        e = 0
        pp = 1
        while x % p == 0:
            x //= p
            e += 1
            pp *= p
        omega += e
        sigma *= (pp * p - 1) // (p - 1)
    return omega, sigma

low_hits = []
all_hits = []
min_nonperfect_omega = None
first_min_nonperfect = None

for n in range(2, LIMIT + 1):
    omega, sigma = factor_stats(n)
    if (n * n) % sigma != 0:
        continue
    all_hits.append(n)
    if omega <= 3:
        low_hits.append(n)
    if sigma != 2 * n:
        if min_nonperfect_omega is None or omega < min_nonperfect_omega:
            min_nonperfect_omega = omega
            first_min_nonperfect = n

assert low_hits == [6, 28], low_hits
assert min_nonperfect_omega == 4, (min_nonperfect_omega, first_min_nonperfect)
assert first_min_nonperfect == 364, first_min_nonperfect

omega364, sigma364 = factor_stats(364)
assert omega364 == 4
assert sigma364 == 784
assert 364 * 364 == 169 * 784
assert sigma364 != 2 * 364

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"hits={len(all_hits)}",
    f"low_hits={low_hits}",
    f"min_nonperfect_omega={min_nonperfect_omega}",
    f"first_min_nonperfect={first_min_nonperfect}",
)
