#!/usr/bin/env python3
"""Independent integer enumeration for the conditional contact--midpoint-height theorem.
Run: python3 verify.py
No external dependencies or files.
"""
from collections import defaultdict
from math import comb

checks=0

def check(condition, detail):
    global checks
    checks+=1
    if not condition:
        raise AssertionError(detail)

def half_counts(n,h):
    if h==0:
        assert n%2==0
        m=n//2
        return [((r+1)*comb(n-r-2,m-r-1))//m for r in range(m)]
    m=(n-h)//2; ell=(n+h)//2
    return [((h+r)*comb(n-r-1,m-r))//ell for r in range(m+1)]

def half_dynamic(n):
    # DP of all nonnegative walk prefixes; contacts count at positive times
    d={(0,0):1}
    for t in range(1,n+1):
        e=defaultdict(int)
        for (h,r),v in d.items():
            e[h+1,r]+=v
            if h>0: e[h-1,r+(h==1)]+=v
        d=e
    return d

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def full_counts(n,h):
    a=half_counts(n,h)
    v=conv(a,a)
    return ([0]+v) if h==0 else v

def enumerate_dyck(n):
    # Independently enumerate all full paths, without formula/half decomposition
    totals=defaultdict(int)
    def rec(t,height,mid,returns):
        if t==2*n:
            check(height==0,('completion',n))
            totals[mid,returns]+=1
            return
        if t==n: mid=height
        if height+1<=2*n-t: rec(t+1,height+1,mid,returns)
        if height>0:
            r=returns+(height==1 and t+1<2*n)
            rec(t+1,height-1,mid,r)
    rec(0,0,-1,0)
    return totals

for n in range(1,151):
    dp=half_dynamic(n)
    for h in range(n%2,n+1,2):
        a=half_counts(n,h)
        m=(n-h)//2
        ballot=(h+1)*comb(n+1,m)//(n+1)
        check(sum(a)==ballot,('ballot',n,h))
        if h:
            for r,v in enumerate(a): check(v==dp.get((h,r),0),('half',n,h,r))
        else:
            for r,v in enumerate(a): check(v==dp.get((0,r+1),0),('halfzero',n,r))
        for r in range(1,len(a)-1):
            check(a[r]*a[r]>=a[r-1]*a[r+1],('LC',n,h,r))
        if h+2<=n:
            b=half_counts(n,h+2)
            for r in range(len(b)-1):
                check(b[r]*a[r+1]>b[r+1]*a[r],('half LR strict',n,h,r))
    if n<=80:
        rows={h:full_counts(n,h) for h in range(n%2,n+1,2)}
        for h in range(n%2,n-1,2):
            low=rows[h]; high=rows[h+2]
            for i in range(max(len(low),len(high))):
                for j in range(i+1,max(len(low),len(high))):
                    li=low[i] if i<len(low) else 0
                    lj=low[j] if j<len(low) else 0
                    hi=high[i] if i<len(high) else 0
                    hj=high[j] if j<len(high) else 0
                    check(li*hj<=lj*hi,('full LR',n,h,i,j))
    if n<=11:
        direct=enumerate_dyck(n)
        check(sum(direct.values())==comb(2*n,n)//(n+1),('Catalan',n))
        for h in range(n%2,n+1,2):
            counts=full_counts(n,h)
            for r,v in enumerate(counts):
                check(v==direct.get((h,r),0),('full',n,h,r,v,direct.get((h,r),0)))
        for key,v in direct.items():
            h,r=key
            check(r<len(full_counts(n,h)),('bad support',n,key))
print('PASS',checks,'exact integer assertions; n<=150 half-profile; n<=80 full LR minors; n<=11 complete Dyck enumeration')
