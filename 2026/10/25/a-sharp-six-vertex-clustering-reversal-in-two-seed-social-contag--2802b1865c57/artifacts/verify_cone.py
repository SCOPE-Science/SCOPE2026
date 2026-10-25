#!/usr/bin/env python3
"""Exact finite checks for two-seed threshold-two contagion on cone networks.
No third-party packages; all graph and seed cases enumerated directly.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb


def graph(n, edges):
    adj = [0] * n
    for u, v in edges:
        assert 0 <= u < v < n
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj


def from_mask(n, mask):
    return graph(n, [e for k, e in enumerate(combinations(range(n), 2)) if (mask >> k) & 1])


def cascade(adj, seed):
    n = len(adj)
    active = sum(1 << i for i in seed)
    while True:
        new = active
        for v in range(n):
            if not (active >> v) & 1 and (adj[v] & active).bit_count() >= 2:
                new |= 1 << v
        if new == active:
            return active
        active = new


def distribution(adj):
    n = len(adj)
    return Counter(cascade(adj, pair).bit_count() for pair in combinations(range(n), 2))


def mean_from_dist(d):
    return Fraction(sum(s * m for s, m in d.items()), sum(d.values()))


def component_sizes(adj):
    n = len(adj)
    visited = 0
    sizes = []
    for root in range(n):
        if (visited >> root) & 1: continue
        current = 1 << root
        while True:
            enlarged = current
            for v in range(n):
                if (current >> v) & 1: enlarged |= adj[v]
            if enlarged == current: break
            current = enlarged
        visited |= current
        sizes.append(current.bit_count())
    return sorted(sizes)


def connected(adj):
    return len(component_sizes(adj)) == 1


def triangle_count(adj):
    n = len(adj)
    return sum(((adj[a] >> b)&1) and ((adj[a] >> c)&1) and ((adj[b] >> c)&1)
               for a,b,c in combinations(range(n), 3))


def degree_sequence(adj):
    return tuple(sorted(row.bit_count() for row in adj))


def cone(base):
    m = len(base)
    return graph(m + 1, [(u, v) for u in range(m) for v in range(u+1, m)
                          if (base[u] >> v) & 1] + [(u,m) for u in range(m)])


def cone_distribution_from_sizes(sizes):
    d = Counter()
    for s in sizes:
        d[1+s] += comb(s+1, 2)
    for i in range(len(sizes)):
        for j in range(i+1, len(sizes)):
            d[1+sizes[i]+sizes[j]] += sizes[i]*sizes[j]
    return d


def cone_mean_from_sizes(sizes):
    n = 1 + sum(sizes)
    return Fraction(1,1) + sum((Fraction(s*s*(2*n-1-s),n*(n-1)) for s in sizes),Fraction(0,1))


def fan_and_triangle(n):
    assert n>=6
    # Peripheral vertices 0,...,n-2. Hub n-1.
    m=n-1
    path = graph(m, [(u, u+1) for u in range(m-1)])
    # Triangle on first 3, path on remaining m-3 vertices.
    tri_path = graph(m, [(0,1),(1,2),(0,2)] + [(u,u+1) for u in range(3,m-1)])
    return cone(path),cone(tri_path)


def test_cone_formula():
    cases = 0
    seeds = 0
    for m in range(2,7):
        for mask in range(1 << comb(m,2)):
            h=from_mask(m, mask)
            g=cone(h)
            sizes=component_sizes(h)
            actual=distribution(g)
            expected=cone_distribution_from_sizes(sizes)
            assert actual==expected,(m,mask,actual,expected)
            assert mean_from_dist(actual)==cone_mean_from_sizes(sizes)
            cases+=1
            seeds+=comb(m+1,2)
    return cases,seeds


def test_sharp_small_graphs():
    # Full enumeration of every labelled undirected simple graph with n<=5.
    # Same degree sequence, more triangles, smaller two-seed mean? Must not occur.
    counts={}
    for n in range(2,6):
        sequences=defaultdict(dict)
        total_connected=0
        for mask in range(1 << comb(n,2)):
            adj=from_mask(n,mask)
            if not connected(adj):continue
            total_connected+=1
            key=degree_sequence(adj)
            tri=triangle_count(adj)
            score=mean_from_dist(distribution(adj))
            if tri in sequences[key]:
                old=sequences[key][tri]
                assert old==score,('same degree+tri but different cascade',n,mask,key,tri,old,score)
            else:sequences[key][tri]=score
        # Check no increase in triangles decreases mean size for degree-matched networks.
        comparisons=0
        for D,tables in sequences.items():
            for lo, hi in combinations(sorted(tables),2):
                assert tables[lo] <= tables[hi],('triangle reversal',n,D,lo,hi,tables)
                comparisons+=1
        counts[n]=(1<<comb(n,2),total_connected,len(sequences),comparisons)
    return counts


def test_examples():
    ans=[]
    for n in [6,7,8,9,13,24]:
        f,b=fan_and_triangle(n)
        sf=mean_from_dist(distribution(f)); sb=mean_from_dist(distribution(b))
        assert degree_sequence(f)==degree_sequence(b)
        assert triangle_count(b)-triangle_count(f)==1
        delta=Fraction(3*(n-4)*(n+1),n*(n-1))
        assert sf==n and sf-sb==delta
        ans.append((n,tuple(degree_sequence(f)),triangle_count(f),triangle_count(b),str(sf),str(sb),str(delta)))
    return ans


def test_distribution_example():
    f,b=fan_and_triangle(6)
    return dict(distribution(f)),dict(sorted(distribution(b).items())),degree_sequence(f),sorted(tuple(row.bit_count() for row in b))


def main():
    # Exhaustive cone identity and spectral/graph summary checks independent of networkx.
    # 2^15 bases at m=6, each with 21 unordered seed pairs.
    cone_cases, seeds=test_cone_formula()
    small=test_sharp_small_graphs()
    samples=test_examples()
    distrib=test_distribution_example()
    print('cone_graphs_checked',cone_cases)
    print('cone_seed_pairs_checked',seeds)
    print('small_graph_exhaustion_(total_labeled,connected,degree_classes,triangle_pair_comparisons)',small)
    print('infinite_family_sample_points',samples)
    print('six_vertex_cascade_histograms_and_degrees',distrib)
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':main()
