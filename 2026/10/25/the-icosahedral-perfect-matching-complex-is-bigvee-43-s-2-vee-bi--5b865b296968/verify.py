#!/usr/bin/env python3
"""Reconstruct and check the icosahedral perfect-matching complex; Python 3 standard library only."""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

# Twelve-vertex icosahedron: poles 0 and 11, two staggered pentagons.
V = range(12)
E = set()
def edge(a,b):
    assert a != b
    E.add(tuple(sorted((a,b))))
for i in range(5):
    t,b=1+i,6+i
    edge(0,t); edge(11,b)
    edge(t,1+(i+1)%5);edge(b,6+(i+1)%5)
    edge(t,b);edge(t,6+(i-1)%5)
edges=sorted(E)
assert len(edges)==30
neigh={v:set() for v in V}
for a,b in edges:neigh[a].add(b);neigh[b].add(a)
assert all(len(neigh[v])==5 for v in V)
edgeindex={e:i for i,e in enumerate(edges)}
perfs=[]
def generate(free, acc):
    if free==0:
        perfs.append(tuple(sorted(acc)));return
    u=(free&-free).bit_length()-1
    for v in sorted(neigh[u]):
        if free & (1<<v):
            generate(free^ (1<<u) ^ (1<<v), acc+(edgeindex[tuple(sorted((u,v)))],))
generate((1<<12)-1,())
assert len(perfs)==125 and len(set(perfs))==125

@lru_cache(None)
def count_pm(free):
    if not free:return 1
    u=(free&-free).bit_length()-1
    return sum(count_pm(free^(1<<u)^(1<<v)) for v in neigh[u] if free&(1<<v))
assert count_pm((1<<12)-1)==125

faces=set()
for match in perfs:
    mask=sum(1<<j for j in match)
    sub=mask
    while sub:
        faces.add(sub);sub=(sub-1)&mask
assert len(faces)==4055
sizes=Counter(f.bit_count() for f in faces)
assert [sizes[k] for k in range(1,7)]==[30,315,1260,1575,750,125]
def matchings_of_size(k):
    return sum(len({v for j in inds for v in edges[j]})==2*k
               for inds in combinations(range(30),k))
assert [matchings_of_size(k) for k in (1,2,3)]==[30,315,1400]
assert 1400-sizes[3]==140   # 140 size-three matchings are not extendable.

U=set(faces);pairs=[]
for i in range(len(edges)):
    bit=1<<i
    local=[(s,s|bit) for s in sorted(U) if not (s&bit) and (s|bit) in U]
    for a,b in local:
        assert a in U and b in U
        U.remove(a);U.remove(b)
    pairs.extend(local)
assert len(pairs)==1977
critical=Counter(s.bit_count()-1 for s in U)
assert critical=={0:1,2:62,3:38}

# Face boundary with lexicographically ascending vertex order.
def bdry(s):
    result=[]
    j=0; t=s
    while t:
        b=t&-t;t^=b
        result.append((s^b,1 if j%2==0 else -1));j+=1
    return result

matching=dict(pairs)
indeg={f:0 for f in faces};arrows={f:[] for f in faces}
num_inc=0
for s in faces:
    if s.bit_count()==1:continue
    for f,_ in bdry(s):
        if matching.get(f)==s:src,dst=f,s
        else:src,dst=s,f
        arrows[src].append(dst);indeg[dst]+=1;num_inc+=1
assert num_inc==15210
Q=deque(x for x in faces if indeg[x]==0)
processed=0
while Q:
    x=Q.popleft();processed+=1
    for y in arrows[x]:
        indeg[y]-=1
        if not indeg[y]:Q.append(y)
assert processed==len(faces), (processed,len(faces))

crit2=sorted(s for s in U if s.bit_count()==3)
crit3=sorted(s for s in U if s.bit_count()==4)
assert len(crit2)==62 and len(crit3)==38

@lru_cache(None)
def projection(s):
    if s in U:return {s:1}
    if s not in matching:return {}
    h=matching[s];eps=dict(bdry(h))[s]
    out=Counter()
    for f,coeff in bdry(h):
        if f==s:continue
        for key,value in projection(f).items():
            out[key]-=eps*coeff*value
    return {k:v for k,v in out.items() if v}

M=[]
for h in crit3:
    c=Counter()
    for f,coef in bdry(h):
        for key,value in projection(f).items():c[key]+=coef*value
    M.append([c.get(f,0) for f in crit2])
assert len(M)==38 and all(len(row)==62 for row in M)
assert sum(x!=0 for row in M for x in row)==240
assert max(abs(x) for row in M for x in row)==2

# Exact integral elementary operations. A +-1 pivot permits unimodular
# row and column eliminations, not merely rational or finite-field rank.
A=[row[:] for row in M]
R,C=len(A),len(A[0]);k=0
while k<min(R,C):
    pivot=next(((i,j) for i in range(k,R) for j in range(k,C) if abs(A[i][j])==1),None)
    if pivot is None:break
    i,j=pivot
    A[k],A[i]=A[i],A[k]
    for row in A:row[k],row[j]=row[j],row[k]
    if A[k][k]==-1:A[k]=[-x for x in A[k]]
    for i in range(R):
        if i!=k and A[i][k]:
            c=A[i][k]
            A[i]=[A[i][j]-c*A[k][j] for j in range(C)]
    for j in range(C):
        if j!=k and A[k][j]:
            c=A[k][j]
            for i in range(R):A[i][j]-=c*A[i][k]
    assert A[k][k]==1
    assert all(A[i][k]==0 for i in range(R) if i!=k)
    assert all(A[k][j]==0 for j in range(C) if j!=k)
    k+=1
assert k==19,(k,Counter(abs(x) for row in A for x in row))
assert all(A[i][j]==(1 if i==j and i<k else 0) for i in range(R) for j in range(C))

# Independent F_2 simplicial boundary rank check using bit-vector Gaussian elimination.
by_sz={j:sorted(s for s in faces if s.bit_count()==j) for j in range(1,7)}
def rank_mod2(sz):
    if sz==1:return 0
    pos={f:i for i,f in enumerate(by_sz[sz-1])}
    basis={}
    for s in by_sz[sz]:
        v=0
        for f,_ in bdry(s):v^=1<<pos[f]
        while v:
            lead=v.bit_length()-1
            if lead not in basis:basis[lead]=v;break
            v^=basis[lead]
    return len(basis)
ranks={sz:rank_mod2(sz) for sz in range(2,7)}
# reduced H_0=0: rank delta_1 on a connected 30-vertex complex is 29.
assert ranks=={2:29,3:286,4:931,5:625,6:125},ranks
betti2=len(by_sz[3])-ranks[3]-ranks[4]
betti3=len(by_sz[4])-ranks[4]-ranks[5]
assert (betti2,betti3)==(43,19)
print('GRAPH vertices=12 edges=30 perfect_matchings=125')
print('FACES total=4055 f_vector=(30,315,1260,1575,750,125)')
print('EXTENDABILITY all_315_two_edge_matchings=yes three_edge_nonextendable=140')
print('MORSE pairs=1977 critical=(1 vertex,62 degree-2,38 degree-3)')
print('ACYCLIC face_poset_vertices=4055 incidences=15210')
print('MORSE_BOUNDARY shape=38x62 nonzero=240 max_abs=2 integer_unit_pivots=19 remainder_zero=true')
print('SIMPLICIAL_MOD2_RANKS',ranks,'BETTI_2=43 BETTI_3=19')
print('HOMOTOPY wedge_43_S2 wedge_19_S3')
print('VERIFY_OK')
