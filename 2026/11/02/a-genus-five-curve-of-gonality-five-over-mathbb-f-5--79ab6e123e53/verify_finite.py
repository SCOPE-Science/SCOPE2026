#!/usr/bin/env python3
"""Exact finite-field checks for a genus-five canonical complete intersection."""
from itertools import product
P = 5

def projective_points(n):
    for first in range(n):
        for tail in product(range(5), repeat=n-first-1):
            yield (0,)*first + (1,) + tail

def quadrics(x):
    a,b,c,d,e = x
    return ((a*b+c*c+2*d*d)%5,
            (4*a*d+b*c+3*d*e+3*e*e)%5,
            (a*a+2*b*b+4*c*c+4*d*e)%5)

# Matrices M satisfy Q(x)=x^t M x (all entries modulo five).
M = [
 [[0,3,0,0,0],[3,0,0,0,0],[0,0,1,0,0],[0,0,0,2,0],[0,0,0,0,0]],
 [[0,0,0,2,0],[0,0,3,0,0],[0,3,0,0,0],[2,0,0,0,4],[0,0,0,4,3]],
 [[1,0,0,0,0],[0,2,0,0,0],[0,0,4,0,0],[0,0,0,0,2],[0,0,0,2,0]]
]

def rank_det(matrix):
    a = [[z%5 for z in row] for row in matrix]
    nrows, ncols = len(a), len(a[0]); rank=0; determinant=1
    for col in range(ncols):
        pivot=next((r for r in range(rank,nrows) if a[r][col]),None)
        if pivot is None: continue
        if pivot!=rank:
            a[rank],a[pivot]=a[pivot],a[rank]
            determinant=(-determinant)%5
        val=a[rank][col]; determinant=determinant*val%5
        inv=pow(val,-1,5)
        a[rank]=[(z*inv)%5 for z in a[rank]]
        for r in range(rank+1,nrows):
            t=a[r][col]
            a[r]=[(u-t*v)%5 for u,v in zip(a[r],a[rank])]
        rank+=1
        if rank==nrows: break
    if nrows!=ncols or rank!=nrows: determinant=0
    return rank,determinant

def nonsingular_four_minor(m):
    for omit in range(5):
        mat=[[m[i][j] for j in range(5) if j!=omit]
             for i in range(5) if i!=omit]
        r,d=rank_det(mat)
        if r==4:return d
    raise AssertionError('No invertible 4x4 principal minor')

assert all(quadrics(x)==tuple(sum(x[i]*mat[i][j]*x[j]
                                    for i in range(5) for j in range(5))%5
                                    for mat in M) for x in projective_points(5))

rank_counts={4:0,5:0}; special=[]
for abc in projective_points(3):
    matrix=[[sum(abc[t]*M[t][i][j] for t in range(3))%5
             for j in range(5)] for i in range(5)]
    r,_=rank_det(matrix)
    assert r in (4,5), (abc,r)
    rank_counts[r]+=1
    if r==4:
        d=nonsingular_four_minor(matrix)
        assert d in (2,3), (abc,d)
        special.append((abc,d))

points=[v for v in projective_points(5) if quadrics(v)==(0,0,0)]
assert rank_counts=={4:4,5:27},rank_counts
assert special==[((1,0,0),2),((1,0,1),3),((1,4,0),3),((0,1,2),3)],special
assert points==[(1,1,4,3,4),(1,2,4,4,2)],points
print('NET_RANK_COUNTS',rank_counts)
print('NON_SPLIT_RANK4',special)
print('RATIONAL_CURVE_POINTS',points)
print('FINITE_VERIFY_OK')
