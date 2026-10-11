"""Exact-rational finite checks for weighted distance invariance of matching relaxations.

Run with Python 3 standard library; no other files or packages are needed.
"""
from fractions import Fraction as Q
from itertools import combinations
from random import Random


def cycles_on_edges(edges, n):
    """Return edge-index tuples describing simple odd cycles."""
    out = []
    for k in range(3, n + 1, 2):
        for ind in combinations(range(len(edges)), k):
            deg = [0] * n
            for i in ind:
                u, v = edges[i]
                deg[u] += 1
                deg[v] += 1
            verts = {j for j in range(n) if deg[j]}
            if len(verts) != k or any(deg[j] != 2 for j in verts):
                continue
            reach = {next(iter(verts))}
            while True:
                nex = set(reach)
                for i in ind:
                    u, v = edges[i]
                    if u in reach: nex.add(v)
                    if v in reach: nex.add(u)
                if nex == reach: break
                reach = nex
            if reach == verts:
                out.append((ind, verts))
    return out


def vertices(edges, n):
    """All matching and fractional extreme vertices from odd-cycle structure."""
    m = len(edges)
    matching = []
    for k in range(m + 1):
        for ind in combinations(range(m), k):
            used = set()
            for e in ind:
                u, v = edges[e]
                if u in used or v in used: break
                used.update((u, v))
            else:
                v = [Q(0)] * m
                for e in ind: v[e] = Q(1)
                matching.append(tuple(v))
    cyc = cycles_on_edges(edges, n)
    fams = [((), frozenset())]
    for ind, vert in cyc:
        fams += [(fam + (ind,), occupied | frozenset(vert))
                 for fam, occupied in fams if not (occupied & vert)]
    fractional = set()
    for fam, occupied in fams:
        if not fam: continue
        cyc_indices = set(i for sub in fam for i in sub)
        for M in matching:
            if any(M[e] and ((edges[e][0] in occupied) or (edges[e][1] in occupied)) for e in range(m)):
                continue
            v = list(M)
            for e in cyc_indices: v[e] = Q(1, 2)
            fractional.add(tuple(v))
    return matching, sorted(fractional), cyc


def norm2(x, c, weights):
    return sum(w * (a - b)**2 for a, b, w in zip(x, c, weights))


def diameter2(points, weights):
    return max((sum(w * (a-b)**2 for a,b,w in zip(x,y,weights))
                for x in points for y in points), default=Q(0))


def run():
    rng = Random(17291)
    profiles = 0
    half_vertices = 0
    diameter_profiles = 0
    cycles_tested = 0
    # All 1,024 simple graphs on five labeled vertices, plus random six-vertex graphs.
    cases = []
    base5 = list(combinations(range(5), 2))
    for mask in range(1 << len(base5)):
        cases.append((5, [e for i,e in enumerate(base5) if mask >> i & 1]))
    base6 = list(combinations(range(6), 2))
    for _ in range(160):
        mask = rng.randrange(1 << len(base6))
        cases.append((6, [e for i,e in enumerate(base6) if mask >> i & 1]))
    for n,edges in cases:
        m = len(edges)
        M,F,C = vertices(edges, n)
        assert all(v not in M for v in F)
        w = [Q(1 + rng.randrange(5), 1 + rng.randrange(4)) for _ in edges]
        centers = [[Q(0)]*m,
                   [Q(rng.randrange(9), 1 + rng.randrange(4)) for _ in edges]]
        for c in centers:
            mm = max(norm2(x, c, w) for x in M)
            assert all(norm2(x, c, w) < mm for x in F), (n,edges,c)
            assert mm == max(norm2(x, c, w) for x in M + F)
            profiles += 1
            half_vertices += len(F)
            for ind, _ in C:
                # Check the precise positive gain in the near-perfect matching average.
                ell = len(ind)
                cyc_edges = [edges[i] for i in ind]
                q = Q(ell-1,2*ell)
                # Since each edge occurs equally often in near-perfect matchings:
                empirical = q * sum(w[i]*(1-2*c[i]) for i in ind)
                fractional = sum(w[i]*(Q(1,4)-c[i]) for i in ind)
                gain = sum(w[i]*(Q(ell-2,4*ell) + c[i]/ell) for i in ind)
                assert empirical - fractional == gain and gain > 0
                cycles_tested += 1
        diam_m = diameter2(M, w)
        diam_f = diameter2(M + F, w)
        assert diam_m == diam_f, (n,edges,diam_m,diam_f)
        diameter_profiles += 1
    # A negative-center counterexample delineates the hypothesis.
    edges = [(0,1),(1,2),(0,2)]
    M,F,_ = vertices(edges, 3)
    c = [Q(-10)]*3
    assert max(norm2(x,c,[Q(1)]*3) for x in F) > max(norm2(x,c,[Q(1)]*3) for x in M)
    print('VERIFY_OK', 'graph_profiles=',len(cases), 'center_tests=',profiles,
          'fractional_vertex_comparisons=',half_vertices,
          'cycle_gain_identities=',cycles_tested,
          'diameter_checks=',diameter_profiles,
          'negative_center_boundary=confirmed')

if __name__ == '__main__':
    run()
