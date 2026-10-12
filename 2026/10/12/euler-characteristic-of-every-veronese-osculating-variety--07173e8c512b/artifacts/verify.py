from itertools import product
from math import comb

def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail

def closed_formula(n, d, k):
    q = d - k
    upper = min(n + 1, d // q)
    return sum(
        (-1) ** (j + 1)
        * comb(n + 1, j)
        * comb(n + d - j * q, n)
        for j in range(1, upper + 1)
    )

triples = 0
monomials = 0
weight_checks = 0
stable_checks = 0

for n in range(1, 6):
    for d in range(1, 11):
        comps = list(compositions(d, n + 1))
        B = d + 1
        weights = []
        for a in comps:
            weights.append(sum(a[i] * (B ** i) for i in range(n + 1)))
        assert len(weights) == len(set(weights))
        weight_checks += len(weights)

        for k in range(d):
            triples += 1
            q = d - k
            direct = sum(1 for a in comps if max(a) >= q)
            monomials += len(comps)
            assert direct == closed_formula(n, d, k), (n, d, k, direct, closed_formula(n, d, k))
            if d > 2 * k:
                assert direct == (n + 1) * comb(n + k, n)
                stable_checks += 1

print("VERIFY_OK", triples, monomials, weight_checks, stable_checks)
