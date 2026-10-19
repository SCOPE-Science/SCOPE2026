#!/usr/bin/env python3
"""Exact standalone arithmetic checks for the statistical interval-map theorem."""
from fractions import Fraction as F
from collections import Counter
from random import Random

a=F(1,4);b=F(1,2)
def f(x):return (abs(abs(12*x-4)-1)+1)/4
def g(x):return abs(8*x-1)/4
def A(x):
    if x<=a:return 1-g(x)
    if x<=b:return 1-f(x)
    return 1-x
def B(x):
    if x<=a:return 1-g(x)
    if x<=b:return 1-x
    if x<=1-a:return f(1-x)
    return 1-x
def occupation(T,x,n):
    values=[]
    for _ in range(n):values.append(x);x=T(x)
    return Counter(values)

def signed(c):return {x:v for x,v in c.items() if v}

rng=Random(98211)
for n in range(1,35):
    for _ in range(120):
        x=F(rng.randrange(1000),1000)
        diff=occupation(A,x,n);diff.subtract(occupation(B,x,n))
        m=n//2
        if a<x<=b:
            y=x
            for _ in range(m):y=f(y)
            expected=Counter([1-y]);expected.subtract(Counter([1-x]))
        elif b<x<1-a:
            y=1-x;z=y
            for _ in range(m):z=f(z)
            expected=Counter([y]);expected.subtract(Counter([z]))
        else:expected=Counter()
        assert signed(diff)==signed(expected),(n,x,diff,expected)
for m in range(1,50):
    x=a+F(1,4*3**m);y=x
    for _ in range(m):y=f(y)
    assert y==b and abs(y-x)==F(1,4)*(1-F(1,3**m))

# Polynomial helpers: coefficient arrays in ascending monomial degree.
def mul(p,q):
    o=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):o[i+j]+=x*y
    return o
def power(p,k):
    o=[F(1)]
    for _ in range(k):o=mul(o,p)
    return o
def sub(p,q):
    n=max(len(p),len(q));return [(p[i] if i<len(p) else 0)-(q[i] if i<len(q) else 0) for i in range(n)]
def integ(p,l,r):return sum(c*(r**(j+1)-l**(j+1))/F(j+1) for j,c in enumerate(p))
branches=[(a,F(1,3),[F(-1,2),F(3)]), (F(1,3),F(5,12),[F(3,2),F(-3)]), (F(5,12),b,[F(-1),F(3)])]
def D(i,j):
    z=F(0)
    for l,r,v in branches:
        rv=[1-v[0],-v[1]]
        xx=[F(0),F(1)];rx=[F(1),F(-1)]
        z+=integ(sub(mul(power(xx,i),power(rv,j)),mul(power(rx,i),power(v,j))),l,r)
    return z/(2*(b-a))
M=[[D(i,j) for j in range(4)]for i in range(4)]
for i in range(3):
    for j in range(3):assert M[i][j]+M[j][i]==0
assert M[3][3]==-F(1,138240)
assert M[2][3]+M[3][2]==-F(1,207360)
for j in (0,1):assert M[j][3]+M[3][j]==0
assert A(F(2,5))!=B(F(2,5))
print('VERIFICATION_OK exact signed orbits 4080; sharp witnesses 49; polynomial covariance coefficients 16')
