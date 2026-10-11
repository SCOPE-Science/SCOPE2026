#!/usr/bin/env python3
"""Exact eigenpair checks for the degree-two Walsh/Hamming-shell concentration theorem.
Standard Python library only; finite checks are not proofs of all-size assertions.
"""
from itertools import combinations
from fractions import Fraction
from math import comb, isqrt

def values(n,k):
    m=comb(n,k)
    d=n-2*k;t=d*d
    a0=Fraction(t*t-2*t+3*n*n-2*n,2*n*(n-1))
    a1=Fraction((n*n-t)*(t+n-2),n*(n-1)*(n-2))
    a2=Fraction((n*n-t)*((n-2)**2-t),n*(n-1)*(n-2)*(n-3))
    return tuple(Fraction(m,2**n)*a for a in (a0,a1,a2))

def K(n,x,y):
    d=(x^y).bit_count(); t=n-2*d
    return 1+t+(t*t-n)//2

def eigcheck(n,k):
    S=[sum(1<<i for i in c) for c in combinations(range(n),k)]
    lam=values(n,k)
    def vectors(x):
        f1=((x&1)!=0)-((x&2)!=0)
        f2=f1*(((x&4)!=0)-((x&8)!=0))
        return (1,int(f1),int(f2))
    Vs=[vectors(x) for x in S]
    assert any(v[1] for v in Vs) and any(v[2] for v in Vs)
    for i,x in enumerate(S):
        rr=[0,0,0]
        for y,v in zip(S,Vs):
            z=K(n,x,y)
            for j in range(3):rr[j]+=z*v[j]
        for j in range(3):
            assert Fraction(rr[j],2**n)==lam[j]*Vs[i][j],(n,k,j,rr[j],lam[j],Vs[i])
    # Trace = spatial fraction times bandwidth dimension, exact.
    d0,d1,d2=1,n-1,comb(n,2)-n
    assert lam[0]*d0+lam[1]*d1+lam[2]*d2 == Fraction(len(S)*(1+n+comb(n,2)),2**n)
    t=(n-2*k)**2
    assert (lam[0]==lam[1])== ((t-n)**2==4*(n-1))
    assert (lam[1]==lam[2])==(t==1)
    assert (lam[0]==lam[2])==(n==5 and t==1 or n==6 and t==0)

def main():
    cases=0
    for n in range(5,12):
        for k in range(2,n-1):
            if comb(n,k)>500:continue
            eigcheck(n,k);cases+=1
    # Additional arithmetic collision checks without huge matrix enumeration.
    arith=0
    for n in range(5,501):
        for k in range(2,n-1):
            a0,a1,a2=values(n,k)
            r=isqrt(n-1);s=abs(n-2*k)
            exp01=(r*r==n-1 and s in (r-1,r+1))
            assert (a0==a1)==exp01
            assert (a1==a2)==(n%2==1 and s==1)
            assert (a0==a2)==((n==5 and s==1) or (n==6 and s==0))
            arith+=1
    print('VERIFY_OK eigenpair_cases=%d arithmetic_collision_cases=%d'%(cases,arith))

if __name__=='__main__':main()
