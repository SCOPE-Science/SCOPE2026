#!/usr/bin/env python3
"""Exact finite verification of icosahedral matching-complex homology symmetries.
Dependencies: networkx, sympy. No stored tables or network access required.
"""
import collections
import functools
import math
import random
from collections import defaultdict, deque
import networkx as nx
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

G=nx.icosahedral_graph()
assert len(G)==12 and G.number_of_edges()==30
E=sorted(tuple(sorted(edge)) for edge in G.edges())
edge_index={frozenset(e):i for i,e in enumerate(E)}
faces_with_occupied=[(0,0)]
for i,(u,v) in enumerate(E):
    occupied=(1<<u)|(1<<v)
    faces_with_occupied += [
        (f|(1<<i),seen|occupied)
        for f,seen in faces_with_occupied if not seen&occupied
    ]
faces={f for f,_ in faces_with_occupied}
face_counts=collections.Counter(f.bit_count()-1 for f in faces)
assert len(faces)==5888
assert tuple(face_counts[i] for i in range(-1,6))==(1,30,315,1400,2535,1482,125)

# A vertex-by-vertex matching, with the fixed shuffle seed part of the definition.
order=list(range(30)); random.Random(209).shuffle(order)
unpaired=set(faces); pairs=[]
for i in order:
    bit=1<<i
    for f in list(unpaired):
        u=f|bit
        if not f&bit and u in unpaired:
            unpaired.remove(f); unpaired.remove(u); pairs.append((f,u))
assert len(pairs)==2889 and len(unpaired)==110
critical3=sorted(f for f in unpaired if f.bit_count()==4)
critical4=sorted(f for f in unpaired if f.bit_count()==5)
assert len(critical3)==87 and len(critical4)==23
assert len(critical3)+len(critical4)==len(unpaired)
paired_up={l:u for l,u in pairs}

def signed_boundary(f):
    bits=[i for i in range(30) if f&(1<<i)]
    return [(f^(1<<i),1 if j%2==0 else -1) for j,i in enumerate(bits)]

# Full augmented Hasse diagram acyclicity, not merely a sample check.
adj={f:[] for f in faces};indeg={f:0 for f in faces};incidences=0
for u in faces:
    for lower,_ in signed_boundary(u):
        incidences+=1
        source,target=(lower,u) if paired_up.get(lower)==u else (u,lower)
        adj[source].append(target); indeg[target]+=1
q=deque(f for f in faces if indeg[f]==0);visited=0
while q:
    f=q.popleft();visited+=1
    for v in adj[f]:
        indeg[v]-=1
        if indeg[v]==0:q.append(v)
assert visited==len(faces)

idx3={f:i for i,f in enumerate(critical3)}
idx4={f:i for i,f in enumerate(critical4)}
lower3={l:u for l,u in pairs if l.bit_count()==4}
lower4={l:u for l,u in pairs if l.bit_count()==5}

@functools.lru_cache(None)
def proj3(f):
    if f in idx3:return {idx3[f]:1}
    u=lower3.get(f)
    if u is None:return {}
    bd=dict(signed_boundary(u)); pivot=bd[f]
    ans=defaultdict(int)
    for lower,c in bd.items():
        if lower==f:continue
        for j,v in proj3(lower).items():ans[j]-=c*pivot*v
    return {j:v for j,v in ans.items() if v}

@functools.lru_cache(None)
def proj4(f):
    if f in idx4:return {idx4[f]:1}
    u=lower4.get(f)
    if u is None:return {}
    bd=dict(signed_boundary(u));pivot=bd[f]
    ans=defaultdict(int)
    for lower,c in bd.items():
        if lower==f:continue
        for j,v in proj4(lower).items():ans[j]-=c*pivot*v
    return {j:v for j,v in ans.items() if v}

columns=[]
for t in critical4:
    col=defaultdict(int)
    for lower,c in signed_boundary(t):
        for j,v in proj3(lower).items():col[j]+=c*v
    columns.append([col.get(i,0) for i in range(len(critical3))])
B=Matrix(columns).T
assert B.shape==(87,23)
D=smith_normal_form(B,domain=ZZ)
nonzero=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
assert sorted(nonzero)==[1]*22+[3]


# Independent integer maximal minor certificate: 23 independent rows modulo 101,
# followed by a fraction-free exact integer determinant.
rows_mod101=[[int(B[i,j])%101 for i in range(87)] for j in range(23)]
rr=0;chosen_rows=[]
for col in range(87):
    pivot=next((i for i in range(rr,23) if rows_mod101[i][col]),None)
    if pivot is None:continue
    rows_mod101[rr],rows_mod101[pivot]=rows_mod101[pivot],rows_mod101[rr]
    inv=pow(rows_mod101[rr][col],-1,101)
    rows_mod101[rr]=[(x*inv)%101 for x in rows_mod101[rr]]
    for r in range(rr+1,23):
        coeff=rows_mod101[r][col]
        if coeff:
            rows_mod101[r]=[(x-coeff*y)%101 for x,y in zip(rows_mod101[r],rows_mod101[rr])]
    chosen_rows.append(col);rr+=1
    if rr==23:break
