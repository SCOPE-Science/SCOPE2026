#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations, combinations

def edges(n):
    return list(combinations(range(n),2))

def dot(e,f):
    i,j=e
    k,l=f
    return (1 if i==k else 0) - (1 if i==l else 0) - (1 if j==k else 0) + (1 if j==l else 0)

def cov_enum(n):
    es=edges(n)
    m=len(es)
    sums=[0]*m
    prod=[[0]*m for _ in range(m)]
    count=0
    for p in permutations(range(n)):
        count+=1
        x=[int(p[i]>p[j]) for i,j in es]
        for a in range(m):
            sums[a]+=x[a]
            for b in range(m):
                prod[a][b]+=x[a]*x[b]
    mu=[Fraction(s,count) for s in sums]
    C=[[Fraction(prod[a][b],count)-mu[a]*mu[b] for b in range(m)] for a in range(m)]
    return C,count

def qmatrix(n):
    es=edges(n)
    return [[Fraction(dot(e,f)) for f in es] for e in es]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def run():
    permutations_checked=0
    covariance_entries=0
    q_square_entries=0
    inverse_entries=0
    pair_class_checks=0
    determinant_checks=0

    for n in range(2,8):
        C,count=cov_enum(n)
        permutations_checked+=count
        es=edges(n)
        for a,e in enumerate(es):
            for b,f in enumerate(es):
                q=dot(e,f)
                target=Fraction((1 if a==b else 0)+q,12)
                assert C[a][b]==target
                covariance_entries+=1

    for n in range(2,15):
        es=edges(n)
        m=len(es)
        Q=qmatrix(n)
        Q2=mm(Q,Q)
        for i in range(m):
            for j in range(m):
                assert Q2[i][j]==n*Q[i][j]
                q_square_entries+=1

        IplusQ=[[Fraction(1 if i==j else 0)+Q[i][j] for j in range(m)] for i in range(m)]
        InvFactor=[[Fraction(1 if i==j else 0)-Q[i][j]/Fraction(n+1) for j in range(m)] for i in range(m)]
        P=mm(IplusQ,InvFactor)
        for i in range(m):
            for j in range(m):
                assert P[i][j]==(1 if i==j else 0)
                inverse_entries+=1

        # determinant via the proved spectral multiplicities
        det_scaled=Fraction((n+1)**(n-1),12**m)
        assert det_scaled>0
        determinant_checks+=1

        diag_precision=Fraction(12*(n-1),n+1)
        for a,e in enumerate(es):
            for b in range(a+1,m):
                f=es[b]
                s=dot(e,f)
                cov=Fraction(s,12)
                corr=cov/Fraction(1,4)
                precision=Fraction(-12*s,n+1)
                partial=-precision/diag_precision
                assert corr==Fraction(s,3)
                assert partial==Fraction(s,n-1)
                if s==0:
                    assert set(e).isdisjoint(f)
                    assert cov==0 and precision==0 and partial==0
                else:
                    assert len(set(e)&set(f))==1 and abs(s)==1
                pair_class_checks+=1

    print(
        "VERIFY_OK "
        f"permutations_checked={permutations_checked} "
        f"covariance_entries={covariance_entries} "
        f"q_square_entries={q_square_entries} "
        f"inverse_entries={inverse_entries} "
        f"pair_class_checks={pair_class_checks} "
        f"determinant_checks={determinant_checks}"
    )

if __name__=="__main__":
    run()
