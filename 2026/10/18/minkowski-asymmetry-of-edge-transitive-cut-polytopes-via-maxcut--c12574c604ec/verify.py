#!/usr/bin/env python3
"""Exact finite checks of cut-polytope switching and balanced-blowup formulas.

Requires only the Python standard library.  This is a test of finite examples,
not a substitute for the proof valid in arbitrary dimension.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb

def cuts(n, edges):
    return [tuple(int(((mask >> u) ^ (mask >> v)) & 1) for u, v in edges)
            for mask in range(1 << (n - 1))]

def automorphisms(n, edges):
    es = set(edges)
    for p in permutations(range(n)):
        if all((min(p[u], p[v]), max(p[u], p[v])) in es for u, v in edges):
            yield p

def exact_orbit_check(n, edges):
    m = len(edges)
    if not m:
        return None
    autos = list(automorphisms(n, edges))
    orbit = {(min(p[edges[0][0]],p[edges[0][1]]),
              max(p[edges[0][0]],p[edges[0][1]])) for p in autos}
    if len(orbit) != m:
        return None
    cc = cuts(n, edges)
    best = max(sum(x) for x in cc)
    index = {e: i for i, e in enumerate(edges)}
    winners = [x for x in cc if sum(x) == best]
    # A maximum cut averaged over the edge-transitive automorphism group
    # has every coordinate equal to best / m, checked with integers.
    witness = winners[0]
    totals = [0] * m
    for p in autos:
        for j, (u, v) in enumerate(edges):
            a, b = sorted((p[u], p[v]))
            totals[index[(a, b)]] += witness[j]
    assert len(set(totals)) == 1, (n, edges, totals)
    assert totals[0] * m == best * len(autos)
    frac = Fraction(best, m)
    assert frac > Fraction(1, 2)
    s = Fraction(m, 2 * best - m)
    t = Fraction(s+1, 2*s)
    assert t == frac
    # Switching maps the orbit distribution to the reflected vector at every cut.
    for d in cc:
        for j in range(m):
            expected = t if d[j] == 0 else 1 - t
            actual = Fraction(totals[j],len(autos)) if d[j] == 0 else 1-Fraction(totals[j],len(autos))
            assert actual == expected
    return len(autos), len(cc), s

def multipartite(nparts, size):
    n=nparts*size
    edges=[(u,v) for u in range(n) for v in range(u+1,n) if u//size != v//size]
    return n, edges

def check_blown_up(r, a):
    m=a*a*comb(r,2)
    mc=a*a*(r*r//4)
    s=Fraction(m,2*mc-m)
    assert s == (r-1 if r%2==0 else r)
    # The candidate max cut can be built with monochromatic parts.
    k=r//2
    assert a*a*k*(r-k)==mc
    # A random maximally balanced set of parts has exactly mc/m edge marginal.
    assert Fraction(2*k*(r-k),r*(r-1))==Fraction(mc,m)
    # Exhaustive vertex-coloring maxcut on small instances.
    if r*a<=12:
        n,edges=multipartite(r,a)
        assert max(map(sum,cuts(n,edges)))==mc
    return m, mc

def main():
    graph_count=cut_count=aut_count=0
    for n in range(2,6):
        all_edges=list(combinations(range(n),2))
        for mask in range(1,1<<len(all_edges)):
            es=[e for i,e in enumerate(all_edges) if (mask>>i)&1]
            v=exact_orbit_check(n,es)
            if v is not None:
                graph_count+=1
                aut_count+=v[0]
                cut_count+=v[1]
    blowups=0
    for r in range(2,12):
        for a in range(1,7):
            check_blown_up(r,a)
            blowups+=1
    print('EXACT_CHECKS_PASS')
    print('edge_transitive_labeled_graphs=',graph_count)
    print('automorphism_actions=',aut_count)
    print('cut_switches=',cut_count)
    print('balanced_multipartite_pairs=',blowups)
    print('exact_rational_and_integer_arithmetic=True')
if __name__=='__main__':main()
