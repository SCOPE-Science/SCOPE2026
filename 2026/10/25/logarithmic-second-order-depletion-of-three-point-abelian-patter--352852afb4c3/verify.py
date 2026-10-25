#!/usr/bin/env python3
"""Finite exact checks for the triple-prefix enumeration; stdlib only."""
from math import gcd
from fractions import Fraction

def forest_bruteforce(a,b,c):
    parent=list(range(2*(c+1)))
    def find(x):
        while x!=parent[x]:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for t in (a,b,c):
        for i in range(t+1):
            j=t-i
            u,v=find(i),find(c+1+j)
            if u==v: return False
            parent[u]=v
    return True

def direct(N):
    return sum(c>a+b+gcd(b-a,c-b)
               for a in range(N+1)
               for b in range(a+1,N+1)
               for c in range(b+1,N+1))

def reduced(N):
    return sum(max(0,min(N-x-y+1,y-gcd(x,y)))
               for x in range(1,N)
               for y in range(1,N-x+1))

def totient(d):
    return sum(gcd(d,j)==1 for j in range(1,d+1))

def M(t):
    return sum(max(0,t-2*v) for v in range(1,t//2+1))

checks=0
for a in range(0,8):
    for b in range(a+1,13):
        for c in range(b+1,23):
            assert forest_bruteforce(a,b,c)==(c>a+b+gcd(b-a,c-b))
            checks+=1
for N in range(2,29):
    assert reduced(N)==direct(N),N
    checks+=1
for n in range(2,90):
    assert M(n)==((n-1)**2)//4
    checks+=1
for n in range(2,95):
    lhs=sum(gcd(x,y) for x in range(1,n+1) for y in range(1,n+1))
    rhs=sum(totient(d)*(n//d)**2 for d in range(1,n+1))
    assert lhs==rhs
    checks+=1
for N in (30,50,100,200,400):
    q=sum(min(N-x-y+1,y) for x in range(1,N) for y in range(1,N-x+1))
    assert q>=reduced(N)
    checks+=1
print('VERIFY_OK', checks, 'finite exact assertions')
