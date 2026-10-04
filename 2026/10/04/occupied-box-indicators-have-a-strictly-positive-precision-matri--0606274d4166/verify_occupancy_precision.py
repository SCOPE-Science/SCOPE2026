#!/usr/bin/env python3
from fractions import Fraction
import itertools
import random


def normalize(raw):
    s=sum(raw)
    return [Fraction(x,s) for x in raw]


def formula_cov(ps,n):
    m=len(ps)
    q=[(1-p)**n for p in ps]
    C=[[Fraction(0) for _ in range(m)] for __ in range(m)]
    for i in range(m):
        C[i][i]=q[i]*(1-q[i])
        for j in range(i+1,m):
            c=(1-ps[i]-ps[j])**n-q[i]*q[j]
            C[i][j]=C[j][i]=c
    return C


def determinant(A):
    A=[row[:] for row in A]
    n=len(A)
    d=Fraction(1)
    sign=1
    for k in range(n):
        pivot=next((i for i in range(k,n) if A[i][k] != 0),None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            A[k],A[pivot]=A[pivot],A[k]
            sign=-sign
        p=A[k][k]
        d*=p
        for i in range(k+1,n):
            if A[i][k] != 0:
                f=A[i][k]/p
                for j in range(k+1,n):
                    A[i][j]-=f*A[k][j]
    return sign*d


def inverse(A):
    n=len(A)
    M=[A[i][:]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if M[i][k] != 0)
        if pivot != k:
            M[k],M[pivot]=M[pivot],M[k]
        p=M[k][k]
        M[k]=[x/p for x in M[k]]
        for i in range(n):
            if i != k and M[i][k] != 0:
                f=M[i][k]
                M[i]=[x-f*y for x,y in zip(M[i],M[k])]
    return [row[n:] for row in M]


def exact_enumerated_cov(ps,n):
    m=len(ps)
    mean=[Fraction(0) for _ in range(m)]
    second=[[Fraction(0) for _ in range(m)] for __ in range(m)]
    for seq in itertools.product(range(m),repeat=n):
        prob=Fraction(1)
        occ=[0]*m
        for x in seq:
            prob*=ps[x]
            occ[x]=1
        for i in range(m):
            mean[i]+=prob*occ[i]
            for j in range(m):
                second[i][j]+=prob*occ[i]*occ[j]
    return [[second[i][j]-mean[i]*mean[j] for j in range(m)] for i in range(m)]


def run():
    rng=random.Random(20261003)
    formula_checks=0
    offdiag_checks=0
    rank_one_draw_checks=0
    pd_minor_checks=0
    inverse_positive_checks=0
    partial_sign_checks=0
    enumeration_checks=0

    for _ in range(5000):
        m=rng.randrange(2,8)
        ps=normalize([rng.randrange(1,20) for __ in range(m)])
        n=rng.randrange(1,9)
        C=formula_cov(ps,n)
        q=[(1-p)**n for p in ps]
        for i in range(m):
            assert C[i][i]==q[i]*(1-q[i])
            formula_checks+=1
            for j in range(i+1,m):
                expected=(1-ps[i]-ps[j])**n-q[i]*q[j]
                assert C[i][j]==C[j][i]==expected
                assert expected<0
                formula_checks+=1
                offdiag_checks+=1

        if n==1:
            for i in range(m):
                assert sum(C[i])==0
            # Any leading (m-1)-square principal block is positive definite.
            for k in range(1,m):
                assert determinant([row[:k] for row in C[:k]])>0
            assert determinant(C)==0
            rank_one_draw_checks+=m+1
        else:
            for k in range(1,m+1):
                assert determinant([row[:k] for row in C[:k]])>0
                pd_minor_checks+=1
            O=inverse(C)
            for i in range(m):
                for j in range(m):
                    assert O[i][j]>0
                    inverse_positive_checks+=1
                    if i<j:
                        # Precision positivity means the full-order partial correlation has negative sign.
                        assert -O[i][j]<0
                        partial_sign_checks+=1

    # Direct iid sample-space reconstruction for small cases.
    for _ in range(500):
        m=rng.randrange(2,5)
        n=rng.randrange(1,5)
        ps=normalize([rng.randrange(1,9) for __ in range(m)])
        C1=formula_cov(ps,n)
        C2=exact_enumerated_cov(ps,n)
        assert C1==C2
        enumeration_checks+=m*m

    print(
        'VERIFY_OK '
        f'formula_checks={formula_checks} '
        f'offdiag_checks={offdiag_checks} '
        f'rank_one_draw_checks={rank_one_draw_checks} '
        f'pd_minor_checks={pd_minor_checks} '
        f'inverse_positive_checks={inverse_positive_checks} '
        f'partial_sign_checks={partial_sign_checks} '
        f'enumeration_checks={enumeration_checks}'
    )


if __name__=='__main__':
    run()
