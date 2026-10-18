#!/usr/bin/env python3
"""Independent multiplicity-weighted reflection quotient and small-group check."""
from collections import Counter
import networkx as nx

def weighted_quotient(m):
    nbr=[]
    for j in range(m+1):
        if j==0: nbr.append([1,1,m])
        elif j==m: nbr.append([m-1,m-1,0])
        else: nbr.append([j-1,j+1,m-j])
    return nbr

def stable(m):
    nbr=weighted_quotient(m)
    lab=[0]+[1]*m
    history=[lab]
    for i in range(m+1):
        s=[(lab[j],tuple(sorted(Counter(lab[t] for t in nbr[j]).items()))) for j in range(m+1)]
        dic={v:k for k,v in enumerate(sorted(set(s)))}
        nxt=[dic[v] for v in s]
        if len(set(nxt))==len(set(lab)):break
        history.append(nxt)
        lab=nxt
    else:raise AssertionError('no stabilization')
    return history

def expect(m,r,j):
    if r==0:return 0 if j==0 else 1
    if r==1:return 0 if j==0 else 1 if j in (1,m) else 2
    if r==2:
        if j==0:return 0
        if j in (1,m):return 1
        if j==2:return 2
        if j==m-1:return 3
        return 4
    if j<=r:return j
    if j>=m-r+1:return j
    return -1

checks=0
for m in range(4,151):
    history=stable(m)
    rmax=max(3,m//2)
    assert len(history)-1==rmax,(m,len(history)-1,rmax)
    for r,lab in enumerate(history):
        for a in range(m+1):
            for b in range(a):
                assert (lab[a]==lab[b])==(expect(m,r,a)==expect(m,r,b)),(m,r,a,b)
                checks+=1
print('QUOTIENT PASS: m=4..150, exact predicted round partitions and depth,',checks,'pair comparisons')

for m in range(4,11):
    n=2*m
    G=nx.Graph(); G.add_nodes_from(range(n))
    G.add_edges_from((i,(i+1)%n) for i in range(n))
    G.add_edges_from((i,i+m) for i in range(m))
    orbits=[set() for _ in range(n)]
    count=0
    for p in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter():
        count+=1
        assert p[0] in range(n)
        if p[0]==0:
            for i in range(n):orbits[i].add(p[i])
    assert count==4*m,(m,count)
    for i in range(n):
        expect_set={i,(-i)%n}
        assert orbits[i]==expect_set,(m,i,orbits[i],expect_set)
print('AUTOMORPHISMS PASS: m=4..10, full groups and rooted reflection orbits')
