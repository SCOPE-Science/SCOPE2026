#!/usr/bin/env python3
"""Exact finite tests of a primorial obstruction for coprime linear representations."""
from math import gcd, prod

def primes_upto(r):
    return [n for n in range(2,r+1) if all(n%d for d in range(2,int(n**.5)+1))]

def obstruction(a,b,r):
    assert a>=3 and gcd(a,b)==1
    q=prod(p for p in primes_upto(r) if a%p)
    assert b>a*q
    target=next(t for t in range(1,a) if gcd(t,a)==1 and t!=b%a)
    lower=r*b;upper=(r+1)*b
    # q*k has desired residue target modulo a.
    k0=(target*pow(q,-1,a))%a
    k=(lower//q+1)
    k+=((k0-k)%a)
    n=q*k
    assert lower<n<upper and n%a==target and gcd(n,a)==1
    counter=0
    for y in range(n//b+1):
        if (n-b*y)%a==0:
            x=(n-b*y)//a
            counter+=1
            assert gcd(x,y)>1,(a,b,r,n,x,y)
    return n,counter,q

def exact_g2(b):
    assert b>=3 and b%2==1
    top=6*b+20
    def representable(n):
        return any((n-b*y)%2==0 and gcd((n-b*y)//2,y)==1 for y in range(n//b+1))
    assert not representable(4*b-2)
    assert all(representable(n) for n in range(4*b-1,top+1))
    return 4*b-2

if __name__=='__main__':
    c=0
    for a in range(3,13):
        for r in (2,3,5,7,11):
            q=prod(p for p in primes_upto(r) if a%p)
            b=a*q+1
            while gcd(a,b)!=1: b+=1
            n,cnt,q=obstruction(a,b,r)
            c+=1
    for b in range(3,102,2): exact_g2(b)
    print(f'CERTIFICATE_OK primorial_obstructions={c} exact_boundary_cases=50')
