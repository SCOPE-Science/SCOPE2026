#!/usr/bin/env python3
"""Exact-rational checks for sparse symmetric K_{2,m} rank-defect geometry.

The checks corroborate, but do not replace, the dimension argument and
published radicality theorem given in RESULT.md.
"""
from fractions import Fraction as Q
from random import Random


def rank(a):
    x = [[Q(v) for v in row] for row in a]
    if not x:
        return 0
    n, m = len(x), len(x[0]); r = 0
    for j in range(m):
        pivot = next((i for i in range(r, n) if x[i][j]), None)
        if pivot is None:
            continue
        x[r], x[pivot] = x[pivot], x[r]
        s = x[r][j]
        x[r] = [v/s for v in x[r]]
        for i in range(n):
            if i != r and x[i][j]:
                f = x[i][j]
                x[i] = [u-f*v for u,v in zip(x[i], x[r])]
        r += 1
        if r == n:
            break
    return r


def determinant(a):
    x = [[Q(v) for v in row] for row in a]
    n=len(x); result=Q(1)
    for j in range(n):
        i=next((i for i in range(j,n) if x[i][j]),None)
        if i is None:return Q(0)
        if i != j:
            x[i],x[j]=x[j],x[i];result=-result
        z=x[j][j];result*=z
        for i in range(j+1,n):
            if x[i][j]:
                v=x[i][j]/z
                for k in range(j+1,n):x[i][k]-=v*x[j][k]
    return result


def residual(c,b):
    t=len(b[0]);return [c[i][:]+b[i][:] for i in range(2)]+[
        [b[0][j],b[1][j]]+[Q(0)]*t for j in range(t)]


def predicted(t,c,b):
    if t==1:
        return all(not b[i][0] for i in range(2)) and determinant(c)==0
    if t==2:
        rb=rank(b)
        if rb==2:return False
        if rb==0:return True
        j=next(j for j in range(2) if b[0][j] or b[1][j])
        v=[-b[1][j],b[0][j]]
        return sum(v[i]*c[i][k]*v[k] for i in range(2) for k in range(2))==0
    if t==3:return rank(b)<=1
    return True


def test_boundary():
    rng=Random(20261017)
    for t in range(1,9):
        # Includes rank-zero, rank-one and full-row-rank B, isotropic and
        # nonisotropic restrictions of C, and arbitrary small integer data.
        for z in range(350):
            c=[[Q(rng.randrange(-2,3)) for _ in range(2)] for _ in range(2)]
            c[1][0]=c[0][1]
            b=[[Q(rng.randrange(-2,3)) for _ in range(t)] for _ in range(2)]
            if z%9==0: b[1]=[2*x for x in b[0]]
            if z%13==0: b=[[Q(0)]*t for _ in range(2)]
            assert (rank(residual(c,b))<=t)==predicted(t,c,b),(t,c,b)
    return True


def test_schur():
    rng=Random(137)
    for m in range(3,8):
        for k in range(80):
            z=[Q(rng.choice([-3,-2,-1,1,2,3])) for _ in range(m)]
            b=[Q(rng.randrange(-3,4)) for _ in range(m)]
            d=[Q(rng.randrange(-3,4)) for _ in range(m)]
            a,c=Q(rng.randrange(-3,4)),Q(rng.randrange(-3,4))
            mat=[[a,Q(0)]+b,[Q(0),c]+d]
            for j in range(m):
                mat.append([b[j],d[j]]+[z[j] if i==j else Q(0) for i in range(m)])
            s11=a-sum(b[i]*b[i]/z[i] for i in range(m))
            s22=c-sum(d[i]*d[i]/z[i] for i in range(m))
            s12=-sum(b[i]*d[i]/z[i] for i in range(m))
            s=[[s11,s12],[s12,s22]]
            assert rank(mat)==m+rank(s)
            product=Q(1)
            for zi in z:product*=zi
            assert determinant(mat)==product*determinant(s)
    return True


def test_rank_defect_witness():
    # An exact nontrivial smooth-rank-defect point with every leaf diagonal
    # invertible, in the first genuinely new size m=5.
    m=5
    z=[Q(i+1) for i in range(m)]
    b=[Q(1),Q(1),Q(0),Q(0),Q(0)]
    d=[Q(1),Q(-2),Q(0),Q(0),Q(0)]
    assert sum(b[i]*d[i]/z[i] for i in range(m))==0
    a=sum(b[i]*b[i]/z[i] for i in range(m))
    c=sum(d[i]*d[i]/z[i] for i in range(m))
    mat=[[a,Q(0)]+b,[Q(0),c]+d]
    for j in range(m):
        mat.append([b[j],d[j]]+[z[j] if i==j else Q(0) for i in range(m)])
    assert rank(mat)==m
    assert b[0]!=0  # The differential of the bilinear equation is nonzero.

if __name__=='__main__':
    assert test_boundary() and test_schur()
    test_rank_defect_witness()
    print('VERIFY_OK')
