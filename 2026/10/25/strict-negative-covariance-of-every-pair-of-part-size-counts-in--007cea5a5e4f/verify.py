#!/usr/bin/env python3
"""Integer-only checks for the finite uniform-partition covariance theorem."""
from fractions import Fraction

def partition_numbers(N):
    p=[1]+[0]*N
    for j in range(1,N+1):
        for k in range(j,N+1): p[k]+=p[k-j]
    return p

def partitions(n, lower=1):
    if n==0:
        yield ()
        return
    for k in range(lower,n+1):
        for tail in partitions(n-k,k): yield (k,)+tail

def run():
    p=partition_numbers(100)
    count=0
    def ck(x,desc):
        nonlocal count
        assert x,desc
        count+=1
    # The strict elementary 2/3 step inequality for all base points 1..25.
    for t in range(1,26):
        for a,b in [(2,2),(2,3),(3,3)]:
            ck(p[t+a]*p[t+b] > p[t]*p[t+a+b], ('step',t,a,b))
    # Outside the strict-log-concavity tail the quotient F=S(n-1)/p(n) is monotone.
    S=0
    F=[Fraction(0)]
    for n in range(1,28):
        S+=p[n-1]
        F.append(Fraction(S,p[n]))
    for n in range(0,26):
        ck(F[n+1]>=F[n],('Fmon',n))
        ck(F[n+1]>F[n] or n==1,('Fstrict',n))
    ck(p[27] < 2*p[26], 'tail quotient less than two')
    for k in range(2,27):
        ck(p[k]*p[26]>=p[k-1]*p[27],('ratios',k))
    # BO p(a)*p(b)>p(a+b) if a,b>=2 and a+b>=10.
    for a in range(2,101):
        for b in range(2,101-a):
            if a+b>=10: ck(p[a]*p[b]>p[a+b],('BO finite probe',a,b))
    # Exact mixed-moment formulas for all size pairs through n=32.
    for n in range(2,33):
        for i in range(1,n):
            sx=sum(p[n-a*i] for a in range(1,n//i+1))
            for j in range(i+1,n+1):
                sy=sum(p[n-b*j] for b in range(1,n//j+1))
                sxy=sum(p[n-a*i-b*j] for a in range(1,n//i+1) for b in range(1,n//j+1) if n>=a*i+b*j)
                covnum=p[n]*sxy-sx*sy
                ck(covnum<0,('cov',n,i,j,covnum))
    # Independently enumerate partitions (no use of coefficient formulas) n<=12.
    for n in range(2,13):
        cases=list(partitions(n))
        ck(len(cases)==p[n],('enumerate',n))
        marg=[0]*(n+1)
        cross=[[0]*(n+1) for _ in range(n+1)]
        for lam in cases:
            v=[0]*(n+1)
            for s in lam:v[s]+=1
            for i in range(1,n+1):
                marg[i]+=v[i]
                for j in range(i+1,n+1):cross[i][j]+=v[i]*v[j]
        for i in range(1,n+1):
            ck(marg[i]==sum(p[n-a*i] for a in range(1,n//i+1)), ('marg',n,i))
            for j in range(i+1,n+1):
                target=sum(p[n-a*i-b*j] for a in range(1,n//i+1) for b in range(1,n//j+1) if n>=a*i+b*j)
                ck(cross[i][j]==target,('mixed',n,i,j))
    # At n=3, size-presence (not counts) is positively correlated: boundaries matter.
    cases=list(partitions(3))
    a=sum(1 in x for x in cases);b=sum(2 in x for x in cases);ab=sum(1 in x and 2 in x for x in cases)
    ck(ab*len(cases)-a*b>0,'size-presence warning')
    print(f'PASS: {count} exact integer/rational assertions, unrestricted theorem from the analytical proof; p(100)={p[100]}')
if __name__=='__main__':run()
