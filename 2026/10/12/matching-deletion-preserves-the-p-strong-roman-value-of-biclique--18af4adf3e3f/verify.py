from itertools import product
from math import ceil


def graph(r, s, t):
    adj = [set() for _ in range(r + s)]
    for i in range(r):
        for j in range(s):
            if i < t and j == i:
                continue
            u, v = i, r + j
            adj[u].add(v)
            adj[v].add(u)
    return adj


def feasible(labels, adj, p):
    zeros = {i for i, x in enumerate(labels) if x == 0}
    Delta = max(map(len, adj))
    cap = ceil((Delta + p) / p)
    if any(x < 0 or x > cap for x in labels):
        return False
    for v, x in enumerate(labels):
        if x != 0:
            continue
        if not any(labels[u] >= 1 + ceil(len(adj[u] & zeros) / p) for u in adj[v]):
            return False
    return True


def brute_gamma(r, s, t, p):
    adj = graph(r, s, t)
    Delta = max(map(len, adj))
    cap = ceil((Delta + p) / p)
    target = 2 + ceil((r - 1) / p) + ceil((s - 1) / p)
    tested = 0
    # It is enough to seek a counterexample below target and verify the witness at target.
    for labels in product(range(cap + 1), repeat=r + s):
        w = sum(labels)
        if w >= target:
            continue
        tested += 1
        if feasible(labels, adj, p):
            raise AssertionError((r, s, t, p, w, labels))
    # theorem's explicit construction
    labels = [0] * (r + s)
    if t == 0:
        a, b = 0, r
    else:
        a, b = 0, r  # endpoints of the first deleted edge
    labels[a] = 1 + ceil((s - 1) / p)
    labels[b] = 1 + ceil((r - 1) / p)
    assert sum(labels) == target
    assert feasible(labels, adj, p), (r, s, t, p, labels)
    return tested


def phi(z, p):
    if z == 0:
        return 0
    return min(ceil(z / p), 2 * ceil((z - 1) / p))


exhaustive_cases = 0
assignments_below_target = 0
for r, s in [(3, 3), (3, 4)]:
    for t in range(r + 1):
        for p in (3, 4, 5):
            assignments_below_target += brute_gamma(r, s, t, p)
            exhaustive_cases += 1

lemma_checks = 0
construction_checks = 0
for r in range(3, 21):
    for s in range(r, 31):
        for p in range(3, 21):
            for m in (r, s):
                for z in range(m):
                    H = m - z + phi(z, p)
                    assert H >= 1 + ceil((m - 1) / p)
                    lemma_checks += 1
            for t in range(r + 1):
                adj = graph(r, s, t)
                labels = [0] * (r + s)
                labels[0] = 1 + ceil((s - 1) / p)
                labels[r] = 1 + ceil((r - 1) / p)
                assert feasible(labels, adj, p)
                assert sum(labels) == 2 + ceil((r - 1) / p) + ceil((s - 1) / p)
                construction_checks += 1

print(
    'ALL CHECKS PASSED; '
    f'exhaustive_cases={exhaustive_cases}; '
    f'assignments_below_target={assignments_below_target}; '
    f'lemma_checks={lemma_checks}; '
    f'construction_checks={construction_checks}; '
    'exhaustive_families=(3,3),(3,4); p=3,4,5'
)
