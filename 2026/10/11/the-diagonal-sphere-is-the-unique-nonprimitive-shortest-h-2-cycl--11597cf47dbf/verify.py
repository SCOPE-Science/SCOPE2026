#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

# Published Bagchi--Datta vertex set x_ij, 1 <= i <= j <= 4.
V=[(i,j) for i in range(1,5) for j in range(i,5)]
vid={v:k for k,v in enumerate(V)}
alpha={1:2,2:3,3:1,4:4}
beta={1:2,2:1,3:4,4:3}

def pv(v,p):
    a,b=sorted((p[v[0]],p[v[1]])); return (a,b)
def ptuple(p): return tuple(vid[pv(v,p)] for v in V)
def comp(p,q): return tuple(p[q[i]] for i in range(len(V)))
G={tuple(range(10))}; stack=list(G)
for_gen=[ptuple(alpha),ptuple(beta)]
while stack:
    g=stack.pop()
    for h in for_gen:
        x=comp(h,g)
        if x not in G: G.add(x); stack.append(x)
assert len(G)==12

seed_labels=[
[(1,1),(2,2),(3,3),(1,2),(1,3)],
[(1,1),(2,2),(1,2),(1,4),(3,4)],
[(1,1),(2,2),(1,4),(2,4),(3,4)],
[(1,1),(2,2),(1,2),(1,3),(2,4)],
[(1,1),(2,2),(1,3),(2,4),(3,4)]]
seeds=[frozenset(vid[x] for x in s) for s in seed_labels]
assert [len({frozenset(g[i] for i in s) for g in G}) for s in seeds]==[12,12,12,6,6]
facets={frozenset(g[i] for i in s) for g in G for s in seeds}
assert len(facets)==48
faces={k:set() for k in range(1,6)}
for F in facets:
    for k in range(1,6):
        faces[k].update(combinations(sorted(F),k))
assert [len(faces[k]) for k in range(1,6)]==[10,45,110,120,48]

def boundary(k):
    # C_k -> C_(k-1), with increasing orientations.
    cols=sorted(faces[k+1]); rows=sorted(faces[k]); ri={r:i for i,r in enumerate(rows)}
    M=[[0]*len(cols) for _ in rows]
    for j,s in enumerate(cols):
        for a in range(k+1):
            f=s[:a]+s[a+1:]
            M[ri[f]][j]=1 if a%2==0 else -1
    return M,rows,cols
D1,verts,edges=boundary(1)
D2,edges2,tris=boundary(2)
D3,tris2,tets=boundary(3)
assert edges==edges2 and tris==tris2

def matmul(A,B):
    out=[[0]*len(B[0]) for _ in A]
    for i,row in enumerate(A):
        for k,a in enumerate(row):
            if a:
                for j,b in enumerate(B[k]):
                    if b: out[i][j]+=a*b
    return out
assert all(x==0 for row in matmul(D1,D2) for x in row)
assert all(x==0 for row in matmul(D2,D3) for x in row)

def det_bareiss(A):
    A=[r[:] for r in A]; n=len(A)
    if n==0: return 1
    sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            q=next((q for q in range(k+1,n) if A[q][k]),None)
            if q is None: return 0
            A[k],A[q]=A[q],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        prev=pivot
        for i in range(k+1,n): A[i][k]=0
        for j in range(k+1,n): A[k][j]=0
    return sign*A[-1][-1]

def minor(M,rows,cols): return [[M[i][j] for j in cols] for i in rows]
# Full-rank certificates fixed from exact elimination on this published complex.
D1_rows=tuple(range(9)); D1_cols=(0,1,2,3,4,5,6,7,8)
# The first nine lexicographic edges are not a tree, so select a star at vertex 0 instead.
D1_cols=tuple(edges.index((0,j)) for j in range(1,10))
assert abs(det_bareiss(minor(D1,D1_rows,D1_cols)))==1
# Since every column of D1 sums to zero, rank(D1)=9.
D2_rows=(0,1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,24,25,26,27,28,30,31,32,33,35,36,37,39,40,42)
D2_cols=tuple(range(36))
assert det_bareiss(minor(D2,D2_rows,D2_cols))==1
# im(D2) lies in ker(D1), whose dimension is 45-9=36, hence rank(D2)=36.
D3_rows=(0,1,2,3,4,5,6,8,9,10,11,12,13,15,16,17,18,19,21,22,23,24,26,27,28,30,31,33,36,37,38,39,41,42,43,45,46,47,48,50,51,52,54,56,59,60,61,63,64,65,66,68,69,71,72,74,77,78,79,80,82,83,85,88,91,92,93,95,96,98,101,103,106)
D3_cols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,59,61,62,63,66,72,75,76,78,80,88,91,95,97,100,111)
assert det_bareiss(minor(D3,D3_rows,D3_cols))==-1
# This unimodular rank-73 minor also proves im(D3) is a primitive sublattice of C2.

