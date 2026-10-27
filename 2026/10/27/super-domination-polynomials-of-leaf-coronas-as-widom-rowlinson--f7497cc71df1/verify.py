#!/usr/bin/env python3
"""Exact small-graph checks for a leaf-corona super domination identity."""
from itertools import combinations
from collections import Counter
from random import Random


def corona_neighbors(n, edges):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        adj[i].add(i+n)
        adj[i+n].add(i)
    for i,j in edges:
        adj[i].add(j)
        adj[j].add(i)
    return adj


def direct_polynomial(n,edges):
    adj=corona_neighbors(n,edges)
    count=Counter()
    for bits in range(1<<(2*n)):
        U={i for i in range(2*n) if not(bits>>i & 1)}
        good=all(any(u in adj[v] and len(adj[v] & U)==1
                     for v in range(2*n) if v not in U)
                 for u in U)
        if good:count[2*n-len(U)]+=1
    return count


def components(n,edges,U):
    adj=[set() for _ in range(n)]
    for i,j in edges:
        adj[i].add(j);adj[j].add(i)
    unseen=set(U); answer=0
    while unseen:
        answer+=1
        stack=[unseen.pop()]
        while stack:
            x=stack.pop()
            for y in adj[x]&unseen:
                unseen.remove(y);stack.append(y)
    return answer


def component_polynomial(n,edges):
    count=Counter()
    for bits in range(1<<n):
        U={i for i in range(n) if bits>>i & 1}
        count[2*n-len(U)]+=2**components(n,edges,U)
    return count


def hom_polynomial(n,edges):
    # Color 0 means both arm vertices selected; 1/2 mean just one selected.
    # Only color pairs (1,2) and (2,1) are forbidden across base edges.
    count=Counter()
    for integer in range(3**n):
        a=[];v=integer
        for _ in range(n):
            a.append(v%3);v//=3
        if any((a[i],a[j]) in ((1,2),(2,1)) for i,j in edges):
            continue
        count[n+a.count(0)]+=1
    return count


def test(n,edges):
    a=direct_polynomial(n,edges)
    b=component_polynomial(n,edges)
    c=hom_polynomial(n,edges)
    assert a==b==c, (n,edges,a,b,c)
    assert min(a)==n and a[n]==2**components(n,edges,set(range(n)))
    if n>=2 and components(n,edges,set(range(n)))==1:
        low=a[n+1]
        assert low==sum(2**components(n,edges,set(range(n))-{i})
                        for i in range(n))
        assert (low==2*n)==all(components(n,edges,set(range(n))-{i})==1
                                 for i in range(n))
    return sum(a.values())


def main():
    total=0
    for n in range(1,5):
        pairs=list(combinations(range(n),2))
        for bits in range(1<<len(pairs)):
            E=[e for j,e in enumerate(pairs) if bits>>j&1]
            test(n,E);total+=1
    rng=Random(113)
    for n,k in [(5,50),(6,50),(7,8)]:
        pairs=list(combinations(range(n),2))
        for _ in range(k):
            bits=rng.getrandbits(len(pairs))
            E=[e for j,e in enumerate(pairs) if bits>>j&1]
            if n<=6:test(n,E)
            else:
                # Direct checking for n=7 costs 2^14 vertex subsets each.
                test(n,E)
            total+=1
    print('PASS:',total,'base graphs, direct graph definition, induced-component expansion and 3-state homomorphism count agree')
    for n,edges in [(4,[(0,1),(1,2),(2,3)]),(4,[(0,1),(1,2),(2,3),(3,0)]),(5,[(0,1),(1,2),(2,3),(3,4)])]:
        print('n=',n,'m=',len(edges),'poly=',dict(sorted(component_polynomial(n,edges).items())))

if __name__=='__main__':main()
