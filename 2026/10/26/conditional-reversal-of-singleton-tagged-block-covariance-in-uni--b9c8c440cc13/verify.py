"""Exact finite checks for random-set-partition covariance sign reversal.
Run with Python 3; no third-party packages.
"""
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict
from math import comb

@lru_cache(None)
def stirling(n, k):
    if n == k == 0:
        return 1
    if n < 0 or k < 1 or k > n:
        return 0
    return stirling(n - 1, k - 1) + k * stirling(n - 1, k)

def bell(n):
    return sum(stirling(n, k) for k in range(n + 1))

def covariance_formula(n, k=None):
    if k is None:
        a,b,c,d=bell(n),bell(n-1),bell(n-1),bell(n-2)
    else:
        a=stirling(n,k);b=stirling(n-1,k-1)
        c=stirling(n-1,k);d=stirling(n-2,k-1)
    if not a:
        raise ValueError('out of range')
    return Fraction((n-1)*((n-2)*d*a - n*b*c), a*a)

def set_partitions(n):
    # Each restricted-growth string corresponds to a unique set partition.
    def rec(a, m):
        if len(a)==n:
            yield tuple(a)
        else:
            for j in range(m+2):
                yield from rec(a+[j],max(m,j))
    if n==0:
        yield ()
    else:
        yield from rec([0],0)

def direct_covariance(n, k=None):
    dat=[]
    for labels in set_partitions(n):
        if k is not None and max(labels)+1!=k:
            continue
        counts={i: labels.count(i) for i in set(labels)}
        L=counts[labels[0]]
        T=sum(c==1 for c in counts.values())
        dat.append((L,T))
    N=len(dat)
    return Fraction(sum(x*y for x,y in dat),N)-Fraction(sum(x for x,y in dat)*sum(y for x,y in dat),N*N)

def main():
    checks=0
    for n in range(2,9):
        for k in [None,*range(1,n+1)]:
            got=direct_covariance(n,k)
            exp=covariance_formula(n,k)
            assert got==exp,(n,k,got,exp)
            checks+=1
    for n in range(4,100):
        a=stirling(n,2)
        two=Fraction((n-1)*((n-4)*2**(n-2)+2),a*a)
        assert covariance_formula(n,2)==two>0
        checks+=2
        z=stirling(n,n-2)
        near=Fraction(2*comb(n,3)*3*comb(n,4),n*z*z)
        assert covariance_formula(n,n-2)==near>0
        checks+=2
    for n in range(2,100):
        assert covariance_formula(n,None)<0
        checks+=1
        if n>=3:
            assert bell(n)*bell(n-2)*(n-1)<=n*bell(n-1)**2
            checks+=1
    print('PASS',checks,'exact assertions; exhaustive set partitions n=2..8; formulas/signs to n=99')

if __name__=='__main__':
    main()