tri_idx={t:i for i,t in enumerate(tris)}
def tet_cycle(t):
    z=[0]*len(tris)
    for a in range(4): z[tri_idx[t[:a]+t[a+1:]]]+=1 if a%2==0 else -1
    return z
# Integral 2-cocycle certificate: phi D3 = 0 and phi evaluates 1 on a primitive witness.
phi=[-1,0,0,0,0,-1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,-1,0,-2,-1,0,0,-1,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,0,0,0,1,0,0,0,0,0,0,-1,-1,0,0,-1,0,-1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,-1,0,1,0]
assert len(phi)==len(tris)
assert all(sum(phi[i]*D3[i][j] for i in range(len(tris)))==0 for j in range(len(tets)))

missing=[]
for s in combinations(range(10),4):
    if s not in faces[4] and all(tuple(q) in faces[3] for q in combinations(s,3)):
        missing.append(s)
assert len(missing)==35
z0=tet_cycle(missing[0]); assert sum(a*b for a,b in zip(phi,z0))==1
# z0 is not a boundary, so rank(D3)<=73; the displayed minor gives equality.
# Therefore rank H2 = 110-36-73 = 1. The unimodular D3 minor makes C2/im(D3)
# torsion-free, hence H2 is torsion-free and isomorphic to Z. The cocycle value 1
# proves [z0] is a primitive generator.
vals=[sum(a*b for a,b in zip(phi,tet_cycle(t))) for t in missing]
assert Counter(abs(v) for v in vals)==Counter({1:34,2:1})
diagonal=tuple(sorted(vid[(i,i)] for i in range(1,5)))
assert diagonal in missing
assert abs(vals[missing.index(diagonal)])==2
assert all(abs(v)==1 for t,v in zip(missing,vals) if t!=diagonal)
# Any nonzero 2-cycle on <=3 vertices is impossible. On exactly four vertices,
# the edge-boundary equations force the full oriented tetrahedral boundary;
# it exists precisely when all four triangles are present. If the tetrahedron is
# itself a face, that cycle is a boundary. Thus the 35 missing tetrahedra are
# exactly all minimum-support nonzero H2 cycles.
# Exhaustively verify the four-vertex kernel statement over the induced triangle sets.
for s in combinations(range(10),4):
    present=[t for t in combinations(s,3) if t in faces[3]]
    if len(present)<4:
        # Every triangle has an edge unique among the present faces unless all 4 are present;
        # direct brute force over coefficients in {-1,0,1} is sufficient for support-4 cycles.
        # More generally the 4-vertex triangle-edge boundary matrix has independent columns here.
        cols=[tris.index(t) for t in present]
        # each present triangle has a boundary edge; verify no nonzero rational dependence via a minor search
        # simple elimination over fractions
        A=[[D2[i][j] for j in cols] for i in range(len(edges))]
        rank=0; c=0
        from fractions import Fraction
        A=[[Fraction(x) for x in row] for row in A]
        while c<len(cols) and rank<len(A):
            p=next((r for r in range(rank,len(A)) if A[r][c]),None)
            if p is None: c+=1; continue
            A[rank],A[p]=A[p],A[rank]; q=A[rank][c]
            A[rank]=[x/q for x in A[rank]]
            for r in range(len(A)):
                if r!=rank and A[r][c]:
                    q=A[r][c]; A[r]=[x-q*y for x,y in zip(A[r],A[rank])]
            rank+=1; c+=1
        assert rank==len(cols)
# A4 orbits.
unseen={frozenset(t) for t in missing}; orbits=[]
while unseen:
    t=next(iter(unseen)); o={frozenset(g[i] for i in t) for g in G}; o &= {frozenset(x) for x in missing}
    orbits.append(o); unseen-=o
sizes=sorted(len(o) for o in orbits)
assert sizes==[1,4,6,12,12]
assert next(o for o in orbits if len(o)==1)=={frozenset(diagonal)}
print('VERIFY_OK f=10,45,110,120,48 H2=Z missing_tetrahedra=35 primitive=34 double=1 diagonal=x11-x22-x33-x44 orbits=1,4,6,12,12 primitive_orbits=4,6,12,12')
