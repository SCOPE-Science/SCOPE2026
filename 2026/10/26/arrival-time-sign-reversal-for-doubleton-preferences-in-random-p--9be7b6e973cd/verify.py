#!/usr/bin/env python3
"""Independent exact finite checks for an analytic parking-function result."""
from itertools import product
from fractions import Fraction
from math import comb

def b(m, r, N):
    if r < 0 or r > m:
        return Fraction(0)
    return Fraction(comb(m,r)*(N-1)**(m-r), N**m)

def covariance_formula(n, i, r):
    N=n+1
    return Fraction(N-i+1,N)*(b(n-i,r-1,N)-b(n-i,r,N)-b(n-1,r-1,N)+b(n-1,r,N))

def distinct_formula(n,i):
    N=n+1
    return Fraction(N-i+1,N)*(Fraction((N-1)**(n-i),N**(n-i))-Fraction((N-1)**(n-1),N**(n-1)))

def enumerate_and_check(n):
    cnt=0; suml=[0]*n; sumu=[0]*(n+1)
    pairs=[[0]*(n+1) for _ in range(n)]
    pairsk=[0]*n; sumk=0
    for arr in product(range(n),repeat=n):
        filled=[False]*n; lucky=[]
        for a in arr:
            x=a
            while x<n and filled[x]: x+=1
            if x>=n:break
            lucky.append(int(x==a)); filled[x]=True
        else:
            cnt+=1
            counts=[arr.count(j) for j in range(n)]
            species=[counts.count(r) for r in range(n+1)]
            k=n-species[0]
            sumk+=k
            for j in range(n):
                suml[j]+=lucky[j]
                pairsk[j]+=lucky[j]*k
                for r in range(n+1):pairs[j][r]+=lucky[j]*species[r]
            for r in range(n+1):sumu[r]+=species[r]
    assert cnt==(n+1)**(n-1)
    for j in range(n):
        for r in range(1,n+1):
            actual=Fraction(pairs[j][r],cnt)-Fraction(suml[j]*sumu[r],cnt**2)
            predicted=covariance_formula(n,j+1,r)
            assert actual==predicted,(n,j+1,r,actual,predicted)
        dactual=Fraction(pairsk[j],cnt)-Fraction(suml[j]*sumk,cnt**2)
        assert dactual==distinct_formula(n,j+1)
    print('PARK_EXHAUSTIVE_PASS',n,cnt,'strata',n*n)

def check_formula(n):
    for i in range(1,n+1):
        assert covariance_formula(n,i,1)>0 if i>=2 else covariance_formula(n,i,1)==0
        if i>=2:
            for r in sorted(set([3,4,n//2,n])):
                if 3<=r<=n: assert covariance_formula(n,i,r)<0
        if i==1:
            for r in range(1,n+1):assert covariance_formula(n,i,r)==0
        assert distinct_formula(n,i)>0 if i>=2 else distinct_formula(n,i)==0
    signs=[(covariance_formula(n,i,2)>0)-(covariance_formula(n,i,2)<0) for i in range(2,n+1)]
    if n<=4:
        assert all(v<0 for v in signs)
    else:
        assert signs[0]>0 and signs[-1]<0
        nozeros=[v for v in signs if v!=0]
        assert nozeros==sorted(nozeros,reverse=True)
        assert sum(v==0 for v in signs)<=1

if __name__=='__main__':
    for n in range(2,8):enumerate_and_check(n)
    for n in range(2,201):check_formula(n)
    print('SIGN_AND_RICHNESS_CHECK_PASS n=2..200')
    print('VERIFY_OK')
