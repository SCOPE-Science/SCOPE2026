"""Exact finite checks of span-conditioned gap stochastic orders.

Run: python verify.py
No external packages or files are required.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter, defaultdict
from math import comb

checks=0

def ok(test, message):
    global checks
    checks += 1
    if not test:
        raise AssertionError(message)

def choose(n,k):
    return comb(n,k) if 0 <= k <= n else 0

def compositions(n,k):
    if k==1:
        yield (n,)
        return
    for breaks in combinations(range(1,n),k-1):
        yield tuple(b-a for a,b in zip((0,)+breaks,breaks+(n,)))

for N in range(2,12):
    for k in range(2,N+1):
        samples=list(combinations(range(1,N+1),k))
        span=Counter()
        conditional=defaultdict(Counter)
        rows=[]
        for ss in samples:
            g=tuple(b-a for a,b in zip(ss,ss[1:]))
            r=ss[-1]-ss[0]
            span[r]+=1
            conditional[r][g]+=1
            A=sum(h==1 for h in g)
            Q=F(sum(h*h for h in g),r*r)
            rows.append((r,A,Q,g))
        total=len(samples)
        ER=sum(F(r,total) for r,A,Q,g in rows)
        EA=sum(F(A,total) for r,A,Q,g in rows)
        EAR=sum(F(r*A,total) for r,A,Q,g in rows)
        EQR=sum(F(r*Q,total) for r,A,Q,g in rows)
        EQ=sum((Q for r,A,Q,g in rows),F(0))/total
        m=k-1
        ok(ER==F((k-1)*(N+1),k+1), ('mean range',N,k))
        ok(EA==F(k*(k-1),N), ('mean adj',N,k))
        ok(EAR-EA*ER==F(-2*(k-1)*(N-k),N*(k+1)), ('cov',N,k))
        EQpred=sum((F(span[r],total) * F(2*r-m+1,(m+1)*r) for r in span),F(0))
        ok(EQ==EQpred, ('mean norm squares',N,k))
        E1R=sum((F(span[r],total*r) for r in span),F(0))
        ok(EQR-EQ*ER==F(m-1,m+1)*(ER*E1R-1),('Q covariance',N,k))
        for r in range(m,N):
            c=choose(r-1,m-1)
            ok(span[r]==(N-r)*c,('span mass',N,k,r))
            expected=set(compositions(r,m))
            ok(set(conditional[r])==expected,('gap support',N,k,r))
            ok(all(conditional[r][g]==N-r for g in expected),('gap conditional uniform',N,k,r))
            for t in range(1,N):
                ec=sum(F(v*sum(z<=t for z in g),span[r]) for g,v in conditional[r].items())
                expected_ec=m*(1-F(choose(r-t-1,m-1),c))
                ok(ec==expected_ec,('threshold mean',N,k,r,t))
            eq=sum(F(v*sum(z*z for z in g),span[r]*r*r) for g,v in conditional[r].items())
            ok(eq==F(2*r-m+1,(m+1)*r),('conditional Q',N,k,r))
        for r in range(m,N-1):
            old=list(compositions(r,m)); new=list(compositions(r+1,m))
            oldw=F(1,len(old));neww=F(1,len(new))
            for h in new:
                mass=sum((oldw*F(g[i],r) for g in old for i in range(m) if tuple(g[j]+(i==j) for j in range(m))==h),F(0))
                ok(mass==neww,('polya recursion',N,k,r,h))
            old_q=F(sum(sum(z*z for z in g) for g in old),len(old)*r*r)
            new_q=F(sum(sum(z*z for z in h) for h in new),len(new)*(r+1)*(r+1))
            ok(new_q>=old_q,('convex order consequence',N,k,r))
            for t in range(1,N):
                old_c=F(sum(sum(z<=t for z in g) for g in old),len(old))
                new_c=F(sum(sum(z<=t for z in h) for h in new),len(new))
                ok(new_c<=old_c,('short-gap regression',N,k,r,t))
        if k<N:
            for t in range(1,N-k+1):
                ECT=sum(F(sum(z<=t for z in g),total) for r,A,Q,g in rows)
                ERCT=sum(F(r*sum(z<=t for z in g),total) for r,A,Q,g in rows)
                ok(ERCT-ER*ECT<0,('strict negative',N,k,t))
        if 3<=k<N:
            ok(EQR-EQ*ER>0,('strict positive',N,k))
print('exact_checks_passed:',checks)
