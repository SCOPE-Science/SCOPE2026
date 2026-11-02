#!/usr/bin/env python3
"""Independent LCF-graph construction and exact matching-cycle check (stdlib)."""
from itertools import combinations
from collections import Counter, deque

N = 18
edges = set()
def add(a, b):
    assert a != b
    edges.add((min(a, b), max(a, b)))
for v in range(N):
    add(v, (v + 1) % N)
for v, step in enumerate((5, 7, -7, 7, -7, -5) * 3):
    add(v, (v + step) % N)
assert len(edges) == 27
neigh = [set() for _ in range(N)]
for a, b in edges:
    neigh[a].add(b); neigh[b].add(a)
assert all(len(x) == 3 for x in neigh)

# A concrete adjacency-preserving bijection from the affine incidence model:
# first nine coordinates (x,y), then nine lines (direction,offset).
label = (0, 2, 8, 12, 10, 6, 16, 4, 14, 1, 11, 15, 17, 3, 7, 5, 13, 9)
assert len(set(label)) == 18
from itertools import product
pts = list(product(range(3), repeat=2))
lns = list(product(range(3), range(3)))
image_edges = set()
for i, (x, y) in enumerate(pts):
    for j, (s, c) in enumerate(lns):
        if (x if s == 0 else y if s == 1 else (x + y) % 3) == c:
            a, b = label[i], label[j + 9]
            image_edges.add((min(a, b), max(a, b)))
assert edges == image_edges

# LCF bipartition obtained without any point/line indexing.
color = {0: 0}; queue = deque([0])
while queue:
    u = queue.popleft()
    for v in neigh[u]:
        if v not in color:
            color[v] = 1 - color[u]; queue.append(v)
        else:
            assert color[v] != color[u]
assert Counter(color.values()) == {0: 9, 1: 9}
left = sorted(u for u in color if color[u] == 0)
right = sorted(u for u in color if color[u] == 1)

matchings = []
def rec(i, taken, selected):
    if i == 9:
        matchings.append(frozenset(selected)); return
    u = left[i]
    for v in sorted(neigh[u]):
        if v not in taken:
            rec(i + 1, taken | {v}, selected + [(min(u, v), max(u, v))])
rec(0, set(), [])
assert len(matchings) == len(set(matchings)) == 42

def alternating_cycle_length(a, b):
    difference = a ^ b
    if not difference:
        return None
    incidence = {}
    for u, v in difference:
        incidence.setdefault(u, set()).add(v)
        incidence.setdefault(v, set()).add(u)
    if not all(len(x) == 2 for x in incidence.values()):
        return None
    root = next(iter(incidence)); reached = {root}; stack = [root]
    while stack:
        for v in incidence[stack.pop()]:
            if v not in reached:
                reached.add(v); stack.append(v)
    return len(difference) if len(reached) == len(incidence) else None

adjs = {6: [set() for _ in matchings], 8: [set() for _ in matchings]}
for i, j in combinations(range(42), 2):
    length = alternating_cycle_length(matchings[i], matchings[j])
    if length in adjs:
        adjs[length][i].add(j); adjs[length][j].add(i)
assert sum(map(len, adjs[6])) // 2 == 72
assert sum(map(len, adjs[8])) // 2 == 108
assert Counter(map(len, adjs[6])) == {3: 36, 6: 6}
assert Counter(map(len, adjs[8])) == {0: 6, 6: 36}

def bfs(graph, src):
    dist = {src: 0}; queue = deque([src])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in dist:
                dist[v] = dist[u] + 1; queue.append(v)
    return dist

assert Counter(len(bfs(adjs[6], i)) for i in range(42)) == {21: 42}
assert Counter(len(bfs(adjs[8], i)) for i in range(42)) == {1: 6, 36: 36}
union = [adjs[6][i] | adjs[8][i] for i in range(42)]
assert all(len(bfs(union, i)) == 42 for i in range(42))
assert Counter(max(bfs(union, i).values()) for i in range(42)) == {3: 42}
assert Counter(bfs(union, i)[j] for i, j in combinations(range(42), 2)) == {1: 180, 2: 504, 3: 177}
print('LCF_PAPPUS_ALTERNATING_CYCLE_INDEPENDENT_PASS')
