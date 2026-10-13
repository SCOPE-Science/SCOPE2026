#!/usr/bin/env python3
from math import isqrt

LIMIT = 500_000

def spf_table(n):
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for m in range(p*p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf

spf = spf_table(LIMIT)

def factor(n, table):
    out = []
    while n > 1:
        p = table[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out

def sigma_phi(fac):
    sigma = 1
    phi = 1
    for p, e in fac:
        sigma *= (p ** (e + 1) - 1) // (p - 1)
        phi *= p ** (e - 1) * (p - 1)
    return sigma, phi

records = []
max_s = 2
for n in range(1, LIMIT + 1):
    fac = factor(n, spf) if n > 1 else []
    if any(e != 1 for _, e in fac):
        continue
    if n == 1:
        sigma = phi = 1
    else:
        sigma, phi = sigma_phi(fac)
    s = sigma + phi
    max_s = max(max_s, s)
    records.append((n, fac, s))

spf_s = spf_table(max_s)

def tau_from_spf(n):
    if n == 1:
        return 1
    ans = 1
    while n > 1:
        p = spf_s[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        ans *= e + 1
    return ans

def is_prime(n):
    return n >= 2 and spf_s[n] == n

hits = []
composite_hits = []

for n, fac, s in records:
    direct = (tau_from_spf(s) == 4)
    if n == 1:
        predicted = False
    elif len(fac) == 1:
        predicted = (fac[0][0] % 2 == 1)
    else:
        predicted = (
            len(fac) == 2
            and fac[0][0] == 2
            and is_prime(2 * fac[1][0] + 1)
        )
    assert direct == predicted, (n, fac, s, direct, predicted)
    if direct:
        hits.append(n)
        if len(fac) >= 2:
            q = n // 2
            assert n == 2*q and is_prime(q) and is_prime(2*q + 1)
            composite_hits.append(n)

assert hits[:12] == [3,5,6,7,10,11,13,17,19,22,23,29], hits[:12]
assert composite_hits[:10] == [6,10,22,46,58,82,106,166,178,226], composite_hits[:10]

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"squarefree_checked={len(records)}",
    f"hits={len(hits)}",
    f"composite_hits={len(composite_hits)}",
    f"first_hits={hits[:16]}",
    f"first_composite_hits={composite_hits[:12]}",
)
