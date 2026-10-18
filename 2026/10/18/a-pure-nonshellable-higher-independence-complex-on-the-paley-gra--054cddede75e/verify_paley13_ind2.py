#!/usr/bin/env python3
"""Exact, dependency-free verification for the two-independence complex of Paley(13).
All matrices use oriented simplices with increasing residue labels 0,...,12.
"""
from collections import Counter
from itertools import combinations

N=13
QUADRATIC_RESIDUES=frozenset((x*x)%N for x in range(1,N))
assert QUADRATIC_RESIDUES == frozenset((1,3,4,9,10,12))
NEIGHBORS=tuple(sum(1<<j for j in range(N) if j!=i and (j-i)%N in QUADRATIC_RESIDUES) for i in range(N))

def vertices(mask):
    return [i for i in range(N) if (mask>>i)&1]

def fast_test(mask):
    return all((mask&NEIGHBORS[v]).bit_count()<=1 for v in vertices(mask))

def independent_components_at_most_two(mask):
    rest=set(vertices(mask))
    while rest:
        seed=rest.pop()
        todo=[seed]
        size=0
        while todo:
            v=todo.pop()
            size+=1
            if size>2:
                return False
            ns={w for w in rest if (NEIGHBORS[v]>>w)&1}
            rest.difference_update(ns)
            todo.extend(ns)
    return True

F={k:[] for k in range(4)}
for mask in range(1,1<<N):
    good=fast_test(mask)
    assert good==independent_components_at_most_two(mask),mask
    if good:
        d=mask.bit_count()-1
        assert d<=3
        F[d].append(mask)
assert tuple(len(F[i]) for i in range(4))==(13,78,143,78)
assert all(len(F[d])==len(set(F[d])) for d in F)
# Purity is not assumed: explicitly establish that every lower face
# extends to a 3-simplex. A face of size >=1 is contained in some
# tetrahedron; all 78 tetrahedra are facets.
for d in (0,1,2):
    for face in F[d]:
        assert any((face & tet)==face for tet in F[3]),(d,face)
print('F_VECTOR',(13,78,143,78))
print('PURE_DIMENSION_THREE_FACETS',len(F[3]))

# Fundamental group presentation with star spanning tree (0,i).
# Each triangle (0,i,j) sets generator g_{ij}=1. Each other triangle
# relates its three corresponding generators; once two are trivial,
# so is the third. Exhaustiveness verifies all 66 generators eliminated.
triples=[vertices(t) for t in F[2]]
known={(i,j) for i in range(1,N) for j in range(i+1,N) if (1|(1<<i)|(1<<j)) in set(F[2])}
assert len(known)==33
rounds=[len(known)]
while True:
    was=len(known)
    for a,b,c in triples:
        if 0 in (a,b,c):
            continue
        edges={(a,b),(a,c),(b,c)}
        if len(edges-known)==1:
            known|=edges
    if len(known)==was:
        break
    rounds.append(len(known))
assert len(known)==66,(len(known),rounds)
print('PI_1_TRIVIAL_TRIANGLE_ELIMINATION',rounds)

# Boundary C_3 -> C_2. All operations below are invertible over Z:
# row/column permutations, sign changes, subtraction of integer multiples.
# Integer diagonal form consisting of 76 entries +1 and two zero columns
# exhibits the full Smith form without relying on modular calculations.
index2={mask:i for i,mask in enumerate(F[2])}
M=[[0]*len(F[3]) for _ in F[2]]
for col,mask in enumerate(F[3]):
    for sign_idx,v in enumerate(vertices(mask)):
        M[index2[mask^(1<<v)]][col]=1 if sign_idx%2==0 else -1

def diagonal_units(a):
    a=[r[:] for r in a]
    nr=len(a);nc=len(a[0]);k=0;max_abs=0
    while k<min(nr,nc):
        # Markowitz unit pivot reduces coefficient growth.
        rowcounts=[sum(a[r][c]!=0 for c in range(k,nc)) for r in range(k,nr)]
        colcounts=[sum(a[r][c]!=0 for r in range(k,nr)) for c in range(k,nc)]
        choices=[]
        for r in range(k,nr):
            for c in range(k,nc):
                if abs(a[r][c])==1:
                    choices.append(((rowcounts[r-k]-1)*(colcounts[c-k]-1),r,c))
        if not choices:
            if any(a[r][c] for r in range(k,nr) for c in range(k,nc)):
                raise AssertionError('Nonzero remaining block without unit pivot')
            break
        _,r,c=min(choices)
        a[k],a[r]=a[r],a[k]
        for row in a:row[k],row[c]=row[c],row[k]
        if a[k][k]==-1:
            a[k]=[-x for x in a[k]]
        for rr in range(k+1,nr):
            factor=a[rr][k]
            if factor:
                for cc in range(k,nc):
                    a[rr][cc]-=factor*a[k][cc]
        for cc in range(k+1,nc):
            factor=a[k][cc]
            if factor:
                for rr in range(k,nr):
                    a[rr][cc]-=factor*a[rr][k]
        assert a[k][k]==1
        assert all(a[rr][k]==0 for rr in range(k+1,nr))
        assert all(a[k][cc]==0 for cc in range(k+1,nc))
        max_abs=max(max_abs,max(abs(a[rr][cc]) for rr in range(k,nr) for cc in range(k,nc)))
        k+=1
    assert all(a[r][c]==(1 if r==c and r<k else 0) for r in range(nr) for c in range(nc))
    return k,max_abs
rank3,largest=diagonal_units(M)
assert rank3==76,rank3
print('INTEGER_UNIT_SMITH_DIAGONAL',rank3,'ONES',len(F[3])-rank3,'ZERO_COLUMNS', 'largest_intermediate',largest)
# Integral simplicial chain relation d2*d3=0.
index1={mask:i for i,mask in enumerate(F[1])}
B2=[[0]*len(F[2]) for _ in F[1]]
for col,mask in enumerate(F[2]):
    for t,v in enumerate(vertices(mask)):
        B2[index1[mask^(1<<v)]][col]=(-1)**t
for col in range(len(F[3])):
    z=[sum(B2[r][m]*M[m][col] for m in range(len(F[2]))) for r in range(len(F[1]))]
    assert not any(z)
print('CHAIN_SQUARE_ZERO')
# Since 1-skeleton is the complete graph on 13 vertices,
# rank(d1)=12.  The verified pi1=1 gives H1=0, thus rank(d2)=66.
rank2=len(F[1])-(len(F[0])-1)
assert rank2==66
b2=len(F[2])-rank2-rank3
b3=len(F[3])-rank3
assert (b2,b3)==(1,2)
print('INTEGRAL_REDUCED_HOMOLOGY',{'degree_2_Z_rank':b2,'degree_3_Z_rank':b3,'all_torsion':0})
# The two-skeleton is simply connected, hence a wedge of 77 S^2;
# attaching the 78 three-cells with 76 unit invariant factors gives
# the homotopy type S^2 v S^3 v S^3.
print('VERIFIED_PALEY13_SECOND_INDEPENDENCE_MIXED_WEDGE')
