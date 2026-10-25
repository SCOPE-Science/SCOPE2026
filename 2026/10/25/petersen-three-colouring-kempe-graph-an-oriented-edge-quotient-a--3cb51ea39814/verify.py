"""Exact Petersen vertex-three-colouring Kempe graph verification (stdlib only).

A vertex of KG(5,2) is a two-subset of {0,1,2,3,4}; adjacent pairs are disjoint.
An edge of the Kempe graph switches colours a,b on one whole connected component
of the induced a/b-vertex subgraph. All arithmetic and searches are exhaustive.
"""
from itertools import combinations, permutations
from collections import Counter, deque

BASE = tuple(range(5))
PAIRS = tuple(combinations(BASE, 2))
N = len(PAIRS)
NBR = tuple(frozenset(j for j, q in enumerate(PAIRS)
                       if not (set(p) & set(q))) for p in PAIRS)
E = tuple((i,j) for i in range(N) for j in NBR[i] if i < j)
assert N == 10 and len(E) == 15 and all(len(a) == 3 for a in NBR)

# Independent state generators: graph-colouring search and canonical star construction.
def backtrack(states, partial):
    i = len(partial)
    if i == N:
        states.add(tuple(partial)); return
    for c in range(3):
        if all(partial[j] != c for j in NBR[i] if j < i):
            backtrack(states, partial + (c,))

brute = set()
backtrack(brute, ())
constructive = set()
for i in BASE:
    for j in BASE:
        if j == i: continue
        others = frozenset(BASE) - {i,j}
        A = frozenset(u for u,p in enumerate(PAIRS) if i in p)
        B = frozenset(u for u,p in enumerate(PAIRS) if j in p and i not in p)
        C = frozenset(u for u,p in enumerate(PAIRS) if frozenset(p) <= others)
        assert len(A) == 4 and len(B) == 3 and len(C) == 3
        assert A | B | C == frozenset(range(N)) and not (A & B | A & C | B & C)
        for perm in permutations(range(3)):
            c = tuple(perm[0] if u in A else perm[1] if u in B else perm[2]
                      for u in range(N))
            constructive.add(c)
assert constructive == brute and len(brute) == 120
states = tuple(sorted(brute))
idx = {v: k for k,v in enumerate(states)}

# Independent Kempe implementations: breadth-first connected components and DSU.
def swaps_bfs(c):
    out = set()
    for a,b in combinations(range(3), 2):
        remain = {u for u,colour in enumerate(c) if colour in (a,b)}
        while remain:
            root = min(remain); remain.remove(root); component = {root}
            q = deque([root])
            while q:
                u = q.popleft()
                for v in NBR[u]:
                    if v in remain:
                        remain.remove(v); component.add(v); q.append(v)
            nc = list(c)
            for u in component: nc[u] = b if c[u] == a else a
            out.add(tuple(nc))
    return out

def swaps_dsu(c):
    out = set()
    for a,b in combinations(range(3),2):
        parent = list(range(N))
        def find(u):
            while parent[u] != u:
                u = parent[u]
            return u
        for u,v in E:
            if c[u] in (a,b) and c[v] in (a,b):
                parent[find(u)] = find(v)
        components = {}
        for u,col in enumerate(c):
            if col in (a,b):components.setdefault(find(u), []).append(u)
        for comp in components.values():
            nc = list(c)
            for u in comp:nc[u] = a+b-c[u]
            out.add(tuple(nc))
    return out

graph = []
for c in states:
    bs,ds = swaps_bfs(c),swaps_dsu(c)
    assert bs == ds and len(bs) == 6 and bs <= brute
    graph.append(frozenset(idx[d] for d in bs))
assert all(i not in graph[i] for i in range(120))
assert all(i in graph[j] for i in range(120) for j in graph[i])
assert sum(map(len,graph)) // 2 == 360

def ordered_pair(c):
    classes = tuple(frozenset(PAIRS[u] for u in range(N) if c[u] == a)
                    for a in range(3))
    assert sorted(map(len,classes)) == [3,3,4]
    big = next(x for x in classes if len(x) == 4)
    center = [i for i in BASE if all(i in p for p in big)]
    assert len(center)==1
    i = center[0]
    smaller = [x for x in classes if len(x)==3]
    smallstars = [j for j in BASE if j != i and any(all(j in p for p in s) for s in smaller)]
    assert len(smallstars)==1
    return i,smallstars[0]

labels = tuple(ordered_pair(c) for c in states)
assert len(set(labels)) == 20
assert Counter(labels) == Counter({(i,j):6 for i in BASE for j in BASE if i!=j})
quot = {a:set() for a in labels}
for p, neighbors in enumerate(graph):
    for q in neighbors:
        if labels[p] != labels[q]:quot[labels[p]].add(labels[q])
for i,j in quot:
    expected = {(i,k) for k in BASE if k not in (i,j)} | {(j,i)}
    assert quot[i,j] == expected
assert sum(map(len,quot.values()))//2 == 40

# Independent graph model: take the line graph of the graph in which each K5 edge is subdivided once.
# Its 20 graph edges are incidences (original vertex i, original K5 edge {i,j}).
incidences = {(i,tuple(sorted((i,j)))):(i,j) for i,j in quot}
assert len(incidences) == 20
for a in incidences:
    theoretical = {incidences[b] for b in incidences if b!=a and (a[0] == b[0] or a[1] == b[1])}
    assert quot[incidences[a]] == theoretical

# Exhaustive all-source shortest paths, not a sampled run.
def shells(adj, src):
    d = {src:0}; q=deque([src])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in d:d[v]=d[u]+1;q.append(v)
    return tuple(sorted(Counter(d.values()).items())),len(d)

assert {shells(quot,s) for s in quot} == {(((0,1),(1,4),(2,6),(3,9)),20)}
profile = (((0,1),(1,6),(2,25),(3,61),(4,27)),120)
assert {shells({i:graph[i] for i in range(120)},s) for s in range(120)} == {profile}

# Full global palette permutation acts freely and vertex aut S5 moves any ordered pair to any other.
# Explicitly test the graph automorphisms on the enumerated colourings.
for p in permutations(BASE):
    image_index = {i: PAIRS.index(tuple(sorted((p[a],p[b])))) for i,(a,b) in enumerate(PAIRS)}
    for c in states[::6]:
        t = [0]*N
        for u in range(N):t[image_index[u]] = c[u]
        assert tuple(t) in brute
for p in permutations(range(3)):
    assert all(tuple(p[x] for x in c) in brute for c in states)

print('VERIFY_OK')
print('states=120 edges=360 degree=6 radius=diameter=4')
print('labeled_distance_shells=1,6,25,61,27')
print('palette_quotient_states=20 edges=40 degree=4 radius=diameter=3')
print('palette_quotient_shells=1,4,6,9; line graph of subdivided K5')
