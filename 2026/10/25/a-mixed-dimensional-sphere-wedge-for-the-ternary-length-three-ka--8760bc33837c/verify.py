#!/usr/bin/env python3
"""Exact integral simplicial Morse verification for the length-three ternary Kautz digraph.

Requires only Python >=3.9 standard library; deterministic, exhaustive, no downloads.
Run: python3 verify.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import product

ALPHABET = (0, 1, 2)
LENGTH = 3
V = tuple(p for p in product(ALPHABET, repeat=LENGTH)
          if all(p[j] != p[j+1] for j in range(LENGTH-1)))
LABEL = {v:i for i,v in enumerate(V)}
ARCS = tuple((LABEL[v], LABEL[v[1:] + (a,)])
             for v in V for a in ALPHABET if a != v[-1])
assert len(V)==12 and len(ARCS)==24 and len(set(ARCS))==24
incoming = [[] for _ in V]
for e,(u,w) in enumerate(ARCS):
    assert u != w
    incoming[w].append(e)
assert all(len(x)==2 for x in incoming)

def acyclic_functional(eids):
    predecessor = {ARCS[e][1]:ARCS[e][0] for e in eids}
    for v in predecessor:
        cur=v
        seen=set()
        while cur in predecessor and cur not in seen:
            seen.add(cur)
            cur=predecessor[cur]
        if cur in seen:
            return False
    return True

faces=[]
for choices in product((0,1,2),repeat=len(V)):
    selected=[incoming[v][choice-1] for v,choice in enumerate(choices) if choice]
    if acyclic_functional(selected):
        faces.append(sum(1<<e for e in selected))
assert len(faces)==314928 and len(set(faces))==len(faces)
all_faces=set(faces)
fvector=[sum(m.bit_count()==k for m in faces) for k in range(12)]
assert fvector==[1,24,261,1698,7344,22176,47712,73152,78336,55808,23808,4608]
assert sum((-1)**(k-1)*a for k,a in enumerate(fvector))==4

# Check maximal-face profile, not inferred from a Morse matching.
facets=Counter()
full=(1<<len(ARCS))-1
for m in faces:
    remain=full^m
    while remain:
        b=remain&-remain
        remain-=b
        if (m|b) in all_faces:
            break
    else:
        facets[m.bit_count()-1]+=1
assert facets=={9:132,10:4608}
rootpair_counts=Counter()
for m in faces:
    if m.bit_count()!=10:continue
    if any((m|(1<<edge)) in all_faces for edge in range(len(ARCS)) if not (m>>edge)&1):
        continue
    chosen_targets={ARCS[edge][1] for edge in range(len(ARCS)) if (m>>edge)&1}
    roots=tuple(v for v in range(len(V)) if v not in chosen_targets)
    assert len(roots)==2
    rootpair_counts[roots]+=1
assert len(rootpair_counts)==24
assert Counter(rootpair_counts.values())=={5:21,9:3}

# A second cycle test: under indegree<=1, a directed cycle is exactly
# a cycle in the underlying undirected graph. Union/find checks maximal faces.
def undirected_forest(edges):
    parent=list(range(len(V)))
    def root(x):
        while x != parent[x]:
            x=parent[x]
        return x
    for e in edges:
        u,w=ARCS[e]
        u=root(u)
        w=root(w)
        if u==w:return False
        parent[u]=w
    return True

for choice in product((0,1,2), repeat=len(V)):
    edges=[incoming[v][k-1] for v,k in enumerate(choice) if k]
    m=sum(1<<e for e in edges)
    assert (m in all_faces) == undirected_forest(edges)

# Independent maximal-face count from the directed matrix-tree theorem;
# Bareiss fraction-free determinant for an integer 11 x 11 minor.
def determinant_bareiss(matrix):
    M=[row[:] for row in matrix]
    n=len(M)
    denominator=1
    sign=1
    for k in range(n-1):
        if M[k][k]==0:
            for j in range(k+1,n):
                if M[j][k]:
                    M[k],M[j]=M[j],M[k]
                    sign=-sign
                    break
            else:return 0
        pivot=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=M[i][j]*pivot-M[i][k]*M[k][j]
                assert numerator%denominator==0
                M[i][j]=numerator//denominator
        for i in range(k+1,n):M[i][k]=0
        denominator=pivot
    return sign*M[-1][-1]
N=len(V)
L=[[0]*N for _ in range(N)]
for u,v in ARCS:
    L[v][v]+=1
    L[v][u]-=1
assert determinant_bareiss([row[1:] for row in L[1:]])==384
assert facets[10]==12*384

# Complete lexicographic elementary matching on the augmented poset.
matched=set()
pairs=[]
for edge in range(len(ARCS)):
    bit=1<<edge
    for m in faces:
        if m not in matched and not (m&bit) and (m|bit) in all_faces and (m|bit) not in matched:
            matched.add(m)
            matched.add(m|bit)
            pairs.append((m,m|bit))
assert len(pairs)==157440
# Replace the augmented empty-face pair by one critical 0-cell;
# all remaining pairs are nonempty faces of the simplicial complex.
assert pairs[0][0]==0
basepoint=pairs[0][1]
pairs=pairs[1:]
lo2hi=dict(pairs)
hi2lo={h:l for l,h in pairs}
critical=[m for m in faces if m!=0 and m not in lo2hi and m not in hi2lo]
assert basepoint in critical
assert Counter(m.bit_count()-1 for m in critical)=={0:1,8:3,9:22,10:23}
assert 2*len(pairs)+len(critical)==len(faces)-1

# Full Hasse digraph: a matched cover is directed lower->upper,
# all other covers upper->lower. Check every codimension-one incidence.
nonempty=[m for m in faces if m]
indegree={m:0 for m in nonempty}
incidence=0
for m in nonempty:
    bits=m
    while bits:
        b=bits&-bits;bits-=b
        lower=m^b
        if not lower:continue
        incidence+=1
        if lo2hi.get(lower)==m:
            indegree[m]+=1
        else:
            indegree[lower]+=1
assert incidence==2361936
ready=deque(m for m,n in indegree.items() if n==0)
visited=0
while ready:
    m=ready.popleft()
    visited+=1
    if m in lo2hi:
        h=lo2hi[m]
        indegree[h]-=1
        if indegree[h]==0:ready.append(h)
    bits=m
    while bits:
        b=bits&-bits;bits-=b
        lower=m^b
        if lower and lo2hi.get(lower)!=m:
            indegree[lower]-=1
            if indegree[lower]==0:ready.append(lower)
assert visited==len(nonempty)

# Integral signed Morse differentials in increasing edge-mask orientations.
# To project (d-1)-cells: discard matched uppers, expand matched lowers
# through the boundary of their matched d-cell, and retain critical cells.
def morse_boundary(lowdim):
    targets=sorted(m for m in critical if m.bit_count()==lowdim+1)
    sources=sorted(m for m in critical if m.bit_count()==lowdim+2)
    coords={m:i for i,m in enumerate(targets)}
    @lru_cache(maxsize=None)
    def reduce(m):
        if m in coords:return {coords[m]:1}
        if m in hi2lo:return {}
        assert m in lo2hi
        h=lo2hi[m]
        pairing_bit=h^m
        pairing_sign=(-1)**((h&(pairing_bit-1)).bit_count())
        out=defaultdict(int)
        bits=h
        while bits:
            b=bits&-bits;bits-=b
            q=h^b
            if q==m:continue
            coeff=-((-1)**((h&(b-1)).bit_count()))*pairing_sign
            for i,z in reduce(q).items():out[i]+=coeff*z
        return {i:v for i,v in out.items() if v}
    M=[[0]*len(sources) for _ in targets]
    for col,h in enumerate(sources):
        bits=h
        while bits:
            b=bits&-bits;bits-=b
            q=h^b
            sgn=(-1)**((h&(b-1)).bit_count())
            for i,z in reduce(q).items():M[i][col]+=sgn*z
    return M
A=morse_boundary(8)
B=morse_boundary(9)
assert len(A)==3 and all(len(row)==22 for row in A)
assert len(B)==22 and all(len(row)==23 for row in B)
assert all(sum(A[i][j]*B[j][k] for j in range(22))==0
           for i in range(3) for k in range(23))

# Record concise signed boundary certificates using all nonzero coordinates.
A_sparse=[(i,j,x) for i,row in enumerate(A) for j,x in enumerate(row) if x]
B_sparse=[(i,j,x) for i,row in enumerate(B) for j,x in enumerate(row) if x]
assert A_sparse==[(0,10,1),(0,11,-1),(1,12,-1),(2,19,-1)]

# Arithmetic cancellation at a unit coefficient does not introduce torsion.
def unit_eliminate(matrix):
    M=[row[:] for row in matrix]
    count=0
    while M and M[0]:
        candidate=next(((i,j) for i,row in enumerate(M) for j,a in enumerate(row) if abs(a)==1),None)
        if candidate is None:break
        i,j=candidate
        p=M[i][j]
        M=[[M[r][c]-(M[r][j]*M[i][c])//p
            for c in range(len(M[0])) if c!=j]
            for r in range(len(M)) if r!=i]
        count+=1
    assert all(v==0 for row in M for v in row)
    return count
assert unit_eliminate(A)==3
assert unit_eliminate(B)==11
# A's pivot columns 10,12,19 can be canceled first; after this deletion
# the surviving 10->9 boundary still cancels through eleven units.
pivot_cols=(10,12,19)
assert all(abs(A[i][pivot_cols[i]])==1 for i in range(3))
assert all(A[i][pivot_cols[j]]==0 for i in range(3) for j in range(3) if i!=j)
B_after=[[x for x in row] for k,row in enumerate(B) if k not in pivot_cols]
assert unit_eliminate(B_after)==11

print('VERTICES',len(V),'ARCS',len(ARCS))
print('F_VECTOR',fvector)
print('FACETS',dict(sorted(facets.items())))
print('NONSPANNING_FACET_ROOT_PAIRS',len(rootpair_counts),'MULTIPLICITIES',dict(sorted(Counter(rootpair_counts.values()).items())))
print('ROOTED_SPANNING_OUT_TREES_EACH',384)
print('MATCHED_NONEMPTY_PAIRS',len(pairs),'CRITICAL',dict(sorted(Counter(m.bit_count()-1 for m in critical).items())))
print('HASSE_INCIDENCES',incidence,'ACYCLIC_TOPOLOGICAL_VISITS',visited)
print('MORSE_BOUNDARY_9_TO_8',A_sparse)
print('MORSE_BOUNDARY_10_TO_9',B_sparse)
print('UNIT_CANCELS',3,11,'REMAINING_9_SPHERES',8,'REMAINING_10_SPHERES',12)
print('VERIFY_OK')
