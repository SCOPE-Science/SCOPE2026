#!/usr/bin/env python3
"""Affine-template adjacency certificate and a six-rung twist witness.

Only standard Python is required. The periodic tail is proved mathematically:
each offset in the seven templates is in [-2,3]. An overlap test
between a translated pair is equality of four template entries, hence
has the form a*n+b=0 (mod 2*n), |b|<=12. For n>=13 its truth value
is independent of n: exactly b=0 and a even. Checking n=13
therefore checks every n>=13.
"""
from collections import Counter

def R(n):
    return [(0,1,2,3),(0,1,2,n),(0,1,2,n+2),
            (0,1,3,n+1),(0,1,n-1,n),(0,1,n,2*n-2),(0,1,n,n+1)]

def orbit_data(n):
    N=2*n
    reps=R(n)
    orbits=[]
    classes={}
    for k,rr in enumerate(reps):
        orb=set()
        for s in range(N):
            B=frozenset((v+s)%N for v in rr)
            orb.add(B)
            if B in classes:assert classes[B]==k,('overlap',n,k)
            classes[B]=k
        orbits.append(orb)
    counts=[]
    for rr in reps:
        B=set(rr)
        row=[0]*7
        # Any 3-overlap has an aligned vertex, so <=16 shifts per template.
        for j,target in enumerate(reps):
            shifts={(u-v)%N for u in rr for v in target}
            cand={frozenset((v+shift)%N for v in target) for shift in shifts}
            row[j]=sum(C!=frozenset(rr) and len(B.intersection(C))==3 for C in cand)
        counts.append(row)
    return len(classes),[len(o) for o in orbits],counts,classes

expected=[[2,2,2,1,0,1,0],
          [2,0,1,1,2,1,1],
          [2,1,0,1,2,1,1],
          [1,1,1,0,1,0,1],
          [0,2,2,1,0,1,2],
          [1,1,1,0,1,0,1],
          [0,2,2,2,4,2,0]]
for n in range(6,14):
    total,sizes,rows,classes=orbit_data(n)
    assert total==13*n
    assert sizes==[2*n]*6+[n]
    assert rows==expected,(n,rows)
    print('n=%d classes=%s orbit_sizes=%s degree=%s' %
          (n,total,sizes,[sum(x) for x in rows]))
print('Symbolic stabilization: entries a*n+b have |b|<=3; four-entry differences have |b|<=12.\n'
      'For n>=13, equality modulo 2*n iff the coefficient of n is even and b=0.\n'
      'Every possible >=3-set intersection is among 16 aligned shifts; n=13 certifies all n>=13.')
print('A..G neighbor matrix:')
for row in expected:print(' '.join(map(str,row)))

def mobius_adj(n):
    N=2*n
    return [set([(v-1)%N,(v+1)%N,(v+n)%N]) for v in range(N)]

def circular_adj(n):
    return [set([v//n*n+((v%n-1)%n),v//n*n+((v%n+1)%n),(v+n)%(2*n)]) for v in range(2*n)]

def forces(adj,blue):
    N=len(adj)
    while len(blue)<N:
        more={next(iter(w)) for x in blue if len(w:=(adj[x]-blue))==1}
        if not more:return False
        blue|=more
    return True

def zfgraph(n,adj):
    from itertools import combinations
    N=2*n
    states=[frozenset(s) for s in combinations(range(N),4) if forces(adj,set(s))]
    mp={s:i for i,s in enumerate(states)}
    edges=[set() for s in states]
    for i,S in enumerate(states):
        for v in S:
            for w in range(N):
                if w not in S:
                    j=mp.get(frozenset((S-{v})|{w}))
                    if j is not None:edges[i].add(j)
    return edges

def trace_power(graph,k):
    total=0
    for root in range(len(graph)):
        v={root:1}
        for _ in range(k):
            new={}
            for u,m in v.items():
                for w in graph[u]:new[w]=new.get(w,0)+m
            v=new
        total+=v.get(root,0)
    return total
m=zfgraph(6,mobius_adj(6));c=zfgraph(6,circular_adj(6))
assert len(m)==len(c)==78
assert sum(map(len,m))//2==sum(map(len,c))//2==288
tr_m=[trace_power(m,k) for k in range(2,7)]
tr_c=[trace_power(c,k) for k in range(2,7)]
assert tr_m[:4]==tr_c[:4]
assert tr_m[-1]==464832 and tr_c[-1]==464856
print('n=6 zero-forcing exchange graphs: both |V|=78, |E|=288')
print('walk traces lengths 2..6, mobius =',tr_m)
print('walk traces lengths 2..6, circular =',tr_c)
print('trace(A^6) differs by 24, therefore they are non-isomorphic')
print('PASS symbolic adjacency/periodicity check and finite twist witness')
