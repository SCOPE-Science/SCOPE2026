#!/usr/bin/env python3
from itertools import combinations, permutations, product
from collections import Counter, defaultdict, deque

FACETS = {
(1,2,3,4),(1,2,3,5),(1,2,4,6),(1,2,5,6),(1,3,4,7),(1,3,5,7),
(1,4,6,8),(1,4,7,9),(1,4,8,9),(1,5,6,10),(1,5,7,11),(1,5,10,12),
(1,5,11,12),(1,6,8,10),(1,7,9,11),(1,8,9,12),(1,8,10,12),(1,9,11,12),
(2,3,4,13),(2,3,5,8),(2,3,8,10),(2,3,10,11),(2,3,11,13),(2,4,6,14),
(2,4,13,14),(2,5,6,9),(2,5,8,9),(2,6,7,12),(2,6,7,14),(2,6,9,12),
(2,7,10,11),(2,7,10,12),(2,7,11,13),(2,7,13,14),(2,8,9,12),(2,8,10,12),
(3,4,7,12),(3,4,12,13),(3,5,7,8),(3,6,7,12),(3,6,7,14),(3,6,11,13),
(3,6,11,14),(3,6,12,13),(3,7,8,14),(3,8,10,14),(3,10,11,14),(4,5,8,9),
(4,5,8,11),(4,5,9,10),(4,5,10,12),(4,5,11,12),(4,6,8,11),(4,6,11,14),
(4,7,9,10),(4,7,10,12),(4,11,12,14),(4,12,13,14),(5,6,9,10),(5,7,8,11),
(6,8,10,13),(6,8,11,13),(6,9,10,13),(6,9,12,13),(7,8,11,13),
(7,8,13,14),(7,9,10,11),(8,10,13,14),(9,10,11,14),(9,10,13,14),
(9,11,12,14),(9,12,13,14)
}
V=tuple(range(1,15))

def faces(k):
    return sorted({tuple(sorted(c)) for f in FACETS for c in combinations(f,k)})
E=faces(2); T=faces(3); ESET=set(E); TSET=set(T)
assert (len(V),len(E),len(T),len(FACETS)) == (14,86,144,72)

# Contract a spanning tree in the connected one-skeleton.
adj={v:set() for v in V}
for a,b in E: adj[a].add(b); adj[b].add(a)
seen={1}; q=deque([1]); TREE=set()
while q:
    u=q.popleft()
    for v in sorted(adj[u]):
        if v not in seen:
            seen.add(v); q.append(v); TREE.add(tuple(sorted((u,v))))
assert len(TREE)==13 and len(seen)==14
NTE=[e for e in E if e not in TREE]
EI={e:i for i,e in enumerate(NTE)}
assert len(NTE)==73

def relation(t):
    a,b,c=sorted(t); row=[0]*73
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        e=tuple(sorted(e))
        if e in EI: row[EI[e]] += s
    return row
R=[relation(t) for t in T]

# Fixed full-rank row certificate. Bareiss determinant is exactly 5.
ROWS=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,30,31,32,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,54,55,57,61,62,63,64,65,66,70,72,74,75,76,78,79,80,82,88,89,94,109,112,113,134]

def bareiss_det(A):
    A=[row[:] for row in A]; n=len(A); sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            j=next((j for j in range(k+1,n) if A[j][k]),None)
            assert j is not None
            A[k],A[j]=A[j],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        for i in range(k+1,n): A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]
DET=bareiss_det([R[i] for i in ROWS])
assert abs(DET)==5

# Mod-5 rank is 72, so every maximal minor is divisible by 5.
def rref_mod(A,p):
    A=[[x%p for x in row] for row in A]; m=len(A); n=len(A[0]); r=0; piv=[]
    for c in range(n):
        pr=next((i for i in range(r,m) if A[i][c]),None)
        if pr is None: continue
        A[r],A[pr]=A[pr],A[r]
        inv=pow(A[r][c],-1,p); A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]; A[i]=[(x-q*y)%p for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
    return r,piv,A
rank5,piv,A=rref_mod(R,5)
assert rank5==72
# The quotient Z^73/<R> is finite of order dividing 5 by DET, and divisible by 5 by rank5.
# Hence H1 is Z/5.

free=[c for c in range(73) if c not in piv]
assert len(free)==1
y=[0]*73; y[free[0]]=1
for i,c in enumerate(piv): y[c]=(-A[i][free[0]])%5
assert all(sum(a*b for a,b in zip(row,y))%5==0 for row in R)

def edgeval(u,v):
    e=tuple(sorted((u,v))); z=y[EI[e]] if e in EI else 0
    return z if u<v else -z

def ordered_coord(seq):
    return sum(edgeval(seq[i],seq[(i+1)%len(seq)]) for i in range(len(seq)))%5

def inc_coord(c): return ordered_coord(tuple(sorted(c)))

cliques=[c for c in combinations(V,3) if all(tuple(sorted(e)) in ESET for e in combinations(c,2))]
empty=[c for c in cliques if c not in TSET]
assert len(cliques)==308 and len(empty)==164
cc=Counter(inc_coord(c) for c in empty)
assert cc==Counter({1:41,2:44,3:38,4:41})
assert 0 not in cc
# Up to reversal, ±1 and ±2 each have 82 representatives.
assert cc[1]+cc[4]==82 and cc[2]+cc[3]==82

# Full simplicial automorphism group: a facet-degree signature partitions vertices
# into invariant cells, after which only 27,648 candidate permutations remain.
deg={v:sum(v in e for e in E) for v in V}
def vsig(v):
    pats=[]
    for f in FACETS:
        if v in f: pats.append(tuple(sorted(deg[u] for u in f if u!=v)))
    return (deg[v],tuple(sorted(pats)))
cells=defaultdict(list)
for v in V: cells[vsig(v)].append(v)
CELLS=sorted((tuple(sorted(g)) for g in cells.values()), key=lambda g:(len(g),g))
assert sorted(map(len,CELLS))==[2,4,4,4]
permlists=[list(permutations(g)) for g in CELLS]
AUT=[]
for ps in product(*permlists):
    mp={}
    for g,p in zip(CELLS,ps): mp.update(zip(g,p))
    if all(tuple(sorted(mp[x] for x in f)) in FACETS for f in FACETS): AUT.append(mp)
assert len(AUT)==4

def compose(f,g): return {v:f[g[v]] for v in V}
def order(f):
    cur={v:v for v in V}
    for k in range(1,9):
        cur=compose(f,cur)
        if all(cur[v]==v for v in V): return k
    raise AssertionError
assert sorted(order(a) for a in AUT)==[1,2,4,4]

rep=next(c for c in empty if inc_coord(c)==1)
mult=[]
for a in AUT:
    mult.append(ordered_coord(tuple(a[x] for x in rep)))
assert sorted(mult)==[1,2,3,4]

seen=set(); orbits=[]
for c in empty:
    if c in seen: continue
    orb={tuple(sorted(a[x] for x in c)) for a in AUT}
    seen |= orb; orbits.append(orb)
assert Counter(map(len,orbits))==Counter({4:39,2:4})

print('VERIFY_OK f=14,86,144,72 H1_Z=Z/5 det_minor=5 rank_mod5=72 graph_triangles=308 facial3=144 empty3=164 all_empty3_generators=yes unoriented_class_counts=82,82 aut=C4 aut_H1_units=1,2,3,4 carrier_orbits=39x4+4x2')
