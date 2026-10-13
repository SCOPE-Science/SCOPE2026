#!/usr/bin/env python3
"""Finite regression checks for the low-Omega collision theorem for D(n)=n*tau(n)."""
from collections import defaultdict

LIMIT = 1_000_000

spf = list(range(LIMIT + 1))
if LIMIT >= 1:
    spf[1] = 1
for i in range(2, int(LIMIT ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i*i, LIMIT + 1, i):
            if spf[j] == j:
                spf[j] = i

def omega_tau(n):
    if n == 1:
        return 0, 1
    om = 0
    tau = 1
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
            om += 1
        tau *= e + 1
    return om, tau

fibers = defaultdict(list)
count = 0
for n in range(1, LIMIT + 1):
    om, tau = omega_tau(n)
    if om <= 3:
        count += 1
        fibers[n * tau].append(n)

nontrivial = {v: xs for v, xs in fibers.items() if len(xs) > 1}
assert nontrivial == {108: [18, 27]}, nontrivial
assert omega_tau(18) == (3, 6)
assert omega_tau(27) == (3, 4)
assert 18 * 6 == 27 * 4 == 108
print(f"VERIFY_OK limit={LIMIT} low_omega_inputs={count} nontrivial_fibers={nontrivial}")
