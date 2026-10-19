"""Independent constraint-hitting-set census using the 18-vertex LCF Pappus graph.

Run: python3 verify_lcf.py (Python standard library only).
LCF chords [5,7,-7,7,-7,-5] repeated three times.
"""
from collections import Counter, deque
from itertools import combinations

SIZE = 18
SHIFT = (5, 7, -7, 7, -7, -5) * 3
adj = [set() for _ in range(SIZE)]
for v in range(SIZE):
    for w in ((v + 1) % SIZE, (v + SHIFT[v]) % SIZE):
        adj[v].add(w)
        adj[w].add(v)
assert all(len(a) == 3 for a in adj)
assert sum(map(len, adj)) // 2 == 27

# A direct isomorphism certificate to the affine 3-net incidence representation.
# LCF index i maps to the incidence-graph index isom[i].
isom = (0, 9, 6, 17, 4, 12, 8, 16, 3, 14, 2, 11, 5, 13, 1, 10, 7, 15)
assert set(isom) == set(range(SIZE))
for v in range(SIZE):
    t = isom[v]
    if t < 9:
        x, y = divmod(t, 3)
        target = {9 + 3 * m + ((y - m * x) % 3) for m in range(3)}
    else:
        m, b = divmod(t - 9, 3)
        target = {3 * x + (m * x + b) % 3 for x in range(3)}
    assert {isom[w] for w in adj[v]} == target

# A code must hit every closed neighborhood and every symmetric difference
# of two distinct closed neighborhoods. This is a finite hitting-set system.
closed = [sum(1 << w for w in ({v} | adj[v])) for v in range(SIZE)]
requirements = closed + [closed[u] ^ closed[v]
                         for u, v in combinations(range(SIZE), 2)]
assert len(requirements) == 171
assert 0 not in requirements

def covers_all(mask):
    return all((mask & required) != 0 for required in requirements)

classes = {k: [] for k in range(SIZE + 1)}
for mask in range(1 << SIZE):
    if covers_all(mask):
        classes[mask.bit_count()].append(mask)
assert not any(classes[k] for k in range(9))
assert len(classes[9]) == 1028
assert len(classes[10]) == 8640
assert sum(map(len, classes.values())) == 52638

# Enumerate edges from the Johnson graph J(18,k), retained only if both
# endpoints are hitting sets. This gives graph components exactly.
def exchange_graph(nodes):
    positions = {x: i for i, x in enumerate(nodes)}
    edges = [set() for _ in nodes]
    for i, code in enumerate(nodes):
        selected = [a for a in range(SIZE) if code & (1 << a)]
        absent = [b for b in range(SIZE) if not code & (1 << b)]
        for a in selected:
            for b in absent:
                other = code ^ (1 << a) ^ (1 << b)
                j = positions.get(other)
                if j is not None:
                    edges[i].add(j)
    assert all(i in edges[j] for i, neigh in enumerate(edges) for j in neigh)
    return edges

def components(edges):
    unseen = set(range(len(edges)))
    parts = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        q = [start]
        for i in q:
            for j in edges[i] & unseen:
                unseen.remove(j)
                q.append(j)
        parts.append(q)
    return parts

g9 = exchange_graph(classes[9])
g10 = exchange_graph(classes[10])
parts9 = components(g9)
parts10 = components(g10)
assert sorted(map(len, parts9)) == [514, 514]
assert list(map(len, parts10)) == [8640]
assert sum(map(len, g9)) // 2 == 3780
assert sum(map(len, g10)) // 2 == 128700
assert Counter(map(len, g9)) == {2: 108, 4: 216, 5: 216, 7: 108,
                                 11: 270, 15: 108, 27: 2}

def point_count(mask):
    # The points of the incidence model are known through the isomorphism.
    return sum(bool(mask & (1 << i)) for i, v in enumerate(isom) if v < 9)

point_histories = [Counter(point_count(classes[9][i]) for i in p) for p in parts9]
assert set(map(lambda c: tuple(sorted(c)), point_histories)) == {(0,1,2,3,4),(5,6,7,8,9)}
assert sorted(tuple(sorted(c.values())) for c in point_histories) == [
    (1, 27, 81, 162, 243), (1, 27, 81, 162, 243)]

# Complete BFS from every optimum; disconnected pairs are excluded
# from the definition of eccentricity.
ecc = Counter()
centers = []
for part in parts9:
    pset = set(part)
    for start in part:
        dist = {start: 0}
        queue = deque([start])
        while queue:
            x = queue.popleft()
            for y in g9[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1
                    queue.append(y)
        assert set(dist) == pset
        ecc[max(dist.values())] += 1
        if max(dist.values()) == 4:
            centers.append(classes[9][start])
assert ecc == {4: 2, 5: 54, 6: 162, 7: 486, 8: 324}
all_points = sum(1 << i for i, w in enumerate(isom) if w < 9)
all_lines = sum(1 << i for i, w in enumerate(isom) if w >= 9)
assert sorted(centers) == sorted([all_points, all_lines])

print("graph_vertices=18 graph_edges=27 isomorphism_certificate=verified")
print("requirements=171 tested_masks=262144 minimum=9 total_codes=52638")
print("k=9 states=1028 edges=3780 components=[514,514]")
print("k=10 states=8640 edges=128700 components=[8640]")
print("k=9 point_partition=0..4 versus 5..9")
print("k=9 degree_histogram=" + repr(sorted(Counter(map(len,g9)).items())))
print("k=9 component_eccentricity_histogram=" + repr(sorted(ecc.items())))
print("counts_k9_to_k18=" + repr([len(classes[k]) for k in range(9,19)]))
print("VERIFIED")
