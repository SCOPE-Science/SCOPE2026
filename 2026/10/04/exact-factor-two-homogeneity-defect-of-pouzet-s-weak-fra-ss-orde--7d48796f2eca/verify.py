from itertools import product
from collections import defaultdict, Counter
from math import factorial

def weak_orders(n):
    for k in range(1, n + 1):
        target = set(range(k))
        for ranks in product(range(k), repeat=n):
            if set(ranks) == target:
                yield ranks

def qf_signature(ranks):
    n = len(ranks)
    eq = tuple(ranks[i] == ranks[j] for i in range(n) for j in range(n))
    rel = tuple(
        ranks[i] < ranks[j] and ranks[i] < ranks[l] and ranks[j] != ranks[l]
        for i in range(n) for j in range(n) for l in range(n)
    )
    return eq + rel

expected_full = [1, 3, 13, 75, 541, 4683]
expected_qf = [1, 2, 7, 38, 271, 2342]

for n in range(1, 7):
    groups = defaultdict(list)
    full = list(weak_orders(n))
    for ranks in full:
        groups[qf_signature(ranks)].append(ranks)

    assert len(full) == expected_full[n - 1]
    assert len(groups) == expected_qf[n - 1]
    sizes = Counter(map(len, groups.values()))
    assert sizes[1] == 1
    assert sizes[2] == len(groups) - 1
    assert set(sizes) <= {1, 2}

    injective = [r for r in full if len(set(r)) == n]
    injective_groups = {qf_signature(r) for r in injective}
    assert len(injective) == factorial(n)
    if n == 1:
        assert len(injective_groups) == 1
    else:
        assert len(injective_groups) == factorial(n) // 2

print("VERIFY_OK")
