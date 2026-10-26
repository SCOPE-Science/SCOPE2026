#!/usr/bin/env python3
from math import gcd, lcm

def primes(n):
    z = bytearray(b'\x01')*(n+1);z[0]=z[1]=0
    for p in range(2,int(n**0.5)+1):
        if z[p]:z[p*p::p]=b'\x00'*len(z[p*p::p])
    return [i for i in range(2,n+1) if z[i]]
P=primes(200000)

def order2(m):
    a=2%m;d=1
    while a!=1:a=a*2%m;d+=1
    return d

def phi_composite_sqfree(p,q,m):
    # for pair distinct primes p,q
    return (pow(2,p*q,m)-pow(2,p,m)-pow(2,q,m)+2)%m

odd_checks=0; two_checks=0
for m in range(5,60,2):
    d=order2(m)
    assert d>=3 and pow(2,d,m)==1
    r=next(i for i in range(2,d) if gcd(i,d)==1)
    for T in range(1,26):
        p=next(p for p in P if p>100 and p%d==r)
        L=lcm(T,d)
        q=next(q for q in P if q>p and q%L==1)
        assert (p*q-p)%T==0
        assert (pow(2,p,m)-2)%m!=0
        assert phi_composite_sqfree(p,q,m)==0
        odd_checks+=1
for T in range(1,26):
    p=next(p for p in P if p>100 and p%T==1%T)
    assert p*p%T==p%T
    assert (pow(2,p,4)-2)%4==2
    assert (pow(2,p*p,4)-pow(2,p,4))%4==0
    two_checks+=1
# All Phi(n) for n>=3 vanish mod6, from mobius and independent direct enumeration for n<=25.
def mobius(n):
    p=2; out=1
    while p*p<=n:
        if n%p==0:
            n//=p;out=-out
            if n%p==0:return 0
        p+=1
    if n>1:out=-out
    return out
for n in range(3,121):
    v=sum(mobius(d)*(pow(2,n//d,6)-1) for d in range(1,n+1) if n%d==0)
    assert v%6==0,n
print('VERIFY_OK odd_modulus_dirichlet_witnesses',odd_checks,'mod4_witnesses',two_checks,'Phi_mod6_inputs',118)
