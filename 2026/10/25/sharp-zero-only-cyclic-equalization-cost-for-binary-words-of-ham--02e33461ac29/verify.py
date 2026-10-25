#!/usr/bin/env python3
"""Exact verification of optimal zero-only simultaneous padding for weight-two binary words."""
from itertools import combinations
from collections import Counter


def cost_formula(n,a,b,c,d):
    I=set(range(a+1,b+1));J=set(range(c+1,d+1))
    r=b-a;s=d-c
    if I < J or J < I:
        return abs(n-r-s)
    if not I & J:
        return abs(r-s)
    return min(abs(r-s), abs(n-r-s))


def rotated_equal(n,a,b,c,d,z):
    # Literal word construction, independent of the two-gap argument.
    u=''.join('1' if i in (a,b) else '0' for i in range(n))
    v=''.join('1' if i in (c,d) else '0' for i in range(n))
    U=''.join('0'*z[i]+u[i] for i in range(n))+'0'*z[n]
    V=''.join('0'*z[i]+v[i] for i in range(n))+'0'*z[n]
    return V in (U+U)[:2*len(U)-1]


def compositions(k,number):
    if number==1:
        yield (k,)
    else:
        for i in range(k+1):
            for rest in compositions(k-i, number-1):
                yield (i,)+rest


def cost_search(n,a,b,c,d,bound):
    for k in range(bound+1):
        for z in compositions(k,n+1):
            if rotated_equal(n,a,b,c,d,z):
                return k
    raise AssertionError('No padding found')


def audit(n, brute=False):
    intervals=list(combinations(range(n),2))
    hist=Counter()
    extremes=[]
    for a,b in intervals:
      for c,d in intervals:
        k=cost_formula(n,a,b,c,d)
        if brute:
            actual=cost_search(n,a,b,c,d,k)
            assert actual==k,(n,a,b,c,d,k,actual)
        hist[k]+=1
        if k==n-3: extremes.append(((a,b),(c,d)))
    if n>=4:
        assert max(hist)==n-3
        assert hist[n-3]==4*n,(n,hist[n-3])
    return dict(sorted(hist.items()))

if __name__=='__main__':
    for n in range(3,13):
        h=audit(n,brute=(n<=8))
        print(n,h,'pairs',sum(h.values()))
    # family with n-3 optimal cost
    for n in range(4,101):
        assert cost_formula(n,0,1,0,2)==n-3
    print('VERIFY_OK')
