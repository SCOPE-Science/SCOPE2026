#!/usr/bin/env python3
"""Independent enumeration of k-limited dominating sets in clique coronas.

Graph convention: core vertices 0..n-1; attached clique for core v has
indices n+v*s,...,n+(v+1)*s-1. Uses unweighted bitmasks and integer math.
"""
from collections import Counter
from itertools import combinations
from math import comb


def graph_neighborhoods(n, core_edges, s):
    size = n * (s + 1)
    nbr = [0] * size
    for u,v in core_edges:
        nbr[u] |= 1 << v
        nbr[v] |= 1 << u
    for u in range(n):
        cluster = [u]+list(range(n+u*s,n+(u+1)*s))
        for a,b in combinations(cluster,2):
            nbr[a] |= 1 << b
            nbr[b] |= 1 << a
    return nbr


def brute(n, core_edges, s, k):
    adj=graph_neighborhoods(n,core_edges,s)
    allv=(1<<len(adj))-1
    counts=Counter()
    for mask in range(1<<len(adj)):
        excluded=allv^mask
        # check covering of all outside vertices independently
        if any(not (adj[v]&mask) for v in range(len(adj)) if excluded&(1<<v)):
            continue
        if any((adj[v]&excluded).bit_count()>k for v in range(len(adj)) if mask&(1<<v)):
            continue
        counts[mask.bit_count()]+=1
    return counts


def derived(n, core_edges, s, k):
    # Sum over selected core masks and multiplicity-weighted private counts.
    adj=[0]*n
    for u,v in core_edges:
        adj[u] |= 1<<v
        adj[v] |= 1<<u
    from collections import defaultdict
    pol=defaultdict(int)
    for mask in range(1<<n):
        poly={mask.bit_count():1}
        for v in range(n):
            outside=(adj[v]&((1<<n)-1^mask)).bit_count()
            if mask & (1<<v): lower=max(0,s+outside-k)
            else: lower=max(1,s+1-k)
            nxt=defaultdict(int)
            for degree,weight in poly.items():
                for j in range(lower,s+1):
                    nxt[degree+j] += weight*comb(s,j)
            poly=nxt
        for d,c in poly.items():pol[d]+=c
    return Counter(pol)


def expected_min_count(n, core_edges, s, k):
    adj=[0]*n
    for u,v in core_edges:
        adj[u]|=1<<v
        adj[v]|=1<<u
    gamma=n*max(1,s+1-k)
    if k<=s:
        seen=set();product=1
        for v in range(n):
            if v in seen:continue
            component={v};front=[v];seen.add(v)
            while front:
                x=front.pop()
                for y in range(n):
                    if adj[x]>>y&1 and y not in seen:
                        seen.add(y);component.add(y);front.append(y)
            h=len(component)
            product *= comb(s,k-1)**h + comb(s,k)**h
        return gamma,product
    count=0
    for mask in range(1<<n):
        if all((adj[v]&((1<<n)-1^mask)).bit_count() <= k-s for v in range(n) if mask>>v&1):
            count+=s**(n-mask.bit_count())
    return gamma,count


def verify():
    cases=0;checked=0;graphs=0
    for n in range(1,5):
        allpairs=list(combinations(range(n),2))
        maxgraphs=1<<len(allpairs)
        for e_mask in range(maxgraphs):
            core_edges=[e for i,e in enumerate(allpairs) if e_mask>>i&1]
            graphs+=1
            # all graphs through order four; s<=2 for order four to bound effort
            sizes=range(1,3) if n==4 else range(1,4)
            for s in sizes:
                for k in range(1,s+n+1):
                    actual=brute(n,core_edges,s,k)
                    predicted=derived(n,core_edges,s,k)
                    if actual!=predicted:
                        raise AssertionError(('polynomial',n,core_edges,s,k,actual,predicted))
                    minimum=min(actual)
                    gamma,count=expected_min_count(n,core_edges,s,k)
                    if (minimum,actual[minimum])!=(gamma,count):
                        raise AssertionError(('minima',n,core_edges,s,k,minimum,actual[minimum],gamma,count))
                    cases+=1
                    checked+=1<<(n*(s+1))
    print('ALL_CHECKS_PASS')
    print('core_graphs:',graphs)
    print('graph_parameter_cases:',cases)
    print('initial_vertex_subsets:',checked)
    print('verified: all-set polynomial, domination number, minimum-set count')


if __name__=='__main__': verify()
