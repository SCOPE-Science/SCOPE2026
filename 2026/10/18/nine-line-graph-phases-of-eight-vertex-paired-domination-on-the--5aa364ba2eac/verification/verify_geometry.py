"""Independent coordinate/Hall enumeration and line-graph identification.

Run with Python 3.10+: python verification/verify_geometry.py
Does not use a graph library or the bit-mask matching recursion.
"""
from collections import Counter, deque
from itertools import combinations, permutations

F = range(3)
points = tuple((x, y) for x in F for y in F)
lines = tuple((m, b) for m in F for b in F)


def incident(p, l):
    x, y = p
    m, b = l
    return (y - m*x - b) % 3 == 0


def paired_dominating(P, L):
    P, L = set(P), set(L)
    # The graph has exactly nine point and nine line vertices.
    if any(not any(incident(p, l) for l in L) for p in points if p not in P):
        return False
    if any(not any(incident(p, l) for p in P) for l in lines if l not in L):
        return False
    # Enumerating every bijection is an exact Hall/matching test.
    return any(all(incident(p, l) for p, l in zip(sorted(P), ordering))
               for ordering in permutations(sorted(L)))


def all_pairs(r):
    return [(frozenset(P), frozenset(L))
            for P in combinations(points, r) for L in combinations(lines, r)
            if paired_dominating(P, L)]


def shape_p(P):
    return tuple(sorted((sum(p[0] == x for p in P) for x in F), reverse=True))


def template(c, m):
    Pc = frozenset((c, y) for y in F)
    Lm = frozenset((m, b) for b in F)
    extp = set(points) - Pc
    extl = set(lines) - Lm
    # Dominance is automatic after selecting the six-vertex core.
    # A fourth matching edge exists by either a direct incidence
    # or a two-edge alternating reassignment through the core matching.
    allowable = set()
    for p in extp:
        for l in extl:
            x, y = p
            u, b = l
            direct = incident(p, l)
            cross = (y - m*x + m*c - (u*c+b)) % 3 == 0
            if direct or cross:
                allowable.add((p, l))
    return Pc, Lm, allowable


def cycle_sizes(adj):
    unseen = set(adj)
    lengths = []
    while unseen:
        start = next(iter(unseen))
        queue = [start]
        seen = {start}
        unseen.remove(start)
        for a in queue:
            for b in adj[a]:
                if b in unseen:
                    unseen.remove(b)
                    seen.add(b)
                    queue.append(b)
        lengths.append(len(seen))
    return sorted(lengths)


def diameter(adj):
    best = 0
    for root in adj:
        depth = {root: 0}
        queue = deque([root])
        while queue:
            v = queue.popleft()
            for u in adj[v]:
                if u not in depth:
                    depth[u] = depth[v] + 1
                    queue.append(u)
        assert len(depth) == len(adj)
        best = max(best, max(depth.values()))
    return best


if __name__ == '__main__':
    low = {r: all_pairs(r) for r in (1, 2, 3)}
    print('smaller_sizes=' + str({2*r: len(low[r]) for r in low}))
    assert [len(low[r]) for r in (1, 2, 3)] == [0, 0, 9]
    cores = {(frozenset((c, y) for y in F), frozenset((m, b) for b in F))
             for c in F for m in F}
    assert set(low[3]) == cores
    print('minimum_cores=9')

    found = set(all_pairs(4))
    print('eight_vertex_sets=' + str(len(found)))
    assert len(found) == 216
    counts = Counter(shape_p(P) for P, L in found)
    all_ptypes = Counter(shape_p(P) for P in combinations(points, 4))
    print('four_point_types=' + str(sorted((str(k), all_ptypes[k], counts[k]) for k in all_ptypes)))
    assert counts == {(3, 1, 0): 216}
    assert all_ptypes == {(3, 1, 0): 18, (2, 2, 0): 27, (2, 1, 1): 81}

    expected = {}
    for c in F:
        for m in F:
            Pc, Lm, allowed = template(c, m)
            assert len(allowed) == 24
            for p, l in allowed:
                state = (Pc | {p}, Lm | {l})
                assert state not in expected
                expected[state] = (c, m, p, l)
    assert found == set(expected)
    print('unique_core_classification=9_by_24')

    comp_properties = Counter()
    for c in F:
        for m in F:
            Pc, Lm, allowed = template(c, m)
            # Each configuration is one edge in the small bipartite graph B.
            # Sharing an endpoint is precisely a legal single-vertex exchange.
            edges = sorted(allowed)
            adjacency = {e: {f for f in edges if f != e and (e[0] == f[0] or e[1] == f[1])}
                         for e in edges}
            assert len(edges) == 24
            assert {len(adj) for adj in adjacency.values()} == {6}
            assert sum(map(len, adjacency.values()))//2 == 72
            assert diameter(adjacency) == 3
            # The 12 missing edges of B have degree two at all 12 endpoints,
            # and form ONE cycle, not multiple disjoint even cycles.
            missing = {(p, l) for p in points if p not in Pc
                       for l in lines if l not in Lm} - allowed
            assert len(missing) == 12
            forbidden_adj = {('p', p): set() for p in points if p not in Pc}
            forbidden_adj.update({('l', l): set() for l in lines if l not in Lm})
            for p, l in missing:
                forbidden_adj[('p', p)].add(('l', l))
                forbidden_adj[('l', l)].add(('p', p))
            assert {len(n) for n in forbidden_adj.values()} == {2}
            assert cycle_sizes(forbidden_adj) == [12]
            comp_properties[(len(edges), sum(map(len, adjacency.values()))//2,
                             diameter(adjacency), len(missing))] += 1
    assert comp_properties == {(24, 72, 3, 12): 9}
    print('line_graph_components=' + str(sorted(comp_properties.items())))

    # A jump between balanced four-point/four-line sets can replace only a point
    # or only a line, and the full column and full slope are each invariant.
    states = list(found)
    lookup = set(states)
    edge_count = 0
    cross = 0
    for P, L in states:
        core = expected[(P, L)][:2]
        for pp in P:
            for pq in points:
                if pq in P: continue
                other = ((P-{pp})|{pq},L)
                if other in lookup:
                    edge_count += 1
                    cross += expected[other][:2] != core
        for ll in L:
            for lq in lines:
                if lq in L:continue
                other=(P,(L-{ll})|{lq})
                if other in lookup:
                    edge_count += 1
                    cross += expected[other][:2] != core
    assert cross == 0 and edge_count//2 == 648
    print('global_exchange_edges=648 cross_core_edges=0')
    print('VERIFY_OK')
