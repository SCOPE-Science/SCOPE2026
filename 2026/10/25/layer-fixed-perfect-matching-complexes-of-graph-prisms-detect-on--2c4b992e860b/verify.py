#!/usr/bin/env python3
"""Finite checks for the layer-fixed perfect-matching-complex theorem.

No external packages are required. These checks illustrate the general proof;
the infinite-family conclusion follows from the face bijection and acyclic matching.
"""
from itertools import combinations
from collections import deque


def base_perfect_matchings(n, edges):
    edge_set = set(edges)
    def rec(uncovered):
        if not uncovered:
            yield ()
            return
        v = min(uncovered)
        for w in sorted(uncovered - {v}):
            if (min(v, w), max(v, w)) in edge_set:
                for tail in rec(uncovered - {v, w}):
                    yield ((v, w),) + tail
    return list(rec(set(range(n))))


def prism_faces(n, edges):
    # Edge numbers 0..n-1 are rungs. Each base edge supplies two
    # horizontal edges; its orbit is the corresponding edge of the base.
    prism_edges = [(2*v, 2*v+1) for v in range(n)]
    for a,b in edges:
        prism_edges.extend(((2*a, 2*b), (2*a+1, 2*b+1)))
    edge_index = {tuple(sorted(e)):i for i,e in enumerate(prism_edges)}
    adjacency = {v:[] for v in range(2*n)}
    for i,(a,b) in enumerate(prism_edges):
        adjacency[a].append((b,i))
        adjacency[b].append((a,i))
    def pm(uncovered):
        if not uncovered:
            yield ()
            return
        v = min(uncovered)
        for w,i in adjacency[v]:
            if w in uncovered:
                for tail in pm(uncovered - {v,w}):
                    yield (i,)+tail
    faces = {frozenset()}
    for facet in pm(set(range(2*n))):
        for mask in range(1 << n):
            faces.add(frozenset(facet[j] for j in range(n) if mask >> j & 1))
    return faces, prism_edges


def fixed_orbit_faces(n, edges):
    faces, pe = prism_faces(n, edges)
    involution = {i:i for i in range(n)}
    for j in range(len(edges)):
        involution[n+2*j] = n+2*j+1
        involution[n+2*j+1] = n+2*j
    fixed = [f for f in faces if frozenset(involution[i] for i in f) == f]
    orbits = set()
    for f in fixed:
        orbit = {i for i in f if i < n}
        orbit.update(n+j for j in range(len(edges)) if n+2*j in f)
        orbits.add(frozenset(orbit))
    return orbits


def whiskered_matching_faces(n, edges):
    faces = set()
    m = len(edges)
    for mask in range(1 << m):
        chosen = [j for j in range(m) if mask >> j & 1]
        endpoints = [v for j in chosen for v in edges[j]]
        if len(set(endpoints)) != 2*len(chosen):
            continue
        unused = [v for v in range(n) if v not in endpoints]
        for flags in range(1 << len(unused)):
            f = {n+j for j in chosen}
            f.update(unused[k] for k in range(len(unused)) if flags >> k & 1)
            faces.add(frozenset(f))
    return faces


def verify_matching_acyclic(n, edges, faces):
    upper_to_lower = {}
    critical = set()
    for f in faces:
        occupied = {v for j in f if j >= n for v in edges[j-n]}
        uncovered = [v for v in range(n) if v not in occupied]
        if not uncovered:
            critical.add(f)
        else:
            v = uncovered[0]
            if v in f:
                upper_to_lower[f] = f - {v}
    assert set(upper_to_lower.values()).isdisjoint(critical)
    assert len(upper_to_lower) * 2 + len(critical) == len(faces)
    graph = {f:[] for f in faces}
    indeg = {f:0 for f in faces}
    for f in faces:
        for v in f:
            down = f - {v}
            a,b = (down,f) if upper_to_lower.get(f) == down else (f,down)
            graph[a].append(b)
            indeg[b] += 1
    dq = deque(f for f,d in indeg.items() if not d)
    processed = 0
    while dq:
        f = dq.popleft()
        processed += 1
        for g in graph[f]:
            indeg[g] -= 1
            if indeg[g] == 0:
                dq.append(g)
    assert processed == len(faces), 'Cycle in oriented face poset'
    return len(upper_to_lower), len(critical)


def run():
    checks = 0
    big_checks = 0
    for n in range(1,6):
        all_edges = list(combinations(range(n),2))
        for mask in range(1 << len(all_edges)):
            edges = [e for j,e in enumerate(all_edges) if mask >> j & 1]
            actual = fixed_orbit_faces(n,edges)
            target = whiskered_matching_faces(n,edges)
            assert actual == target, (n,edges)
            pm = len(base_perfect_matchings(n,edges))
            expected = 0 if not pm else pm * (-1)**(n//2-1)
            chi = -sum((-1)**len(f) for f in target)
            assert chi == expected, (n,edges,chi,pm)
            if n <= 4:
                pair_count,crit_count = verify_matching_acyclic(n,edges,target)
                assert crit_count == pm
                big_checks += 1
            checks += 1
    for n,edges in [
        (6,[(i,(i+1)%6) if i<5 else (0,5) for i in range(6)]),
        (6,list(combinations(range(6),2))),
        (6,[(a,b) for a in range(3) for b in range(3,6)]),
        (7,[(i,i+1) for i in range(6)]+[(0,6)]),
    ]:
        edges = sorted(set(tuple(sorted(e)) for e in edges))
        actual = fixed_orbit_faces(n,edges)
        target = whiskered_matching_faces(n,edges)
        assert actual == target
        pm = len(base_perfect_matchings(n,edges))
        assert len(verify_matching_acyclic(n,edges,target)) == 2
        chi = -sum((-1)**len(f) for f in target)
        expected = 0 if not pm else pm*(-1)**(n//2-1)
        assert chi == expected, (n,edges,chi,expected)
        big_checks += 1
        checks += 1
    print(f'PASS: {checks} base graphs; {big_checks} acyclic full matching certificates')
    print('Checks: prism facets; invariant faces; orbit-sunlet isomorphism;')
    print('        acyclic pivot matching; perfect-matching Euler formula.')

if __name__ == '__main__':
    run()
