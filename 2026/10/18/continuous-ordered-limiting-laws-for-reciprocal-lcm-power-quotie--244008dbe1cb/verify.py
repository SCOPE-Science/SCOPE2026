#!/usr/bin/env python3
"""Elementary exact checks for the local identities and a finite-sample illustration."""
from fractions import Fraction as F
from math import isclose

def factors(n):
    d={}; p=2
    while p*p<=n:
        while n%p==0: d[p]=d.get(p,0)+1;n//=p
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return d

def S(p,a):return sum((F(1,p**j) for j in range(a+1)),F(0))

def local(p,a):
    if a==0:return F(1)
    return (S(p,a)+S(p,a-1))/2

def local_via_square_difference(p,a):
    if a==0:return F(1)
    return F(p**a,2)*(S(p,a)**2-S(p,a-1)**2)

def global_local(n):
    v=F(1)
    for p,a in factors(n).items():v*=local(p,a)
    return v

def global_from_mobius(n):
    # Expansion of F_2 as a square-free divisor sum (exact arithmetic).
    fac=list(factors(n))
    total=F(0)
    for bits in range(1<<len(fac)):
        d=1;mu=1
        for j,p in enumerate(fac):
            if bits>>j&1:d*=p;mu*=-1
        x=n//d
        sm=F(1)
        for p,a in factors(x).items():sm*=S(p,a)
        total+=mu*sm*sm
    return F(n,2**len(fac))*total

def prime_list(n):
    b=bytearray(b'\x01')*(n+1);b[:2]=b'\x00\x00'
    for p in range(2,int(n**.5)+1):
        if b[p]:b[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [i for i,z in enumerate(b) if z]

for p in (2,3,5,7,11,13,17,19):
    for a in range(1,9):assert local(p,a)==local_via_square_difference(p,a)
for n in range(1,1201): assert global_local(n)==global_from_mobius(n)
for p in prime_list(250):
    x=F(1,p)
    # Exact sum of geometric probabilities at kappa=2, simplified symbolically.
    factor=1+x*x/(2*(1-x))
    assert factor==1+F(1,2*p*(p-1))
pr=prime_list(100000)
product=1.
for p in pr:product*=1+1/(2*p*(p-1))
empirical=sum(float(global_local(n)) for n in range(1,6001))/6000
assert 1<empirical<1.65 and 1<product<1.65
print('VERIFY_OK', 'exact_comparisons',1200,'local_checks',64,'truncated_mean',round(product,8),'empirical_mean',round(empirical,8))
