"""Separate direct brute-force Hamilton-path and rotation graph check.
Run: python3 verify_independent.py
"""
from itertools import combinations, permutations
from collections import deque,Counter

vertices = list(combinations(range(5), 2))
edge = {(i,j) for i in range(10) for j in range(10) if i!=j and set(vertices[i]).isdisjoint(vertices[j])}
assert len(edge)==30
# Independent brute-force search: enumerate all permutations with each possible
# first vertex, retaining exactly one orientation of each undirected path.
paths=set()
for start in range(10):
    rest=tuple(v for v in range(10) if v!=start)
    for tail in permutations(rest):
        path=(start,)+tail
        if start < tail[-1] and all((path[i],path[i+1]) in edge for i in range(9)):
            paths.add(path)
assert len(paths)==120
by_endpair=Counter(tuple(sorted((p[0],p[-1]))) for p in paths)
assert len(by_endpair)==30 and set(by_endpair.values())=={4}

def normalize(path):
    r=tuple(reversed(path))
    return min(tuple(path),r)

# Reconfiguration with both endpoint choices, directly as edge deletion/addition.
link={p:set() for p in paths}
for p in paths:
    for oriented in (p, tuple(reversed(p))):
        for i in range(8):
            if (oriented[i],oriented[-1]) not in edge: continue
            q=normalize(oriented[:i+1]+(oriented[-1],)+tuple(reversed(oriented[i+1:-1])))
            assert q in paths
            link[p].add(q)
assert all(len(link[p])==4 for p in paths)
assert all(p in link[q] for p in paths for q in link[p])
assert sum(map(len,link.values()))//2==240
# Direct BFS in explicitly built rotation graph (not the group Cayley graph).
dist=[]
for start in paths:
    levels={start:0};queue=deque([start])
    while queue:
        v=queue.popleft()
        for w in link[v]:
            if w not in levels:
                levels[w]=levels[v]+1;queue.append(w)
    assert len(levels)==120
    dist.append(tuple(Counter(levels.values())[i] for i in range(7)))
assert all(row==(1,4,11,25,39,29,11) for row in dist)
print('VERIFY_INDEPENDENT_OK undirected_Hamiltonian_paths=120 endpoint_nonedge_pairs=30 four_each=true')
print('VERIFY_INDEPENDENT_OK rotation_graph_vertices=120 edges=240 degree=4')
print('VERIFY_INDEPENDENT_OK connected=true diameter=6 distance_distribution=1,4,11,25,39,29,11')
