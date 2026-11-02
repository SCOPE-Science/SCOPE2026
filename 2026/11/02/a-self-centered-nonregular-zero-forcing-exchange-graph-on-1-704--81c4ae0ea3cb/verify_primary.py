"""Exact certificate for the minimum zero-forcing exchange graph of GP(8,3).

Only Python's standard library is needed. Run: python3 verify_primary.py.
All index labels are zero-based; a_i=i and b_i=8+i.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

N = 16
BASE_EDGES = set()
for i in range(8):
    for a,b in ((i,(i+1)%8),(i,i+8),(i+8,8+(i+3)%8)):
        BASE_EDGES.add(tuple(sorted((a,b))))
assert len(BASE_EDGES) == 24
NEIGHBORS = [set() for _ in range(N)]
for a,b in BASE_EDGES:
    NEIGHBORS[a].add(b)
    NEIGHBORS[b].add(a)
assert all(len(x)==3 for x in NEIGHBORS)

def closure(initial):
    """Simultaneously apply every currently legal force until stability."""
    blue = set(initial)
    while True:
        add = set()
        for v in blue:
            unseen = NEIGHBORS[v] - blue
            if len(unseen) == 1:
                add.update(unseen)
        if not add:
            return blue
        blue.update(add)

universe = set(range(N))
assert sum(closure(c)==universe for c in combinations(range(N), 5)) == 0
family = [frozenset(c) for c in combinations(range(N), 6)
          if closure(c) == universe]
assert len(family) == 1704
index = {s:i for i,s in enumerate(family)}
assert len(index) == len(family)

# Independent graph construction: a pair of 6-sets are adjacent exactly
# when they share a 5-element face. Assemble all cliques over such faces.
common_faces = defaultdict(list)
for i,s in enumerate(family):
    for v in s:
        common_faces[frozenset(s-{v})].append(i)
graph = [set() for _ in family]
for ids in common_faces.values():
    for u,v in combinations(ids,2):
        graph[u].add(v)
        graph[v].add(u)
assert all(u in graph[v] for v,js in enumerate(graph) for u in js)
assert sum(map(len,graph))//2 == 16560
expected_degrees={16:240,17:96,18:336,19:192,20:288,21:192,22:240,24:120}
assert dict(sorted(Counter(map(len,graph)).items())) == expected_degrees

pair_d = Counter(); pair_johnson_gap=Counter(); wiener=0; ecc=Counter()
for source in range(len(family)):
    distances = [-1]*len(family)
    distances[source] = 0
    queue=deque([source])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if distances[w] == -1:
                distances[w] = distances[v]+1
                queue.append(w)
    assert -1 not in distances
    ecc[max(distances)] += 1
    for target in range(source+1,len(family)):
        d=distances[target]
        ambient=6-len(family[source]&family[target])
        assert d>=ambient
        pair_d[d]+=1
        pair_johnson_gap[d-ambient]+=1
        wiener+=d
expected_distance={1:16560,2:127008,3:417720,4:565488,5:276792,6:47388}
expected_gap={0:1441284,1:9648,2:24}
assert dict(sorted(pair_d.items())) == expected_distance
assert dict(sorted(pair_johnson_gap.items())) == expected_gap
assert dict(ecc)=={6:1704}
assert wiener==5453976
assert sum(pair_d.values())==len(family)*(len(family)-1)//2
print('PRIMARY_FINITE_PASS base_vertices=16 base_edges=24 size5_witnesses=0 size6_witnesses=1704')
print('EXCHANGE_GRAPH_OK vertices=1704 edges=16560 radius=6 diameter=6')
print('DISTANCES_OK '+str(dict(sorted(pair_d.items()))))
print('JOHNSON_EXCESS_OK '+str(dict(sorted(pair_johnson_gap.items()))))
print('WIENER_OK '+str(wiener))
print('DEGREES_OK '+str(expected_degrees))
