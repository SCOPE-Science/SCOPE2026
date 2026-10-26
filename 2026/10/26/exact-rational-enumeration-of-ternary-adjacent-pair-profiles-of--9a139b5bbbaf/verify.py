#!/usr/bin/env python3
"""Recompute a ternary ordered-bigram spectrum from two independent finite descriptions.

Standard library only. This tests bounded cases; the infinite identity is proved
by the directed Euler-trail decomposition in RESULT.md.
"""
from itertools import product


def mul(a,b,M):
    c=[0]*(M+1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:M-i+1]):
                c[i+j]+=x*y
    return c


def geom(k,M):
    a=[0]*(M+1)
    for i in range(0,M+1,k): a[i]=1
    return a


def shift(a,k,M):
    return [0]*k+a[:M+1-k] if k<=M else [0]*(M+1)


def add(a,b): return [x+y for x,y in zip(a,b)]


def sub(a,b): return [x-y for x,y in zip(a,b)]


def scale(a,k): return [k*x for x in a]


def series(M=15):
    unit=[1]+[0]*M
    g1=geom(1,M)
    g2=geom(2,M)
    g3=geom(3,M)
    loops2=mul(g1,g1,M)
    loops3=mul(loops2,g1,M)
    base=mul(g3,mul(g2,mul(g2,g2,M),M),M)
    c0=add(base,shift(base,3,M))
    c1=add(shift(base,1,M),shift(base,2,M))
    d0=sub(c0,add(unit,scale(shift(g2,2,M),3)))
    d1=sub(c1,shift(g2,1,M))
    connected=add(d0,scale(d1,6))
    pair=add(scale(shift(g2,1,M),2),shift(g2,2,M))
    result=add(unit,scale(shift(g1,1,M),3))
    result=add(result,scale(mul(loops2,pair,M),3))
    return add(result,mul(loops3,connected,M))


def direct(n):
    observed=set()
    for w in product(range(3),repeat=n):
        p=[0]*9
        for x,y in zip(w,w[1:]): p[3*x+y]+=1
        observed.add(tuple(p))
    return len(observed)


def graph(n):
    # Distinct enumeration independent of words: traverse nonnegative 3x3 matrices
    # of total n-1, accept exactly connected Euler trails.
    m=n-1
    if not m: return 1
    count=0
    def rec(partial,remaining,parts):
        nonlocal count
        if parts==1:
            p=partial+[remaining]
            im=[sum(p[3*i+j] for j in range(3))-sum(p[3*j+i] for j in range(3)) for i in range(3)]
            if sorted(im) not in ([0,0,0],[-1,0,1]): return
            active={i for i in range(3) if any(p[3*i+j] or p[3*j+i] for j in range(3))}
            if not active:return
            reached={min(active)}
            while True:
                new=reached|{j for i in reached for j in active if p[3*i+j] or p[3*j+i]}
                if new==reached:break
                reached=new
            if reached==active:count+=1
            return
        for v in range(remaining+1):rec(partial+[v],remaining-v,parts-1)
    rec([],m,9)
    return count


if __name__=='__main__':
    expected=[1,9,24,65,156,342,683,1272,2226,3708]
    s=series(16)
    assert s[:10]==expected,(s[:10],expected)
    for n in range(1,11):
        a=direct(n)
        b=s[n-1]
        assert a==b,(n,a,b)
    for n in range(1,9):
        c=graph(n)
        assert c==s[n-1],(n,c,s[n-1])
    print('PASS: exact series values at lengths 1-10, word enumeration 1-10,')
    print('and independent balanced connected-matrix enumeration 1-8.')
    print('Values for lengths 1-10:',s[:10])
