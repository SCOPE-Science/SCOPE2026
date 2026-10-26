#!/usr/bin/env python3
"""Exact combinatorial checks for normal-fan hypersimplex small resolutions.
All arithmetic is rational or integer; no network or third-party packages.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def rank(matrix):
    if not matrix: return 0
    A=[[Fraction(x) for x in row] for row in matrix]
    nr,nc=len(A),len(A[0]); r=0
    for col in range(nc):
        ip=next((i for i in range(r,nr) if A[i][col]),None)
        if ip is None: continue
        A[r],A[ip]=A[ip],A[r]
        q=A[r][col]
        A[r]=[x/q for x in A[r]]
        for i in range(r+1,nr):
            if A[i][col]:
                c=A[i][col]; A[i]=[x-c*y for x,y in zip(A[i],A[r])]
        r+=1
        if r==nr:break
    return r


def det(A):
    A=[row[:] for row in A]; n=len(A); sign=1; prev=1
    if not n:return 1
    for k in range(n-1):
        if A[k][k]==0:
            j=next((j for j in range(k+1,n) if A[j][k]),None)
            if j is None:return 0
            A[k],A[j]=A[j],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
            A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]


def fan_unimodularity(n,k):
    # N=Z^n/Z(1,...,1), use images of e_0,...,e_(n-2) as basis,
    # image e_(n-1) equals minus their sum.
    E=[]
    for i in range(n):E.append([int(i==j)-(int(i==n-1)) for j in range(n-1)])
    count=0
    for B in combinations(range(n),k):
        B=set(B)
        ray=[E[j] if j in B else [-z for z in E[j]] for j in range(n)]
        assert [sum(E[j][h] for j in B)+sum(E[j][h] for j in range(n) if j not in B) for h in range(n-1)]==[0]*(n-1)
        # Each local triangulation omits one ray in B or its complement:
        for omit in range(n):
            d=det([v for j,v in enumerate(ray) if j!=omit])
            assert abs(d)==1,(n,k,B,omit,d)
            count+=1
    return count


def chambers(n,k):
    subsets=list(combinations(range(n),k));m=len(subsets)
    if m>11:return None
    rows=[[int(j in B) for j in range(n)]+[-1] for B in subsets]
    # Whitney subset expression for central hyperplane-arrangement regions:
    # (-1)^r chi(-1)= sum_{S}(-1)^{|S|+rank(S)}.
    total=0
    for mask in range(1<<m):
        s=[rows[j] for j in range(m) if (mask>>j)&1]
        total+=(-1)**(mask.bit_count()+rank(s))
    return total

if __name__=='__main__':
    for n,k in [(4,2),(5,2),(6,2),(6,3)]:
        found=fan_unimodularity(n,k)
        assert found==n*comb(n,k)
    assert chambers(4,2)==46
    assert chambers(5,2)==332
    print('VERIFY_OK: exact ray-basis determinants for (4,2),(5,2),(6,2),(6,3); central arrangement regions 46,332')
