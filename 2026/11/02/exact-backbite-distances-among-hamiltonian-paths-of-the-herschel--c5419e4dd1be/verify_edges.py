"""Edge-subset enumeration and pairwise edge-exchange verification.

Run with Python 3: python verify_edges.py. No external packages are required.
"""
from collections import Counter, deque
from itertools import combinations
from functools import lru_cache

N = 11
# Explicit bipartite edge list, independent of path recursion.
left_neighborhoods = (
    (5, 6, 7, 8), (5, 6, 9, 10), (7, 8, 9, 10),
    (5, 7, 9), (6, 8, 10),
)
edges = tuple((v, w) for v in range(5) for w in left_neighborhoods[v])
assert len(edges) == 18
adj = [set() for _ in range(N)]
for a, b in edges:
    adj[a].add(b)
    adj[b].add(a)

states = []  # (edge_mask, sorted two endpoints)
for selected in combinations(range(18), 10):
    deg = [0]*N
    for j in selected:
        a, b = edges[j]
        deg[a] += 1
        deg[b] += 1
    if sorted(deg) != [1,1] + [2]*9:
        continue
    # A connected 11-vertex, ten-edge maximum-degree-two graph is a path.
    block_adj = [set() for _ in range(N)]
    for j in selected:
        a, b = edges[j]
        block_adj[a].add(b)
        block_adj[b].add(a)
    reached = {0}
    todo = [0]
    for u in todo:
        for v in block_adj[u]:
            if v not in reached:
                reached.add(v)
                todo.append(v)
    if len(reached) != N:
        continue
    edge_mask = sum(1 << j for j in selected)
    states.append((edge_mask, tuple(i for i in range(N) if deg[i] == 1)))
assert len(states) == 222
assert len(set(s[0] for s in states)) == len(states)

# If one edge of a Hamiltonian path is exchanged for an edge at an old
# endpoint, the resulting spanning path is exactly an endpoint backbite.
# This enumerates all such exchanges without constructing ordered paths.
neighbors = [set() for _ in states]
for i in range(len(states)):
    m, endpoints = states[i]
    for j in range(i+1, len(states)):
        new_mask, _ = states[j]
        if (m ^ new_mask).bit_count() != 2:
            continue
        added = new_mask & ~m
        assert added.bit_count() == 1
        added_edge = edges[added.bit_length()-1]
        if not any(z in endpoints for z in added_edge):
            continue
        neighbors[i].add(j)
        neighbors[j].add(i)
assert sum(map(len, neighbors)) == 888
assert all(len(ns) == 4 for ns in neighbors)

hist = Counter()
ecc = Counter()
diametral = Counter()
for root in range(222):
    distances = [-1]*222
    distances[root] = 0
    todo = deque([root])
    while todo:
        u = todo.popleft()
        for v in neighbors[u]:
            if distances[v] < 0:
                distances[v] = distances[u] + 1
                todo.append(v)
    assert min(distances) == 0
    ecc[max(distances)] += 1
    for j in range(root+1, 222):
        hist[distances[j]] += 1
        if distances[j] == 9:
            diametral[root] += 1
            diametral[j] += 1
assert dict(sorted(hist.items())) == {
    1: 444, 2: 1152, 3: 2436, 4: 4326, 5: 6348,
    6: 6189, 7: 3078, 8: 546, 9: 12,
}
assert ecc == {8: 198, 9: 24}
assert len(diametral) == 24 and set(diametral.values()) == {1}

# Per unordered endpoint pair, the counts are independent of path ordering.
ep_counts = Counter(endpoints for _, endpoints in states)
assert len(ep_counts) == 15
same_edge = {(5,6), (7,8), (9,10)}
same_pole = {(a,b) for a,b in combinations((5,7,9),2)} | \
            {(a,b) for a,b in combinations((6,8,10),2)}
assert all(ep_counts[x] == 14 for x in same_edge)
assert all(ep_counts[x] == 12 for x in same_pole)
assert all(ep_counts[x] == 18 for x in ep_counts if x not in same_edge | same_pole)
assert set(states[i][1] for i in diametral) == set(ep_counts) - same_edge - same_pole
assert Counter(states[i][1] for i in diametral) == {x:4 for x in ep_counts if x not in same_edge | same_pole}

# Dynamic-programming recurrence for ordered Hamiltonian paths from a to b:
# F(v,S)=sum_{w adjacent v, w not in S} F(w,S union {w}),
# with F(v,V)=1 precisely if v=b. The endpoint ordering a<b
# counts each undirected Hamiltonian path once.
@lru_cache(maxsize=None)
def path_extensions(v, used, target):
    if used == (1 << N)-1:
        return int(v == target)
    return sum(path_extensions(w, used | (1 << w), target)
               for w in adj[v] if not used & (1 << w))
for a, b in combinations(range(5, 11), 2):
    assert path_extensions(a, 1 << a, b) == ep_counts[(a, b)]
print('EDGE_SUBSETS_43758_EXHAUSTIVE_222_PATHS_PASS')
print('EDGE_EXCHANGE_444_EDGES_FOUR_REGULAR_CONNECTED_PASS')
print('ALTERNATE_DISTANCE_HISTOGRAM_RADIUS8_DIAMETER9_PASS')
print('ALTERNATE_ENDPOINT_CLASSES_AND_TWELVE_DISJOINT_DIAMETERS_PASS')
