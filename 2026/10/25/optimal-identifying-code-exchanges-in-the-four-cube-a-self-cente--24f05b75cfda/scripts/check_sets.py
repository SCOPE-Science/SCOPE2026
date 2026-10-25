#!/usr/bin/env python3
"""Independent set-theoretic exhaustive certificate for Q4 code exchanges.

Run with Python 3.10 or later: python scripts/check_sets.py
Uses concrete 4-tuples, subsets and intersections, plus shared-six-element cores.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, product
import json

V = tuple(product((0, 1), repeat=4))
closed_neighborhood = {
    v: frozenset(w for w in V if sum(x != y for x, y in zip(v, w)) <= 1)
    for v in V
}


def is_identifying(code):
    signatures = [frozenset(code.intersection(closed_neighborhood[v])) for v in V]
    return all(signatures) and len(set(signatures)) == len(V)

# Upward closure: ruling out all 6-element codes rules out every smaller code.
assert not any(is_identifying(frozenset(t)) for t in combinations(V, 6))
weak_six = sum(1 for t in combinations(V, 6)
               if len({frozenset(set(t).intersection(closed_neighborhood[v]))
                       for v in V}) == len(V))
assert weak_six == 192
code_list = [frozenset(t) for t in combinations(V, 7)
             if is_identifying(frozenset(t))]
assert len(code_list) == 960

# Two different 7-subsets are adjacent iff they share a six-element core.
by_core = defaultdict(list)
for i, code in enumerate(code_list):
    for core in combinations(sorted(code), 6):
        by_core[frozenset(core)].append(i)
neighbor = [set() for _ in code_list]
for group in by_core.values():
    for i, j in combinations(group, 2):
        neighbor[i].add(j)
        neighbor[j].add(i)
assert all(len(x) == 9 for x in neighbor)
assert sum(len(x) for x in neighbor) // 2 == 4320

shells = Counter()
for root in range(len(code_list)):
    dist = [-1] * len(code_list)
    dist[root] = 0
    q = deque([root])
    while q:
        i = q.popleft()
        for j in neighbor[i]:
            if dist[j] == -1:
                dist[j] = dist[i] + 1
                q.append(j)
    assert -1 not in dist
    profile = tuple(Counter(dist).get(d, 0) for d in range(8))
    shells[profile] += 1
assert shells == Counter({(1, 9, 35, 132, 300, 338, 130, 15): 960})

# Every vertex lies in twelve triangles, independently computed from edge sets.
triangle_profiles = Counter(
    sum(len(neighbor[i].intersection(neighbor[j])) for j in neighbor[i]) // 2
    for i in range(len(code_list))
)
assert triangle_profiles == Counter({12: 960})
print(json.dumps(dict(minimum_size=7, optimal_codes=len(code_list),
                      weak_separating_six_sets=weak_six,
                      exchange_edges=sum(map(len, neighbor)) // 2,
                      degree_counts=dict(Counter(map(len, neighbor))),
                      distance_profiles=[dict(shells=list(profile), multiplicity=n)
                                         for profile, n in sorted(shells.items())],
                      local_triangle_counts=dict(triangle_profiles),
                      radius=7, diameter=7), sort_keys=True, indent=2))
