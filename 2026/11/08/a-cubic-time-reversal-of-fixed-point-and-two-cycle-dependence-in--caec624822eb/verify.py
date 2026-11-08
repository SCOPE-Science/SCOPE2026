#!/usr/bin/env python3
"""Exact finite tests for the random-transposition covariance theorem."""
from fractions import Fraction
from math import factorial
from itertools import permutations

def modes(n):
    a=n-1; b=n*(n-3)//2; c=(n-1)*(n-2)//2
    d=n*(n-1)*(n-5)//6; e=(n-1)*(n-2)*(n-3)//6
    A=Fraction(n-2,n)
    p=A**3
    q=A*Fraction(n-4,n)
    r=Fraction(n*n-6*n+12,n*n)
    s=Fraction(n-6,n)
    return a,b,c,d,e,p,q,r,s

def numerator(n,t):
    a,b,c,d,e,p,q,r,s=modes(n)
    return d*r**t-e*s**t-a*b*p**t+a*c*q**t

def expected_cov(n,t):
    return numerator(n,t)/2

def cycle_counts(perm):
    n=len(perm); seen=set(); ones=twos=0
    for i in range(n):
        if i not in seen:
            j=i; k=0
            while j not in seen:
                seen.add(j); k+=1; j=perm[j]
            if k==1: ones+=1
            if k==2: twos+=1
    return ones,twos

def exact_walk_cov(n, tmax):
    ident=tuple(range(n)); states={ident:1};denom=1
    for t in range(tmax+1):
        m1=m2=m12=0
        for perm,v in states.items():
            x,y=cycle_counts(perm)
            m1+=x*v; m2+=y*v; m12+=x*y*v
        observed=Fraction(m12,denom)-Fraction(m1*m2,denom*denom)
        predicted=expected_cov(n,t)
        assert observed==predicted,(n,t,observed,predicted)
        print(f'n={n} t={t} covariance={predicted} states={len(states)}')
        if t==tmax:break
        nextstates={}
        for perm,v in states.items():
            for i in range(n):
                for j in range(n):
                    if i==j: new=perm
                    else:
                        z=list(perm); z[i],z[j]=z[j],z[i]; new=tuple(z)
                    nextstates[new]=nextstates.get(new,0)+v
        states=nextstates;denom*=n*n

def first_positive(n,lim=3000):
    signs=[];first=None
    for t in range(1,lim+1):
        F=numerator(n,t)
        signs.append(1 if F>0 else (0 if F==0 else -1))
        if F>0 and first is None:first=t
    if first is not None:
        assert all(x<=0 for x in signs[:first-1])
        assert all(x>0 for x in signs[first-1:])
    return first

def main():
    for n,t in [(6,5),(7,3)]:exact_walk_cov(n,t)
    for n in range(6,11):
        print('transition',n,first_positive(n, 1000))
        a,b,c,d,e,p,q,r,s=modes(n)
        assert r>p>q>s>=0
        assert a*c-a*b==n-1
        assert d-e==-(n-1)
        assert numerator(n,0)==0
        assert expected_cov(n,1)==Fraction(-2*(n-1),n*n)
        assert numerator(n,2)-p*numerator(n,1)==Fraction(-4*(n-1)*(5*n**3-30*n**2+52*n-16),n**5)
    print('ALL EXACT TESTS PASSED')
if __name__=='__main__':main()
