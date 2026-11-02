"""Standalone exact verification of Petersen Hamiltonian-path Pósa graph.
Run with Python 3.9+; standard library only.
"""
from itertools import combinations, permutations
from collections import Counter, deque
V = list(combinations(range(5), 2))
index = {p:i for i,p in enumerate(V)}
N = [set() for _ in V]
for i,a in enumerate(V):
    for j,b in enumerate(V):
        if i!=j and set(a).isdisjoint(b): N[i].add(j)
assert len(V)==10 and all(len(x)==3 for x in N)
def canon(path):
    path=tuple(path)
    return min(path, path[::-1])
paths=set()
def visit(p,used):
    if len(p)==10:
        paths.add(canon(p));return
    for y in N[p[-1]]:
        if not (used >> y & 1): visit(p+[y],used | (1<<y))
for x in range(10):visit([x],1<<x)
paths=sorted(paths);loc={p:i for i,p in enumerate(paths)}
assert len(paths)==120
# Direct application at either free endpoint, no group assumptions.
G=[set() for _ in paths]
for p in paths:
    for orientation in (p,p[::-1]):
        for i in range(8):
            if orientation[-1] in N[orientation[i]]:
                q=canon(orientation[:i+1]+orientation[:i:-1])
                assert q in loc
                G[loc[p]].add(loc[q])
assert all(len(nb)==4 for nb in G)
assert all(i in G[j] for j,nb in enumerate(G) for i in nb)
assert sum(map(len,G))//2 == 240
# Full permutation action. g induces a permutation on the ten 2-subsets.
S5=list(permutations(range(5)))
action={g:tuple(index[tuple(sorted((g[x],g[y])))] for x,y in V) for g in S5}
reference=paths[0]
images={canon(tuple(action[g][x] for x in reference)):g for g in S5}
assert len(images)==120 and set(images)==set(paths)
generators=tuple(sorted(images[paths[q]] for q in G[loc[reference]]))
expected={
    (3,1,4,2,0),
    (1,0,3,2,4),
    (4,1,3,0,2),
    (3,1,2,0,4)
}
assert set(generators)==expected
# For each group element, left action sends 4 reference-neighbors to 4 actual neighbors.
for g,act in action.items():
    p=canon(tuple(act[x] for x in reference))
    expected_nb={loc[canon(tuple(act[x] for x in paths[j]))] for j in G[loc[reference]]}
    assert expected_nb==G[loc[p]]
# Independent group multiplication description: right-Cayley on S5.
def compose(g,h):return tuple(g[h[i]] for i in range(5))
q=deque([tuple(range(5))]); dist={q[0]:0}
while q:
    g=q.popleft()
    for s in generators:
        h=compose(g,s)
        if h not in dist:
            dist[h]=dist[g]+1;q.append(h)
shells=[Counter(dist.values())[i] for i in range(7)]
assert len(dist)==120 and shells==[1,4,11,25,39,29,11]
# Explicit exhaustive path metric agrees with Cayley shortest word lengths.
for p in paths:
    src=loc[p]; seen={src:0};q=deque([src])
    while q:
        v=q.popleft()
        for w in G[v]:
            if w not in seen:seen[w]=seen[v]+1;q.append(w)
    assert len(seen)==120 and Counter(seen.values())==Counter(dict(enumerate(shells)))
# Check the four Hamiltonian paths for one fixed nonedge pair.
a=index[(0,1)]; b=index[(0,2)]
fixed=[p for p in paths if {p[0],p[-1]}=={a,b}]
assert len(fixed)==4
print('PETERSEN_PATHS_OK',len(paths),'ENDPOINT_PAIR_WITNESSES',len(fixed))
print('REGULAR_S5_ACTION_OK',len(images),'GENERATORS',generators)
print('BACKBITE_CAYLEY_OK',sum(map(len,G))//2,'EDGES')
print('EXACT_METRIC_OK',shells,'RADIUS',6,'DIAMETER',6)
print('PRIMARY_CERTIFICATE_OK')
