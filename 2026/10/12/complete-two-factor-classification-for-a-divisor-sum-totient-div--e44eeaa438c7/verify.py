#!/usr/bin/env python3
from math import isqrt

LIMIT = 5_000_000

def spf_table(n):
    spf = list(range(n + 1))
    spf[0] = 0
    spf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for m in range(p*p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf

def factor(n, spf):
    out = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out

def sigma_from_factor(fac):
    ans = 1
    for p, e in fac:
        ans *= (p ** (e + 1) - 1) // (p - 1)
    return ans

def phi_from_factor(fac):
    ans = 1
    for p, e in fac:
        ans *= p ** (e - 1) * (p - 1)
    return ans

spf = spf_table(LIMIT)
checked = 0
direct_hits = []
square_checks = 0
odd_branch_hits = 0

for n in range(2, LIMIT + 1):
    fac = factor(n, spf)
    if sum(e for _, e in fac) != 2:
        continue
    checked += 1
    sig = sigma_from_factor(fac)
    ph = phi_from_factor(fac)
    direct = ((n * ph) % sig == 0)

    if len(fac) == 1:
        p, e = fac[0]
        assert e == 2
        predicted = False
        square_checks += 1
    else:
        (p, ep), (q, eq) = fac
        assert ep == eq == 1 and p < q
        predicted = (p == 2 and q == 3) or (p >= 3 and q == p*p - p - 1)
        if predicted and p >= 3:
            assert (n * ph) // sig == q * (p - 2)
            odd_branch_hits += 1

    assert direct == predicted, (n, fac, sig, ph, direct, predicted)
    if direct:
        direct_hits.append(n)

assert direct_hits[:6] == [6, 15, 95, 287, 1199, 4607], direct_hits[:10]

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"omega2_checked={checked}",
    f"hits={len(direct_hits)}",
    f"square_checks={square_checks}",
    f"odd_branch_hits={odd_branch_hits}",
    f"first_hits={direct_hits[:12]}",
)
