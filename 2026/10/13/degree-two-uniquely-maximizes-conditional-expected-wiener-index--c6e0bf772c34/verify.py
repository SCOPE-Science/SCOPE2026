#!/usr/bin/env python3
"""Exact finite checks for degree-conditioned Wiener regressions in labelled trees.
Only standard-library integer and rational arithmetic is used."""
from fractions import Fraction
from itertools import product
from math import comb
import heapq

def falling(a, k):
    if k < 0 or k > a: return 0
    out = 1
    for j in range(k): out *= a-j
    return out

def F(m,t):
    return sum((Fraction(falling(t,j),m**j) for j in range(t+1)), Fraction(0))

def prediction(n,r):
    m=n-1
    if m==1: return Fraction(1), Fraction(0), Fraction(1)
    t=m-1-r
    ft=F(m,t)
    root=m*ft
    other=comb(m,2)*((m+r-r*r)*ft+m*(r-1))/(m-1)
    return root,other,root+other

def tree_edges(code,n):
    deg=[1]*n
    for v in code:deg[v]+=1
    leaves=[i for i,x in enumerate(deg) if x==1]
    heapq.heapify(leaves)
    g=[[] for _ in range(n)]
    for v in code:
        u=heapq.heappop(leaves)
        g[u].append(v);g[v].append(u)
        deg[u]-=1;deg[v]-=1
        if deg[v]==1:heapq.heappush(leaves,v)
    a,b=leaves
    g[a].append(b);g[b].append(a)
    return g

def distances(g):
    n=len(g)
    parents=[-1]*n;parents[0]=0
    dist=[0]*n
    seq=[0]
    for x in seq:
        for y in g[x]:
            if parents[y]==-1:
                parents[y]=x;dist[y]=dist[x]+1;seq.append(y)
    size=[1]*n
    for x in reversed(seq[1:]):size[parents[x]]+=size[x]
    root=sum(size[1:])
    total=sum(size[x]*(n-size[x]) for x in range(1,n))
    return root,total-root,total

def run():
    trees=0;cells=0;formula_checks=0;ordering_checks=0
    for n in range(2,9):
        sums={r:[0,0,0,0] for r in range(n-1)}
        for code in product(range(n),repeat=n-2):
            g=tree_edges(code,n)
            r=len(g[0])-1
            root,other,w=distances(g)
            v=sums[r]
            v[0]+=1;v[1]+=root;v[2]+=other;v[3]+=w
            trees+=1
        for r,v in sums.items():
            assert v[0]==comb(n-2,r)*(n-1)**(n-2-r),(n,r,v[0])
            assert tuple(Fraction(v[i],v[0]) for i in (1,2,3))==prediction(n,r),(n,r)
            cells+=1;formula_checks+=4
        if n>=4:
            w=[prediction(n,r)[2] for r in range(n-1)]
            assert w[1]>w[0] and all(w[j]>w[j+1] for j in range(1,n-2))
            ordering_checks+=n-2
        elif n==3:
            assert prediction(n,0)[2]==prediction(n,1)[2]==4
    # Separate algebraic checks, exact rationals for cases far beyond enumeration.
    tests=0
    for m in range(3,81):
        m0=prediction(m+1,0)[2]
        m1=prediction(m+1,1)[2]
        w=[prediction(m+1,r)[2] for r in range(m)]
        assert m1>m0
        assert all(w[r]>w[r+1] for r in range(1,m-1))
        if m>=4:
            # The nonroot distance expectation is equal at root degrees 2 and 3.
            assert prediction(m+1,1)[1]==prediction(m+1,2)[1]
        for r in range(2,m-1):
            t=m-r-2
            assert (m+r*(r+1))*F(m,t)>r*m
            tests+=1
    print('PASS exact_Cayley_trees',trees,'degree_cells',cells,'mean_and_count_checks',formula_checks,
          'finite_mode_comparisons',ordering_checks,'exact_inequality_cases',tests)
if __name__=='__main__':run()
