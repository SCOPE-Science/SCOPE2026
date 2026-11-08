"""Separate exact checks for the cherry/parity covariance formula.
Usage: python3 check.py (Python standard library only).
"""
from functools import lru_cache
from fractions import Fraction
from math import comb

@lru_cache(None)
def all_trees(n):
    if n == 0:
        return (None,)
    return tuple((l,r) for i in range(n) for l in all_trees(i) for r in all_trees(n-1-i))

def statistics(tree, depth=0):
    if tree is None:
        return ((-1)**depth,0)
    l,r=tree
    a,c=statistics(l, depth+1)
    b,d=statistics(r, depth+1)
    return a+b,c+d+int(l is None and r is None)

N=100
C=[0]*(N+1);D=[0]*(N+1);H=[0]*(N+1);Q=[0]*(N+1)
C[0]=D[0]=1
for n in range(1,N+1):
    for i in range(n):
        j=n-1-i
        C[n]+=C[i]*C[j]
        D[n]-=D[i]*C[j]+C[i]*D[j]
        H[n]+=H[i]*C[j]+C[i]*H[j]
        Q[n]-=Q[i]*C[j]+D[i]*H[j]+H[i]*D[j]+C[i]*Q[j]
    if n==1:
        H[n]+=1
        Q[n]-=2

checks=0
for n in range(10):
    trees=all_trees(n)
    assert len(trees)==C[n]
    d=h=q=0
    for tree in trees:
        v,c=statistics(tree)
        d+=v;h+=c;q+=v*c
    assert (d,h,q)==(D[n],H[n],Q[n]),(n,d,h,q,D[n],H[n],Q[n]);checks+=4

# Separate formal-derivative coefficient equations for D, H, Q.
Dp=[0]*(N+1);Hp=[0]*(N+1);Qp=[0]*(N+1)
Dp[0]=1
for n in range(1,N+1):
    Dp[n]=-2*sum(C[i]*Dp[n-1-i] for i in range(n))
    Hp[n]=(n==1)+2*sum(C[i]*Hp[n-1-i] for i in range(n))
    Qp[n]=-2*(n==1)-2*sum(C[i]*Qp[n-1-i]+Hp[i]*Dp[n-1-i] for i in range(n))
    assert Dp[n]==D[n];assert Hp[n]==H[n];assert Qp[n]==Q[n]
    assert C[n]==comb(2*n,n)//(n+1)
    assert H[n]==comb(2*n-2,n-1)
    checks+=5

# Finite covariance tests, and convergence diagnostics (not a proof of limit).
def cov(n):
    return Fraction(Q[n],C[n])-Fraction(D[n]*H[n],C[n]**2)
assert cov(1)==0 and cov(2)==0
assert cov(3)==Fraction(24,25)
assert cov(4)==Fraction(-24,49)
assert cov(5)==Fraction(4,7)
assert cov(6)==Fraction(-12,121)
for n in range(7,N+1):
    assert cov(n)>0
print('CHECKS_PASS',checks+6+(N-6))
for n in (3,4,5,6,7,10,20,50,100):
    print('n=',n,'cov=',float(cov(n)), 'exact=',str(cov(n))[:70])
