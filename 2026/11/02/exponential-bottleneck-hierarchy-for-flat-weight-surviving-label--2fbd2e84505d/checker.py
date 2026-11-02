"""Finite arithmetic sanity checks for the flat-weight surviving-label chain.
These checks do not certify any asymptotic limit.
"""
from fractions import Fraction
from math import comb, factorial

CHECKS=0
def check(condition):
    global CHECKS
    assert condition
    CHECKS += 1

def stirling(n):
    a=[[0]*(n+1) for _ in range(n+1)]
    a[0][0]=1
    for m in range(1,n+1):
        for j in range(1,m+1):
            a[m][j]=a[m-1][j-1]+j*a[m-1][j]
    return a[n]

def transitions(n,k,S):
    return {j:Fraction(comb(k,j)*factorial(j)*S[j],k**n)
            for j in range(1,k+1)}

for n in range(3,18):
    S=stirling(n)
    expected={1:Fraction(0)}
    for k in range(2,n+1):
        p=transitions(n,k,S)
        q=1-p[k]
        check(sum(p.values())==1)
        check(q>=Fraction((k-1)**n,k**n))
        check(p[1]==Fraction(k,k**n))
        check(q>0)
        if k==2:
            check(q==Fraction(2,2**n))
        if k==3:
            check(q==Fraction(3*(2**n-1),3**n))
        expected[k]=(1+sum(p[j]*expected[j] for j in range(1,k)))/q
    err=float(expected[n])-2**(n-1)-(1.5**n)/3
    check(abs(err)<= 3*n*(4/3)**n+n**3)

# Exact visiting probability recurrence, independently of the holding-time recursion.
for n in range(3,13):
    S=stirling(n)
    P={k:transitions(n,k,S) for k in range(2,n+1)}
    for r in (2,3):
        h={k:(Fraction(1) if k==r else Fraction(0)) for k in range(1,r+1)}
        for k in range(r+1,n+1):
            q=1-P[k][k]
            h[k]=sum(P[k][j]*h[j] for j in range(1,k))/q
        check(0<h[n]<=1)
        check(1-h[n]<= n**r*Fraction((r-1)**n,r**n))

print('PASS:',CHECKS,'exact rational assertions')
