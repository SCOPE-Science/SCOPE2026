"""Exhaustive edge-distance and basis-exchange verifier for the seven-petal flower snark.

Run: python3 verify_distances.py
Only the Python standard library is needed.
"""
from collections import Counter, deque
from itertools import combinations

N = 7
V = [(i, t) for i in range(N) for t in "abcd"]
number = {v: j for j, v in enumerate(V)}
E = set()

def add(x, y):
    e = tuple(sorted((number[x], number[y])))
    assert e[0] != e[1]
    E.add(e)

for i in range(N):
    for t in "bcd":
        add((i, "a"), (i, t))
    add((i, "b"), ((i + 1) % N, "b"))
    if i < N - 1:
        for t in "cd":
            add((i, t), (i + 1, t))
    else:
        add((i, "c"), (0, "d"))
        add((i, "d"), (0, "c"))
E = sorted(E)
assert len(V) == 28 and len(E) == 42
adj = [[] for _ in V]
for u, v in E:
    adj[u].append(v)
    adj[v].append(u)
assert all(len(neighbors) == 3 for neighbors in adj)

# Breadth-first vertex distances; convert them to vertex-to-edge distances.
dist = []
for s in range(len(V)):
    d = [-1] * len(V)
    d[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                q.append(v)
    assert -1 not in d
    dist.append([min(d[u], d[v]) for u, v in E])

# Each coordinate is a bitset of edge pairs it separates.
edge_pairs = list(combinations(range(len(E)), 2))
separators = []
for row in dist:
    bits = sum(1 << j for j, (e, f) in enumerate(edge_pairs) if row[e] != row[f])
    separators.append(bits)
full = (1 << len(edge_pairs)) - 1

def resolving(s):
    bits = 0
    for v in s:
        bits |= separators[v]
    return bits == full

triples = list(combinations(range(28), 3))
assert len(triples) == 3276
assert sum(resolving(t) for t in triples) == 0
bases = [s for s in combinations(range(28), 4) if resolving(s)]
assert len(bases) == 1932
assert resolving(tuple(sorted(number[(i, t)] for i, t in ((0, "a"), (0, "b"), (1, "c"), (4, "c")))))
lookup = {s: i for i, s in enumerate(bases)}
assert len(lookup) == len(bases)

# One-landmark replacement, regardless of adjacency of the exchanged vertices.
adjex = [set() for _ in bases]
for i, basis in enumerate(bases):
    for gone in basis:
        partial = set(basis) - {gone}
        for new in range(28):
            if new == gone or new in partial:
                continue
            j = lookup.get(tuple(sorted(partial | {new})))
            if j is not None and j != i:
                adjex[i].add(j)
assert all(i in adjex[j] for i, nbrs in enumerate(adjex) for j in nbrs)
assert sum(map(len, adjex)) == 35840

# Every vertex supplies a BFS start; hence these are exact eccentricities,
# not samples or upper bounds from a handful of roots.
ecc = Counter()
for root in range(len(bases)):
    d = [-1] * len(bases)
    d[root] = 0
    q = deque([root])
    while q:
        i = q.popleft()
        for j in adjex[i]:
            if d[j] == -1:
                d[j] = d[i] + 1
                q.append(j)
    assert -1 not in d
    ecc[max(d)] += 1
assert ecc == {5: 1932}
print("graph: vertices=28 edges=42 degree=3")
print("edge-pair separation constraints=861")
print("3-subsets checked=3276 resolving=0")
print("4-subsets checked=20475 resolving=1932")
print("witness={a0,b0,c1,c4}")
print("basis-exchange: vertices=1932 edges=17920 components=1")
print("eccentricities: {5: 1932}; radius=5 diameter=5")
print("VERIFIED")
