#!/usr/bin/env python3
"""Finite structural and homology checks for affine-plane incidence class deletion.

Pure Python 3; no network or third-party packages. Proof for arbitrary orders is
mathematical and does not depend on these sample calculations.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb


def affine_incidence_without_class(q):
    """Desarguesian affine plane over the prime field F_q, deleting slope -1."""
    assert q in (3, 5), 'The finite checks use prime fields of orders 3 and 5.'
    n = 2 * q * q
    P = list(range(q*q))
    L = list(range(q*q, n))
    adj = [set() for _ in range(n)]
    for x in range(q):
        for y in range(q):
            p = x*q+y
            for d in range(q):
                c = x if d == 0 else (y - (d-1)*x) % q
                ell = q*q + d*q + c
                adj[p].add(ell)
                adj[ell].add(p)
    return P, L, adj


def distances(adj):
    all_dist = []
    for v in range(len(adj)):
        dist = [-1] * len(adj)
        dist[v] = 0
        dq = deque([v])
        while dq:
            x = dq.popleft()
            for w in adj[x]:
                if dist[w] == -1:
                    dist[w] = dist[x]+1
                    dq.append(w)
        assert all(x >= 0 for x in dist)
        all_dist.append(dist)
    return all_dist


def faces_of_threshold(dists, r):
    n = len(dists)
    bysize = [[] for _ in range(n+1)]
    def visit(prefix, candidates):
        if prefix:
            bysize[len(prefix)].append(prefix)
        for j, v in enumerate(candidates):
            nxt = [w for w in candidates[j+1:] if dists[v][w] <= r]
            visit(prefix+(v,), nxt)
    visit((), list(range(n)))
    return [xs for xs in bysize[1:] if xs]


def mod2_boundary_rank(lower, upper):
    ind = {face: i for i, face in enumerate(lower)}
    pivot = {}
    for face in upper:
        col = 0
        for i in range(len(face)):
            col ^= 1 << ind[face[:i]+face[i+1:]]
        while col:
            high = col.bit_length()-1
            if high in pivot:
                col ^= pivot[high]
            else:
                pivot[high] = col
                break
    return len(pivot)


def check(q):
    P, L, adj = affine_incidence_without_class(q)
    n = 2*q*q
    assert len(P) == len(L) == q*q
    assert sum(map(len, adj))//2 == q**3
    assert all(len(vs) == q for vs in adj)
    D = distances(adj)
    assert max(map(max, D)) == 4
    # The missing distance-three graph consists of disjoint q-cliques
    # on point classes of deleted slope -1 and line parallel classes.
    point_classes = [[x*q+y for x in range(q) for y in range(q)
                      if (y + x) % q == c] for c in range(q)]
    line_classes = [[q*q + d*q+c for c in range(q)] for d in range(q)]
    C = point_classes + line_classes
    assert len(C) == 2*q and all(len(z) == q for z in C)
    mark = [None]*n
    for i,cl in enumerate(C):
        for v in cl:
            assert mark[v] is None
            mark[v] = i
    assert None not in mark
    distcounts = Counter()
    for a in range(n):
        for b in range(a+1, n):
            t = D[a][b]
            distcounts[t] += 1
            if a in P and b in L:
                assert t == (1 if b in adj[a] else 3)
            elif a in L and b in L:
                assert t == (4 if mark[a] == mark[b] else 2)
            elif a in P and b in P:
                assert t == (4 if mark[a] == mark[b] else 2)
            assert (t == 4) == (mark[a] == mark[b])
    assert distcounts[4] == q*q*(q-1)
    # Rips at scale two has only two types of facets:
    # one-side multipartite cliques, or one apex plus its neighbors.
    if q == 3:
        F2 = faces_of_threshold(D, 2)
        F3 = faces_of_threshold(D, 3)
        assert [len(xs) for xs in F2] == [18, 81, 108, 18]
        assert [len(xs) for xs in F3] == [18, 135, 540, 1215, 1458, 729]
        set2 = set(face for group in F2 for face in group)
        X = set()
        Y = set()
        for face in set2:
            pt = [v for v in face if v in P]
            ln = [v for v in face if v in L]
            if not ln or (len(ln) == 1 and all(ln[0] in adj[v] for v in pt)):
                X.add(face)
            if not pt or (len(pt) == 1 and all(pt[0] in adj[v] for v in ln)):
                Y.add(face)
        common = {(v,) for v in range(n)} | {
            (p, ell) for p in P for ell in adj[p]}
        assert X | Y == set2
        assert X & Y == common
        beta = []
        for faces, expected in [(F2, [1, 0, 26, 0]),
                                (F3, [1, 0, 0, 0, 0, 64])]:
            ranks = [mod2_boundary_rank(faces[d-1], faces[d])
                     for d in range(1, len(faces))]
            bettis = [len(faces[d])-(ranks[d-1] if d else 0)-
                      (ranks[d] if d < len(ranks) else 0)
                      for d in range(len(faces))]
            assert bettis == expected
            beta.append((ranks, bettis))
        print('q=3 verified: Pappus 18 vertices, 27 incidence edges, diameter=4;')
        print('  distance counts:', dict(sorted(distcounts.items())))
        print('  Rips2 f-vector [18,81,108,18], mod2 ranks', beta[0][0],
              'Betti', beta[0][1])
        print('  exact two-subcomplex cover: intersection is the 18-vertex incidence graph')
        print('  Rips3 f-vector [18,135,540,1215,1458,729], mod2 ranks',
              beta[1][0], 'Betti', beta[1][1])
    else:
        # No exponential face enumeration at q=5. Check metric partition
        # and exact pairwise adjacency conditions, not large homology.
        print('q=5 verified: 50 vertices, 125 incidence edges, diameter=4;')
        print('  distance counts:', dict(sorted(distcounts.items())))
        print('  10 disjoint forbidden five-cliques at Rips scale three')
    b = q**3-2*q*q+1
    assert b > 0
    print('  formula: beta1(Rips1)=', b,
          'beta2(Rips2)=', b if q > 3 else b+2*(q-1)**q,
          'high(Rips2)=', 2*(q-1)**q if q > 3 else 'merged degree 2',
          'beta_{2q-1}(Rips3)=', (q-1)**(2*q))

if __name__ == '__main__':
    check(3)
    check(5)
    print('VERIFY_OK')
