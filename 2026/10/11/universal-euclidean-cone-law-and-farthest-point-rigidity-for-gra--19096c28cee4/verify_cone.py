#!/usr/bin/env python3
"""Exact integer checks for the Euclidean cone law of graphical zonotopes.

Run with Python 3, no third-party packages. These finite checks corroborate,
but do not replace, the all-graph cut inequality in the accompanying proof.
"""
from itertools import product
from collections import deque


def bipartite_components(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    color = [-1]*n
    nontrivial_components = 0
    for root in range(n):
        if color[root] != -1:
            continue
        if adj[root]:
            nontrivial_components += 1
        color[root] = 0
        q = deque([root])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == color[u]:
                    return False, -1, color
                if color[v] == -1:
                    color[v] = 1-color[u]
                    q.append(v)
    return True, nontrivial_components, color


def complete_bipartite(n, edges, coloring):
    if not edges:
        return False
    a = sum(x == 0 for x in coloring)
    b = n-a
    return a > 0 and b > 0 and len(edges) == a*b


def orientations(n, edges):
    for signs in product((-1, 1), repeat=len(edges)):
        d = [0]*n
        for (u,v), s in zip(edges,signs):
            d[u] += s
            d[v] -= s
        yield signs, tuple(d), sum(x*x for x in d)


def check(n, edges):
    edges = tuple(edges)
    edge_set = set(edges)
    base = list(orientations(n, edges))
    best_base = max(rec[2] for rec in base)
    best_cone = -1
    max_vertices = set()
    expected_extremes = set()
    for signs,d,base_sq in base:
        for spokes in product((-1,1), repeat=n):
            hub = -sum(spokes)
            cone = tuple(d[i]+spokes[i] for i in range(n))+(hub,)
            norm2 = sum(t*t for t in cone)
            if norm2 > best_cone:
                best_cone = norm2
                max_vertices = {cone}
            elif norm2 == best_cone:
                max_vertices.add(cone)
            neg = {i for i,s in enumerate(spokes) if s == -1}
            complete_cut = all((min(u,v),max(u,v)) in edge_set
                               for u in neg for v in range(n) if v not in neg)
            nonpositive_cut_contribution = True
            if 0<len(neg)<n:
                for (u,v),s in zip(edges,signs):
                    if (u in neg) != (v in neg):
                        # The cut contribution at vertices in neg must be negative.
                        if s * (1 if u in neg else -1) != -1:
                            nonpositive_cut_contribution = False
                            break
            if base_sq == best_base and complete_cut and nonpositive_cut_contribution:
                expected_extremes.add(cone)
    assert best_cone == n*(n+1)+best_base, (n, edges, best_cone, best_base)
    assert max_vertices == expected_extremes, (n,edges,len(max_vertices),len(expected_extremes))
    bip,c,color = bipartite_components(n,edges)
    if bip:
        degrees = [0]*n
        for u,v in edges:
            degrees[u] += 1
            degrees[v] += 1
        assert best_base == sum(d*d for d in degrees)
        extra = 2 if complete_bipartite(n,edges,color) else 0
        assert len(max_vertices) == (1<<(c+1))+extra, (n,edges,len(max_vertices),c,extra)
    return (bip,best_cone,len(max_vertices))


def main():
    graph_checks = 0
    bip_checks = 0
    for n in range(2,6):
        pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
        for mask in range(1<<len(pairs)):
            edges = [e for k,e in enumerate(pairs) if mask & (1<<k)]
            bip,_,_ = check(n,edges)
            graph_checks += 1
            bip_checks += int(bip)
    extras = [
        (6, [(i,i+1) for i in range(5)]),
        (6, [(i,(i+1)%6) for i in range(6)]),
        (6, [(i,j) for i in range(3) for j in range(3,6)]),
        (6, [(i,j) for i in range(2) for j in range(2,6)]),
        (6, [(0,i) for i in range(1,6)]),
        (6, [(0,1),(1,2),(2,0),(2,3),(3,4),(4,5)]),
    ]
    for n,edges in extras:
        bip,_,_ = check(n,edges)
        graph_checks += 1
        bip_checks += int(bip)
    print(f'PASS: {graph_checks} labeled/simple graph instances, including {bip_checks} bipartite ones; exact cone diameters, equality-cut criteria, and bipartite farthest-vertex counts.')

if __name__ == '__main__':
    main()