assert len(chosen_rows)==23
minor=B.extract(chosen_rows,list(range(23)))
minor_det=int(minor.det(method="bareiss"))
assert minor_det%3==0 and minor_det!=0
# An adjacent basis exchange often gives a primitive 3-minor.
minor_inv=minor.inv()
for candidate in range(87):
    if candidate in chosen_rows:continue
    row=B.row(candidate)
    coordinates=row*minor_inv
    swap=next((j for j,x in enumerate(coordinates) if abs(int(x*minor_det))==3),None)
    if swap is not None:
        chosen_rows[swap]=candidate
        minor=B.extract(chosen_rows,list(range(23)))
        minor_det=int(minor.det(method="bareiss"))
        break
assert abs(minor_det)==3

# Verify projected cellular boundary commutes with the simplicial boundary
# on *every* 4-simplex, independently of any equivariance calculation.
for f in (x for x in faces if x.bit_count()==5):
    lhs=defaultdict(int);rhs=defaultdict(int)
    for lower,c in signed_boundary(f):
        for i,v in proj3(lower).items():lhs[i]+=c*v
    for j,v in proj4(f).items():
        for i in range(87):
            if B[i,j]:rhs[i]+=int(B[i,j])*v
    assert all(lhs.get(i,0)==rhs.get(i,0) for i in range(87))

# Classify all automorphisms as rotations and orientation-reversing symmetries.
planar,embedding=nx.check_planarity(G)
assert planar
autos=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
assert len(autos)==120
antipode={v:next(w for w in G if nx.shortest_path_length(G,v,w)==3) for v in G}
assert all(antipode[antipode[v]]==v for v in G)
assert any(all(a[v]==antipode[v] for v in G) for a in autos)
assert all(antipode[a[v]]==a[antipode[v]] for a in autos for v in G)
reference=list(embedding.neighbors_cw_order(0))
def orientation(a):
    mapped=[a[v] for v in reference]
    nb=list(embedding.neighbors_cw_order(a[0]));start=nb.index(mapped[0])
    if all(mapped[i]==nb[(start+i)%5] for i in range(5)):
        sign=1
    else:
        assert all(mapped[i]==nb[(start-i)%5] for i in range(5))
        sign=-1
    for vertex in G:
        local=list(embedding.neighbors_cw_order(vertex))
        transformed=[a[v] for v in local]
        target=list(embedding.neighbors_cw_order(a[vertex]))
        start_at=target.index(transformed[0])
        assert all(transformed[i]==target[(start_at+sign*i)%5] for i in range(5))
    return sign
assert orientation(antipode)==-1

def perm_order(a):
    out=1
    for x in G:
        y=a[x]; length=1
        while y!=x:y=a[y];length+=1
        out=math.lcm(out,length)
    return out

def image_face(f,p):
    mapped=[p[i] for i in range(30) if f&(1<<i)]
    parity=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))%2
    return sum(1<<j for j in mapped),(-1 if parity else 1)

def edge_perm(a):
    return {i:edge_index[frozenset((a[u],a[v]))] for i,(u,v) in enumerate(E)}

def classkey(a):
    sign=orientation(a)
    rotation=a if sign==1 else {v:antipode[a[v]] for v in G}
    return (sign,perm_order(rotation))

# Rational H_3 is the only reduced rational homology; its trace equals
# negative the *augmented* signed Lefschetz alternating face trace.
characters=defaultdict(set);class_sizes=collections.Counter()
for a in autos:
    p=edge_perm(a)
    L=-1 # empty face, degree -1
    for f in faces:
        if not f:continue
        mapped,sgn=image_face(f,p)
        if mapped==f:L+=sgn * (-1 if f.bit_count()%2==0 else 1)
    key=classkey(a)
    class_sizes[key]+=1
    characters[key].add(-L)
assert all(len(v)==1 for v in characters.values())
assert dict(class_sizes)=={(1,1):1,(1,2):15,(1,3):20,(1,5):24,
                           (-1,1):1,(-1,2):15,(-1,3):20,(-1,5):24}
assert {k:next(iter(v)) for k,v in characters.items()}=={
 (1,1):64,(1,2):0,(1,3):-2,(1,5):-1,
 (-1,1):16,(-1,2):0,(-1,3):-2,(-1,5):1}

# Compute the unique mod-3 critical 4-cycle (the Bockstein antecedent
# of the order-three summand in integral H_3).
def rref_mod3(rows):
    A=[[int(x)%3 for x in row] for row in rows]
    rr=0;pivots=[];cols=len(A[0])
    for cc in range(cols):
        pivot=next((j for j in range(rr,len(A)) if A[j][cc]),None)
        if pivot is None:continue
        A[rr],A[pivot]=A[pivot],A[rr]
        inv=pow(A[rr][cc],-1,3)
        A[rr]=[(inv*x)%3 for x in A[rr]]
        for j in range(len(A)):
            if j!=rr and A[j][cc]:
                mult=A[j][cc]
                A[j]=[(x-mult*y)%3 for x,y in zip(A[j],A[rr])]
        pivots.append(cc);rr+=1
    return A,pivots

