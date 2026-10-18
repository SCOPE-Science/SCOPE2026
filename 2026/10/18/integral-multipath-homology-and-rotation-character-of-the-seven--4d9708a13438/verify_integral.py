#!/usr/bin/env python3
"""Exact integral discrete-Morse certificate for the 7-vertex cyclic-tournament multipath complex.
Run with Python >=3.9; standard library only.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache

n=7
arcs=[(a,b) for a in range(n) for b in range(n) if (b-a)%n in (1,2,3)]
assert len(arcs)==21
faces=[0]
for j,(a,b) in enumerate(arcs):
    newborn=[]
    for s in faces:
        outgoing=[-1]*n;incoming=[-1]*n
        for i,(u,v) in enumerate(arcs):
            if s&(1<<i):outgoing[u]=v;incoming[v]=u
        if outgoing[a]!=-1 or incoming[b]!=-1:continue
        cur=b
        while cur!=-1 and cur!=a:cur=outgoing[cur]
        if cur==-1:newborn.append(s|(1<<j))
    faces.extend(newborn)
face_set=set(faces)
assert len(face_set)==2927
fvector=Counter(s.bit_count()-1 for s in faces)
assert [fvector[k] for k in range(6)]==[21,168,630,1113,819,175]

# Sequential elementary vertex matchings on the unpaired faces.
critical=face_set-{0}; pairs=[]
for j in range(len(arcs)):
    pp=[(s,s|(1<<j)) for s in critical if not s&(1<<j) and s|(1<<j) in critical]
    for s,t in pp:
        critical.remove(s);critical.remove(t)
    pairs.extend(pp)
assert len(pairs)==(2926-96)//2==1415
c=Counter(s.bit_count()-1 for s in critical)
assert dict(c)=={0:1,3:24,4:54,5:17}
lower=dict(pairs);upper={t:s for s,t in pairs}

def boundary(s):
    x=s;j=0
    while x:
        bit=x&-x
        yield s^bit, (-1 if j%2 else 1)
        x-=bit;j+=1

# Verify the complete Hasse orientation is acyclic (matched arrows up, all others down).
indeg={s:0 for s in critical|set(lower)|set(upper)}
adj=defaultdict(list)
for s in faces:
    if s==0:continue
    for f,_ in boundary(s):
        if not f:continue
        a,b=(f,s) if lower.get(f)==s else (s,f)
        adj[a].append(b);indeg[b]+=1
q=deque(s for s,d in indeg.items() if d==0); visited=0
while q:
    s=q.popleft();visited+=1
    for t in adj[s]:
        indeg[t]-=1
        if indeg[t]==0:q.append(t)
assert visited==2926,('cycle detected',visited)

@lru_cache(None)
def flow(s):
    if s in critical:return {s:1}
    if s in upper:return {}
    assert s in lower
    top=lower[s]
    coeff=next(a for t,a in boundary(top) if t==s)
    out=defaultdict(int)
    for t,a in boundary(top):
        if t==s:continue
        for r,v in flow(t).items():out[r]-=coeff*a*v
    return {r:v for r,v in out.items() if v}

bydim=defaultdict(list)
for s in critical:bydim[s.bit_count()-1].append(s)
for k in bydim:bydim[k].sort()

def morse_matrix(k):
    rows=bydim[k-1];cols=bydim[k]
    ri={s:i for i,s in enumerate(rows)}
    A=[[0]*len(cols) for _ in rows]
    for j,s in enumerate(cols):
        for f,sgn in boundary(s):
            for r,v in flow(f).items():A[ri[r]][j]+=sgn*v
    return A
A=morse_matrix(4)
B=morse_matrix(5)
assert len(A)==24 and all(len(r)==54 for r in A)
assert len(B)==54 and all(len(r)==17 and not any(r) for r in B)

def exact_rank(A):
    b=[[Fraction(v) for v in row] for row in A]
    m=len(b);n=len(b[0]);rank=0
    for j in range(n):
        pivot=next((i for i in range(rank,m) if b[i][j]),None)
        if pivot is None:continue
        b[rank],b[pivot]=b[pivot],b[rank]
        v=b[rank][j]
        for i in range(rank+1,m):
            if b[i][j]:
                t=b[i][j]/v
                for h in range(j,n):b[i][h]-=t*b[rank][h]
        rank+=1
        if rank==m:break
    return rank
assert exact_rank(A)==11
minor_rows=[3,2,12,13,11,14,5,4,20,10,1]
minor_cols=[5,9,14,15,17,23,25,27,32,46,47]

def determinant(B):
    b=[row[:] for row in B]
    n=len(b);sign=1;prev=1
    for k in range(n-1):
        if b[k][k]==0:
            q=next((i for i in range(k+1,n) if b[i][k]),None)
            if q is None:return 0
            b[q],b[k]=b[k],b[q];sign=-sign
        p=b[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=b[i][j]*p-b[i][k]*b[k][j]
                assert num%prev==0
                b[i][j]=num//prev
        for i in range(k+1,n):b[i][k]=0
        prev=p
    return sign*b[n-1][n-1]
D=determinant([[A[i][j] for j in minor_cols] for i in minor_rows])
assert abs(D)==1
print('PASS: 2927 faces, 1415 Morse pairs, acyclic Hasse orientation')
print('Morse critical vector: one 0-cell; 24 3-cells; 54 4-cells; 17 5-cells')
print('Integral Morse boundary ranks: d4=11, d5=0; unimodular 11-minor:',D)
print('Reduced integral homology: H3=Z^13, H4=Z^43, H5=Z^17, all other zero')
