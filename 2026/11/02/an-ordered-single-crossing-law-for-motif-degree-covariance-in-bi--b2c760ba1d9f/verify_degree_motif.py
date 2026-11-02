#!/usr/bin/env python3
"""Independent finite-graph checks of a degree/motif covariance identity.

Run: python3 verify_degree_motif.py
Uses only the Python standard library. Graph enumeration is exhaustive only for n<=6.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial

MOTIFS = {
    'edge': (2, [(0, 1)]),
    'path3': (3, [(0, 1), (1, 2)]),
    'triangle': (3, [(0, 1), (0, 2), (1, 2)]),
    'two_edges': (4, [(0, 1), (2, 3)]),
    'path4': (4, [(0, 1), (1, 2), (2, 3)]),
    'star4': (4, [(0, 1), (0, 2), (0, 3)]),
    'cycle4': (4, [(0, 1), (1, 2), (2, 3), (3, 0)]),
    'clique4': (4, list(combinations(range(4), 2))),
}

def fall(a, r):
    z = 1
    for i in range(r):
        z *= a - i
    return z if 0 <= r <= a else 0

def motif_masks(n, h, hedges, positions):
    masks = set()
    for vertices in permutations(range(n), h):
        bits = 0
        for x, y in hedges:
            a, b = sorted((vertices[x], vertices[y]))
            bits |= 1 << positions[(a, b)]
        masks.add(bits)
    return tuple(masks)

def formula(n, hedges, num_copies, k, p):
    q = 1 - p
    h = max(max(edge) for edge in hedges) + 1
    deg = [0] * h
    for a,b in hedges:
        deg[a] += 1
        deg[b] += 1
    pk = Fraction(comb(n - 1, k)) * p**k * q**(n-1-k)
    f = -h + sum(Fraction(fall(k, d), fall(n-1, d)) / p**d for d in deg)
    return num_copies * p**len(hedges) * pk * f

def run():
    checked = 0
    for n in range(3, 7):
        pairs = tuple(combinations(range(n), 2))
        positions = {edge: i for i, edge in enumerate(pairs)}
        m = len(pairs)
        avail = {name: (h, hedges, motif_masks(n, h, hedges, positions))
                 for name, (h, hedges) in MOTIFS.items() if h <= n}
        # For every graph, accumulate exact integer polynomial coefficients
        # of the degree-k count, motif count and their product, indexed by edges.
        tables = {name: [[0] * (m + 1) for _ in range(3 * n)] for name in avail}
        for graph in range(1 << m):
            e = graph.bit_count()
            degree = [0] * n
            for idx, (u, v) in enumerate(pairs):
                if (graph >> idx) & 1:
                    degree[u] += 1
                    degree[v] += 1
            ds = [degree.count(k) for k in range(n)]
            for name, (_, _, copies) in avail.items():
                x = sum(graph & c == c for c in copies)
                tbl = tables[name]
                tbl[2*n][e] += x
                for k in range(n):
                    tbl[k][e] += ds[k]
                    tbl[n+k][e] += ds[k]*x
        for p in (Fraction(1, 5), Fraction(2, 5), Fraction(3, 5)):
            a, b = p.numerator, p.denominator
            weights = [a**j * (b-a)**(m-j) for j in range(m+1)]
            total = b**m
            for name, (_, hedges, copies) in avail.items():
                tbl = tables[name]
                ex = Fraction(sum(z*w for z,w in zip(tbl[2*n],weights)), total)
                for k in range(n):
                    ed = Fraction(sum(z*w for z,w in zip(tbl[k],weights)), total)
                    edx = Fraction(sum(z*w for z,w in zip(tbl[n+k],weights)), total)
                    observed = edx - ed*ex
                    expected = formula(n,hedges,len(copies),k,p)
                    assert observed == expected, (n,name,k,p,observed,expected)
                    checked += 1
        print(f'n={n}: checked {len(avail)} motifs, all degrees, three probabilities')
    # Strict ordering of critical values for all example motifs.
    for n in range(4,30):
        for h,edges in MOTIFS.values():
            if h>n: continue
            deg=[0]*h
            for u,v in edges: deg[u]+=1;deg[v]+=1
            delta=min(deg)
            def f(k,p):
                return -h + sum(Fraction(fall(k,d),fall(n-1,d))/p**d for d in deg)
            roots=[]
            for k in range(delta,n-1):
                lo=1e-12;hi=1.
                for _ in range(90):
                    mid=(lo+hi)/2
                    if float(f(k, Fraction(mid)))>0:lo=mid
                    else:hi=mid
                root=(lo+hi)/2
                assert (not roots or roots[-1]<root), (n,h,edges,k,roots,root)
                roots.append(root)
                checked+=1
    print(f'PASS: {checked} exact-enumeration and threshold-order checks')

if __name__ == '__main__':
    run()
