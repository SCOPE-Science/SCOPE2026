#!/usr/bin/env python3
"""Exact independent cycle-type computation of embedded monogenic submonoids."""
from collections import Counter
from functools import lru_cache
from math import factorial, comb, lcm
from fractions import Fraction

@lru_cache(None)
def partitions(n,maxpart=None):
    if maxpart is None:maxpart=n
    if n==0:return ((),)
    out=[]
    for j in range(min(n,maxpart),0,-1):
        for tail in partitions(n-j,j):out.append((j,)+tail)
    return tuple(out)

def phi(n):
    a=n;p=2
    while p*p<=n:
        if n%p==0:
            a=a//p*(p-1)
            while n%p==0:n//=p
        p+=1
    if n>1:a=a//n*(n-1)
    return a

def perm_types(n):
    for v in partitions(n):
        c=Counter(v)
        z=1
        for j,m in c.items():z*=j**m*factorial(m)
        period=lcm(*v) if v else 1
        weight=Fraction(factorial(n),z)
        assert weight.denominator==1
        yield int(weight),period

def summary(n):
    H=0;S=Fraction(0)
    for k in range(1,n+1):
        a=comb(n,k)*k**(n-k)
        H+=a*factorial(k)
        S+=a*sum((Fraction(w,phi(p)) for w,p in perm_types(k)),Fraction(0))
    assert S.denominator==1
    # All deeper-tail maps have unique generated submonoid.
    M=n**n-H+int(S)
    return M,H,n**n-M
if __name__=='__main__':
    for n in range(1,19):
        M,H,D=summary(n)
        print(n,M,H,D, f'D/H={D/H:.6f}')
    assert [summary(n)[0] for n in range(1,7)]==[1,4,26,237,2842,42488]
    print('PARTITION_CHECK_OK')
