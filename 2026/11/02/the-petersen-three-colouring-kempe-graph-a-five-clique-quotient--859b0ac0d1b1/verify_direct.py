"""Exhaustive direct check of Petersen vertex-3-colouring Kempe dynamics.

Requires only Python 3 standard library.  Vertices are unordered pairs of {0,...,4},
adjacent iff disjoint.  Every proper named 3-colouring is enumerated from 3^10.
"""
from collections import Counter, deque
from itertools import combinations, permutations, product

V = list(combinations(range(5), 2))
E = [(i, j) for i in range(10) for j in range(i + 1, 10)
     if not set(V[i]).intersection(V[j])]
N = [set() for _ in V]
for i, j in E:
    N[i].add(j)
    N[j].add(i)
assert len(V) == 10 and len(E) == 15 and all(len(x) == 3 for x in N)

C = [tuple(x) for x in product(range(3), repeat=10)
     if all(x[i] != x[j] for i, j in E)]
assert len(C) == 120
index = {c: i for i, c in enumerate(C)}
G = [set() for _ in C]
for i, c in enumerate(C):
    for a, b in combinations(range(3), 2):
        unseen = {v for v in range(10) if c[v] in (a, b)}
        while unseen:
            first = unseen.pop()
            component = {first}
            queue = [first]
            for u in queue:
                for v in N[u]:
                    if v in unseen:
                        unseen.remove(v)
                        component.add(v)
                        queue.append(v)
            updated = list(c)
            for v in component:
                updated[v] = b if c[v] == a else a
            j = index[tuple(updated)]
            assert j != i
            G[i].add(j)

assert all(len(G[i]) == 6 for i in range(120))
assert all(i in G[j] for i in range(120) for j in G[i])
assert sum(len(x) for x in G) // 2 == 360
# The only one-vertex Kempe component is the two-subset {c,t};
# hence elementary recolouring alone has 60 disjoint two-state components.
single_edges = set()
for i, c in enumerate(C):
    nearby = [j for j in G[i] if sum(c[k] != C[j][k] for k in range(10)) == 1]
    assert len(nearby) == 1
    single_edges.add(tuple(sorted((i, nearby[0]))))
assert len(single_edges) == 60
assert len({v for e in single_edges for v in e}) == 120

shells = []
for i in range(120):
    d = {i: 0}
    queue = deque([i])
    while queue:
        u = queue.popleft()
        for v in G[u]:
            if v not in d:
                d[v] = d[u] + 1
                queue.append(v)
    assert len(d) == 120
    hist = Counter(d.values())
    shells.append(hist)
    assert tuple(hist[k] for k in range(5)) == (1, 6, 25, 61, 27)
assert sum(sum(len(G[i] & G[j]) for j in G[i]) for i in range(120)) == 0

# Canonicalize the three named colours; the six relabellings are distinct.
canon = [min(tuple(p[t] for t in c) for p in permutations(range(3))) for c in C]
partitions = sorted(set(canon))
assert len(partitions) == 20
pos = {p: i for i, p in enumerate(partitions)}
Q = [set() for _ in partitions]
for i in range(120):
    for j in G[i]:
        a, b = pos[canon[i]], pos[canon[j]]
        if a != b:
            Q[a].add(b)
assert sum(map(len, Q)) // 2 == 40
assert all(len(x) == 4 for x in Q)
# Verify five intrinsic cliques, each induced by a choice of size-four star.
def star_center(c):
    classes = [set(V[i] for i in range(10) if c[i] == x) for x in range(3)]
    large = [S for S in classes if len(S) == 4]
    assert len(large) == 1
    center = [v for v in range(5) if all(v in e for e in large[0])]
    assert len(center) == 1
    return center[0]
centers = [star_center(p) for p in partitions]
for a in range(5):
    clique = [i for i in range(20) if centers[i] == a]
    assert len(clique) == 4
    assert all(j in Q[i] for i, j in combinations(clique, 2))
for i in range(20):
    assert len([j for j in Q[i] if centers[j] != centers[i]]) == 1
assert Counter(centers) == Counter({x: 4 for x in range(5)})

print('DIRECT_PETERSEN_KEMPE_PASS')
print('colorings=120 moves=360 degree=6 quotient_vertices=20 quotient_edges=40')
print('shells_per_coloring=(1,6,25,61,27) radius=4 diameter=4')
print('unordered_distance_distribution=(360,1500,3660,1620)')
print('one_vertex_recoloring_graph=60K2')
