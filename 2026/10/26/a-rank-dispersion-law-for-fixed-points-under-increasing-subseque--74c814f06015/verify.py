#!/usr/bin/env python3
"""Exact independent enumeration of permutation fixed-point/increasing-subsequence dependence."""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def ranks(n, k, i):
    den=comb(n-1,k-1)
    return [Fraction(comb(i-1,r-1)*comb(n-i,k-r),den) if 0<=r-1<=i-1 and 0<=k-r<=n-i else Fraction(0) for r in range(1,k+1)]


def covariance_formula(n,k,i=None):
    iset=range(1,n+1) if i is None else [i]
    return Fraction(comb(n-1,k-1),n*factorial(k-1))*sum((q-Fraction(1,k))**2 for j in iset for q in ranks(n,k,j))


def subsequence_counts(p):
    n=len(p)
    dp=[[0]*(n+1) for _ in range(n)]
    for j in range(n):
        dp[j][1]=1
        for i in range(j):
            if p[i]<p[j]:
                for k in range(2,j+2):dp[j][k]+=dp[i][k-1]
    return [sum(row[k] for row in dp) for k in range(n+1)]


def run():
    checks=0
    total_perm=0
    for n in range(2,9):
        fac=factorial(n)
        ez=[0]*(n+1); efz=[0]*(n+1)
        ei=[[0]*(n+1) for _ in range(n)]
        for p in permutations(range(1,n+1)):
            z=subsequence_counts(p)
            fidx=[i for i in range(n) if p[i]==i+1]
            f=len(fidx)
            total_perm+=1
            for k in range(2,n+1):
                ez[k]+=z[k];efz[k]+=f*z[k]
                for i in fidx:ei[i][k]+=z[k]
        for k in range(2,n+1):
            true=Fraction(efz[k],fac)-Fraction(ez[k],fac) # E F =1
            formula=covariance_formula(n,k)
            assert true==formula,(n,k,true,formula)
            checks+=1
            for i in range(n):
                true_local=Fraction(ei[i][k],fac)-Fraction(ez[k],fac*n)
                formula_local=covariance_formula(n,k,i+1)
                assert true_local==formula_local,(n,k,i,true_local,formula_local)
                checks+=1
                assert formula_local>=0
                checks+=1
            assert formula>0
            checks+=1
    for n in (9,10,12,16,22,35):
        for k in range(2,n+1):
            q=[ranks(n,k,i) for i in range(1,n+1)]
            assert all(sum(row)==1 for row in q)
            assert covariance_formula(n,k)>0
            checks+=2
            if k==2:
                assert covariance_formula(n,k)==Fraction(n+1,6)
                checks+=1
            if k==3:
                assert covariance_formula(n,k)==Fraction((n+1)*(3*n-4),60)
                checks+=1
            if k==n:
                assert covariance_formula(n,k)==Fraction(n-1,factorial(n))
                checks+=1
            for i in range(1,n+1):
                loc=covariance_formula(n,k,i)
                eq=(k==2 and n%2==1 and i==(n+1)//2)
                assert (loc==0)==eq,(n,k,i,loc)
                checks+=1
    for k in range(2,13):
        term=Fraction(4**(k-1)*factorial(k-1)**2,factorial(2*k-1))
        integrated=sum(Fraction(comb(k-1,j)**2*factorial(2*j)*factorial(2*k-2-2*j),factorial(2*k-1)) for j in range(k))
        assert term==integrated
        assert term>Fraction(1,k)
        checks+=2
    print(f'PASS: {checks} exact comparisons, {total_perm} complete permutations, n=2..8 exhaustive; n<=35 symbolic identities.')

if __name__=='__main__':run()
