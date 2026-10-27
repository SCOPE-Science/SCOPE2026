#!/usr/bin/env python3
"""Exhaustive small-graph check of an independence-profile / two-type separation theorem.
Only Python 3 standard library is required.
"""
from itertools import combinations, permutations, product
from collections import defaultdict


def all_edges(n):
    return tuple(combinations(range(n), 2))


def triangle_free(n, edges):
    E = set(edges)
    return all(not all(tuple(sorted(e)) in E for e in combinations(t, 2))
               for t in combinations(range(n), 3))


def connected(n, edges):
    if n <= 1:
        return True
    neighbors = [[] for _ in range(n)]
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)
    seen = {0}
    todo = [0]
    while todo:
        for b in neighbors[todo.pop()]:
            if b not in seen:
                seen.add(b)
                todo.append(b)
    return len(seen) == n


def independence_polynomial(n, edges):
    masks = [(1 << a) | (1 << b) for a, b in edges]
    coeff = [0] * (n+1)
    for S in range(1 << n):
        if all(S & m != m for m in masks):
            coeff[S.bit_count()] += 1
    return tuple(coeff)


def disjoint_independent_pairs(n, edges):
    # Colours 0,1,2 mean membership in neither/S/T respectively.
    # Only monochromatic 1--1 and 2--2 edges are forbidden.
    ans = 0
    for colours in product(range(3), repeat=n):
        if all(not (colours[a] == colours[b] in (1, 2)) for a, b in edges):
            ans += 1
    return ans


def canonical_code(n, edges):
    # Completeness: all n! vertex permutations, all binom(n,2) pairs.
    E = set(edges)
    pairs = all_edges(n)
    return min(tuple(int(tuple(sorted((p[i], p[j]))) in E) for i, j in pairs)
               for p in permutations(range(n)))


def census(n):
    by_iso = {}
    for flags in product((0, 1), repeat=len(all_edges(n))):
        E = tuple(e for e, flag in zip(all_edges(n), flags) if flag)
        if not triangle_free(n, E):
            continue
        key = canonical_code(n, E)
        if key not in by_iso:
            by_iso[key] = E
    return tuple(by_iso.values())


def isomorphic(n, G, H):
    return canonical_code(n, G) == canonical_code(n, H)


def main():
    for n in range(1, 6):
        gs = census(n)
        seen = defaultdict(list)
        seen_connected = defaultdict(list)
        for G in gs:
            p = independence_polynomial(n, G)
            t = disjoint_independent_pairs(n, G)
            seen[p].append((G, t))
            if connected(n, G):
                seen_connected[p].append((G, t))
        collisions = [v for v in seen.values() if len(v)>1]
        connected_collisions = [v for v in seen_connected.values() if len(v)>1]
        print('n=%d triangle_free_iso=%d polynomial_collision_classes=%d connected_collision_classes=%d'
              % (n,len(gs),len(collisions),len(connected_collisions)))
        if n < 5:
            assert not collisions
        if n == 5:
            assert len(gs) == 14
            assert len(collisions) == 1 and len(collisions[0]) == 2
            assert not connected_collisions
            assert {x[1] for x in collisions[0]} == {103, 105}
            assert all(independence_polynomial(n, G)[:4] == (1,5,6,2)
                       for G, _ in collisions[0])
    G5a=((0,1),(1,2),(2,3),(0,3)) # C4 plus isolated 4
    G5b=((0,1),(0,2),(0,3),(3,4)) # 5-vertex fork tree
    G6a=((0,4),(0,5),(1,3),(1,4),(2,3),(2,4)) # C4 with a 2-edge tail
    G6b=((0,1),(0,4),(1,2),(1,5),(2,3),(3,4)) # C5 with a leaf
    for n,G,H,p,phi_g,phi_h in [
        (5,G5a,G5b,(1,5,6,2,0,0),105,103),
        (6,G6a,G6b,(1,6,9,3,0,0,0),209,203)]:
        assert triangle_free(n,G) and triangle_free(n,H)
        assert not isomorphic(n,G,H)
        assert independence_polynomial(n,G)==p==independence_polynomial(n,H)
        assert disjoint_independent_pairs(n,G)==phi_g
        assert disjoint_independent_pairs(n,H)==phi_h
        assert sorted(sum(v in e for e in G) for v in range(n)) == \
               sorted(sum(v in e for e in H) for v in range(n)) if n==6 else True
        if n==6:
            assert connected(n,G) and connected(n,H)
        count=sum(p)
        print('witness n=%d I(1)=%d nonedge_types=%d edge_types=%d,%d all_types=%d,%d'
              %(n,count,count*count,phi_g,phi_h,count*count+phi_g,count*count+phi_h))
    print('ALL_CHECKS_PASS')

if __name__=='__main__':
    main()
