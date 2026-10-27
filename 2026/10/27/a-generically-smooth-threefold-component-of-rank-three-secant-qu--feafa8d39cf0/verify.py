#!/usr/bin/env python3
"""Exact rank check for the transverse divisor local model; illustrative, not a proof of all degrees."""
from fractions import Fraction

def rank(matrix):
    mat = [[Fraction(x) for x in row] for row in matrix]
    r = 0
    if not mat: return 0
    n = len(mat[0])
    for c in range(n):
        pivot = next((i for i in range(r, len(mat)) if mat[i][c]), None)
        if pivot is None: continue
        mat[r],mat[pivot] = mat[pivot],mat[r]
        d = mat[r][c]
        mat[r] = [v/d for v in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c]:
                q=mat[i][c]
                mat[i]=[x-q*y for x,y in zip(mat[i],mat[r])]
        r+=1
        if r==len(mat):break
    return r

def residue(poly,mod):
    z=poly[:]+[0]*max(0,len(mod)-len(poly))
    k=len(mod)-1
    for i in range(len(z)-1,k-1,-1):
        x=z[i]
        if x:
            for j in range(k+1): z[i-k+j]-=x*mod[j]
    return z[:k]

def calc(m):
    # Fermat plane section, with line y=0, affine polynomial t^m+1,
    # roots distinct over characteristic zero.
    mod=[1]+[0]*(m-1)+[1]
    # matrices for map (a,b) -> ((a*t^j) mod P2 for j=0,1;
    #                              (b*t^j) mod P2 for j=0,1,2).
    rows=[]
    for k in range(3, m):
        for j in range(2):
            row=[]
            for col in range(m):
                z=residue([0]*(col+j)+[1],mod)
                row.append(z[k])
            row += [0]*m
            rows.append(row)
        for j in range(3):
            row=[0]*m
            for col in range(m):
                z=residue([0]*(col+j)+[1],mod)
                row.append(z[k])
            rows.append(row)
    r=rank(rows)
    return 2*m-r

for m in range(3,15):
    dim=calc(m)
    assert dim == (6 if m==3 else 3), (m,dim)
    print('m=%d; tangent_dimension=%d' % (m,dim))
print('VERIFY_OK')
