"""Independent LCF-model verification of the Möbius-Kantor zero-forcing result.

Finite exhaustive enumeration; no extra packages required.
"""
import json
from collections import Counter, defaultdict, deque
from itertools import combinations

n = 16
# LCF [5,-5]^8: Hamilton cycle plus the eight alternating 5-chords.
G = [set() for _ in range(n)]
for i in range(n):
    j = (i + 1) % n
    G[i].add(j); G[j].add(i)
for i in range(n):
    j = (i + (5 if i % 2 == 0 else -5)) % n
    G[i].add(j); G[j].add(i)
assert len({tuple(sorted((i, j))) for i in range(n) for j in G[i]}) == 24
assert all(len(s) == 3 for s in G)

# Explicit graph isomorphism: GP vertex v maps to LCF vertex relabel[v].
relabel = [0, 5, 6, 7, 8, 13, 14, 15, 1, 4, 11, 2, 9, 12, 3, 10]
assert sorted(relabel) == list(range(n))
gp_edges = set()
for i in range(8):
    for x, y in ((i, (i+1) % 8), (i, i+8), (i+8, 8+(i+3) % 8)):
        gp_edges.add(tuple(sorted((relabel[x], relabel[y]))))
lcf_edges = {tuple(sorted((i, j))) for i in range(n) for j in G[i]}
assert gp_edges == lcf_edges

# Apply one permissible force at a time, unlike synchronous bit-mask closure.
def forces_all(seed):
    blue = set(seed)
    while True:
        if len(blue) == n:
            return True
        step = None
        for u in sorted(blue):
            choices = G[u] - blue
            if len(choices) == 1:
                step = next(iter(choices))
                break
        if step is None:
            return False
        blue.add(step)

counts = {}
minimum = set()
for k in range(7):
    F = set()
    for c in combinations(range(n), k):
        if forces_all(c):
            F.add(frozenset(c))
    counts[k] = len(F)
    if k == 6:
        minimum = F
assert [counts[k] for k in range(7)] == [0,0,0,0,0,0,1704]

# Edges by shared five-subset, not by iterating all ordered exchanges.
buckets = defaultdict(list)
for six in minimum:
    for x in six:
        buckets[six - {x}].append(six)
links = {s: set() for s in minimum}
for B in buckets.values():
    for a, b in combinations(B, 2):
        links[a].add(b)
        links[b].add(a)
assert len(links) == 1704
edge_count = sum(map(len, links.values())) // 2
assert edge_count == 16560
assert Counter(map(len, links.values())) == {16: 240, 17: 96, 18: 336, 19: 192,
                                            20: 288, 21: 192, 22: 240, 24: 120}
sliding = 0
for s, neighbors in links.items():
    for t in neighbors:
        if min(s ^ t) in G[max(s ^ t)]:
            sliding += 1
assert sliding == 0

# All ordered shortest-path searches, without symmetry reduction.
def shortest_lengths(start):
    d = {start: 0}
    todo = deque([start])
    while todo:
        s = todo.popleft()
        for t in links[s]:
            if t not in d:
                d[t] = d[s] + 1
                todo.append(t)
    return d

profile = Counter()
for s in minimum:
    distances = shortest_lengths(s)
    assert len(distances) == 1704
    profile[max(distances.values())] += 1
assert profile == {6: 1704}
summary = {
    'representation': 'LCF [5,-5]^8', 'graph_isomorphism_checked': True,
    'zero_forcing_counts_through_6': {str(k): counts[k] for k in range(7)},
    'minimum_sets': len(minimum), 'jump_edges': edge_count,
    'slide_edges': sliding // 2,
    'jump_degree_distribution': dict(sorted(Counter(map(len, links.values())).items())),
    'jump_connected': True, 'jump_eccentricities': dict(sorted(profile.items())),
    'jump_radius': min(profile), 'jump_diameter': max(profile),
    'slide_components': len(minimum), 'slide_isolated': len(minimum)
}
print(json.dumps(summary, sort_keys=True, indent=2))
