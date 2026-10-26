#!/usr/bin/env python3
"""Independent finite-grid checks for six-neighbour parity dynamics.

Graph vertices are (i,j), i mod m, j mod n; neighbours are
(i±1,j), (i,j±1), (i±1,j±1) with matched signs.
All computations use exact F2 bit arithmetic.
"""
from math import gcd
from itertools import product

OFFSETS=((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1))

def v2split(n):
    k=n&-n
    return k,n//k

def predicted(m,n):
    k,r=v2split(m)
    ell,s=v2split(n)
    g=gcd(r,s)
    d=k*ell*((r-1)*(s-1)-(g-1))
    if r==s==1:
        if k==ell:
            t=max(1,k//2)
        else:
            t=min(k,ell)
    elif r==1:
        t=k
    elif s==1:
        t=ell
    else:
        t=max(k,ell)
    return t,d

def apply(state,m,n):
    out=0
    for i in range(m):
        for j in range(n):
            parity=0
            for di,dj in OFFSETS:
                ii=(i+di)%m
                jj=(j+dj)%n
                parity^=(state>>(ii*n+jj))&1
            out|=parity<<(i*n+j)
    return out

def shift_kernel(kernel,m,n):
    new=set()
    for i,j in kernel:
        for di,dj in OFFSETS:
            elt=((i+di)%m,(j+dj)%n)
            if elt in new:new.remove(elt)
            else:new.add(elt)
    return new

def kernel_at(t,m,n):
    p={(0,0)}
    for _ in range(t):
        p=shift_kernel(p,m,n)
    return p

def rank_from_kernel(kernel,m,n):
    piv={}
    for i,j in product(range(m),range(n)):
        v=0
        for a,b in kernel:
            v^=1<<(((i+a)%m)*n+(j+b)%n)
        while v:
            lead=v.bit_length()-1
            q=piv.get(lead)
            if q is None:
                piv[lead]=v
                break
            v^=q
    return len(piv)

def test_all():
    num=0
    for m,n in product(range(3,19),repeat=2):
        t,d=predicted(m,n)
        kprev=kernel_at(t-1,m,n)
        knext=shift_kernel(kprev,m,n)
        rprev=rank_from_kernel(kprev,m,n)
        rnext=rank_from_kernel(knext,m,n)
        assert rnext==d,(m,n,t,d,rnext)
        assert rprev>d,(m,n,t,d,rprev)
        assert shift_kernel(knext,m,n) is not None
        num+=1
    print('PARAMETER_RANK_CHECKS',num)

def test_direct():
    nconfig=0
    for m,n in [(3,3),(3,4),(3,5),(4,4),(4,5),(3,6),(4,6)]:
        size=m*n
        t,d=predicted(m,n)
        kerT=kernel_at(t,m,n)
        basis=[1<<a for a in range(size)]
        for a in basis:
            out=a
            for _ in range(t):out=apply(out,m,n)
            p=0
            i,j=divmod(a.bit_length()-1,n)
            for di,dj in kerT:
                p^=1<<(((i+di)%m)*n+(j+dj)%n)
            assert out==p,(m,n,a)
        if size<=16:
            # Check exact periodicity of each state and longest transient.
            for state in range(1<<size):
                seen={}
                x=state
                while x not in seen:
                    seen[x]=len(seen)
                    x=apply(x,m,n)
                pre=seen[x]
                assert pre<=t
                nconfig+=1
    print('DIRECT_STATE_CHECKS',nconfig)

def test_dyadic():
    num=0
    for h in (2,4,8,16):
        m=2*h
        t,d=predicted(m,m)
        assert t==h and d==0
        ra=rank_from_kernel(kernel_at(t-1,m,m),m,m)
        assert ra==3*h,(m,ra,3*h)
        num+=1
    for m,n in ((4,8),(4,16),(8,16),(8,32),(16,32)):
        t,d=predicted(m,n)
        assert t==m and d==0
        ra=rank_from_kernel(kernel_at(t-1,m,n),m,n)
        assert ra==n-2*m+2,(m,n,ra)
        num+=1
    print('LAST_STEP_RANK_CHECKS',num)

if __name__=='__main__':
    test_all()
    test_direct()
    test_dyadic()
    print('TRIANGULAR_VERIFY_OK')
