#!/usr/bin/env python3
"""Exact finite verification of the two-coordinate Fock cone theorem.

This checker is supplementary: asymptotic and global norm assertions
require the analytic arguments in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb, factorial, sqrt, pi


def lam(n, m):
    s = n + m + 1
    return Q(sum(comb(s,j) for j in range(n+1)), 2**s)


def beta_lam(n,m):
    s=n+m
    v=sum(((-1)**j)*comb(m,j)*(Q(1)-Q(1,2**(n+j+1)))/Q(n+j+1) for j in range(m+1))
    return v*Q(factorial(s+1),factorial(n)*factorial(m))


def w2(n,m):
    s=n+m+1
    return Q((n+1)*comb(s,n+1)**2,2**(2*s+2))


def shell_exact(s):
    return sum((lam(n,s-n)*(1-lam(n,s-n)) for n in range(s+1)),Q(0))


def shell_closed(s):
    k=s+1
    return Q(k*comb(2*k,k), 2*4**k)


def total_closed(N):
    k=N+1
    return Q(k*(2*k+1)*comb(2*k,k), 6*4**k)

count=0
for n in range(11):
 for m in range(11):
    assert lam(n,m)==beta_lam(n,m)
    assert lam(n,m)+lam(m,n)==1
    assert (n+1)*(lam(n+1,m)-lam(n,m))**2==w2(n,m)
    count += 3
for s in range(45):
    assert shell_exact(s)==shell_closed(s)
    count += 1
for N in range(28):
    lhs=sum((shell_exact(s) for s in range(N+1)),Q(0))
    assert lhs == total_closed(N)
    tr=sum((lam(n,s-n) for s in range(N+1) for n in range(s+1)),Q(0))
    assert tr==Q((N+1)*(N+2),4)
    count+=2
for a in range(1,100):
    # Two neighboring levels tie for the maximizing weight for fixed a=n+1.
    n=a-1
    wbest=w2(n,a-1)
    assert wbest==w2(n,a)
    for m in range(max(0,a-12),a+13):
        assert w2(n,m)<=wbest
        count+=1
    count+=1
    # Wallis-bound monotonicity is exact, no floating point needed.
    if a>1:
        assert a*Q(comb(2*a,a)**2,16**a)>(a-1)*Q(comb(2*a-2,a-1)**2,16**(a-1))
        count+=1
for N in (100,1000,10000):
    k=N+1
    coeff=total_closed(N)
    assert abs(float(coeff)/N**1.5-1/(3*sqrt(pi)))<0.04
    count+=1
print(f"PASS: {count} exact/numeric supplementary assertions; critical infinite assertions proved in RESULT.md")
