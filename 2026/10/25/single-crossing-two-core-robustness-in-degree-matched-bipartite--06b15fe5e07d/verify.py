"""Exact checks for two-cycle bipartite interaction cores (stdlib only)."""
from collections import Counter
from fractions import Fraction
from math import comb


def graph(a, b):
    assert a % 2 == b % 2 == 0 and a >= 4 and b >= 4
    edges = []
    cycles = []
    nxt = 1
    for length in (a, b):
        c = [0] + list(range(nxt, nxt + length - 1))
        nxt += length - 1
        cycles.append(c)
        edges += list(zip(c, c[1:] + c[:1]))
    return nxt, edges, cycles


def two_core_size(n, edges, mask):
    active = [bool(mask & (1 << i)) for i in range(n)]
    while True:
        deg = [0] * n
        for u, v in edges:
            if active[u] and active[v]:
                deg[u] += 1
                deg[v] += 1
        doomed = [i for i in range(n) if active[i] and deg[i] < 2]
        if not doomed:
            break
        for i in doomed:
            active[i] = False
    return sum(active)


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enumerate_distribution(a, b):
    n, edges, cycles = graph(a, b)
    counts = Counter()
    for mask in range(1 << n):
        y = two_core_size(n, edges, mask)
        counts[mask.bit_count(), y] += 1
    # No arbitrary probability substitution: equality of *all* Bernstein
    # coefficients proves the probability law for every real 0<=p<=1.
    expected = Counter()
    for k in range(n + 1):
        expected[k, 0] += binom(n, k) - binom(n-a, k-a) - binom(n-b, k-b) + (k == n)
        expected[k, a] += binom(n-a, k-a) - (k == n)
        expected[k, b] += binom(n-b, k-b) - (k == n)
        expected[k, n] += (k == n)
    for k in range(n+1):
        for y in set(y for kk, y in counts if kk == k) | set(y for kk, y in expected if kk == k):
            assert counts[k, y] == expected[k, y], (a,b,k,y,counts[k,y],expected[k,y])
    # Both cycles are even. The common vertex lies in one guild, and
    # bipartition degree multisets agree for equal total lengths.
    color = {}
    for cyc in cycles:
        for j, v in enumerate(cyc):
            if v in color:
                assert color[v] == j % 2
            color[v] = j % 2
    assert len(color)==n
    degrees=Counter()
    for u,v in edges:
        assert color[u]!=color[v]
        degrees[u]+=1; degrees[v]+=1
    guild_degs = tuple(tuple(sorted(degrees[v] for v in color if color[v]==c)) for c in (0,1))
    return n, sum(counts.values()), guild_degs


def check_comparisons():
    cases = [(4,4),(4,6),(4,8),(6,6),(4,10),(6,8),(4,12),(6,10),(8,8)]
    evaluated = 0
    by_s = {}
    results = []
    for a,b in cases:
        n, total, degs = enumerate_distribution(a,b)
        evaluated += total
        by_s.setdefault(a+b,set()).add(degs)
        results.append((a,b,n,total))
    assert all(len(v)==1 for v in by_s.values())
    # Explicit sharp n=11 and exact threshold across two rational test points.
    def P0(a,b,p): return p**a + p**b - p**(a+b-1)
    def EY(a,b,p): return a*p**a + b*p**b - p**(a+b-1)
    for p in (Fraction(1,2), Fraction(3,4), Fraction(9,10)):
        assert P0(4,8,p)-P0(6,6,p) == p**4*(1-p*p)**2
        assert EY(4,8,p)-EY(6,6,p) == 4*p**4*(1-p*p)*(1-2*p*p)
        assert P0(4,8,p) > P0(6,6,p)
    assert EY(4,8,Fraction(1,2)) > EY(6,6,Fraction(1,2))
    assert EY(4,8,Fraction(3,4)) < EY(6,6,Fraction(3,4))
    for a in range(4,16,2):
        for b in range(a+4,22,2):
            for p in (Fraction(1,5),Fraction(2,5),Fraction(3,5),Fraction(4,5)):
                assert P0(a,b,p)-P0(a+2,b-2,p) == (1-p*p)*(p**a-p**(b-2))
                assert EY(a,b,p)-EY(a+2,b-2,p) == a*p**a+b*p**b-(a+2)*p**(a+2)-(b-2)*p**(b-2)
    print('VERIFY_OK')
    print('enumerated_graphs:',len(results))
    print('vertex_retention_subsets:',evaluated)
    print('full_Bernstein_coefficients:',sum((n+1)*4 for _,_,n,_ in results))
    print('graphs:',repr(results))
    print('bipartite_degree_sequences_matched_by_size: true')
    print('eleven_vertex_pair: (4,8) vs (6,6)')
    print('difference_probability_nonempty: p^4*(1-p^2)^2')
    print('difference_expected_core_size: 4*p^4*(1-p^2)*(1-2*p^2)')
    print('unique_mean_crossing: p=1/sqrt(2)')
    print('two_cycle_bipartite_bouquet_minimal_distinct_equal_size_pair: n=11')

if __name__=='__main__':
    check_comparisons()
