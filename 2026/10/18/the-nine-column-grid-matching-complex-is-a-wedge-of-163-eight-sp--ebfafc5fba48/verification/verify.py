#!/usr/bin/env python3
"""Exact integral discrete-Morse certificate checker for a nine-column strip grid.

Run with Python 3.10+: python verify.py . No external Python packages required.
The checker regenerates the pivot tree, critical cells, signed Morse boundary,
an explicit unimodular minor, and an independent matching-polynomial count.
"""
import json
from pathlib import Path
from functools import lru_cache
from collections import Counter

CERT = json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf-8'))
N = 9
edges = []
for col in range(N):
    for row in range(2):
        edges.append((3*col+row, 3*col+row+1))
    if col+1<N:
        for row in range(3):
            edges.append((3*col+row, 3*(col+1)+row))
assert edges == [tuple(pair) for pair in CERT['graph_edges']]
m = len(edges)
assert m == 42
adj = []
for i,(u,v) in enumerate(edges):
    adj.append(sum(1<<j for j,(s,t) in enumerate(edges)
                   if j!=i and (u in (s,t) or v in (s,t))))
full = (1<<m)-1
policy = {}

@lru_cache(None)
def count_critical(A):
    if not A:
        return (1,)
    candidates=[]
    left=A
    while left:
        q=left&-left;left-=q;i=q.bit_length()-1;neighbors=adj[i]&A
        if not neighbors:
            policy[A]=i
            return ()
        score=(neighbors.bit_count(),
               -sum((adj[j]&A).bit_count() for j in range(m) if neighbors>>j&1),i)
        candidates.append((score,i))
    p=min(candidates)[1]
    policy[A]=p
    neighbors=adj[p]&A;earlier=0;hist=Counter()
    while neighbors:
        b=neighbors&-neighbors;neighbors-=b;q=b.bit_length()-1
        sub=A&~((1<<p)|earlier|b|adj[q])
        for k,c in enumerate(count_critical(sub)):
            if c:
                hist[k+1]+=c
        earlier |= b
    return tuple(hist[i] for i in range(max(hist,default=-1)+1))

assert count_critical(full) == (0,)*9+(182,19)
assert {str(A):p for A,p in policy.items()} == CERT['policy']
critical=[]
def gather(A,forced):
    if not A:
        critical.append(forced)
        return
    p=policy[A];neighbors=adj[p]&A;earlier=0
    while neighbors:
        b=neighbors&-neighbors;neighbors-=b;q=b.bit_length()-1
        gather(A&~((1<<p)|earlier|b|adj[q]),forced|b)
        earlier |= b
gather(full,0)
crit8=sorted(v for v in critical if v.bit_count()==9)
crit9=sorted(v for v in critical if v.bit_count()==10)
assert crit8 == CERT['critical_8simplices']
assert crit9 == CERT['critical_9simplices']
assert len(critical) == 201 and len(set(critical)) == 201
indices={v:i for i,v in enumerate(crit8)}

@lru_cache(600000)
def pair(F):
    A=full
    while A:
        p=policy[A];bit=1<<p
        if F&bit:
            return (F^bit,1)  # paired upper simplex
        B=adj[p]&A;chosen=F&B
        if not chosen:
            return (F|bit,-1) # paired lower simplex
        b=chosen&-chosen
        A &= ~((1<<p)|(B&(b-1))|b|adj[b.bit_length()-1])
    return (0,0)

def boundary_sign(face,upper):
    b=upper^face
    assert b.bit_count()==1
    return (-1) if (upper&(b-1)).bit_count()%2 else 1

@lru_cache(1200000)
def reduce8(F):
    if F in indices:
        return {indices[F]:1}
    U,position=pair(F)
    if position==1:
        return {}
    assert position==-1
    result=Counter();coefficient=-boundary_sign(F,U)
    mask=U
    while mask:
        b=mask&-mask;mask-=b;G=U^b
        if G==F:
            continue
        sign=coefficient*boundary_sign(G,U)
        for i,v in reduce8(G).items():
            result[i]+=sign*v
    return {i:v for i,v in result.items() if v}

columns=[]
for top in crit9:
    boundary=Counter();mask=top
    while mask:
        b=mask&-mask;mask-=b;F=top^b
        for i,v in reduce8(F).items():
            boundary[i]+=boundary_sign(F,top)*v
    columns.append({i:v for i,v in boundary.items() if v})
assert columns == [{int(i):v for i,v in col.items()} for col in CERT['boundary_columns']]
assert sum(len(col) for col in columns)==159

# The given 19-by-19 determinant is evaluated over Z by exact Bareiss elimination.
def determinant_bareiss(M):
    A=[list(row) for row in M]
    n=len(A);sign=1;previous=1
    for k in range(n-1):
        if A[k][k]==0:
            for j in range(k+1,n):
                if A[j][k]:
                    A[j],A[k]=A[k],A[j]
                    sign=-sign
                    break
            else:
                return 0
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=pivot*A[i][j]-A[i][k]*A[k][j]
                assert numerator%previous==0
                A[i][j]=numerator//previous
        for i in range(k+1,n):
            A[i][k]=0
        previous=pivot
    return sign*A[-1][-1]
rows=CERT['unit_minor_rows']
assert len(rows)==19 and len(set(rows))==19 and all(0<=i<182 for i in rows)
minor=[[columns[j].get(i,0) for j in range(19)] for i in rows]
assert determinant_bareiss(minor)==CERT['unit_minor_det']==1

# Independent column-by-column matching polynomial of the strip, using eight
# boundary occupancy masks and all possible nonoverlapping vertical dimers.
state={(0,0):1}
for col in range(N):
    nxt=Counter()
    for (incoming,number),multiplicity in state.items():
        for vertical in (0,0b011,0b110):
            if incoming&vertical:
                continue
            free=0b111&~(incoming|vertical)
            outgoing=free
            while True:
                if col<N-1 or outgoing==0:
                    nxt[(outgoing,number+(vertical!=0)+outgoing.bit_count())]+=multiplicity
                if outgoing==0:break
                outgoing=(outgoing-1)&free
    state=nxt
face_vector=[0]*14
for (outgoing,k),v in state.items():
    assert outgoing==0
    face_vector[k]+=v
assert face_vector == CERT['matching_face_vector_including_empty']
assert sum(face_vector)==7594361
assert -sum((-1)**i*v for i,v in enumerate(face_vector)) == CERT['reduced_euler_characteristic']==163

print('PASS: 3x9 grid; 42 graph edges; 7,594,361 matching faces including empty')
print('PASS: acyclic pivot/first-neighbor matching tree; 182 critical 8-cells, 19 critical 9-cells')
print('PASS: signed integer Morse boundary, 182 x 19; 159 nonzero coefficients')
print('PASS: explicit 19x19 minor has determinant +1; homotopy wedge of 163 eight-spheres')
print('PASS: independently computed matching polynomial and reduced Euler characteristic 163')
