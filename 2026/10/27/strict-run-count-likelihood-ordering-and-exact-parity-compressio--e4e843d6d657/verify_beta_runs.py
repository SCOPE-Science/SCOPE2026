#!/usr/bin/env python3
"""Exact checks of finite binary-run count kernels and beta-Pólya mixtures."""
from fractions import Fraction
from itertools import product
from math import comb, factorial


def cb(n,k):
    return comb(n,k) if 0 <= k <= n else 0


def count_at_fixed_h(n,h,r):
    if h==0:
        return int(r==1)
    j=r//2
    if r%2==0:
        return 2*cb(h-1,j-1)*cb(n-h-1,j-1)
    return (cb(h-1,j)*cb(n-h-1,j-1)+cb(h-1,j-1)*cb(n-h-1,j))


def rising(x,k):
    v=Fraction(1)
    for z in range(k):
        v*=x+z
    return v


def beta_runs(n,alpha):
    denom=rising(2*alpha,n)
    p=[Fraction(0)]*(n+1)
    for h in range(n//2+1):
        d=1 if 2*h==n else 2
        folded_w=d*comb(n,h)*rising(alpha,h)*rising(alpha,n-h)/denom
        for r in range(1,n+1):
            p[r]+=folded_w*Fraction(count_at_fixed_h(n,h,r),comb(n,h))
    assert sum(p)==1
    return p


def check():
    pairs=0
    strict=0
    checked=0
    for n in range(2,15):
        H=n//2
        K=[[count_at_fixed_h(n,h,r) for r in range(1,n+1)] for h in range(H+1)]
        for h in range(H+1):
            assert sum(K[h])==comb(n,h),(n,h)
        for h in range(H+1):
            for hp in range(h+1,H+1):
                for r in range(n):
                    for s in range(r+1,n):
                        assert K[h][r]*K[hp][s]>=K[h][s]*K[hp][r],(n,h,hp,r,s)
                        pairs+=1
        for h in range(H+1):
            for j in range(1,(n-1)//2+1):
                assert 2*j*K[h][2*j]==(n-2*j)*K[h][2*j-1],(n,h,j)
        for alpha,beta in ((Fraction(1,3),Fraction(2,3)),(Fraction(1,2),Fraction(5,2)),(Fraction(1),Fraction(2)),(Fraction(2),Fraction(7))):
            P=beta_runs(n,alpha)
            Q=beta_runs(n,beta)
            for r in range(1,n):
                lhs=Q[r+1]*P[r]-Q[r]*P[r+1]
                assert lhs>=0,(n,alpha,beta,r,lhs)
                assert (lhs>0)==(r%2==1),(n,alpha,beta,r,lhs)
                strict+=bool(lhs)
                checked+=1
        if n<=11:
            brute=[[0]*(n+1) for _ in range(H+1)]
            for bits in product((0,1),repeat=n):
                h=min(sum(bits),n-sum(bits))
                r=1+sum(bits[i]!=bits[i+1] for i in range(n-1))
                brute[h][r]+=1
            for h in range(H+1):
                factor=1 if 2*h==n else 2
                assert all(brute[h][r]==factor*K[h][r-1] for r in range(1,n+1)),(n,h)
    for n in (2,3,5,8,13):
        for a in (Fraction(1,3),Fraction(1),Fraction(7,2)):
            P=beta_runs(n,a)
            mean=sum(r*P[r] for r in range(1,n+1))
            assert mean == 1+(n-1)*a/(2*a+1),(n,a,mean)
    return f'PASS exact integer kernel 2<=n<=14; {pairs} TP2 minors; {checked} adjacent-beta-ratio checks ({strict} strict); direct binary-word census 2<=n<=11; exact expectation checks.'

if __name__=='__main__':
    print(check())
