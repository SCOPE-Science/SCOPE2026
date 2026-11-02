#!/usr/bin/env python3
"""Standalone finite checks of the Stern second-neighbor gcd formulas.
All infinite statements require the separate mathematical proof.
"""
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt

def stern(size):
    s=[0]*(size+3)
    s[1]=1
    for n in range(2,size+3):
        s[n] = s[n//2] if n%2==0 else s[n//2]+s[n//2+1]
    return s

def predicted_gcd(n,s):
    k=0
    m=n
    while m & 1:
        k+=1
        m>>=1
    u=m//2
    return gcd(2*k+1, s[u]-s[u+1])

def prime_powers(n):
    p=2
    while p*p<=n:
        if n%p==0:
            pk=1
            while n%p==0:
                pk*=p;n//=p
            yield pk, p
        p+=1
    if n>1:yield n,n

def delta(d):
    if not d&1:return Fraction(0)
    ans=Fraction(2**((d-1)//2),2**d-1)
    for pk,p in prime_powers(d):
        ans/=pk//p*(p+1)
    return ans

def check(N=2**18):
    s=stern(N+2)
    hist=Counter()
    for n in range(N):
        g=gcd(s[n],s[n+2])
        assert (g&1) and (g==predicted_gcd(n,s)),(n,g,predicted_gcd(n,s))
        hist[g]+=1
    for d in range(1,201):
        q=Fraction(sum(count for x,count in hist.items() if x%d==0),N)
        if d%2==0:assert q==0
        elif d<=15:print('DIV',d,'obs',float(q),'pred',float(delta(d)),'diff',float(q-delta(d)))
    for d in range(1,100):
        num=sum(1 for a in range(d) for b in range(d) if (a-b)%d==0 and gcd(gcd(a,b),d)==1)
        den=sum(1 for a in range(d) for b in range(d) if gcd(gcd(a,b),d)==1)
        expect=Fraction(1)
        for pk,p in prime_powers(d):expect/=pk//p*(p+1)
        assert Fraction(num,den)==expect,(d,Fraction(num,den),expect)
    print('N',N,'SUPPORT',sorted(hist.items())[:30])
    print('UNIQUE',len(hist),'MAX_G',max(hist),'ODD_G_RATIO',hist[1]/N)
    print('VERIFY_OK')

if __name__=='__main__':check()
