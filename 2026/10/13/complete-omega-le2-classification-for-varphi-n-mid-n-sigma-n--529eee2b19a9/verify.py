#!/usr/bin/env python3
from math import isqrt

LIMIT = 2_000_000
EXPECTED = [2,3,4,6,10,14,15,21,26,35,39,55,155,203]

spf = list(range(LIMIT + 1))
spf[0] = 0
spf[1] = 1
for p in range(2, isqrt(LIMIT) + 1):
    if spf[p] == p:
        for m in range(p*p, LIMIT + 1, p):
            if spf[m] == m:
                spf[m] = p

def factor_stats(n):
    x = n
    omega = 0
    sigma = 1
    phi = 1
    fac = []
    while x > 1:
        p = spf[x]
        e = 0
        pp = 1
        while x % p == 0:
            x //= p
            e += 1
            pp *= p
        fac.append((p,e))
        omega += e
        sigma *= (pp*p - 1) // (p - 1)
        phi *= p**(e-1) * (p-1)
    return fac, omega, sigma, phi

hits = []
checked = 0
semiprime_pairs = []

for n in range(2, LIMIT + 1):
    fac, omega, sigma, phi = factor_stats(n)
    if omega > 2:
        continue
    checked += 1
    direct = ((n * sigma) % phi == 0)
    if direct:
        hits.append(n)
        if len(fac) == 2:
            semiprime_pairs.append((fac[0][0], fac[1][0]))

assert hits == EXPECTED, hits
assert semiprime_pairs == [
    (2,3),(2,5),(2,7),(3,5),(3,7),(2,13),
    (5,7),(3,13),(5,11),(5,31),(7,29)
], semiprime_pairs

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"low_omega_checked={checked}",
    f"hits={hits}",
    f"semiprime_pairs={semiprime_pairs}",
)
