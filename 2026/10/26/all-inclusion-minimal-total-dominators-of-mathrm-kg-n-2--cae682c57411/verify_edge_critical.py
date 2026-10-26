"""Exhaustive finite core for minimal total domination in KG(n,2).

Standard library only. Every graph with at most six edges and no isolated
vertices is generated via single-edge augmentation, modulo an explicit
canonical label based on exhaustive permutations within degree classes.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product


def norm_edge(a, b):
    return (min(a, b), max(a, b))


def components(edges):
    vertices = {v for e in edges for v in e}
    unseen = set(vertices)
    comps = []
    while unseen:
        root = min(unseen)
        reached = {root}
        queue = [root]
        while queue:
            u = queue.pop()
            for a, b in edges:
                if a == u and b not in reached:
                    reached.add(b); queue.append(b)
                if b == u and a not in reached:
                    reached.add(a); queue.append(a)
        unseen.difference_update(reached)
        comps.append(reached)
    return comps


def component_signature(vertices, edges):
    v = list(sorted(vertices))
    degree = {u: sum(u in e for e in edges) for u in v}
    blocks = [[u for u in v if degree[u] == d] for d in sorted(set(degree.values()))]
    n = len(v)
    best = None
    for groups in product(*(permutations(b) for b in blocks)):
        order = [u for group in groups for u in group]
        bits = tuple(int(norm_edge(order[i], order[j]) in edges)
                     for i in range(n) for j in range(i+1, n))
        if best is None or bits < best:
            best = bits
    return n, best


def canonical(edges):
    return tuple(sorted(component_signature(comp, edges) for comp in components(edges)))


def vertex_cover_number_leq_three(edges):
    v = sorted({a for e in edges for a in e})
    for k in range(4):
        for cover in combinations(v, k):
            if all(a in cover or b in cover for a, b in edges):
                return k
    return 4


def survivors_by_size():
    levels = [{(): frozenset()}]
    for m in range(1, 7):
        dest = {}
        for graph in levels[-1].values():
            n = max((max(e) for e in graph), default=-1) + 1
            # An added edge joins existing vertices, one new vertex,
            # or two new vertices. No other possibility in an edge graph.
            for u in range(n+1):
                for v in range(u+1, n+2):
                    if u == n and v != n+1:
                        continue
                    if u < n and v <= n:
                        new_edge = norm_edge(u, v)
                        if new_edge not in graph:
                            candidate = graph | {new_edge}
                            dest.setdefault(canonical(candidate), candidate)
                    elif u == n and v == n+1:
                        new_edge = (n, n+1)
                        candidate = graph | {new_edge}
                        dest.setdefault(canonical(candidate), candidate)
        levels.append(dest)
    critical = []
    for m, graphs in enumerate(levels):
        for graph in graphs.values():
            if vertex_cover_number_leq_three(graph) != 3:
                continue
            if all(vertex_cover_number_leq_three(graph - {edge}) == 2 for edge in graph):
                critical.append((m, canonical(graph), graph))
    return levels, critical


def label(edges):
    m = len(edges)
    comps = components(edges)
    sizes = sorted(len(comp) for comp in comps)
    degrees = sorted(sum(v in edge for edge in edges) for v in {a for e in edges for a in e})
    if m == 3 and sizes == [2,2,2] and degrees == [1]*6: return '3K2'
    if m == 4 and sizes == [2,3] and degrees == [1,1,2,2,2]: return 'K3+K2'
    if m == 5 and sizes == [5] and degrees == [2]*5: return 'C5'
    if m == 6 and sizes == [4] and degrees == [3]*4: return 'K4'
    return 'UNKNOWN'


def main():
    levels, critical = survivors_by_size()
    print('Unlabeled no-isolate graphs by edge count:', [len(x) for x in levels])
    summary = []
    for m, _, graph in critical:
        summary.append((m, label(graph), len({x for edge in graph for x in edge})))
    print('All edge-minimal vertex-cover-three graphs:', sorted(summary))
    assert [len(x) for x in levels] == [1,1,2,5,11,26,68]
    assert sorted((m,s) for m,s,v in summary) == [(3,'3K2'),(4,'K3+K2'),(5,'C5'),(6,'K4')]
    assert all(s != 'UNKNOWN' for m,s,v in summary)
    print('FINITE_CLASSIFICATION_OK')

if __name__ == '__main__':
    main()
