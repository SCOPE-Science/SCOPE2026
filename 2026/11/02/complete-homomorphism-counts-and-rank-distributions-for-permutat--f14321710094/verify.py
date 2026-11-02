#!/usr/bin/env python3
"""Separate finite-field matrix check of cycle-evolution endomorphism rank counts.
Run: python3 verify.py. Python standard library only. Enumerates all linear matrices
in indicated small cases and tests multiplication; independently compares with
assignment-based exact counting, including the field F4 extension.
"""
from itertools import product
from collections import Counter
from math import gcd

def mul(a,b,q):
    if q==4:
        # Polynomial basis F2[alpha]/(alpha^2+alpha+1), bit encoding.
        x=(a&1)*(b&1)
        y=((a&1)*((b>>1)&1))^(((a>>1)&1)*(b&1))
        z=((a>>1)&1)*((b>>1)&1)
        return (x^z) | ((y^z)<<1)
    return a*b%q

def add(a,b,q):
    return (a^b) if q==4 else (a+b)%q

def cycles_to_perm(cycles):
    p=[]; offset=0
    for n in cycles:
        p.extend(offset+(i+1)%n for i in range(n))
        offset+=n
    return p

def rank(mat,q):
    a=[list(row) for row in mat]
    n=len(a); m=len(a[0]) if n else 0
    r=0
    for c in range(m):
        pivot=next((i for i in range(r,n) if a[i][c]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=next(i for i in range(1,q) if mul(a[r][c],i,q)==1)
        a[r]=[mul(t,inv,q) for t in a[r]]
        for i in range(n):
            if i==r or a[i][c]==0: continue
            coef=a[i][c]
            a[i]=[add(a[i][j],add(0,mul(coef,a[r][j],q),q) if q==4 else -mul(coef,a[r][j],q),q) for j in range(m)]
        r+=1
        if r==n: break
    return r

def predicted_between(source,target,q):
    # DP with bit mask of distinct SOURCE cycles used by target components.
    dp=Counter({0:1})
    for n in target:
        d=gcd(q-1,2**n-1)
        choices=[(None,1)]+[(i,m*d) for i,m in enumerate(source) if n%m==0]
        nxt=Counter()
        for mask,c in dp.items():
            for src,weight in choices:
                nxt[mask if src is None else mask|(1<<src)]+=c*weight
        dp=nxt
    ans=Counter()
    for mask,c in dp.items():
        ans[sum(m for i,m in enumerate(source) if mask>>i&1)]+=c
    return ans

def exhaustive_between(source,target,q):
    ns=sum(source); nt=sum(target)
    ps=cycles_to_perm(source); pt=cycles_to_perm(target)
    out=Counter()
    for entries in product(range(q),repeat=ns*nt):
        cols=[entries[i*nt:(i+1)*nt] for i in range(ns)]
        ok=True
        for i in range(ns):
            ci=cols[i]; nxt=cols[ps[i]]
            for k in range(nt):
                if mul(ci[k],ci[k],q)!=nxt[pt[k]]:
                    ok=False;break
            if not ok:break
            for j in range(i):
                if any(mul(ci[k],cols[j][k],q)!=0 for k in range(nt)):
                    ok=False;break
            if not ok:break
        if ok:
            rows=[[cols[j][i] for j in range(ns)] for i in range(nt)]
            out[rank(rows,q)]+=1
    return out

def main():
    cases=[
      (2,[1],[1]),(2,[2],[2]),(2,[1,1],[1,1]),
      (2,[1,2],[1,2]),(2,[1,3],[1,3]),
      (2,[2,2],[2,2]),(2,[1,1,2],[1,1,2]),
      (3,[1,2],[1,2]),(3,[2],[2]),
      (4,[2],[2]),(4,[1,2],[1,2]),
      (5,[2],[2]),(7,[2],[2]),
      (2,[1],[2]),(2,[2],[1]),(4,[1],[2]),
      (2,[1,1],[2]),(2,[1],[2,2]),
      (2,[2],[2,2]),(2,[1,2],[2]),
      (3,[1],[2]),(3,[2],[1,2]),
      (2,[1,2],[1,1]),(2,[1,1],[1,2])
    ]
    for q,source,target in cases:
        got=exhaustive_between(source,target,q)
        exp=predicted_between(source,target,q)
        if got!=exp:
            raise AssertionError((q,source,target,dict(got),dict(exp)))
        print('OK q=%s source=%s target=%s ranks=%s total=%d' %
              (q,source,target,dict(sorted(got.items())),sum(got.values())))
    print('VERIFY_OK',len(cases),'independent exhaustive cases')
if __name__=='__main__':main()
