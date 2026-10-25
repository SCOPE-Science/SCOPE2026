#!/usr/bin/env python3
"""Exact reproducible checks for integral magnitude homology of W(3).
Requires Python 3.10+ and sympy (tested with 1.14). No network needed.
"""
from itertools import product
from collections import deque, Counter
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from sympy import Matrix

Q=3

def normalize(v):
    x=next((a for a in v if a%Q),None)
    if x is None:return None
    r=pow(x,-1,Q)
    return tuple(a*r%Q for a in v)

def sympl(v,w):
    return (v[0]*w[2]-v[2]*w[0]+v[1]*w[3]-v[3]*w[1])%Q

points=sorted({normalize(v) for v in product(range(Q),repeat=4)}-{None})
point_index={v:i for i,v in enumerate(points)}
line_sets=set()
for i,v in enumerate(points):
    for w in points[i+1:]:
        if sympl(v,w)==0:
            line_sets.add(frozenset(point_index[normalize(tuple((a*v[z]+b*w[z])%Q for z in range(4)))]
                                    for a,b in product(range(Q),repeat=2) if a or b))
lines=sorted(line_sets,key=lambda z:tuple(sorted(z)))
line_index={x:40+i for i,x in enumerate(lines)}
assert len(points)==len(lines)==40
G=[set() for _ in range(80)]
for j,l in enumerate(lines):
    for i in l:G[i].add(40+j);G[40+j].add(i)
assert set(map(len,G))=={4}
DIST=[]
for source in range(80):
    d=[999]*80;d[source]=0;queue=deque([source])
    while queue:
        u=queue.popleft()
        for v in G[u]:
            if d[v]>d[u]+1:d[v]=d[u]+1;queue.append(v)
    DIST.append(d)
assert max(max(x) for x in DIST)==4

def chains(k,L,start,end):
    out=[]
    def dfs(taken,dist_so_far):
        if len(taken)==k:
            z=L-dist_so_far
            if z>0 and DIST[taken[-1]][end]==z:out.append(tuple(taken+[end]))
            return
        u=taken[-1]
        for v in range(80):
            dv=DIST[u][v]
            if 0<dv<L-dist_so_far and DIST[v][end]<=L-dist_so_far-dv:
                dfs(taken+[v],dist_so_far+dv)
    dfs([start],0)
    return out

def boundary(c):
    out=[]
    for i in range(1,len(c)-1):
        if DIST[c[i-1]][c[i]]+DIST[c[i]][c[i+1]]==DIST[c[i-1]][c[i+1]]:
            out.append((c[:i]+c[i+1:],-1 if i%2 else 1))
    return out

def matrices(u,v):
    C={k:chains(k,5,u,v) for k in (2,3,4)}
    I={k:{c:j for j,c in enumerate(C[k])} for k in (2,3)}
    D3=zeros(len(C[2]),len(C[3]));D4=zeros(len(C[3]),len(C[4]))
    for k,M in [(3,D3),(4,D4)]:
        for j,c in enumerate(C[k]):
            for face,sgn in boundary(c):M[I[k-1][face],j]=sgn
    assert D3*D4==zeros(len(C[2]),len(C[4]))
    return C,I,D3,D4

def smith_stats(M):
    d=smith_normal_form(M,domain=ZZ).diagonal()
    return Counter(abs(int(v)) for v in d if v)

def report_pair(u,v,expected_counts,expected_ranks):
    C,I,D3,D4=matrices(u,v)
    assert tuple(len(C[k]) for k in (2,3,4))==expected_counts
    s3=smith_stats(D3);s4=smith_stats(D4)
    assert s3==Counter({1:expected_ranks[0]})
    assert s4==Counter({1:expected_ranks[1]})
    print('distance',DIST[u][v],'chains',expected_counts,'SNF ranks',expected_ranks)
    return C,I,D3,D4

p=0; adjacent=min(G[p]); remote=next(i for i in range(40,80) if DIST[p][i]==3)
report_pair(p,adjacent,(18,81,120),(18,63))
C,I,D3,D4=report_pair(p,remote,(28,87,72),(28,50))
x=next(b for b in G[remote] if DIST[p][b]==2)
m=next(a for a in G[p] if x in G[a]);A=sorted(G[p]-{m});B=sorted(G[remote]-{x})
assert len(A)==len(B)==3
Z=zeros(len(C[3]),9)
for col,(a,b) in enumerate(product(A,B)):
    for c,sgn in [((p,m,b,remote),1),((p,a,b,remote),-1),((p,a,p,remote),1)]:
        Z[I[3][c],col]=sgn
assert D3*Z==zeros(len(C[2]),9)
assert smith_stats(D4.row_join(Z))==Counter({1:59})
print('nine explicit octagon classes: augmented Smith factors are 59 units')

# Each symplectic transvection is a graph automorphism; certify both point-line orbits.
transvections=[]
for v in points:
    pm=[point_index[normalize(tuple((x+sympl(pv,v)*z)%3 for x,z in zip(pv,v)))] for pv in points]
    lm=[line_index[frozenset(pm[i] for i in line)] for line in lines]
    transvections.append(pm+lm)
for T in transvections:
    assert all({T[v] for v in G[u]}==G[T[u]] for u in range(80))
for target_size,representative in [(160,(p,adjacent)),(1440,(p,remote))]:
    orbit={representative};stack=[representative]
    while stack:
        a,b=stack.pop()
        for T in transvections:
            pair=(T[a],T[b])
            if pair not in orbit:orbit.add(pair);stack.append(pair)
    assert len(orbit)==target_size
    assert all(0<=a<40<=b<80 for a,b in orbit)
    print('point-line orbit of size',target_size,'verified')

# Endpoint reversal is a chain isomorphism, and bipartite parity rules out all other endpoints.
assert 2*1440*9==25920
print('PASS: MH_(3,5) over Z is free of rank 25920; nine explicit classes per nonincident ordered endpoint pair.')
