#!/usr/bin/env python3
"""Independent finite tests of three-colour cyclic dynamics on paths.
Run: python3 verify.py
"""
from itertools import product
from math import comb

def direct_sync(d):
    x=[0]
    for a in d:x.append((x[-1]+a)%3)
    n=len(x)
    for t in range(n):
        if len(set(x))==1:return t
        nxt=x[:]
        for i,a in enumerate(x):
            want=(a+1)%3
            if (i>0 and x[i-1]==want) or (i+1<n and x[i+1]==want):nxt[i]=want
        x=nxt
    raise AssertionError('No synchronization by diameter')

def radius(d):
    s=[0]
    for a in d:s.append(s[-1]+a)
    mx=max(s); maxima=[i for i,z in enumerate(s) if z==mx]
    return max(min(abs(i-j) for j in maxima) for i in range(len(s)))

def walkcoef(k,h):
    # Number of unrestricted {-1,0,+1} paths with net displacement h.
    a={0:1}
    for _ in range(k):
        b={}
        for z,c in a.items():
            for step in (-1,0,1):b[z+step]=b.get(z+step,0)+c
        a=b
    return a.get(h,0)

num=0
for n in range(2,12):
    count=0; dist={}
    for d in product((-1,0,1),repeat=n-1):
        a=direct_sync(d);b=radius(d)
        assert a==b,(n,d,a,b)
        count+=(a==n-1)
        dist[a]=dist.get(a,0)+1
        num+=1
    predicted=2*(walkcoef(n-2,0)+walkcoef(n-2,1))
    assert count==predicted,(n,count,predicted)
    print('n=%d, initial states=%d, maximal_delay_states=%d, distribution=%s'%
          (n,3**n,3*count,','.join('%d:%d'%(i,3*dist.get(i,0)) for i in range(n))))
# All two-symbol paths, independently checked against infection-distance.
two_checked=0
for n in range(2,12):
    for bits in product((0,1),repeat=n):
        d=tuple(((bits[i+1]-bits[i]+1)%3)-1 if False else bits[i+1]-bits[i] for i in range(n-1))
        # A single {0,1} pair gives the same height differences as integer subtraction.
        assert all(z in (-1,0,1) for z in d)
        sim=direct_sync(d)
        want=max(min(abs(i-j) for j,v in enumerate(bits) if v==1)
                 for i in range(n)) if 1 in bits else 0
        assert sim==want,(n,bits,sim,want)
        two_checked+=1
# Independent rational calculation of the one-dependent diffusion variance.
from fractions import Fraction
for a,b in ((Fraction(1,3),Fraction(1,3)),(Fraction(1,2),Fraction(1,3)),
            (Fraction(7,10),Fraction(1,10)),(Fraction(1,2),Fraction(1,2))):
    c=1-a-b; p=(a,b,c)
    single=sum(p[i]*p[j]*(((j-i)%3)==1 or ((j-i)%3)==2)
               for i in range(3) for j in range(3))
    def delta(i,j):return (0,1,-1)[(j-i)%3]
    lag=sum(p[i]*p[j]*p[k]*delta(i,j)*delta(j,k)
            for i in range(3) for j in range(3) for k in range(3))
    assert single+2*lag==18*a*b*c,(a,b,c,single,lag)
print('CCA_PATH_VERIFY_OK; gradient words checked=',num,
      '; labelled states represented=',3*num,'; two-color words checked=',two_checked)

