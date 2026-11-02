#!/usr/bin/env python3
"""Exact-rational exhaustive enumeration for a three-visit aggregated Markov-availability detection theorem."""
from fractions import Fraction as F
from itertools import product
import random

def probs(pi,d,r,n=3):
    u=pi*(1-r); v=(1-pi)*(1-r)
    assert 0<u<1 and 0<v<1 and 0<pi<1 and 0<d<=1
    P=((1-u,u),(v,1-v))
    vct=[1-pi,pi]
    out=[F(0) for _ in range(n+1)]
    for st in product([0,1],repeat=n):
        a=vct[st[0]]
        for i in range(n-1): a*=P[st[i]][st[i+1]]
        for obs in product([0,1],repeat=n):
            b=a
            for i in range(n):
                e= d if st[i] else F(0)
                b*= e if obs[i] else (1-e)
            out[sum(obs)]+=b
    assert sum(out)==1
    return out

def retrieve(g):
    assert len(g)==4
    m=sum(F(i)*g[i] for i in range(4))/3
    S=g[2]+3*g[3]
    t=g[3]
    # Positive square roots are taken exactly where rational in ground-truth examples.
    from math import isqrt
    def sqrtq(x):
        a=isqrt(x.numerator); b=isqrt(x.denominator)
        assert a*a==x.numerator and b*b==x.denominator
        return F(a,b)
    z=sqrtq(t/m)-m
    if z==0: return (m,'unidentifiable')
    r=(S-3*m*m)/(m*z)-2
    d=m+z/r
    pi=m/d
    u=pi*(1-r); v=(1-pi)*(1-r)
    assert 0<u<1 and 0<v<1
    return pi,d,r

def main():
    rng=random.Random(71405)
    checked=0
    for i in range(800):
        pi=F(rng.randint(1,19),20)
        d=F(rng.randint(1,19),20)
        # r in (-1/2, .9), restrict actual transition probabilities
        r=F(rng.randint(-9,18),20)
        if r==0: continue
        u=pi*(1-r); v=(1-pi)*(1-r)
        if not 0<u<1 or not 0<v<1: continue
        g=probs(pi,d,r)
        got=retrieve(g)
        assert got==(pi,d,r),(pi,d,r,got,g)
        checked+=1
    assert checked>500,checked
    for pi,d in [(F(1,2),F(1,4)),(F(1,4),F(1,2)),(F(1,3),F(3,4))]:
        g=probs(pi,d,F(0))
        from math import comb
        m=pi*d
        assert g==[F(comb(3,k))*m**k*(1-m)**(3-k) for k in range(4)]
        assert retrieve(g)==(m,'unidentifiable')
    pi=F(2,5);d=F(3,4);r=F(1,2)
    g=probs(pi,d,r)
    print('PASSED',checked,'positive and negative memory triples; exact r=0 nonidentifiability cases')
    print('example pi=2/5 d=3/4 r=1/2: g=',list(map(str,g)))
    m=sum(F(i)*g[i] for i in range(4))/3
    S=g[2]+3*g[3]; t=g[3]
    print('m=',m,'S=',S,'t=',t,'retrieved=',retrieve(g))
if __name__=='__main__': main()
