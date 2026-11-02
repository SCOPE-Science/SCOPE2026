"""Depth-first path construction and exact backbite-distance census.

Run with Python 3: python verify_dfs.py. No external packages are required.
"""
from collections import Counter, deque
from itertools import combinations

N = 11
# Core vertices 0,1,2; poles 3,4; pair/pole vertices 5,...,10.
adj = [set() for _ in range(N)]
label = {}
for k, (a, b) in enumerate(combinations(range(3), 2)):
    for pole in range(2):
        v = 5 + 2*k + pole
        label[v] = ((a, b), pole)
        for u in (a, b, 3 + pole):
            adj[v].add(u)
            adj[u].add(v)
assert sum(map(len, adj)) == 36
assert sorted(map(len, adj)) == [3]*8+[4]*3

paths = set()
def walk(p, mask):
    if len(p) == N:
        t = tuple(p)
        paths.add(min(t, t[::-1]))
        return
    for v in sorted(adj[p[-1]]):
        if not (mask & (1 << v)):
            walk(p + [v], mask | (1 << v))
for s in range(N):
    walk([s], 1 << s)
paths = sorted(paths)
assert len(paths) == 222
ix = {p: i for i, p in enumerate(paths)}

neighbors = [set() for _ in paths]
for i, path in enumerate(paths):
    for p in (path, path[::-1]):
        for j in range(2, N):
            if p[j] not in adj[p[0]]:
                continue
            q = p[j-1::-1] + (p[j],) + p[j+1:]
            target = min(q, q[::-1])
            assert target in ix and target != path
            neighbors[i].add(ix[target])
assert all(len(ns) == 4 for ns in neighbors)
assert all(i in neighbors[j] for i, ns in enumerate(neighbors) for j in ns)
assert sum(map(len, neighbors)) // 2 == 444

pair_profile = Counter()
for p in paths:
    a, b = label[p[0]], label[p[-1]]
    cls = ('same_edge' if a[0] == b[0]
           else 'same_pole' if a[1] == b[1] else 'opposite_poles')
    pair_profile[cls] += 1
assert pair_profile == {'same_edge': 42, 'same_pole': 72, 'opposite_poles': 108}

hist = Counter()
ecc = Counter()
diametral_degree = [0] * len(paths)
for root in range(len(paths)):
    d = {root: 0}
    todo = deque([root])
    while todo:
        u = todo.popleft()
        for v in neighbors[u]:
            if v not in d:
                d[v] = d[u] + 1
                todo.append(v)
    assert len(d) == len(paths)
    ecc[max(d.values())] += 1
    for v, dist in d.items():
        if v > root:
            hist[dist] += 1
            if dist == 9:
                diametral_degree[root] += 1
                diametral_degree[v] += 1
assert dict(sorted(hist.items())) == {
    1: 444, 2: 1152, 3: 2436, 4: 4326, 5: 6348,
    6: 6189, 7: 3078, 8: 546, 9: 12,
}
assert ecc == {8: 198, 9: 24}
# An explicit diameter witness and its breadth-first distance spheres.
witness_a = (5,0,6,4,8,2,7,3,9,1,10)
witness_b = (6,1,5,3,7,0,8,4,10,2,9)
root = ix[witness_a]
seen = {root: 0}
q = deque([root])
while q:
    u = q.popleft()
    for v in neighbors[u]:
        if v not in seen:
            seen[v] = seen[u] + 1
            q.append(v)
assert seen[ix[witness_b]] == 9
assert [Counter(seen.values())[j] for j in range(10)] == [1,4,12,28,45,55,49,21,6,1]
assert Counter(diametral_degree) == {0: 198, 1: 24}
# A direct independent implication from the exhaustive distance histogram:
# exactly 24 distinct endpoints of the 12 diameter pairs, each in one pair.
exception_pairs = Counter(tuple(sorted((paths[i][0], paths[i][-1])))
                          for i, count in enumerate(diametral_degree) if count)
assert len(exception_pairs) == 6 and set(exception_pairs.values()) == {4}
assert all(label[a][0] != label[b][0] and label[a][1] != label[b][1]
           for a, b in exception_pairs)
print('DFS_222_UNDIRECTED_HAMILTONIAN_PATHS_PASS')
print('BACKBITE_444_EDGES_FOUR_REGULAR_CONNECTED_PASS')
print('ENDPOINT_COUNTS_SAME_EDGE42_SAME_POLE72_OPPOSITE108_PASS')
print('DISTANCES_1TO9_444_1152_2436_4326_6348_6189_3078_546_12_PASS')
print('ECC_198_AT_8_24_AT_9_12_DISJOINT_DIAMETER_PAIRS_PASS')
