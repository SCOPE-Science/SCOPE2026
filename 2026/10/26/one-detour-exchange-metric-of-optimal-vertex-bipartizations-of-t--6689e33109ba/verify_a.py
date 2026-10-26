"""Exact vertex-bipartization and optimum-exchange metric, GP(10,2).

Usage: python verify_a.py > verify_a.json
Python standard library only. Exhaustive finite verification.
"""
import itertools
import json
from collections import Counter, deque

N = 20
pairs = set()
for j in range(10):
    pairs.add(tuple(sorted((j, (j + 1) % 10))))
    pairs.add((j, j + 10))
    pairs.add(tuple(sorted((j + 10, 10 + (j + 2) % 10))))
adj = [[] for _ in range(N)]
for x, y in pairs:
    adj[x].append(y)
    adj[y].append(x)
assert len(pairs) == 30 and all(len(a) == 3 for a in adj)


def is_bipartite_after_deletion(removed):
    colour = [-1] * N
    for start in range(N):
        if (removed >> start) & 1 or colour[start] != -1:
            continue
        colour[start] = 0
        q = deque([start])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if (removed >> y) & 1:
                    continue
                if colour[y] == colour[x]:
                    return False
                if colour[y] == -1:
                    colour[y] = 1 - colour[x]
                    q.append(y)
    return True

zero_counts = []
for k in range(6):
    feasible = 0
    for chosen in itertools.combinations(range(N), k):
        mask = sum(1 << i for i in chosen)
        feasible += is_bipartite_after_deletion(mask)
    zero_counts.append(feasible)
assert zero_counts == [0] * 6
states = []
for chosen in itertools.combinations(range(N), 6):
    mask = sum(1 << i for i in chosen)
    if is_bipartite_after_deletion(mask):
        states.append(mask)
index = {x: i for i, x in enumerate(states)}
assert len(states) == 3240
adj_r = [[] for _ in states]
for i, x in enumerate(states):
    for rem in range(N):
        if not ((x >> rem) & 1):
            continue
        for add in range(N):
            if (x >> add) & 1:
                continue
            y = x ^ (1 << rem) ^ (1 << add)
            if y in index:
                adj_r[i].append(index[y])
for i, neighborhood in enumerate(adj_r):
    assert len(neighborhood) == len(set(neighborhood))
    for j in neighborhood:
        assert i in adj_r[j]

metric = Counter()
ecc = Counter()
example = None
for i, mask in enumerate(states):
    d = [-1] * len(states)
    d[i] = 0
    q = deque([i])
    while q:
        u = q.popleft()
        for v in adj_r[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                q.append(v)
    assert -1 not in d
    ecc[max(d)] += 1
    for j, other in enumerate(states):
        h = 6 - (mask & other).bit_count()
        metric[(h, d[j])] += 1
        if d[j] == h + 1 and example is None:
            example = [list(i for i in range(N) if (mask >> i) & 1),
                       list(i for i in range(N) if (other >> i) & 1), h, d[j]]
assert all(d in (h, h + 1) for h, d in metric)
assert sum(metric.values()) == len(states)**2
result = {
    'representation': 'GP(10,2)',
    'order': 20, 'size': len(pairs),
    'excluded_sizes_0_through_5': zero_counts,
    'minimum_deletion_size': 6,
    'number_of_minimum_deletion_sets': len(states),
    'exchange_edges': sum(map(len, adj_r)) // 2,
    'exchange_degree_histogram': {str(d): n for d, n in sorted(Counter(map(len, adj_r)).items())},
    'exchange_eccentricities': {str(d): n for d, n in sorted(ecc.items())},
    'ordered_distance_by_johnson_histogram': {f'{h},{d}': n for (h, d), n in sorted(metric.items())},
    'excess_distance_ordered_pairs': sum(n for (h, d), n in metric.items() if d > h),
    'first_excess_witness': example
}
print(json.dumps(result, sort_keys=True, separators=(',', ':')))
