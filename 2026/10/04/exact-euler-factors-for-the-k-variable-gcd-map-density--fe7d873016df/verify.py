#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import gcd


def vp(n,p):
    if n == 0:
        return 10**9
    e=0
    while n%p==0:
        n//=p; e+=1
    return e

def gcd_many(xs):
    g=0
    for x in xs: g=gcd(g,x)
    return g

def fk(xs):
    P=1
    for x in xs: P*=x
    return gcd(P,sum(xs))//gcd_many(xs)

def A_formula(k,p):
    return ((p-1)**k+(p-1)*((-1)**k))//p

def c_factor(k,p):
    return Fraction(1,1)-Fraction(1,p)+Fraction((p-1)**k+(p-1)*((-1)**k),p**(k+1))+Fraction(p-1,p*(p**k-1))

def primes_upto(n):
    s=bytearray(b'\x01')*(n+1)
    s[:2]=b'\x00\x00'
    for q in range(2,int(n**0.5)+1):
        if s[q]: s[q*q:n+1:q]=b'\x00'*(((n-q*q)//q)+1)
    return [i for i in range(2,n+1) if s[i]]

valuation_cases=0
for k in (2,3,4):
    for p in (2,3,5):
        for xs in product(range(1,9), repeat=k):
            es=[vp(x,p) for x in xs]
            t=min(es); bs=[x//(p**t) for x in xs]
            r=sum(vp(b,p) for b in bs); s=vp(sum(bs),p)
            lhs=vp(fk(xs),p)
            rhs=min((k-1)*t+r,s)
            assert lhs==rhs,(k,p,xs,lhs,rhs)
            valuation_cases+=1

finite_field_cases=0
for k in range(2,7):
    for p in (2,3,5,7):
        cnt=sum(1 for us in product(range(1,p), repeat=k) if sum(us)%p==0)
        assert cnt==A_formula(k,p),(k,p,cnt,A_formula(k,p))
        finite_field_cases+=1

layer_cases=0
for k in range(2,6):
    for p in (2,3,5,7):
        good0=sum(1 for us in product(range(p),repeat=k)
                  if (sum(us)%p!=0) or (all(u!=0 for u in us) and sum(us)%p==0))
        expected=p**k-p**(k-1)+A_formula(k,p)
        assert good0==expected,(k,p,good0,expected)
        if k==2:
            assert c_factor(k,p)==Fraction(1,1)-Fraction(1,p*p*(p+1))
        layer_cases+=1

ps=primes_upto(200000)
prod3=1.0
for p in ps:
    prod3*=float(c_factor(3,p))
assert 0.3429 < prod3 < 0.3431
print(f'VERIFY_OK valuation_cases={valuation_cases} finite_field_cases={finite_field_cases} layer_cases={layer_cases} primes={len(ps)} D3_partial={prod3:.12f}')
