"""Independent finite checks for graph-metric Rips complexes of affine incidence planes.

Run: python verify_affine_rips.py
No third-party packages required. Matrix ranks are exact over GF(2).
"""
from collections import defaultdict, deque
from itertools import combinations
from math import comb


def graph(q):
    assert q in (2, 3), 'Exact enumeration uses the prime affine planes of orders 2 and 3.'
    points = [(x, y) for x in range(q) for y in range(q)]
    lines = [(slope, intercept) for slope in range(q) for intercept in range(q)]
    lines += [(None, intercept) for intercept in range(q)]
    np = len(points)
    n = np + len(lines)
    edges = set()
    for i, (x, y) in enumerate(points):
        for j, (m, b) in enumerate(lines):
            if (x == b if m is None else (y - m * x - b) % q == 0):
                edges.add(tuple(sorted((i, np+j))))
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    dist = []
    for root in range(n):
        d = [-1]*n
        d[root] = 0
        todo = deque([root])
        while todo:
            a = todo.popleft()
            for b in adj[a]:
                if d[b] < 0:
                    d[b] = d[a] + 1
                    todo.append(b)
        assert all(z >= 0 for z in d)
        dist.append(d)
    return points, lines, adj, dist


def all_cliques(dist, scale):
    N = len(dist)
    cs = defaultdict(list)
    def extend(prefix, candidates):
        for i, v in enumerate(candidates):
            seq = prefix + (v,)
            cs[len(seq)-1].append(seq)
            extend(seq, [w for w in candidates[i+1:] if dist[v][w] <= scale])
    extend((), list(range(N)))
    return cs


def rank_mod2(columns):
    pivots = {}
    for x in columns:
        while x:
            p = x.bit_length()-1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


def betti_by_rank(faces):
    maxd = max(faces)
    boundary_rank = {}
    for d in range(1, maxd+1):
        lower_index = {face:i for i, face in enumerate(faces[d-1])}
        cols = []
        for sigma in faces[d]:
            col = 0
            for tau in combinations(sigma, d):
                col ^= 1 << lower_index[tau]
            cols.append(col)
        boundary_rank[d] = rank_mod2(cols)
    betti = {}
    for d in range(maxd+1):
        betti[d] = len(faces[d])-boundary_rank.get(d,0)-boundary_rank.get(d+1,0)
    betti[0] -= 1
    return {d:r for d,r in betti.items() if r}, boundary_rank


def main():
    for q in (2, 3):
        P, L, adj, dist = graph(q)
        v = len(P)+len(L)
        assert v == q*q + q*(q+1)
        assert sum(len(a) for a in adj)//2 == q*q*(q+1)
        assert max(max(x) for x in dist) == 4
        assert all(d == 2 for i in range(len(P)) for j in range(i+1,len(P)) for d in [dist[i][j]])
        assert all((dist[len(P)+i][len(P)+j]==4) == (L[i][0]==L[j][0])
                   for i in range(len(L)) for j in range(i+1,len(L)))
        for k, expected in [(1,{1:(q-1)**2*(q+1)}),
                            (2, {2:(q-1)**2*(q+1)} if q!=2 else {2:4})]:
            ff = all_cliques(dist,k)
            betti, rr = betti_by_rank(ff)
            if k==2 and q>=3:
                expected={2:(q-1)**2*(q+1), q:(q-1)**(q+1)}
            assert betti == expected, (q,k,betti,expected)
            print(f'order={q} scale={k} vertices={v} fvector={tuple(len(ff[i]) for i in range(max(ff)+1))} ranks={tuple(rr.get(i,0) for i in range(1,max(ff)+1))} reduced_betti={betti}')
        assert all(dist[0][j] <= 3 for j in range(v))  # point vertex is a cone apex at scale 3
        assert all(dist[i][j] <= 4 for i in range(v) for j in range(v))
        print(f'checked_order_{q}: PASS; scale3 cone apex verified; scale4 simplex verified')
    print('VERIFY_OK affine_incidence_rips q=2,3 exact_GF2_scales=1,2; scales=3,4 cones')


if __name__=='__main__':
    main()
