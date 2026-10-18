#!/usr/bin/env python3
"""Exact finite checks of the parking-function occupancy and peak/valley law.

Run with Python 3.9+.  Exhaustive tests are finite checks, not proofs for all n.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial


def valid(m):
    total=0
    for k,v in enumerate(m,1):
        total+=v
        if total<k:
            return False
    return True


def profile_weight(m):
    ans=factorial(sum(m))
    den=1
    for c in m:
        den*=factorial(c)
    return ans//den


def profiles(n):
    # Generate all n+1-compositions (not tuples); exactly n cars and n values.
    def rec(left,k,p):
        if k==1:
            m=(*p,left)
            if valid(m):
                yield m
        else:
            for t in range(left+1):
                yield from rec(left-t,k-1,(*p,t))
    yield from rec(n,n,())


def dp(n):
    # W: count, B: weighted sum of sum m_j^2,
    # Q: weighted sum of sum_{a<b}m_a*m_b*(m_a-m_b).
    states={0:(1,0,0)}
    for j in range(1,n+1):
        nxt={}
        for s,(w,b,q) in states.items():
            for t in range(max(0,j-s),n-s+1):
                mult=comb(n-s,t)
                cur=nxt.get(s+t,(0,0,0))
                nxt[s+t]=(cur[0]+mult*w,
                          cur[1]+mult*(b+t*t*w),
                          cur[2]+mult*(q+t*b-t*t*s*w))
        states=nxt
    return states[n]


def checks():
    assertions=0
    for n in range(2,8):
        P=list(profiles(n))
        cnt={m:profile_weight(m) for m in P}
        W=sum(cnt.values())
        assert W==(n+1)**(n-1)
        assertions+=1
        Wd,Bd,Qd=dp(n)
        B=sum(w*sum(t*t for t in m) for m,w in cnt.items())
        Q=sum(w*sum(m[a]*m[b]*(m[a]-m[b]) for a in range(n) for b in range(a+1,n)) for m,w in cnt.items())
        assert (Wd,Bd,Qd)==(W,B,Q)
        assertions+=1
        for a in range(n):
            for b in range(a+1,n):
                groups=defaultdict(dict)
                for m,w in cnt.items():
                    key=tuple(m[j] for j in range(n) if j not in (a,b))+(m[a]+m[b],)
                    groups[key][m[a]]=w
                for key,weights in groups.items():
                    T=key[-1]
                    ext=[0]*n
                    l=0
                    for j in range(n):
                        if j not in (a,b):
                            ext[j]=key[l];l+=1
                    lower=max((0,*(k+1-sum(ext[:k+1]) for k in range(a,b))))
                    expect={r:comb(T,r) for r in range(lower,T+1)}
                    assert set(weights)==set(expect),(n,a,b,key,weights,expect)
                    assertions+=1
                    assert all(weights[r]*expect[lower]==expect[r]*weights[lower] for r in expect)
                    assertions+=len(expect)
                    for r in range(T+1):
                        s=T-r
                        if r>s:
                            assert weights.get(r,0)>=weights.get(s,0)
                            assertions+=1
    # Direct exhaustive preference-word ordering patterns through n=6.
    for n in range(3,7):
        peak=valley=0
        for v in product(range(1,n+1),repeat=n):
            m=[0]*n
            for j in v:
                m[j-1]+=1
            if not valid(m):
                continue
            peak+=(v[0]<v[1]>v[2])
            valley+=(v[0]>v[1]<v[2])
        W,B,Q=dp(n)
        assert peak-valley==Q//(n*(n-1)*(n-2))
        assert (peak-valley)*n*(n-1)*(n-2)==Q
        assertions+=2
        p0=Fraction(n*(2*n+1),6*(n+1)**2)
        assert Fraction(peak+valley,2*W)==p0
        assert peak>valley
        assertions+=2
    for n in range(3,41):
        W,B,Q=dp(n)
        assert W==(n+1)**(n-1)
        assert Q>0
        assert Q>=n*(n-1)*(n-2)
        assertions+=3
    print('PASS',assertions,'exact assertions; exhaustive word checks n=3..6; full occupancy-profile checks n=2..7; DP n=2..40')

if __name__=='__main__':
    checks()
