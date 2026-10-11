"""Exact finite checks for the odd-girth Minkowski-asymmetry formula.

The theorem for arbitrarily large finite graphs relies on the proof, not
on these finite computations. Run with Python 3 (standard library only).
"""
from fractions import Fraction
from itertools import combinations
from random import Random


def chordless_cycles(n, edges):
    lookup = {tuple(sorted(e)): i for i, e in enumerate(edges)}
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    result = set()

    def dfs(start, path, seen):
        u = path[-1]
        for v in adj[u]:
            if v == start:
                if len(path) < 3 or path[1] > path[-1]:
                    continue
                k = len(path)
                if any((path[i], path[j]) in lookup or (path[j], path[i]) in lookup
                       for i in range(k) for j in range(i+1, k)
                       if j != i+1 and not (i == 0 and j == k-1)):
                    continue
                eids = tuple(sorted(lookup[tuple(sorted((path[i],path[(i+1)%k])))]
                                    for i in range(k)))
                result.add(eids)
            elif v > start and v not in seen:
                dfs(start, path + [v], seen | {v})

    for v in range(n):
        dfs(v, [v], {v})
    return sorted(result, key=lambda c: (len(c),c))


def cut_vectors(n, edges):
    # Vertex zero is fixed outside the chosen shore.
    return [tuple(((mask >> (u-1)) & 1 if u else 0) ^
                  ((mask >> (v-1)) & 1 if v else 0)
                  for u,v in edges) for mask in range(1<<(n-1))]


def test_graph(n, edges):
    m = len(edges)
    if m == 0:
        return (0, 0, 0, 0)
    cycles = chordless_cycles(n, edges)
    odd_lengths = [len(c) for c in cycles if len(c)%2]
    g = min(odd_lengths,default=None)
    want = Fraction(g,g-2) if g else Fraction(1)
    cuts = cut_vectors(n,edges)
    facets = []
    for e in range(m):
        row = [0]*m
        row[e] = 1
        facets.append((tuple(row),1))
        row[e] = -1
        facets.append((tuple(row),0))
    for cyc in cycles:
        k = len(cyc)
        for bits in range(1<<k):
            if bits.bit_count()%2 == 0:
                continue
            row = [0]*m
            for j,e in enumerate(cyc):
                row[e] = 1 if (bits >> j)&1 else -1
            facets.append((tuple(row), bits.bit_count()-1))
    maximum = Fraction(1)
    checked = 0
    for a,b in facets:
        vals = [sum(a[e]*cut[e] for e in range(m)) for cut in cuts]
        hi,lo = max(vals),min(vals)
        assert hi <= b, (n,edges,a,b,hi)
        assert hi == b, (n,edges,a,b,hi)
        summ = sum(a)
        den = 2*b-summ
        assert den > 0
        s = Fraction(summ-2*lo,den)
        maximum = max(maximum,s)
        p,q = want.numerator,want.denominator
        # Exact reflected-corner inequalities: c-(cut-c)/s remains in P.
        for val in vals:
            assert (p+q)*summ-2*q*val <= 2*p*b, (n,edges,a,b,val,want)
            checked += 1
    assert maximum == want, (n,edges,maximum,want)
    return (1, len(cuts),len(facets), checked)


def cycle(n):
    return [tuple(sorted((j,(j+1)%n))) for j in range(n)]


def wheel(n):
    # n rim vertices plus one hub.
    return cycle(n) + [(i,n) for i in range(n)]


def complete_bipartite(p,q):
    return [(i,p+j) for i in range(p) for j in range(q)]


def main():
    counts = [0,0,0,0]
    def add(n,edges):
        val=test_graph(n,edges)
        for j in range(4):counts[j]+=val[j]
    for n in range(2,6):
        pairs=list(combinations(range(n),2))
        for mask in range(1,1<<len(pairs)):
            if n==5 and mask==(1<<10)-1:  # K5 is outside the theorem.
                continue
            add(n,[pair for j,pair in enumerate(pairs) if (mask>>j)&1])
    rng=Random(271828)
    pairs=list(combinations(range(6),2))
    for _ in range(180):
        m=rng.randrange(1,10)  # fewer than 10 edges excludes a K5 minor
        add(6,sorted(rng.sample(pairs,m)))
    for n in (5,6,7,8,9,10,11):
        add(n,cycle(n))
    for n in (4,5,6,7):
        add(n+1,wheel(n))
    for p,q in ((2,3),(2,5),(3,3)):
        add(p+q,complete_bipartite(p,q))
    # Graphs with separated components also lie in the covered class.
    add(9,cycle(3)+[(u+3,v+3) for u,v in cycle(5)]+[(8,0)])
    print('EXACT_CHECKS_OK graphs=%d cut_vectors=%d facet_rows=%d reflected_inequalities=%d' %tuple(counts))

if __name__ == '__main__':
    main()
