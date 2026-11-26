"""Exact component, shape, and distance checks for the Desargues token-slide graphs."""
from collections import Counter, deque
from itertools import combinations

P = tuple(combinations(range(5), 2))
EDGES = {(i, 10+j) for i, p in enumerate(P) for j, q in enumerate(P)
         if set(p).isdisjoint(q)}
# Isomorphism certificate, with rim labels 0..9 and inner labels 10..19.
TO_GP = (0, 19, 13, 2, 8, 17, 11, 6, 15, 4, 5, 14, 18, 7, 3, 12, 16, 1, 10, 9)
gp = {frozenset(e) for i in range(10)
      for e in ((i, (i+1) % 10), (i, 10+i), (10+i, 10+(i+3) % 10))}
assert sorted(TO_GP) == list(range(20))
assert len(EDGES) == 30 and {frozenset((TO_GP[i], TO_GP[j])) for i,j in EDGES} == gp
edge_masks = [(1 << i) | (1 << j) for i, j in sorted(EDGES)]

CENSUS = (
    (20,30,{20:1}), (160,420,{160:1}), (660,2220,{660:1}),
    (1510,5580,{1500:1,1:10}), (1924,6870,{1824:1,10:10}),
    (1320,3840,{970:1,33:10,1:20}), (480,780,{38:10,4:20,1:20}),
    (115,60,{4:20,1:35}), (20,0,{1:20}), (2,0,{1:2}),
)
METRICS = (
    {20:(5,5)}, {160:(5,7)}, {660:(8,9)}, {1500:(8,10)},
    {1824:(9,10),10:(3,4)}, {970:(8,10),33:(4,5)},
    {38:(4,6),4:(1,2)}, {4:(1,2)}, {}, {},
)


def distances(graph, start):
    d = {start: 0}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in d:
                d[v] = d[u]+1
                queue.append(v)
    return d


def check(k):
    states = set()
    for choice in combinations(range(20), k):
        m = sum(1 << i for i in choice)
        if not any(m & e == e for e in edge_masks):
            states.add(m)
    # An edge mask toggles just its two endpoints. Keeping only results in the
    # same independent layer enforces exactly one occupied endpoint before the move.
    graph = {m: {m ^ e for e in edge_masks if (m ^ e) in states} for m in states}
    n_edges = sum(map(len, graph.values())) // 2
    assert n_edges == sum((a ^ b) in edge_masks for a,b in combinations(sorted(states), 2))
    unseen = set(states)
    sizes, metrics, isolates = Counter(), {}, set()
    while unseen:
        c = set(distances(graph, min(unseen)))
        unseen -= c
        size = len(c)
        sizes[size] += 1
        if size == 1:
            isolates.update(c)
            continue
        ecc = [max(distances(graph, a).values()) for a in c]
        pair = min(ecc), max(ecc)
        assert metrics.setdefault(size, pair) == pair
        if k == 5 and size == 10:
            hub = {m for m in c if len(graph[m]) == 3}
            assert len(hub) == 4 and all(not (graph[m] & hub) for m in hub)
            pairs = [frozenset(graph[m]) for m in c-hub]
            assert Counter(pairs) == Counter(map(frozenset, combinations(hub, 2)))
        if k in (7, 8) and size == 4:
            assert sorted(len(graph[m]) for m in c) == [1,1,1,3]
    assert (len(states), n_edges, sizes) == CENSUS[k-1]
    assert metrics == METRICS[k-1]
    if k == 4:
        assert isolates == {sum(1 << (i+s*10) for i,p in enumerate(P) if x in p)
                            for s in (0,1) for x in range(5)}
    print(k, len(states), n_edges, dict(sorted(sizes.items())), dict(sorted(metrics.items())))


if __name__ == '__main__':
    for k in range(1,11):
        check(k)
    print('ALL_CHECKS_OK')
