#!/usr/bin/env python3
"""Independent exact checks of local cyclic-triangle/score dependence."""
from fractions import Fraction
from math import comb
from collections import defaultdict

def checking(n):
    N=n-1; m=N//2
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    hist=defaultdict(int); cases=1<<len(edges)
    for mask in range(cases):
        adj=[[False]*n for _ in range(n)]
        for bit,(i,j) in enumerate(edges):
            if mask>>bit&1: adj[i][j]=True
            else: adj[j][i]=True
        d=sum(adj[0][i] for i in range(1,n))
        cyc=0
        for i in range(1,n):
            if not adj[0][i]: continue
            for j in range(1,n):
                if adj[j][0] and adj[i][j]:cyc+=1
        hist[(d,cyc)]+=1
    assert sum(hist.values())==cases
    tests=0
    for d in range(N+1):
        q=d*(N-d)
        for t in range(N*N+1):
            expected=comb(N,d)*comb(q,t)*2**(len(edges)-N-q) if t<=q else 0
            assert hist[(d,t)]==expected,(n,d,t,hist[(d,t)],expected)
            tests+=1
    Q=m*(N-m)
    post=[]
    for t in range(Q+1):
        raw={b:sum(hist[(d,t)] for d in {b,N-b}) for b in range(m+1)}
        den=sum(raw.values())
        assert den>0
        dist={b:Fraction(raw[b],den) for b in range(m+1)}
        post.append(dist)
        mean=sum(Fraction(d)*hist[(d,t)] for d in range(N+1))/den
        assert mean==Fraction(N,2),(n,t,mean)
        tests+=1
        assert sum(dist.values())==1
        tests+=1
    qsecond=(m-1)*(N-m+1)
    for t in range(Q):
        P,Qp=post[t],post[t+1]
        for b in range(m):
            t1=sum(P[k] for k in range(b+1,m+1))
            t2=sum(Qp[k] for k in range(b+1,m+1))
            assert t2>=t1,(n,t,b,t1,t2)
            if t<=qsecond and b==m-1:
                assert t2>t1,(n,t,b)
            if t>qsecond:
                assert t1==t2
            tests+=1
        def var(dist):return sum(Fraction((N-2*b)**2,4)*z for b,z in dist.items())
        if t<=qsecond: assert var(Qp)<var(P)
        else: assert var(Qp)==var(P)
        tests+=1
    return tests,cases

if __name__=='__main__':
    total=0
    for n in range(3,8):
        a,c=checking(n);total+=a
        print(f'n={n}: tournaments={c}, exact_assertion_groups={a}')
    print('PASS',total,'exact assertion groups')
