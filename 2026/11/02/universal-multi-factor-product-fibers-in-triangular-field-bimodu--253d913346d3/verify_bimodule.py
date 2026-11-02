#!/usr/bin/env python3
"""Exact target fibers for full and Frobenius-twisted triangular bimodule rings."""
from collections import Counter
from fractions import Fraction
from itertools import product

def f4mul(a,b):
    p=0
    for i in range(2):
        if b&(1<<i):p ^= a<<i
    if p&8:p ^= 0b1110  # x^3 = x^2+x
    if p&4:p ^= 0b111  # x^2 = x+1
    return p

def test_f4():
    for a,b,c in product(range(4),repeat=3):
        assert f4mul(f4mul(a,b),c)==f4mul(a,f4mul(b,c))
    for a in range(4):
        assert f4mul(a,1)==a==f4mul(1,a)

def run(Q,T,twist,k):
    # Q,T=4; M=F4^2 with normal or Frobenius-twisted right action.
    assert Q==T==4
    R=list(product(range(4),repeat=4))
    def m(x,y):
        a,u,v,c=x;d,w,z,f=y
        return(f4mul(a,d),f4mul(a,w)^f4mul(u,f),
               f4mul(a,z)^f4mul(v, f4mul(f,f) if twist else f),f4mul(c,f))
    cur=Counter(R)
    for _ in range(2,k+1):
        nxt=Counter()
        for x,num in cur.items():
            for y in R:nxt[m(x,y)]+=num
        cur=nxt
    t=Fraction(3,4);s=t**k;u=1-s;r=s/3
    E=Fraction(1,16)*sum(t**(i-1+k-j) for i in range(1,k+1) for j in range(i+1,k+1))
    for a,v,w,c in R:
        da=u if a==0 else r
        dc=u if c==0 else r
        e=E if a==c==0 else 0
        p=(da*dc-e)/16+(e if v==w==0 else 0)
        assert Fraction(cur.get((a,v,w,c),0),256**k)==p,(Q,T,twist,k,(a,v,w,c))
    print('RING_CHECK',Q,T,'frobenius',twist,'k',k,'zero',cur[(0,0,0,0)])

def test_asymmetric(k):
    # K=F2, L=F4, M=F4; the finite unital (K,L)-bimodule.
    R=list(product(range(2),range(4),range(4)))
    def m(x,y):
        a,u,c=x;d,v,f=y
        return (a*d,(v if a else 0)^f4mul(u,f),f4mul(c,f))
    cur=Counter(R)
    for _ in range(2,k+1):
        nxt=Counter()
        for x,num in cur.items():
            for y in R:nxt[m(x,y)]+=num
        cur=nxt
    tQ=Fraction(1,2);tT=Fraction(3,4)
    sQ=tQ**k;sT=tT**k;uQ=1-sQ;uT=1-sT
    E=Fraction(1,8)*sum(tQ**(i-1)*tT**(k-j) for i in range(1,k+1) for j in range(i+1,k+1))
    for a,v,c in R:
        dQ=uQ if a==0 else sQ
        dT=uT if c==0 else sT/3
        e=E if a==c==0 else 0
        p=(dQ*dT-e)/4+(e if v==0 else 0)
        assert Fraction(cur.get((a,v,c),0),32**k)==p,('ASYMMETRIC',k,(a,v,c))
    print('ASYM_CHECK',k,'zero',cur[(0,0,0)])

if __name__=='__main__':
    test_f4()
    for k in range(1,5):test_asymmetric(k)
    for k in range(1,4):
        run(4,4,False,k)
        run(4,4,True,k)
    print('VERIFY_OK')
