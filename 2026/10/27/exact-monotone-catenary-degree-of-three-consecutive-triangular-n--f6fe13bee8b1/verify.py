#!/usr/bin/env python3
"""Finite cross-checks of a uniform theorem on triangular-number semigroups.

The theorem for every parameter is proved mathematically; this script checks
its relation signs, primitive equal-length pairs and monotone chains on a
specified finite test domain.
"""
from collections import defaultdict
from math import gcd


def dist(x, y):
    return max(sum(max(a-b, 0) for a,b in zip(x,y)),
               sum(max(b-a, 0) for a,b in zip(x,y)))


def factorizations(m, gens):
    a,b,c = gens
    for z in range(m//c+1):
        for y in range((m-z*c)//b+1):
            rest = m-z*c-y*b
            if rest % a == 0:
                yield (rest//a,y,z)


def addition(x,v):
    return tuple(a+b for a,b in zip(x,v))


def scale(k,v):
    return tuple(k*x for x in v)


def negate(v):
    return scale(-1,v)


def relation_data(n):
    t=n//2
    if n%2==0:
        r=(t+1,-t,0)       # length change +1
        s=(0,2*t+3,-(2*t+1)) # length change +2
        zero=addition(s,scale(-2,r))
        moves=[r,s,addition(s,negate(r)),zero]
    else:
        r=(2*t+3,-(2*t+1),0) # length change +2
        s=(0,t+2,-(t+1))     # length change +1
        zero=addition(r,scale(-2,s))
        moves=[r,s,addition(r,negate(s)),zero]
    return r,s,zero,moves


def chain(x,y,n):
    """Produce a monotone connecting chain, using the case proof."""
    t=n//2
    r,s,w,_=relation_data(n)
    d=tuple(b-a for a,b in zip(x,y))
    if n%2==0:
        assert d[0]%(t+1)==0 and d[2]%(2*t+1)==0
        p=d[0]//(t+1)
        q=-d[2]//(2*t+1)
        assert p+2*q>=0
        if p>=0 and q>=0:
            jobs=[(q,s),(p,r)]
        elif p>=0:
            k=-q
            assert p>=2*k
            jobs=[(p-2*k,r),(k,negate(w))]
        else:
            a=-p
            assert q>0 and a<=2*q
            if a<=q:
                jobs=[(a,addition(s,negate(r))),(q-a,s)]
            else:
                jobs=[(2*q-a,addition(s,negate(r))),(a-q,w)]
    else:
        assert d[0]%(2*t+3)==0 and d[2]%(t+1)==0
        p=d[0]//(2*t+3)
        q=-d[2]//(t+1)
        assert 2*p+q>=0
        if p>=0 and q>=0:
            jobs=[(q,s),(p,r)]
        elif p>=0:
            k=-q
            assert k<=2*p
            if k<=p:
                jobs=[(p-k,r),(k,addition(r,negate(s)))]
            else:
                jobs=[(2*p-k,addition(r,negate(s))),(k-p,w)]
        else:
            k=-p
            assert q>=2*k
            jobs=[(q-2*k,s),(k,negate(w))]
    prev=x; prevlength=sum(x); maxedge=0
    for cnt,step in jobs:
        assert cnt>=0
        for _ in range(cnt):
            nxt=addition(prev,step)
            assert min(nxt)>=0, (n,x,y,prev,step)
            assert sum(nxt)>=prevlength
            maxedge=max(maxedge,dist(prev,nxt))
            prev=nxt
            prevlength=sum(nxt)
    assert prev==y, (n,x,y,prev)
    assert maxedge<=2*n+3
    return maxedge


def main():
    tested_fibers=0; pairs=0
    for n in range(3,16):
        gs=tuple(j*(j+1)//2 for j in (n,n+1,n+2))
        r,s,w,moves=relation_data(n)
        L=2*n+3
        assert sum(w)==0
        assert sum(w[i]*gs[i] for i in range(3))==0
        assert gcd(abs(w[0]),gcd(abs(w[1]),abs(w[2])))==1
        assert dist(tuple(max(x,0) for x in w),tuple(max(-x,0) for x in w))==L
        assert all(dist((0,0,0),tuple(max(x,0) for x in v))<=L for v in moves)
        plus=tuple(max(z,0) for z in w)
        minus=tuple(max(-z,0) for z in w)
        assert len(list(factorizations(sum(u*v for u,v in zip(gs,plus)),gs)))>=2
        assert len([f for f in factorizations(sum(u*v for u,v in zip(gs,plus)),gs) if sum(f)==L])==2
        cutoff=min(700,max(140,4*gs[-1]))
        for m in range(1,cutoff+1):
            F=list(factorizations(m,gs))
            if len(F)<2:continue
            tested_fibers+=1
            for i,x in enumerate(F):
                for y in F[i+1:]:
                    if sum(x)<=sum(y):chain(x,y,n)
                    else:chain(y,x,n)
                    pairs+=1
        print('n',n,'gens',gs,'equal-trade-distance',L,'cutoff',cutoff)
    print('PASS: fibers',tested_fibers,'pairs',pairs)

if __name__=='__main__':main()
