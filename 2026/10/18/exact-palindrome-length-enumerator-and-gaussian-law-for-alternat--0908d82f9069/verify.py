#!/usr/bin/env python3
"""Independent exact checks of the alternating-word palindrome-length theorem."""
from math import comb


def from_half_words(n):
    a = [0]*(n+1)
    if n >= 1:
        a[1] += 1
    if n >= 2:
        a[1] += 1
    for r in range(1,n//2+1):
        for initial in (0,1):
            for equal in range(r):
                ways=comb(r-1,equal)
                even=2*r+initial+2*equal+1
                if even<=n:
                    a[2*r]+=ways
                odd=2*r+1+initial+2*equal
                if 2*r+1<=n:
                    if odd<=n:
                        a[2*r+1]+=ways
                    if odd+2<=n:
                        a[2*r+1]+=ways
    return a


def direct(n):
    w=[i&1 for i in range(n)]
    found=set()
    for mask in range(1,1<<n):
        u=tuple(w[i] for i in range(n) if mask>>i&1)
        if u==u[::-1]:
            found.add(u)
    a=[0]*(n+1)
    for u in found:
        a[len(u)]+=1
    return a


def add(a,b,shift=0,sgn=1):
    out=a[:]
    for j,x in enumerate(b):
        if j+shift<len(out):out[j+shift]+=sgn*x
    return out


def recurrence(max_n):
    # (1-z-t^2 z^2+t^2 z^3-t^2 z^4+t^2 z^5)F
    #        =tz+tz^2+t^2z^3+t^2z^4.
    pol=[]
    for n in range(max_n+1):
        a=[0]*(n+1)
        for offset,degree,sign in ((1,0,1),(2,2,1),(3,2,-1),(4,2,1),(5,2,-1)):
            if n>=offset:
                a=add(a,pol[n-offset],degree,sign)
        if n in (1,2):a[1]+=1
        if n in (3,4):a[2]+=1
        pol.append(a)
    return pol


def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a


if __name__=='__main__':
    for n in range(1,18):
        assert direct(n)==from_half_words(n),n
    print('DIRECT_OK n=1..17')
    pol=recurrence(75)
    for n in range(76):
        assert pol[n]==from_half_words(n),n
    print('RATIONAL_RECURRENCE_OK n=0..75')
    for n in range(1,76):
        k=n//2
        total=(2*fib(k+3)-4) if n%2==0 else (fib(k+5)-4)
        assert sum(pol[n])==total,(n,sum(pol[n]),total)
    print('FIBONACCI_SPECIALIZATION_OK n=1..75')
    print('VERIFY_OK')
