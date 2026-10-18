#!/usr/bin/env python3
"""Reconstruct exact chain and support certificates for a Shrikhande graph complex.

Usage: python3 artifacts/verify.py (SymPy required).  No external data files.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

V = tuple(range(16))
STEPS = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}

def edge(a,b):
    x,y = divmod(a,4)
    u,v = divmod(b,4)
    return ((x-u)%4,(y-v)%4) in STEPS

EDGES = {p for p in combinations(V,2) if edge(*p)}
assert len(EDGES) == 48
assert all(sum(edge(a,b) for b in V) == 6 for a in V)
assert all(sum(edge(a,k) and edge(b,k) for k in V)==2
           for a,b in combinations(V,2))

F = {k: [p for p in combinations(V,k)
         if all((a,b) not in EDGES for a,b in combinations(p,2))]
     for k in (1,2,3,4)}
assert [len(F[k]) for k in (1,2,3,4)] == [16,72,96,16]
IX = {k: {p:j for j,p in enumerate(F[k])} for k in (1,2,3,4)}

def boundary(k):
    a = zeros(len(F[k-1]),len(F[k]))
    for j,p in enumerate(F[k]):
        for i in range(k):
            a[IX[k-1][p[:i]+p[i+1:]],j] = (-1)**i
    return a

B2, B3 = boundary(3), boundary(4)
assert B2*B3 == zeros(72,16)
assert (B2.rank(),B3.rank()) == (57,16)

def smith_nonzero(a):
    d = smith_normal_form(a,domain=ZZ)
    return sorted(abs(int(d[i,i])) for i in range(min(d.rows,d.cols)) if d[i,i])

assert smith_nonzero(B3) == [1]*16
# Thus integral H2 is free of rank (96-57-16)=23.

OCT = []
for W in combinations(V,6):
    e = [p for p in combinations(W,2) if p in EDGES]
    if len(e)==3 and len(set.union(*(set(pair) for pair in e)))==6:
        OCT.append((W,tuple(sorted(e))))
assert len(OCT) == 32

def oct_cycle(pairs):
    out = zeros(96,1)
    for choice in product((0,1),repeat=3):
        ordered = tuple(pairs[i][choice[i]] for i in range(3))
        inversions = sum(ordered[i]>ordered[j]
                         for i in range(3) for j in range(i+1,3))
        face = tuple(sorted(ordered))
        out[IX[3][face],0] = (-1)**(sum(choice)+inversions)
    return out

Z = zeros(96,32)
for j,(W,pairs) in enumerate(OCT):
    z = oct_cycle(pairs)
    assert B2*z == zeros(72,1)
    Z[:,j] = z

# Every affine map with a connection-set-preserving linear part is an automorphism.
LINEAR=[]
for a,b,c,d in product(range(4),repeat=4):
    if (a*d-b*c)%2 != 1: continue
    T = lambda x,y: ((a*x+b*y)%4,(c*x+d*y)%4)
    if {T(*s) for s in STEPS} == STEPS:
        LINEAR.append((a,b,c,d))
assert len(LINEAR)==12
PERMS=[]
for t in V:
    xx,yy=divmod(t,4)
    for a,b,c,d in LINEAR:
        p=tuple(4*((a*(i//4)+b*(i%4)+xx)%4)
                  + ((c*(i//4)+d*(i%4)+yy)%4) for i in V)
        assert all(edge(i,j)==edge(p[i],p[j]) for i,j in combinations(V,2))
        PERMS.append(p)
assert len(set(PERMS)) == 192
OSET={W for W,_ in OCT}
representative=OCT[0][0]
assert {tuple(sorted(p[i] for i in representative)) for p in PERMS} == OSET

M = B3.row_join(Z)
assert smith_nonzero(B3.row_join(Z[:,:1])) == [1]*17
assert smith_nonzero(M) == [1]*38 + [2]
# Since the kernel of an integer boundary is primitive in C2,
# this Smith sequence proves index exactly two in integral H2.

# Finite flag-complex support census in characteristic two.
TMASK=[sum(1<<v for v in p) for p in F[3]]
QM = [(sum(1<<v for v in p),
       sum(1<<IX[3][p[:i]+p[i+1:]] for i in range(4))) for p in F[4]]
BM=[]
for p in F[3]:
    BM.append(sum(1<<IX[2][p[:i]+p[i+1:]] for i in range(3)))

def add_to_binary_basis(v,basis):
    while v:
        pivot=v.bit_length()-1
        if pivot in basis:
            v^=basis[pivot]
        else:
            basis[pivot]=v
            return True
    return False

def h2_mod2(W):
    mask=sum(1<<i for i in W)
    piv={}; ntri=0
    for tr,b in zip(TMASK,BM):
        if tr&mask != tr: continue
        ntri+=1
        add_to_binary_basis(b,piv)
    ker=ntri-len(piv)
    piv3={}
    for tetr, bd in QM:
        if tetr&mask == tetr:
            add_to_binary_basis(bd,piv3)
    return ker-len(piv3)

SIX=Counter()
for W in combinations(V,6):
    k=h2_mod2(W)
    assert k in (0,1)
    SIX[k]+=1
    assert (k==1)==(W in OSET)
assert SIX=={0:7976,1:32}

SEVEN=Counter()
for W in combinations(V,7):
    k=h2_mod2(W)
    SEVEN[k]+=1
    numoct=sum(set(O).issubset(W) for O in OSET)
    assert numoct in (0,1)
    assert k==numoct
assert SEVEN=={0:11120,1:320}
# The unique inherited octahedron survives globally mod two because
# adjoining any one octahedral column raises rank of B3 over F2.
piv={}
for j in range(B3.cols):
    word=sum(1<<i for i in range(96) if B3[i,j]%2)
    assert add_to_binary_basis(word,piv)
assert add_to_binary_basis(sum(1<<i for i in range(96) if Z[i,0]%2),piv)

W=(0,1,2,4,7,9,10,11)
TRIANGLES=[
 (0,2,10),(0,2,11),(0,7,9),(0,7,10),(0,9,11),(1,4,10),
 (1,4,11),(1,7,9),(1,7,10),(1,9,11),(2,4,10),(2,4,11)]
SIGNS=[1,-1,1,-1,1,-1,1,-1,1,-1,1,-1]
ZW=zeros(96,1)
for tri,s in zip(TRIANGLES,SIGNS):
    assert tri in IX[3]
    ZW[IX[3][tri],0]=s
assert B2*ZW==zeros(72,1)

# Reconstruct the induced complex and perform two elementary collapses.
WSET=set(W)
FACES={p for k in range(1,5) for p in F[k] if set(p)<=WSET}
assert [sum(len(p)==k for p in FACES) for k in range(1,5)]==[8,19,14,1]
def collapse(coface,free):
    assert coface in FACES and free in FACES
    assert len(coface)==len(free)+1 and set(free)<set(coface)
    assert [c for c in FACES if len(c)>len(free) and set(free)<set(c)]==[coface]
    FACES.remove(coface)
    FACES.remove(free)
collapse((0,2,9,11),(0,2,9))
collapse((2,9,11),(2,9))
assert [sum(len(p)==k for p in FACES) for k in range(1,5)]==[8,18,12,0]
assert {p for p in FACES if len(p)==3}==set(TRIANGLES)

# This closed, connected 2-manifold has Euler characteristic 2.
EDGE_TRI=defaultdict(list)
for tri in TRIANGLES:
    for edge_pair in combinations(tri,2):
        EDGE_TRI[edge_pair].append(tri)
assert len(EDGE_TRI)==18 and all(len(v)==2 for v in EDGE_TRI.values())
# The final sphere's full one-skeleton must be connected.
adjacency=defaultdict(set)
for a,b in EDGE_TRI:
    adjacency[a].add(b);adjacency[b].add(a)
reached={W[0]}; frontier=[W[0]]
while frontier:
    u=frontier.pop()
    for v in adjacency[u]:
        if v not in reached:reached.add(v);frontier.append(v)
assert reached==set(W)
for vertex in W:
    graph=defaultdict(set)
    for tri in TRIANGLES:
        if vertex not in tri: continue
        a,b=tuple(v for v in tri if v!=vertex)
        graph[a].add(b);graph[b].add(a)
    assert len(graph)>=3 and all(len(graph[v])==2 for v in graph)
    seen={next(iter(graph))}; pending=list(seen)
    while pending:
        v=pending.pop()
        for w in graph[v]:
            if w not in seen:seen.add(w);pending.append(w)
    assert len(seen)==len(graph)
assert 8-18+12==2
assert smith_nonzero(M.row_join(ZW))==[1]*39
print('VERIFY_OK SHRIKHANDE_16_48 F_VECTOR_16_72_96_16 H2_Z23')
print('32_OCTAHEDRAL_MINIMUM_CARRIERS ONE_AFFINE_ORBIT_192')
print('SMITH_B3_16_ONES SMITH_B3_PLUS_32_38_ONES_ONE_TWO INDEX2')
print('SEVEN_VERTEX_H2_PROFILE_11120_ZERO_320_ONE UNIQUE_OCT')
print('EIGHT_VERTEX_WITNESS_COLLAPSES_TO_S2 INTEGRAL_SPAN_39_UNITS')
