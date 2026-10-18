#!/usr/bin/env python3
"""Direct finite checks of optimal Horn bases for graph-geodesic convexity."""
from collections import deque
from itertools import combinations, product
from math import factorial
from random import Random


def distances(vertices, edges):
    nbr = [set() for _ in range(vertices)]
    for a,b in edges:
        nbr[a].add(b); nbr[b].add(a)
    out = []
    for u in range(vertices):
        d = [-1]*vertices
        d[u] = 0; q = deque([u])
        while q:
            a=q.popleft()
            for b in nbr[a]:
                if d[b]<0:
                    d[b]=d[a]+1; q.append(b)
        out.append(d)
    return out


def all_intervals(d):
    n=len(d)
    return {(u,v):frozenset(w for w in range(n) if d[u][w]>=0 and d[w][v]>=0 and d[u][w]+d[w][v]==d[u][v])
            for u in range(n) for v in range(u+1,n)}


def geodesic_closure(n, iv, s):
    s=set(s)
    while True:
        t=set(s)
        for u,v in combinations(sorted(s),2):
            t.update(iv[u,v])
        if t==s: return frozenset(s)
        s=t


def basis_closure(s, basis):
    s=set(s)
    while True:
        t=set(s)
        for (u,v),rhs in basis:
            if u in s and v in s: t.update(rhs)
        if t==s: return frozenset(s)
        s=t


def options(n,d,iv):
    """For geodetic pairs: single interior. For cycle antipodes: one per side."""
    out=[]
    for u,v in combinations(range(n),2):
        inter=sorted(iv[u,v]-{u,v})
        if not inter: continue
        if n%2==0 and d[u][v]==n//2 and cycle_distance(n,u,v)==n//2:
            # This branch is for cycles only; order-separated arcs are unique.
            a=[(u+j)%n for j in range(1,n//2)]
            b=[(u-j)%n for j in range(1,n//2)]
            out.append(((u,v),tuple((x,y) for x in a for y in b)))
        else:
            out.append(((u,v),tuple((x,) for x in inter)))
    return out


def cycle_distance(n,u,v):
    return min((v-u)%n,(u-v)%n)


def cycle_edges(n):
    return sorted({tuple(sorted((u,(u+1)%n))) for u in range(n)})


def check(n,iv,basis):
    for mask in range(1<<n):
        s=[i for i in range(n) if (mask>>i)&1]
        x=geodesic_closure(n,iv,s)
        y=basis_closure(s,basis)
        if x!=y:
            raise AssertionError((n,mask,sorted(x),sorted(y)))
    return 1<<n


def check_cycle_bases():
    tested_bases=0; tested_subsets=0; profile=[]
    for n in range(3,11):
        d=distances(n,cycle_edges(n)); iv=all_intervals(d)
        opt=options(n,d,iv)
        predicted = factorial((n-1)//2-1)**n if n%2 else factorial(n//2-1)**n
        # Above is factorial number of optimum bases for cycles of either parity.
        total=1
        for _,opts in opt: total*=len(opts)
        assert predicted==total,(n,predicted,total)
        nonedges=sum(1 for x in iv if d[x[0]][x[1]]>=2)
        predicted_cost=3*nonedges+(n//2 if n%2==0 else 0)
        positions=range(total) if total<=128 else range(12)
        for j in positions:
            if total<=128:
                selected=[]; k=j
                for pair,opts in opt:
                    selected.append((pair,opts[k%len(opts)])); k//=len(opts)
            else:
                rng=Random(1100+n*100+j)
                selected=[(p,rng.choice(opts)) for p,opts in opt]
            cost=sum(2+len(rhs) for _,rhs in selected)
            assert cost==predicted_cost,(n,cost,predicted_cost)
            tested_subsets+=check(n,iv,selected)
            tested_bases+=1
        profile.append((n,predicted_cost,predicted))
    assert dict((n,c) for n,c,_ in profile)=={3:0,4:8,5:15,6:30,7:42,8:64,9:81,10:110},profile
    return tested_bases,tested_subsets,profile


def check_general():
    graphs=0; geodetic=0; nong=0; subsets=0
    for n in range(2,6):
        pairs=list(combinations(range(n),2))
        for mask in range(1<<len(pairs)):
            E=[p for i,p in enumerate(pairs) if (mask>>i)&1]
            d=distances(n,E)
            if -1 in d[0]:continue
            iv=all_intervals(d)
            is_geo=all(len(iv[u,v])==d[u][v]+1 for u,v in iv)
            graphs+=1
            if is_geo:
                geodetic+=1
                opts=[((u,v),tuple((w,) for w in sorted(iv[u,v]-{u,v}))) for u,v in iv if d[u][v]>=2]
                assert all(q for _,q in opts)
                for selector in [0,1]:
                    basis=[(p,choices[min(selector,len(choices)-1)]) for p,choices in opts]
                    subsets+=check(n,iv,basis)
            else:
                nong+=1
                min_d=min(d[u][v] for u,v in iv if len(iv[u,v])>d[u][v]+1)
                ambiguous=next((u,v) for u,v in iv if d[u][v]==min_d and len(iv[u,v])>min_d+1)
                # A single chosen consequence for this first ambiguous pair can
                # derive only the points on one fixed geodesic, not their union.
                u,v=ambiguous
                w=min(iv[u,v]-{u,v})
                basis=[((a,b),(min(iv[a,b]-{a,b}),)) for a,b in iv if d[a][b]>=2]
                derived=basis_closure({u,v},basis)
                assert iv[u,v] - derived,(n,ambiguous,derived,iv[u,v])
    return graphs,geodetic,nong,subsets


def main():
    b,s,profile=check_cycle_bases()
    g,geo,nong,t=check_general()
    print('VERIFY_OK cycles_bases=%d cycle_subsets=%d all_connected_labelled_graphs=%d geodetic=%d nongeodetic=%d graph_subsets=%d' %(b,s,g,geo,nong,t))
    print('cycle_cost_and_optimum_count='+repr(profile))

if __name__=='__main__': main()
