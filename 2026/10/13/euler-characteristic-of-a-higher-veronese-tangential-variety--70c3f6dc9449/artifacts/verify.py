from itertools import product
from math import comb

def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest

pairs = 0
monomials_checked = 0
weight_checks = 0

for n in range(2, 9):
    for d in range(3, 11):
        B = d + 1
        exps = list(compositions(d, n))
        weights = []
        fixed = 0
        for alpha in exps:
            w = sum(alpha[i] * (B ** i) for i in range(n))
            weights.append(w)
            monomials_checked += 1
            if max(alpha) >= d - 1:
                fixed += 1
        assert len(weights) == len(set(weights))
        weight_checks += len(weights)
        assert fixed == n * n, (n, d, fixed)
        pairs += 1

quadratic_checks = 0
for n in range(2, 15):
    d = 2
    exps = list(compositions(d, n))
    fixed = sum(1 for alpha in exps if max(alpha) >= 1)
    assert fixed == comb(n + 1, 2)
    quadratic_checks += 1

print("VERIFY_OK", pairs, monomials_checked, weight_checks, quadratic_checks)
