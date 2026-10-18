"""Exact enumeration certificate for the Petersen graphical-zonotope local-degree spectrum.

Uses only the Python standard library.  All searches are exhaustive over finite,
explicitly bounded sets.  Run: python3 CHECK.py
"""
from collections import Counter
from itertools import combinations, permutations

LABELS = list(combinations(range(5), 2))
INDEX = {v: i for i, v in enumerate(LABELS)}
EDGES = [(i, j) for i in range(10) for j in range(i + 1, 10)
         if set(LABELS[i]).isdisjoint(LABELS[j])]
assert len(EDGES) == 15
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}

# The full S_5 action in the natural Kneser labeling of the Petersen graph.
TRANSFORMS = []
for permutation in permutations(range(5)):
    vertex_map = [INDEX[tuple(sorted(permutation[x] for x in label))]
                  for label in LABELS]
    transform = []
    for a, b in EDGES:
        aa, bb = vertex_map[a], vertex_map[b]
        transform.append((EDGE_INDEX[tuple(sorted((aa, bb)))], aa > bb))
    TRANSFORMS.append(transform)
assert len(TRANSFORMS) == 120


def digraph(mask):
    adj = [[] for _ in range(10)]
    indegrees = [0] * 10
    for i, (a, b) in enumerate(EDGES):
        if mask & (1 << i):
            a, b = b, a
        adj[a].append(b)
        indegrees[b] += 1
    return adj, indegrees


def topo(adj, indegrees):
    zeros = [v for v in range(10) if indegrees[v] == 0]
    for u in zeros:
        for v in adj[u]:
            indegrees[v] -= 1
            if indegrees[v] == 0:
                zeros.append(v)
    return zeros if len(zeros) == 10 else None


def has_cycle_without_toposort(mask):
    # A different algorithm, DFS with a three-color marking, for cross-checking.
    adj, _ = digraph(mask)
    color = [0] * 10
    def visit(u):
        color[u] = 1
        for v in adj[u]:
            if color[v] == 1 or (color[v] == 0 and visit(v)):
                return True
        color[u] = 2
        return False
    return any(color[v] == 0 and visit(v) for v in range(10))


ORIENTATIONS = {}
for mask in range(1 << 15):
    adj, indegrees = digraph(mask)
    order = topo(adj, indegrees)
    if order is None:
        continue
    reach = [0] * 10
    for u in reversed(order):
        for v in adj[u]:
            reach[u] |= (1 << v) | reach[v]
    degree = 0
    for u in range(10):
        for v in adj[u]:
            if not any(w != v and (reach[w] & (1 << v)) for w in adj[u]):
                degree += 1
    # Independent edge-flip definition: a cover is exactly a reversible arc.
    flip_degree = sum(not has_cycle_without_toposort(mask ^ (1 << i))
                      for i in range(15))
    assert degree == flip_degree, (mask, degree, flip_degree)
    ORIENTATIONS[mask] = degree

DEGREES = Counter(ORIENTATIONS.values())
EXPECTED = {9: 1080, 10: 2280, 11: 3600, 12: 3120,
            13: 3120, 14: 2160, 15: 1320}
assert dict(DEGREES) == EXPECTED, (DEGREES, EXPECTED)
assert len(ORIENTATIONS) == 16680
assert sum(d * n for d, n in DEGREES.items()) // 2 == 100080
assert sum(d * n for d, n in DEGREES.items()) % 2 == 0


def transformed_orientation(mask, transform):
    result = 0
    for i, (j, reverse) in enumerate(transform):
        if bool(mask & (1 << i)) ^ reverse:
            result |= 1 << j
    return result


ORBIT_COUNTS = Counter()
seen = set()
for mask, degree in ORIENTATIONS.items():
    if mask in seen:
        continue
    orbit = {transformed_orientation(mask, transform)
             for transform in TRANSFORMS}
    assert all(ORIENTATIONS[m] == degree for m in orbit)
    ORBIT_COUNTS[(degree, len(orbit))] += 1
    seen.update(orbit)
assert len(seen) == 16680
assert sum(ORBIT_COUNTS.values()) == 168
EXPECTED_ORBITS = {
    (9, 60): 2, (9, 120): 8,
    (10, 60): 2, (10, 120): 18,
    (11, 60): 4, (11, 120): 28,
    (12, 60): 4, (12, 120): 24,
    (13, 60): 12, (13, 120): 20,
    (14, 60): 8, (14, 120): 14,
    (15, 20): 6, (15, 60): 16, (15, 120): 2,
}
assert dict(ORBIT_COUNTS) == EXPECTED_ORBITS, ORBIT_COUNTS


def tree_paths(edge_subset):
    tree_adj = [[] for _ in range(10)]
    for i in edge_subset:
        u, v = EDGES[i]
        tree_adj[u].append((v, i))
        tree_adj[v].append((u, i))
    visited = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v, _ in tree_adj[u]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    if len(visited) != 10:
        return None
    constraints = []
    edge_set = set(edge_subset)
    for i, (u, v) in enumerate(EDGES):
        if i in edge_set:
            continue
        stack = [(u, ())]
        visited = {u}
        while stack:
            w, path = stack.pop()
            if w == v:
                constraints.append(path)
                break
            for z, edge_num in tree_adj[w]:
                if z not in visited:
                    visited.add(z)
                    # Boolean: traversing this edge in increasing endpoint order.
                    stack.append((z, path + ((edge_num, w < z),)))
        else:
            raise AssertionError('Disconnected tree path')
    return constraints


def is_coherent_tree(edge_subset, paths):
    locations = {i: j for j, i in enumerate(edge_subset)}
    for bits in range(1 << 9):
        good = True
        for path in paths:
            first = ((bits >> locations[path[0][0]]) & 1) ^ (not path[0][1])
            if any((((bits >> locations[i]) & 1) ^ (not forward)) != first
                   for i, forward in path[1:]):
                good = False
                break
        if good:
            return True
    return False


TREES = 0
GOOD_TREES = set()
for edge_subset in combinations(range(15), 9):
    paths = tree_paths(edge_subset)
    if paths is None:
        continue
    TREES += 1
    if is_coherent_tree(edge_subset, paths):
        GOOD_TREES.add(sum(1 << i for i in edge_subset))
assert TREES == 2000, TREES
assert len(GOOD_TREES) == 540, len(GOOD_TREES)

TREE_ORBITS = Counter()
seen_trees = set()
for tree in GOOD_TREES:
    if tree in seen_trees:
        continue
    orbit = set()
    for transform in TRANSFORMS:
        result = 0
        for i, (j, _) in enumerate(transform):
            if tree & (1 << i):
                result |= 1 << j
        orbit.add(result)
    assert orbit <= GOOD_TREES
    TREE_ORBITS[len(orbit)] += 1
    seen_trees.update(orbit)
assert len(seen_trees) == 540
assert dict(TREE_ORBITS) == {60: 1, 120: 4}, TREE_ORBITS
assert len(GOOD_TREES) * 2 == DEGREES[9]

print('orientation_degree_counts:', sorted(DEGREES.items()))
print('orientation_orbits_by_degree_and_size:', sorted(ORBIT_COUNTS.items()))
print('smooth_spanning_trees:', TREES, len(GOOD_TREES), sorted(TREE_ORBITS.items()))
print('vertices_edges_smooth:', len(ORIENTATIONS), 100080, DEGREES[9])
print('VERIFY_OK')
