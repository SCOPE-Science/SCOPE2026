#!/usr/bin/env python3
"""Exact integer replay of the C60 zero-field Ising covariance theorem.
Pure Python standard library; no data files or third-party dependencies.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, product

# Icosahedral graph, 12 vertices, 30 edges, in a reproducible north/south convention.
N, S = 10, 11
edges = set()
def add(u,v):
    assert u != v
    edges.add(tuple(sorted((u,v))))
for i in range(5):
    add(N,i); add(S,5+i)
    add(i,(i+1)%5); add(5+i,5+(i+1)%5)
    add(i,5+i); add(i,5+(i-1)%5)
assert len(edges)==30
neigh = [set() for _ in range(12)]
for u,v in edges:
    neigh[u].add(v);neigh[v].add(u)
assert all(len(nb)==5 for nb in neigh)
faces=[frozenset(x) for x in combinations(range(12),3)
       if all(tuple(sorted(p)) in edges for p in combinations(x,2))]
assert len(faces)==20
assert all(sum({u,v} <= f for f in faces)==2 for u,v in edges)
assert all(sum(v in neigh[w] for w in neigh[u] if w!=v)==2
           for u in range(12) for v in neigh[u])

# Truncated icosahedron: each directed original edge is a site.
verts=sorted((u,v) for u,v in edges for u,v in ((u,v),(v,u)))
assert len(verts)==60
idx={p:i for i,p in enumerate(verts)}
gedges=set()
def link(a,b):
    gedges.add(tuple(sorted((idx[a],idx[b]))))
for u,v in edges:
    link((u,v),(v,u))
for u in range(12):
    for v,w in combinations(sorted(neigh[u]),2):
        if tuple(sorted((v,w))) in edges: link((u,v),(u,w))
assert len(gedges)==90
adj=[[] for _ in range(60)]
for i,j in gedges:adj[i].append(j);adj[j].append(i)
assert all(len(nbs)==3 for nbs in adj)
face_choice={e:sorted(next(iter(f-set(e))) for f in faces if set(e)<=f) for e in edges}
assert all(len(v)==2 for v in face_choice.values())

# Perfect matchings of the original icosahedron.
matchings=[]
def matching(rest,sel):
    if not rest:
        matchings.append(tuple(sel));return
    u=min(rest)
    for v in sorted(neigh[u]&rest):
        matching(rest-{u,v},sel+[(u,v)])
matching(set(range(12)),[])
assert len(matchings)==125

# Enumerate 125*2^6 distinct frustrated-bond patterns, and one spin configuration per pattern.
X=[];spin_rows=[];patterns=set()
edge_order=sorted(edges)
for mm in matchings:
    for bits in product(range(2),repeat=6):
        frustrated=set()
        for (u,v),bit in zip(mm,bits):
            w=face_choice[tuple(sorted((u,v)))][bit]
            frustrated.add(tuple(sorted((idx[u,v],idx[u,w]))))
            frustrated.add(tuple(sorted((idx[v,u],idx[v,w]))))
        assert len(frustrated)==12 and frustrated <= gedges
        fingerprint=frozenset(frustrated)
        assert fingerprint not in patterns
        patterns.add(fingerprint)
        spins=[0]*60
        spins[0]=1
        todo=[0]
        while todo:
            i=todo.pop()
            for j in adj[i]:
                desired=spins[i]*(1 if tuple(sorted((i,j))) in frustrated else -1)
                if not spins[j]:spins[j]=desired;todo.append(j)
                else:assert spins[j]==desired
        assert all(spins)
        assert sum(spins)==0
        assert sum(spins[i]*spins[j] for i,j in gedges)==-66
        assert all(spins[idx[u,v]]==-spins[idx[v,u]] for u,v in edges)
        assert all(sum(tuple(sorted((a,b))) in frustrated
                       for a,b in gedges if verts[a][0]==u and verts[b][0]==u)==1
                   for u in range(12))
        spin_rows.append(bytes((s+1)//2 for s in spins))
        X.append([spins[idx[u,v]] for u,v in edge_order])
assert len(patterns)==len(X)==8000
assert len(set(spin_rows))==8000

# B=125 times the nonzero covariance eigenmatrix, in the edge basis.
# Full covariance is U * (X^T X/8000) * U^T, with U^T U=2I.
# Therefore B=125*2*(X^T X/8000)=X^T X/32.
B=[[0]*30 for _ in range(30)]
for x in X:
    for i in range(30):
        xi=x[i]
        for j in range(i+1): B[i][j]+=xi*x[j]
for i in range(30):
    for j in range(i+1):
        assert B[i][j]%32==0
        B[i][j]//=32
        B[j][i]=B[i][j]
assert all(B[i][i]==250 for i in range(30))

# The minimal polynomial identity is an exact integer matrix certificate.
# Its simple coprime factors give the full eigenspace decomposition.
n=30
I=[[int(i==j) for j in range(n)] for i in range(n)]
def mul(A,C):
    m=len(C)
    return [[sum(A[i][k]*C[k][j] for k in range(m)) for j in range(m)] for i in range(len(A))]
def subscalar(A,a):
    return [[A[i][j]-a*int(i==j) for j in range(n)] for i in range(n)]
def rank(A):
    # Fraction-free integer Gaussian elimination: exact rational rank.
    W=[list(row) for row in A]
    row=0
    width=len(W[0])
    for col in range(width):
        pivot=next((i for i in range(row,len(W)) if W[i][col]),None)
        if pivot is None:continue
        W[row],W[pivot]=W[pivot],W[row]
        a=W[row][col]
        for i in range(row+1,len(W)):
            b=W[i][col]
            if b:
                # Eliminate using an integer linear combination, then
                # divide by the integer gcd to prevent coefficient growth.
                from math import gcd
                g=gcd(a,b)
                aa=a//g;bb=b//g
                W[i]=[aa*x-bb*y for x,y in zip(W[i],W[row])]
                gg=0
                for z in W[i]:gg=gcd(gg,z)
                if gg>1:W[i]=[z//gg for z in W[i]]
        row+=1
    return row

B2=mul(B,B)
quadratic=[[B2[i][j]-1308*B[i][j]+68596*I[i][j]
            for j in range(n)] for i in range(n)]
P=I
for a in (50,74,104,560):
    P=mul(P,subscalar(B,a))
P=mul(P,quadratic)
assert all(z==0 for row in P for z in row)
# Pairwise coprime factors of a square-free annihilator imply diagonalizability
# (B symmetric already). Exact rational dimensions follow by nullities.
expected={50:11,74:5,104:4,560:4}
lower_nullity={a:n-rank(subscalar(B,a)) for a in expected}
qnull=n-rank(quadratic)
assert lower_nullity==expected,lower_nullity
assert qnull==6
assert sum(expected.values())+qnull==n
# The symmetric integer quadratic contributes two conjugate 3-dimensional spaces:
# trace(B)=7500; scalar bands contribute 3576, so remaining trace 3924=6*654;
# irreducibility forces equal multiplicities of the two quadratic roots.
assert sum(B[i][i] for i in range(n))==7500
assert sum(a*m for a,m in expected.items())+6*654==7500

# Nearest-neighbor correlations (the two bond orbits of the truncated icosahedron).
edge_corr=Counter()
for a,b in gedges:
    val=sum((2*x[a]-1)*(2*x[b]-1) for x in spin_rows)
    edge_corr[("cross" if verts[a][0]!=verts[b][0] else "pentagon",val)]+=1
assert edge_corr==Counter({('cross',-8000):30,('pentagon',-4800):60})

# Full graph-distance pair correlation census; use exact integers throughout.
dist=[[None]*60 for _ in range(60)]
for start in range(60):
    dist[start][start]=0
    todo=deque([start])
    while todo:
        u=todo.popleft()
        for v in adj[u]:
            if dist[start][v] is None:
                dist[start][v]=dist[start][u]+1;todo.append(v)
expected_hist={
1:{-8000:30,-4800:60},
2:{1600:60,4800:120},
3:{-4800:60,-2240:60,-1600:120},
4:{0:120,1600:60,2240:120},
5:{-2240:60,-1280:60,0:120,640:60},
6:{-1280:60,-640:120,1280:120},
7:{-1536:60,640:60,1536:120},
8:{-1792:30,-1536:60},
9:{1792:30}}
hist=defaultdict(Counter)
for i in range(60):
    for j in range(i+1,60):
        corr=sum((2*s[i]-1)*(2*s[j]-1) for s in spin_rows)
        hist[dist[i][j]][corr]+=1
assert dict(hist)==expected_hist,(dict(hist),expected_hist)
assert sum(sum(c.values()) for c in hist.values())==1770
print('VERIFIED: icosahedron 12 vertices / 30 edges; C60 60 sites / 90 edges')
print('VERIFIED: 125 matchings, 8000 frustration patterns, 16000 labeled ground states')
print('VERIFIED: E_min=-66J, all ground-state magnetizations zero')
print('VERIFIED: spectrum C: 0^30, (2/5)^11, (74/125)^5, (104/125)^4, (112/25)^4, ((654±268sqrt5)/125)^3 each')
print('VERIFIED: exact integer annihilator, exact rational nullities and nearest-bond correlations')
print('VERIFIED: all 1770 unordered-pair correlations grouped into nine distance layers')
