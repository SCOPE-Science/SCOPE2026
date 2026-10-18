"""Exact finite verification of the Möbius–Kantor independence-homology character.
Requires numpy and networkx. Run: python verify.py
"""
from collections import Counter
from itertools import product
import numpy as np
import networkx as nx

N=8; V=16
EDGES={tuple(sorted(ab)) for ab in (
    {(i,(i+1)%N) for i in range(N)} |
    {(i,N+i) for i in range(N)} |
    {(N+i,N+(i+3)%N) for i in range(N)})}
G=nx.Graph();G.add_nodes_from(range(V));G.add_edges_from(EDGES)
assert len(EDGES)==24
NEIGH=[0]*V
for a,b in EDGES:
    NEIGH[a]|=1<<b;NEIGH[b]|=1<<a
FACES={d:[] for d in range(8)}
for face in range(1,1<<V):
    if all(not(face & (1<<i) and face&NEIGH[i]) for i in range(V)):
        FACES[face.bit_count()-1].append(face)
assert [len(FACES[d]) for d in range(8)]==[16,96,272,376,240,72,16,2]
INDEX={d:{mask:i for i,mask in enumerate(FACES[d])} for d in FACES}
AUT=[tuple(phi[i] for i in range(V)) for phi in
     nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter()]
assert len(AUT)==96 and len(set(AUT))==96

def image_and_sign(face,perm):
    vals=[perm[i] for i in range(V) if face & (1<<i)]
    sign=-1 if sum(x>y for i,x in enumerate(vals) for y in vals[i+1:])%2 else 1
    return sum(1<<i for i in vals), sign

def matrix(d,p):
    A=np.zeros((len(FACES[d-1]),len(FACES[d])),dtype=np.int64)
    for j,face in enumerate(FACES[d]):
        t=0
        for i in range(V):
            if face&(1<<i):
                A[INDEX[d-1][face^(1<<i)],j]=(-1)**t
                t+=1
    return A%p

def rref(A,p):
    A=A.copy()%p;m,n=A.shape;piv=[];r=0
    for c in range(n):
        choices=np.flatnonzero(A[r:,c])
        if not len(choices):continue
        j=r+int(choices[0]);A[[r,j]]=A[[j,r]]
        A[r]=A[r]*pow(int(A[r,c]),-1,p)%p
        rows=np.flatnonzero(A[:,c]);rows=rows[rows!=r]
        A[rows]=(A[rows]-A[rows,c,None]*A[r])%p
        piv.append(c);r+=1
        if r==m:break
    return A,piv

def fourth_character(p):
    D4=matrix(4,p);D5=matrix(5,p)
    R,piv=rref(D4,p)
    free=[j for j in range(len(FACES[4])) if j not in piv]
    B,cols=rref(D5.T,p)
    assert len(piv)==181 and len(cols)==58 and len(free)==59
    bas={col:B[i] for i,col in enumerate(cols)}
    def modbound(v):
        w=v.copy()%p
        for col,b in bas.items():
            w=(w-int(w[col])*b)%p
        return w
    z=None
    for j in free:
        v=np.zeros(len(FACES[4]),dtype=np.int64);v[j]=1
        for i,c in enumerate(piv):v[c]=(-int(R[i,j]))%p
        if np.any(modbound(v)):
            z=v;break
    assert z is not None and not np.any(D4@z%p)
    w=modbound(z)
    k=int(np.flatnonzero(w)[0]);denom=pow(int(w[k]),-1,p)
    signs=[]
    for perm in AUT:
        gz=np.zeros(len(FACES[4]),dtype=np.int64)
        for j,face in enumerate(FACES[4]):
            new,s=image_and_sign(face,perm)
            gz[INDEX[4][new]]=(gz[INDEX[4][new]]+s*int(z[j]))%p
        t=int(modbound(gz)[k]*denom%p)
        assert t in (1,p-1),t
        assert np.array_equal(modbound(gz),t*w%p)
        signs.append(1 if t==1 else -1)
    return signs

# Two distinct prime reductions; published integral homotopy implies H4 is Z,
# so its integral automorphism has sign ±1, uniquely determined by either prime.
CHI4=fourth_character(101)
assert CHI4==fourth_character(103)
BIP={i for i in range(8) if i%2==0}|{8+i for i in range(8) if i%2==1}
BETA=[1 if p[0] in BIP else -1 for p in AUT]
assert CHI4==BETA
LF=[]
for perm in AUT:
    acc=-1  # augmentation of the reduced simplicial chain complex
    for d,faces in FACES.items():
        for face in faces:
            new,sign=image_and_sign(face,perm)
            if new==face:acc+=(-1)**d*sign
    LF.append(acc)
CHI3=[a-l for a,l in zip(CHI4,LF)]
assert Counter(CHI3)==Counter({0:36,1:16,-1:16,-2:12,2:12,4:2,-4:2})
assert sum(x*x for x in CHI3)==192 and sum(CHI3)==0
assert sum(a*b for a,b in zip(CHI3,CHI4))==0
EIDX={edge:i for i,edge in enumerate(sorted(EDGES))}
def permutation_sign(perm):
    seen=set();cycles=0
    for i in range(len(perm)):
        if i not in seen:
            cycles+=1;j=i
            while j not in seen:
                seen.add(j);j=perm[j]
    return (-1)**(len(perm)-cycles)
EDGE_SIGN=[]
for perm in AUT:
    edge_perm=[EIDX[tuple(sorted((perm[a],perm[b])))] for a,b in sorted(EDGES)]
    EDGE_SIGN.append(permutation_sign(edge_perm))
LINE=[a*b for a,b in zip(BETA,EDGE_SIGN)]
assert sum(a*b for a,b in zip(LINE,CHI3))==96
REMAINDER=[a-b for a,b in zip(CHI3,LINE)]
assert sum(x*x for x in REMAINDER)==96 and 3 in REMAINDER
assert sum(REMAINDER)==0
# All 96 maps, 13 conjugacy classes, and all 1-dimensional characters checked.
IDENT=tuple(range(V));ids={p:i for i,p in enumerate(AUT)}
def compose(a,b):return tuple(a[b[i]] for i in range(V))
def order(a):
    p=IDENT
    for j in range(1,97):
        p=compose(p,a)
        if p==IDENT:return j
    raise AssertionError
orders=[order(g) for g in AUT]
assert Counter((orders[i],CHI4[i],CHI3[i]) for i in range(96))==Counter({
    (1,1,4):1,(2,1,4):1,(2,-1,0):6,(2,-1,2):12,
    (2,1,-2):12,(3,1,1):8,(4,-1,-4):2,(4,1,0):6,
    (6,1,1):8,(8,-1,0):12,(8,1,0):12,(12,-1,-1):16})
# Match the known order-eight cyclic restriction without using it in the computation.
rotation=tuple((i+1)%8 if i<8 else 8+(i+1)%8 for i in range(16))
assert rotation in ids
powers=[IDENT]
for i in range(7):powers.append(compose(rotation,powers[-1]))
assert [CHI3[ids[g]] for g in powers]==[4,0,0,0,4,0,0,0]
assert [CHI4[ids[g]] for g in powers]==[1,-1,1,-1,1,-1,1,-1]
print('PASS: 1090 nonempty faces, 96 automorphisms, two-prime H4 quotient tests')
print('PASS: full H3/H4 characters, 12 trace/order groups, and C8 restriction')
print('PASS: H4=bipartition sign; H3=(bipartition*edge sign) plus irreducible 3D')
