#!/usr/bin/env python3
LIMIT = 2_000_000

def spf_table(limit):
    spf = list(range(limit + 1))
    spf[0] = 0
    spf[1] = 1
    for p in range(2, int(limit ** 0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, limit + 1, p):
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

def omega_big(n, spf):
    return sum(e for _, e in factor(n, spf))

def beta_pp(p, e):
    return (p ** (e + 1) + (-1) ** e) // (p + 1)

def beta(n, spf):
    ans = 1
    for p, e in factor(n, spf):
        ans *= beta_pp(p, e)
    return ans

spf = spf_table(LIMIT)

hits = []
tested = 0
for n in range(1, LIMIT):
    if omega_big(n, spf) <= 2 and omega_big(n + 1, spf) <= 2:
        tested += 1
        if beta(n, spf) == beta(n + 1, spf):
            hits.append(n)

assert hits == [1], hits
assert beta(20, spf) == 12
assert beta(21, spf) == 12
assert omega_big(20, spf) == 3
assert omega_big(21, spf) == 2

formula_checks = 0
primes = [p for p in range(2, int(LIMIT ** 0.5) + 1) if spf[p] == p]
for r in primes:
    assert beta(r * r, spf) == r * r - r + 1
    formula_checks += 1
for i, r in enumerate(primes[:120]):
    for s in primes[i + 1:i + 8]:
        if r * s <= LIMIT:
            assert beta(r * s, spf) == (r - 1) * (s - 1)
            formula_checks += 1

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"tested_low_multiplicity_pairs={tested}",
    f"hits={hits}",
    "sharpness=20",
    f"formula_checks={formula_checks}",
)
