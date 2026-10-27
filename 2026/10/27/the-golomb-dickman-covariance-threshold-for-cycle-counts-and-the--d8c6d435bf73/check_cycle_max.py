"""Exact verification of a cycle-count/longest-cycle covariance identity.

Python 3 standard library only. Analytical proof is in RESULT.md.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial
from functools import lru_cache

@lru_cache(None)
def max_cdf(n, limit):
    """Exact P(maximum cycle length <= limit) for a uniform permutation."""
    if n == 0:
        return Fraction(1)
    if limit <= 0:
        return Fraction(0)
    # Cycle containing the label 1 has uniform length in [1,n].
    return sum((max_cdf(n-r, limit) for r in range(1, min(n, limit)+1)), Fraction(0)) / n

@lru_cache(None)
def mean_max(n):
    if n == 0:
        return Fraction(0)
    return Fraction(n) - sum((max_cdf(n,k) for k in range(1,n)), Fraction(0))

def palm_mean(n, j):
    assert 1 <= j <= n
    m=n-j
    if m <= j: return Fraction(j)
    return Fraction(j)+sum((1-max_cdf(m,k) for k in range(j,m)),Fraction(0))

def predicted_cov(n,j):
    return (palm_mean(n,j)-mean_max(n))/j

def permutation_stats(p):
    n=len(p); seen=[False]*n; M=0; counts=[0]*(n+1)
    for i in range(n):
        if seen[i]:continue
        j=i; length=0
        while not seen[j]:
            seen[j]=True; j=p[j];length+=1
        counts[length]+=1;M=max(M,length)
    return M,counts

def exhaustive(n):
    f=factorial(n)
    sm=0; sj=[0]*(n+1); sjm=[0]*(n+1)
    for p in permutations(range(n)):
        M, counts=permutation_stats(p)
        sm+=M
        for j in range(1,n+1):
            sj[j]+=counts[j]; sjm[j]+=counts[j]*M
    assert Fraction(sm,f)==mean_max(n),('mean',n)
    for j in range(1,n+1):
        direct=Fraction(sjm[j],f)-Fraction(sj[j]*sm,f*f)
        assert direct==predicted_cov(n,j),('cov',n,j,direct,predicted_cov(n,j))
        assert Fraction(sj[j],f)==Fraction(1,j),('cycle mean',n,j)
    return n

def check():
    ct=0
    for n in range(1,9):
        exhaustive(n);ct+=n
    print('exhaustive uniform permutations: n=1..8, covariance checks',ct)
    analytical=0
    for n in range(2,61):
        mu=mean_max(n)
        assert Fraction(n+1,2)<=mu<n
        for j in range(1,n+1):
            cov=predicted_cov(n,j)
            # Check the strict sign theorem with exact rational arithmetic.
            assert (cov>0)-(cov<0)==(Fraction(j)>mu)-(Fraction(j)<mu),(n,j,cov,mu)
            if j>n//2:
                assert cov==Fraction(j-mu,j),(n,j)
            else:
                lower=n-j
                assert cov <= -Fraction(n-2*j+1,2*lower),(n,j,cov)
            analytical+=1
    print('exact recurrence and sign comparisons: n=2..60, pairs',analytical)
    for n in [10,20,40,60,100,140]:
        mu=mean_max(n)
        jstar=min(j for j in range(1,n+1) if j>mu)
        print('n',n,'Emax',str(mu) if n<=10 else f'{float(mu):.10f}',
              'first-positive-length',jstar,'fraction',f'{float(mu/n):.10f}')
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':
    check()
