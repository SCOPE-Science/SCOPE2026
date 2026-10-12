#!/usr/bin/env python3
from math import gcd

LIMIT = 2_000_000

def spf_table(n):
    spf = list(range(n + 1))
    spf[0] = 0
    spf[1] = 1
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf

def factor(n, spf=None):
    out = []
    if spf is not None and n < len(spf):
        while n > 1:
            p = spf[n]
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        return out
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            out.append((d, e))
        d += 1 if d == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out

def pillai_from_factors(fac):
    ans = 1
    for p, a in fac:
        ans *= p ** (a - 1) * ((a + 1) * p - a)
    return ans

def pillai_direct(n):
    return sum(gcd(k, n) for k in range(1, n + 1))

spf = spf_table(LIMIT)

# Formula versus definition on a finite exact sample.
formula_checks = 0
for n in range(1, 5001):
    assert pillai_from_factors(factor(n, spf)) == pillai_direct(n)
    formula_checks += 1

# Exhaustive low-Omega check.
hits = []
composite_candidates = 0
for n in range(2, LIMIT + 1):
    fac = factor(n, spf)
    Omega = sum(e for _, e in fac)
    if Omega <= 3:
        Pn = pillai_from_factors(fac)
        if (Pn + 1) % n == 0:
            hits.append(n)
            assert len(fac) == 1 and fac[0][1] == 1
        elif not (len(fac) == 1 and fac[0][1] == 1):
            composite_candidates += 1

# Symbolic boundary identities, evaluated over representative prime triples.
primes = [p for p in range(2, 300) if spf[p] == p]
triple_checks = 0
for i, p in enumerate(primes):
    for j in range(i + 1, min(i + 12, len(primes))):
        q = primes[j]
        for k in range(j + 1, min(j + 8, len(primes))):
            r = primes[k]
            n = p * q * r
            Pn = (2 * p - 1) * (2 * q - 1) * (2 * r - 1)
            if n <= LIMIT:
                assert Pn == pillai_from_factors([(p, 1), (q, 1), (r, 1)])
            assert (Pn + 1) % n != 0
            triple_checks += 1

# Current known unrestricted counterexample from A018804.
counter = 3 * 37 * 43 * 42307 * 116341
fac_counter = [(3,1),(37,1),(43,1),(42307,1),(116341,1)]
Pc = pillai_from_factors(fac_counter)
assert Pc + 1 == 26 * counter

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"formula_checks={formula_checks}",
    f"low_omega_hits={len(hits)}",
    f"first_hits={hits[:10]}",
    f"composite_low_omega_rejections={composite_candidates}",
    f"triple_checks={triple_checks}",
    "known_counterexample_quotient=26",
)
