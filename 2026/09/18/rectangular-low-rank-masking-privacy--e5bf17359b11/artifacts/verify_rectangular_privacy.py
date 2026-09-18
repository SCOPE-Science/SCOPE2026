#!/usr/bin/env python3
"""Finite checks for the rectangular low-rank masking formulas over F_2."""

from itertools import product
from fractions import Fraction

def rank2(bits, m, n):
    rows=[]
    for i in range(m):
        x=0
        for j in range(n):
            if bits[i*n+j]:
                x |= 1<<j
        rows.append(x)
    r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if (rows[i]>>c)&1), None)
        if piv is None:
            continue
        rows[r], rows[piv]=rows[piv], rows[r]
        for i in range(m):
            if i != r and ((rows[i]>>c)&1):
                rows[i] ^= rows[r]
        r += 1
    return r

def C(m,n,t,q=2):
    z=Fraction(1,1)
    for j in range(t):
        z *= Fraction((q**m-q**j)*(q**n-q**j), q**t-q**j)
    assert z.denominator == 1
    return z.numerator

def all_mats(m,n):
    return list(product((0,1), repeat=m*n))

def dot2(a,b):
    return sum(x*y for x,y in zip(a,b)) & 1

def verify_ball(m,n,r):
    mats=all_mats(m,n)
    ball=[M for M in mats if rank2(M,m,n) <= r]
    best=Fraction(0,1)
    best_rank=None
    for H in mats[1:]:
        s=sum(1 if dot2(H,M)==0 else -1 for M in ball)
        v=Fraction(abs(s),len(ball))
        if v>best:
            best=v
            best_rank=rank2(H,m,n)
    formula=Fraction((2**r)*C(m-1,n-1,r),len(ball))
    assert best == formula
    assert best_rank == 1
    return len(ball), best

def mat_add(A,K):
    return tuple(a^k for a,k in zip(A,K))

def kernel_size(A,m,n):
    # |ker A| = 2^(n-rank A)
    return 2**(n-rank2(A,m,n))

def verify_covariance(m,n,K):
    mats=all_mats(m,n)
    t=rank2(K,m,n)
    vals=[kernel_size(A,m,n) for A in mats]
    vals2=[kernel_size(mat_add(A,K),m,n) for A in mats]
    N=len(vals)
    mu=Fraction(sum(vals),N)
    cov=Fraction(sum((x-mu)*(y-mu) for x,y in zip(vals,vals2)),N)
    var=Fraction(sum((x-mu)*(x-mu) for x in vals),N)
    corr=cov/var
    q=2
    formula=Fraction(q**(m+n-t)-q**m-q**n+1,
                     (q**m-1)*(q**n-1))
    assert corr == formula
    return t,corr

if __name__ == "__main__":
    cases=[(2,3,1),(3,3,1),(3,4,1),(3,3,2)]
    for case in cases:
        v,rho=verify_ball(*case)
        print("rank-ball",case,"volume",v,"rho",f"{rho.numerator}/{rho.denominator}")

    m,n=3,4
    # rank-one mask with a single 1 entry
    K=(1,)+(0,)*(m*n-1)
    t,corr=verify_covariance(m,n,K)
    print("kernel-correlation",(m,n),"rank",t,"corr",f"{corr.numerator}/{corr.denominator}")

    # Factor-two lower-bound algebra for a representative rectangular case.
    q=2; r=1
    lower=Fraction(q**(m+n-r)-q**m-q**n+1,
                   (q**m-1)*(q**n-1))
    assert lower >= Fraction(1,2)*Fraction(1,q**r)
    print("universal-lower",(m,n,r),f"{lower.numerator}/{lower.denominator}",
          ">=",f"{1}/{2*q**r}")
    print("PASS")