matrix_mod3=[[int(B[i,j])%3 for j in range(23)] for i in range(87)]
reduced,pivots=rref_mod3(matrix_mod3)
assert len(pivots)==22
free=next(j for j in range(23) if j not in pivots)
ker=[0]*23;ker[free]=1
for i,c in enumerate(pivots):ker[c]=(-reduced[i][free])%3
assert all(sum(row[j]*ker[j] for j in range(23))%3==0 for row in matrix_mod3)

# A lift to a genuine 4-cycle of the original complex mod 3.
# Gradient arrows lower3 -> other3 on boundaries of their matched 4-cells.
local_adj={f:set() for f in lower3};local_indeg={f:0 for f in lower3}
for f,u in lower3.items():
    for other,_ in signed_boundary(u):
        if other!=f and other in lower3 and other not in local_adj[f]:
            local_adj[f].add(other);local_indeg[other]+=1
q=deque(f for f in lower3 if local_indeg[f]==0)
order3=[]
while q:
    f=q.popleft();order3.append(f)
    for other in local_adj[f]:
        local_indeg[other]-=1
        if local_indeg[other]==0:q.append(other)
assert len(order3)==len(lower3)
chain4=defaultdict(int,{f:ker[i] for i,f in enumerate(critical4)})
chain3=defaultdict(int)
for f,co in chain4.items():
    for lower,c in signed_boundary(f):chain3[lower]=(chain3[lower]+co*c)%3
for f in order3:
    v=chain3[f]
    if not v:continue
    u=lower3[f];pivot=dict(signed_boundary(u))[f]
    coefficient=(-v*pivot)%3
    chain4[u]=(chain4[u]+coefficient)%3
    for lower,c in signed_boundary(u):chain3[lower]=(chain3[lower]+coefficient*c)%3
assert all(x%3==0 for x in chain3.values())
assert sum(bool(x%3) for x in chain4.values())==1009

# The projection P4 takes every mod-3 4-cycle to ker B. This induces
# an isomorphism H_4(F3) -> ker B, since there are no critical 5-cells.
# Natural UCT identifies H_4(F3) with Tor(H_3(Z),F3).
torsion_action=defaultdict(set)
for a in autos:
    p=edge_perm(a)
    transformed=[0]*23
    for f,co in chain4.items():
        if co%3==0:continue
        image,sgn=image_face(f,p)
        for j,v in proj4(image).items():transformed[j]=(transformed[j]+co*sgn*v)%3
    scale=next((s for s in (1,2) if all((transformed[i]-s*ker[i])%3==0 for i in range(23))),None)
    assert scale is not None
    torsion_action[classkey(a)].add(1 if scale==1 else -1)
assert {k:next(iter(v)) for k,v in torsion_action.items()}=={
 (1,1):1,(1,2):1,(1,3):1,(1,5):1,
 (-1,1):-1,(-1,2):-1,(-1,3):-1,(-1,5):-1}

# Decompose the rational character into the rational A5 modules
# V4, V5, V6 (V6 = 3 + 3' over Q), separately by antipodal parity.
# Inverse weighted inner products with A5 character rows:
# [1, 2A, 3A, 5A, 5B] (sizes 1,15,20,12,12).
for parity,expected in [(1,(2,4,2)),(-1,(2,2,1))]:
    plusminus=[]
    for order_ in (1,2,3,5):
        ep=next(iter(characters[(1,order_)])); em=next(iter(characters[(-1,order_)]))
        plusminus.append((ep+parity*em)//2)
    assert all((next(iter(characters[(1,o)]))+parity*next(iter(characters[(-1,o)])))%2==0 for o in (1,2,3,5))
    assert plusminus==([40,0,-2,0] if parity==1 else [24,0,0,-1])
    chars=[[4,0,1,-1],[5,1,-1,0],[6,-2,0,1]]
    multiplicities=[]
    for ch in chars:
        raw=sum(s*c*v for s,c,v in zip((1,15,20,24),ch,plusminus))
        # A5 6-dimensional rational constituent pairs the two complex 3's;
        # its inner product is twice its rational multiplicity.
        divisor=120 if ch[0]==6 else 60
        assert raw%divisor==0
        multiplicities.append(raw//divisor)
    assert tuple(multiplicities)==expected
print('ICOSAHEDRAL_MATCHING_EQUIVARIANT_EXACT_OK')
print('faces=5888; incidences=%d; acyclic_pairs=%d; critical_3=87; critical_4=23' % (incidences,len(pairs)))
print('morse_smith=22x1,1x3; minor_det=%d; H3Z=Z^64+Z/3; H4Z=0' % minor_det)
print('rational_A5_even=2V4+4V5+2V6; rational_A5_odd=2V4+2V5+V6')
print('antipodal_rational_trace=16; antipodal_even=40; antipodal_odd=24')
print('integral_3_torsion_action=orientation_character; 120_of_120_symmetries_checked')
print('mod3_generator_support=1009; exact_chainmap_4_cells=1482')
