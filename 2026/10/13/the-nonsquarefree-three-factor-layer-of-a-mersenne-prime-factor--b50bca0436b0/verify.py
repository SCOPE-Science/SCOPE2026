#!/usr/bin/env python3
from math import isqrt

LIMIT = 2_000_000
Q_LIMIT = 100_000

def spf_table(n):
    spf = list(range(n + 1))
    spf[0] = 0
    spf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf

def factor(n, spf):
    f = {}
    while n > 1:
        p = spf[n]
        f[p] = f.get(p, 0) + 1
        n //= p
    return f

spf = spf_table(LIMIT)

omega3_checked = 0
hits = []
nonsquarefree_hits = []
even_hits = []

for n in range(2, LIMIT + 1):
    f = factor(n, spf)
    if sum(f.values()) != 3:
        continue
    omega3_checked += 1
    beta = sum(f)
    if pow(2, n, beta) == 1 % beta:
        hits.append(n)
        if any(e > 1 for e in f.values()):
            nonsquarefree_hits.append(n)
        if n % 2 == 0:
            even_hits.append(n)

assert nonsquarefree_hits == [12, 52], nonsquarefree_hits
assert even_hits == [12, 52], even_hits

# Direct witness checks.
assert (pow(2, 12, 5) - 1) % 5 == 0
assert (pow(2, 52, 15) - 1) % 15 == 0

# Branch checks for q < Q_LIMIT.
primes = [q for q in range(3, Q_LIMIT) if q < len(spf) and spf[q] == q]
branch_4q = []
branch_2q2 = []
for q in primes:
    m = q + 2
    if pow(2, 4 * q, m) == 1 % m:
        branch_4q.append(q)
    if pow(2, 2 * q * q, m) == 1 % m:
        branch_2q2.append(q)

assert branch_4q == [3, 13], branch_4q
assert branch_2q2 == [], branch_2q2

# Every other finite hit is odd and squarefree.
for n in hits:
    if n in (12, 52):
        continue
    f = factor(n, spf)
    assert n % 2 == 1
    assert len(f) == 3 and all(e == 1 for e in f.values())

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"omega3_checked={omega3_checked}",
    f"omega3_hits={len(hits)}",
    f"nonsquarefree_hits={nonsquarefree_hits}",
    f"even_hits={even_hits}",
    f"branch_4q={branch_4q}",
    f"branch_2q2={branch_2q2}",
    f"first_hits={hits[:12]}",
)
