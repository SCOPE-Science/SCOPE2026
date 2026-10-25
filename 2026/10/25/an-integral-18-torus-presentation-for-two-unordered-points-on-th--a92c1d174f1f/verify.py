#!/usr/bin/env python3
"""Exact integral chain certificate for two unordered particles on K(4,4).
This program uses only the Python standard library.
"""
from itertools import combinations

LEFT = range(4)
RIGHT = range(4)
EDGES = [(i, 4+j) for i in LEFT for j in RIGHT]
CELLS1 = [(v, k) for v in range(8) for k, e in enumerate(EDGES) if v not in e]
CELLS2 = [(i, j) for i, j in combinations(range(16), 2)
          if len(set(EDGES[i] + EDGES[j])) == 4]
IDX1 = {p:k for k,p in enumerate(CELLS1)}
IDX2 = {p:k for k,p in enumerate(CELLS2)}
D = [[0] * len(CELLS2) for _ in CELLS1]
for col,(ei,ej) in enumerate(CELLS2):
    a,b = EDGES[ei]
    c,d = EDGES[ej]
    for edge_cell,sgn in [((b,ej),1), ((a,ej),-1),
                          ((d,ei),-1),((c,ei),1)]:
        D[IDX1[edge_cell]][col] += sgn

def mod_rank(matrix, prime):
    x = [[val % prime for val in row] for row in matrix]
    nrows,ncols = len(x),len(x[0]); r=0
    for j in range(ncols):
        p = next((i for i in range(r,nrows) if x[i][j]),None)
        if p is None: continue
        x[r],x[p]=x[p],x[r]
        inv=pow(x[r][j],-1,prime)
        x[r]=[(v*inv)%prime for v in x[r]]
        for i in range(r+1,nrows):
            if x[i][j]:
                t=x[i][j]
                x[i]=[(u-t*v)%prime for u,v in zip(x[i],x[r])]
        r+=1
        if r==nrows:break
    return r

def determinant(matrix):
    a=[list(map(int,row)) for row in matrix]
    n=len(a); denominator=1; parity=1
    for k in range(n-1):
        if a[k][k]==0:
            p=next((i for i in range(k+1,n) if a[i][k]),None)
            if p is None:return 0
            a[k],a[p]=a[p],a[k];parity=-parity
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator % denominator == 0
                a[i][j]=numerator//denominator
            a[i][k]=0
        denominator=pivot
    return parity*a[n-1][n-1]

assert (len(CELLS1),len(CELLS2))==(96,72)
assert mod_rank(D,3)==60
assert mod_rank(D,5)==60

# Labels: t_(rowpair,columnpair); the row pair contains 0.
ROW_PAIRS = [(0,1),(0,2),(0,3)]
COL_PAIRS = list(combinations(range(4),2))
LABELS=[];TORI=[]
for ra in ROW_PAIRS:
    rb=tuple(x for x in LEFT if x not in ra)
    for ca in COL_PAIRS:
        cb=tuple(x for x in RIGHT if x not in ca)
        ac=[4*i+j for i in ra for j in ca]
        bc=[4*i+j for i in rb for j in cb]
        coeff_a=dict(zip(ac,[1,-1,-1,1]))
        coeff_b=dict(zip(bc,[1,-1,-1,1]))
        z=[0]*len(CELLS2)
        for ei,sign_i in coeff_a.items():
            for ej,sign_j in coeff_b.items():
                p=tuple(sorted((ei,ej)))
                z[IDX2[p]]=sign_i*sign_j*(1 if ei<ej else -1)
        LABELS.append((ra,ca));TORI.append(z)
assert len(TORI)==18
for t in TORI:
    assert sum(x*x for x in t)==16
    assert all(sum(D[i][j]*t[j] for j in range(72))==0 for i in range(96))

# Six independent integral relations. In each row the sole 'omitted' basis
# coordinate has coefficient +1, proving the full integer presentation.
RELATIONS=[
    {0:1,1:-1,2:1,3:1,4:-1,5:1},
    {6:1,7:-1,8:1,9:1,10:-1,11:1},
    {0:1,1:-1,2:1,6:-1,7:1,8:-1,12:1,13:-1,14:1},
    {0:1,1:-1,3:1,6:-1,7:1,9:-1,12:1,13:-1,15:1},
    {1:-1,4:1,7:1,10:-1,13:-1,16:1},
    {0:-2,1:1,2:-1,3:-1,4:1,6:2,7:-1,8:1,9:1,10:-1,12:-1,17:1},
]
BASIS=[0,1,2,3,4,6,7,8,9,10,12,13]
OMITTED=[5,11,14,15,16,17]
for k,rel in enumerate(RELATIONS):
    assert rel[OMITTED[k]]==1
    assert all(index not in rel for j,index in enumerate(OMITTED) if j!=k)
    assert all(sum(s*TORI[t][cell] for t,s in rel.items())==0
               for cell in range(72))

# A unimodular coordinate minor certifies that the 12 chosen tori span
# a primitive sublattice of the full 72-dimensional cellular group.
SELECTED_ROWS=[13,67,31,34,32,37,9,57,38,29,55,14]
MINOR=[[TORI[k][row] for k in BASIS] for row in SELECTED_ROWS]
assert determinant(MINOR)==-1

# Because rank_Q(boundary)=60 and these twelve cycles are independent,
# ker_Z(boundary) has rank 12. The selected torus lattice is primitive in
# C_2=Z^72, so the finite quotient of ker_Z(boundary) by it is trivial.
print('EDGE_COUNT',len(EDGES))
print('CELL_COUNTS',28,len(CELLS1),len(CELLS2))
print('RANK_BOUNDARY_MOD3',mod_rank(D,3))
print('TORUS_COUNT',len(TORI))
print('INTEGER_TORUS_BASIS_INDICES',BASIS)
print('UNIT_COORDINATE_MINOR_ROWS',SELECTED_ROWS)
print('UNIT_COORDINATE_MINOR_DET',determinant(MINOR))
print('RELATIONS_CHECKED',len(RELATIONS))
print('H2_RANK',12)
print('VERIFY_OK_K44_UNORDERED_INTEGRAL_TORUS_PRESENTATION')
