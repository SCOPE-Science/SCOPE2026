#!/usr/bin/env python3
"""Independent finite checks for the rank-stratified X^2=I count over dual numbers.
Standard library only. GF(2) and GF(4) use a polynomial quotient field implementation.
"""
from itertools import product
from fractions import Fraction
from collections import Counter


def fmul(a,b,q):
    if q==2:return a&b
    if q!=4:raise ValueError('checker supports q in {2,4}')
    t=0
    for i in range(2):
        if (b>>i)&1:t ^=a << i
    for i in (2,):
        if (t>>i)&1:t ^= 7 << (i-2) # x^2 + x + 1 = 0
    return t

def mmul(a,b,n,q):
    return tuple(__import__('functools').reduce(lambda x,y:x^y, (fmul(a[i*n+k],b[k*n+j],q) for k in range(n)),0) for i in range(n) for j in range(n))

def rank(A,n,q):
    a=[list(A[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for c in range(n):
        j=next((j for j in range(r,n) if a[j][c]),None)
        if j is None:continue
        a[r],a[j]=a[j],a[r]
        inv=next(t for t in range(1,q) if fmul(t,a[r][c],q)==1)
        a[r]=[fmul(inv,v,q) for v in a[r]]
        for j in range(n):
            if j!=r and a[j][c]:
                fac=a[j][c]
                a[j]=[u^fmul(fac,v,q) for u,v in zip(a[j],a[r])]
        r+=1
    return r

def gl_order(n,q):
    z=1
    for k in range(n):z*=q**n-q**k
    return z

def Phi(k,q):
    p=Fraction(1)
    for i in range(1,k+1):p*=Fraction(q**i-1,q**i)
    return p

def formula(n,q):
    g=gl_order(n,q)
    z={r:g/(Phi(r,q)*Phi(n-2*r,q)) for r in range(n//2+1)}
    assert all(isinstance(v,Fraction) and v.denominator==1 for v in z.values())
    return {r:int(z[r]) for r in z}

def brute(n,q):
    I=tuple(int(i==j) for i in range(n) for j in range(n))
    zero=(0,)*(n*n)
    counts=Counter()
    base={}
    matrices=list(product(range(q),repeat=n*n))
    for A in matrices:
        if mmul(A,A,n,q)!=I:continue
        N=tuple(a^i for a,i in zip(A,I))
        r=rank(N,n,q)
        base[r]=base.get(r,0)+1
        for B in matrices:
            if tuple(x^y for x,y in zip(mmul(A,B,n,q),mmul(B,A,n,q)))==zero:
                counts[r]+=1
    return dict(counts),base

def main():
    tested=0
    for n,q in [(1,2),(2,2),(3,2),(1,4),(2,4)]:
        actual,base=brute(n,q)
        theoretical=formula(n,q)
        assert actual==theoretical,(n,q,actual,theoretical)
        print('exhaustive dual-number matrices: n=%d q=%d reduction_rank_counts=%s base_involutions=%s total=%d'%(n,q,dict(sorted(actual.items())),dict(sorted(base.items())),sum(actual.values())))
        tested+=q**(2*n*n)
    for n in range(1,12):
        hist=formula(n,2)
        assert sum(hist.values())<=gl_order(n,2)*2**(n*n)
    print('FORMULA_INTEGER_CHECKS_PASSED q=2 n=1..11')
    print('ALL_DUAL_NUMBER_INVOLUTION_RANK_CHECKS_PASSED exhaustive_elements=%d'%tested)

if __name__=='__main__':main()
