#!/usr/bin/env python3
LIMIT = 2_000_000

def spf_table(n):
    spf = list(range(n + 1))
    spf[0] = 0
    spf[1] = 1
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == p:
            start = p * p
            for m in range(start, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf

def factor_squarefree_three(n, spf):
    ps = []
    x = n
    while x > 1:
        p = spf[x]
        e = 0
        while x % p == 0:
            x //= p
            e += 1
            if e > 1:
                return None
        ps.append(p)
        if len(ps) > 3:
            return None
    return ps if len(ps) == 3 else None

spf = spf_table(LIMIT)

triples_checked = 0
hits = []
branch_a = 0
branch_b = 0

for n in range(2, LIMIT + 1):
    ps = factor_squarefree_three(n, spf)
    if ps is None:
        continue
    p, q, r = ps
    triples_checked += 1

    s = p + q + r
    direct = (n % s == 0)
    criterion_a = (p == 2 and r == q + 2)
    criterion_b = (p >= 3 and r == p * q - p - q and r > q)
    criterion = criterion_a or criterion_b

    assert direct == criterion, (n, ps, s, direct, criterion)

    if criterion_a:
        assert s == 2 * r
        assert n % (2 * r) == 0
        branch_a += 1
    if criterion_b:
        assert s == p * q
        assert n % (p * q) == 0
        branch_b += 1

    if direct:
        hits.append(n)

assert hits[:6] == [30, 70, 105, 231, 286, 627], hits[:10]

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"triples_checked={triples_checked}",
    f"hits={len(hits)}",
    f"branch_a={branch_a}",
    f"branch_b={branch_b}",
    f"first_hits={hits[:12]}",
)
