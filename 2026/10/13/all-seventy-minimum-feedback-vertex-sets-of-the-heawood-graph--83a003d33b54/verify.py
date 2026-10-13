"""Exact exhaustive census of maximum induced trees in the Heawood graph.

Python 3.9+, standard library only. Vertices 0..6 are Fano points 1..7;
vertices 7..13 are lines (sorted triples of xor-zero vectors).
"""
from collections import Counter, deque
from itertools import combinations

P = tuple(range(1, 8))
LINES = tuple(sorted({tuple(sorted((a, b, a ^ b)))
                      for a in P for b in P if a < b}))
assert len(LINES) == 7
assert all(len(L) == 3 for L in LINES)
LINE_ID = {L: 7 + j for j, L in enumerate(LINES)}
NEIGHBORS = [set() for _ in range(14)]
for j, line in enumerate(LINES):
    for point in line:
        NEIGHBORS[point - 1].add(7 + j)
        NEIGHBORS[7 + j].add(point - 1)
assert all(len(x) == 3 for x in NEIGHBORS)
assert sum(map(len, NEIGHBORS)) == 42


def components_and_forest(deleted):
    """Component count and acyclicity for the *entire* induced complement."""
    remaining = set(range(14)) - set(deleted)
    parts = []
    while remaining:
        v = min(remaining)
        visited = {v}
        frontier = deque([v])
        remaining.remove(v)
        while frontier:
            u = frontier.popleft()
            for w in NEIGHBORS[u]:
                if w in remaining:
                    remaining.remove(w)
                    visited.add(w)
                    frontier.append(w)
        parts.append(visited)
    count_edges = sum(len(NEIGHBORS[v] - set(deleted))
                      for v in set(range(14)) - set(deleted)) // 2
    forest = count_edges == 14 - len(deleted) - len(parts)
    # A finite undirected graph has cycle rank E-V+C >= 0,
    # with equality precisely when all components are trees.
    return len(parts), forest


def form_A_or_B(deleted):
    points = {i + 1 for i in deleted if i < 7}
    lines = {i - 7 for i in deleted if i >= 7}
    if len(points) == 4:
        complementary_three = set(P) - points
        return tuple(sorted(complementary_three)) in LINES, 'A'
    if len(lines) == 4:
        three_remaining_lines = [LINES[j] for j in range(7) if j not in lines]
        return len(set.intersection(*map(set, three_remaining_lines))) == 1, 'A'
    if len(points) == 3 and len(lines) == 1:
        j = next(iter(lines))
        return points.isdisjoint(LINES[j]), 'B'
    if len(lines) == 3 and len(points) == 1:
        p = next(iter(points))
        return all(p not in LINES[j] for j in lines), 'B'
    return False, 'other'

all_good = set()
classes = Counter()
tree_shapes = Counter()
for mask in range(1 << 14):
    deleted = frozenset(i for i in range(14) if mask >> i & 1)
    n_comp, is_forest = components_and_forest(deleted)
    if is_forest and len(deleted) <= 4:
        assert len(deleted) == 4, (deleted, n_comp)
        assert n_comp == 1
        independent = all(not (NEIGHBORS[v] & deleted) for v in deleted)
        assert independent
        predicted, kind = form_A_or_B(deleted)
        assert predicted, (deleted, kind)
        all_good.add(deleted)
        classes[kind] += 1
        deg = Counter(len(NEIGHBORS[v] - deleted)
                      for v in range(14) if v not in deleted)
        tree_shapes[(kind, tuple(sorted(deg.items())))] += 1

predicted_sets = set()
for t in combinations(range(14), 4):
    s = frozenset(t)
    predicted, _ = form_A_or_B(s)
    if predicted:
        predicted_sets.add(s)
assert predicted_sets == all_good
assert len(all_good) == 70
assert classes == {'A': 14, 'B': 56}
assert tree_shapes == {
    ('A', ((1, 6), (3, 4))): 14,
    ('B', ((1, 3), (2, 6), (3, 1))): 56,
}


def lin_map(image_basis):
    """Send the standard F_2 basis 1,2,4 to independent images."""
    def f(v):
        x = 0
        for j in range(3):
            if (v >> j) & 1:
                x ^= image_basis[j]
        return x
    return f


def independent3(a, b, c):
    return a != b and a != c and b != c and (a ^ b) != c

permutations = set()
for a in P:
    for b in P:
        for c in P:
            if not independent3(a, b, c):
                continue
            f = lin_map((a, b, c))
            perm = [f(p) - 1 for p in P]
            for line in LINES:
                target_line = tuple(sorted(f(x) for x in line))
                perm.append(LINE_ID[target_line])
            permutations.add(tuple(perm))
assert len(permutations) == 168

# Polarity/point-line duality on the Fano plane using the standard dot product.
def dot(a, b):
    return (a & b).bit_count() % 2

normal = {}
for j, line in enumerate(LINES):
    n = [v for v in P if all(dot(v, p) == 0 for p in line)]
    assert len(n) == 1
    normal[j] = n[0]
point_to_line = {n: j for j, n in normal.items()}
dual = tuple([7 + point_to_line[p] for p in P]
             + [normal[j] - 1 for j in range(7)])
assert tuple(dual[dual[i]] for i in range(14)) == tuple(range(14))
all_automorphisms = set(permutations)
all_automorphisms |= {tuple(dual[g[i]] for i in range(14)) for g in permutations}
assert len(all_automorphisms) == 336
for g in all_automorphisms:
    for u in range(14):
        assert {g[v] for v in NEIGHBORS[u]} == NEIGHBORS[g[u]]

remaining = set(all_good)
orbits = []
while remaining:
    seed = min(remaining, key=lambda x: tuple(sorted(x)))
    orbit = {frozenset(g[i] for i in seed) for g in all_automorphisms}
    assert orbit <= remaining
    types = {form_A_or_B(s)[1] for s in orbit}
    assert len(types) == 1
    orbits.append((next(iter(types)), len(orbit)))
    remaining -= orbit
assert sorted(orbits) == [('A', 14), ('B', 56)]
print('VERIFY_OK vertices=14 edges=21 masks=16384 optimum=4 minimum_sets=70')
print('VERIFY_OK orbit_types=A:14,B:56 group_order=336 tree_degrees=A:(1^6,3^4),B:(1^3,2^6,3^1)')
