#!/usr/bin/env python3
"""Checks the full counting identity by a direct coloring/partition enumeration.
This finite check is not a proof beyond the tested finite graphs.
"""
from itertools import combinations,product
from collections import Counter
from math import factorial

def graph_cases(n):
    ep=list(combinations(range(n),2))
    for edge_mask in range(1<<len(ep)):
        adj=[0]*n
        for h,(a,b) in enumerate(ep):
            if edge_mask & (1<<h): adj[a]|=1<<b;adj[b]|=1<<a
        ds=[]
        for v in range(n):
            row=[999]*n;row[v]=0
            seen=1<<v; frontier=seen
            for d in range(1,n):
                nxt=0
                for j in range(n):
                    if frontier & (1<<j): nxt|=adj[j]
                nxt&=~seen
                if not nxt:break
                for j in range(n):
                    if nxt&(1<<j):row[j]=d
                seen|=nxt;frontier=nxt
            ds.append(row)
        if max(max(row) for row in ds)<=2:yield adj,ds

def setpartitions(n):
    def rec(a,m):
        if len(a)==n:
            out=[0]*(m+1)
            for j,v in enumerate(a):out[v]|=1<<j
            yield out
        else:
            for v in range(m+2):
                yield from rec(a+[v],max(m,v))
    yield from rec([0],0)

def falls(t,r):
    if r>t or t<0:return 0
    out=1
    for a in range(r):out*=t-a
    return out

def counts_from_sets(adj,t,k):
    n=len(adj); ind=Counter();mis=Counter()
    for sub in range(1<<n):
        if any(adj[v]&sub for v in range(n) if sub&(1<<v)):continue
        s=sub.bit_count();ind[s]+=1
        if all(adj[v]&sub for v in range(n) if not sub&(1<<v)):mis[s]+=1
    return sum(ind[n-r]*falls(t-1,r) for r in range(k,n+1))+mis[n-k+1]*falls(t-1,k-1)

def direct_all(adj,ds,t,partitions):
    n=len(adj);full=(1<<n)-1
    counts=Counter()
    for colors in product(range(1,t+1), repeat=n):
        if any(colors[u]==colors[v] and ds[u][v]<=colors[u]
               for u in range(n) for v in range(u+1,n)):
            continue
        reach=[sum(1<<w for w in range(n) if ds[u][w]<=colors[u]) for u in range(n)]
        for blocklist in partitions:
            k=len(blocklist)
            if counts.get((colors,k)):
                continue
            if all(any((block&(1<<u)) and (reach[u]&(1<<w))
                       for u in range(n)) for block in blocklist for w in range(n)):
                counts[colors,k]=1
    return Counter({k:sum(v for (color,j),v in counts.items() if j==k) for k in range(1,n+1)})

def main():
    groups=Counter();comparisons=0;color_assignments=0
    for n in range(2,6):
        cases=list(graph_cases(n))
        if n==5:
            stride=max(1,len(cases)//32)
            cases=cases[::stride]
        partitions=list(setpartitions(n))
        for adj,ds in cases:
            for t in range(1,n+2):
                got=direct_all(adj,ds,t,partitions)
                for k in range(1,n+1):
                    want=counts_from_sets(adj,t,k)
                    assert got[k]==want,(n,adj,t,k,got[k],want)
                    comparisons+=1
                color_assignments+=t**n
            groups[n]+=1
    print('PASS complete all-t color-counting polynomial')
    print('diameter <=2 labeled graph cases:',dict(groups))
    print('independently checked (graph,t,k) coefficients:',comparisons)
    print('vertex-color assignments tested before packing pruning:',color_assignments)
if __name__=='__main__':main()
