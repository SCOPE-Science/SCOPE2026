"""Exhaustive cycle-hypergraph certificate for a McGee-graph girth transversal.
Standard library only.  The 24-vertex LCF graph is reconstructed in this file.
"""
from itertools import combinations, product
from collections import Counter

N = 24
steps = (12, 7, -7) * 8
edges = {tuple(sorted((i, (i+1) % N))) for i in range(N)}
for i, s in enumerate(steps):
    edges.add(tuple(sorted((i, (i+s) % N))))
assert len(edges) == 36
neighbors = [set() for _ in range(N)]
for u, v in edges:
    neighbors[u].add(v)
    neighbors[v].add(u)
assert all(len(a) == 3 for a in neighbors)

# Every cycle is visited with its least vertex first and its smaller
# endpoint-neighbor second; this removes all rotations and reversals.
cycles = {k: set() for k in range(3, 8)}
def extend(path):
    first, u = path[0], path[-1]
    for v in neighbors[u]:
        if v == first and len(path) >= 3:
            if path[1] < path[-1] and len(path) <= 7:
                cycles[len(path)].add(tuple(path))
        elif len(path) < 7 and v > first and v not in path:
            extend(path + [v])
for first in range(N):
    extend([first])
assert all(not cycles[k] for k in range(3, 7))
assert len(cycles[7]) == 32
assert len({frozenset(c) for c in cycles[7]}) == 32
counts = Counter(v for c in cycles[7] for v in c)
assert {v: counts[v] for v in range(0, N, 3)} == {v: 10 for v in range(0, N, 3)}
assert all(counts[v] == 9 for v in range(N) if v % 3)
# At most 10 of 32 cycles can meet a fixed vertex, hence 3 are insufficient.
assert 3 * max(counts.values()) < len(cycles[7])

masks = [sum(1 << v for v in cycle) for cycle in cycles[7]]
sol = {s for s in combinations(range(N), 4)
       if all(sum(1 << v for v in s) & cycle for cycle in masks)}
pairs = ((0, 12), (3, 15), (6, 18), (9, 21))
mobile = {tuple(sorted(choice)) for choice in product(*pairs)}
exceptional = {(1, 5, 13, 17), (2, 10, 14, 22),
               (4, 8, 16, 20), (7, 11, 19, 23)}
assert sol == mobile | exceptional
assert len(sol) == 20 and len(mobile) == 16 and len(exceptional) == 4

def adjacent(x, y):
    return len(set(x) & set(y)) == 3
links = {frozenset((x,y)) for x,y in combinations(sorted(sol), 2) if adjacent(x,y)}
assert len(links) == 32
for x in mobile:
    assert sum(adjacent(x,y) for y in sol) == 4
for x in exceptional:
    assert not any(adjacent(x,y) for y in sol if x != y)
# The 16 mobile solutions are the independent binary choices in four disjoint
# pairs; a one-vertex exchange changes one coordinate, giving the 4-cube.
for x,y in combinations(mobile,2):
    bitdiff = sum((p[0] in x) != (p[0] in y) for p in pairs)
    assert adjacent(x,y) == (bitdiff == 1)

print('vertices=24 edges=36 girth=7 seven_cycles=32')
print('vertex_cycle_incidence=8x10+16x9 maximum=10 lower_bound=4')
print('checked_four_subsets=10626 optimal_four_subsets=20')
print('family=16 pair-choice + 4 isolated; exchange=Q4 disjoint_union 4K1; exchange_edges=32')
print('VERIFY_OK')
