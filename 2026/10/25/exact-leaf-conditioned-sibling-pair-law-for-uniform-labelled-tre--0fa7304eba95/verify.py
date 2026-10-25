#!/usr/bin/env python3
"""Exact integer crosscheck of joint leaf / sibling-leaf-pair counts for uniform labeled trees."""
from collections import Counter
from itertools import product
from math import comb, factorial

def stirling(n,k):
    if n==k==0:return 1
    if n<0 or k<=0 or k>n:return 0
    row=[0]*(k+1);row[0]=1
    for i in range(1,n+1):
        nex=[0]*(k+1)
        for j in range(1,min(i,k)+1):nex[j]=j*row[j]+row[j-1]
        row=nex
    return row[k]

def allocations(j,ell):
    # Counts assignments of ell distinct elements to j labeled boxes, refined by sum binom(load,2).
    if j==0:return Counter({0:1}) if ell==0 else Counter()
    prev=[[0]*((ell*(ell-1))//2+1) for _ in range(ell+1)];prev[0][0]=1
    for _ in range(j):
        new=[[0]*len(prev[0]) for _ in range(ell+1)]
        for h in range(ell+1):
            for a in range(h+1):
                t=comb(a,2);w=comb(h,a)
                for c,v in enumerate(prev[h-a]):
                    if v:new[h][c+t]+=w*v
        prev=new
    return Counter({c:v for c,v in enumerate(prev[ell]) if v})

def formula(n):
    out=Counter()
    for ell in range(2,n):
        m=n-ell
        if m==1:out[ell,comb(ell,2)]+=n;continue
        vals=Counter()
        for j in range(m+1):
            fac=(-1)**(m-j)*comb(m,j)*j**(m-2)
            for c,v in allocations(j,ell).items(): vals[c]+=fac*v
        for c,v in vals.items():
            if v:assert v>0,(n,ell,c,v)
            if v:out[ell,c]+=comb(n,ell)*v
    return out

def brute(n):
    out=Counter()
    for code in product(range(n),repeat=n-2):
        degrees=[1]*n
        for i in code:degrees[i]+=1
        leaves=[i for i in range(n) if degrees[i]==1]
        if not leaves:raise AssertionError
        dd=degrees[:]
        adj=[[] for _ in range(n)]
        for v in code:
            leaf=next(i for i,d in enumerate(dd) if d==1)
            adj[leaf].append(v);adj[v].append(leaf)
            dd[leaf]-=1;dd[v]-=1
        last=[i for i,d in enumerate(dd) if d==1]
        assert len(last)==2
        u,v=last;adj[u].append(v);adj[v].append(u)
        counts=Counter(adj[x][0] for x in leaves)
        C=sum(comb(v,2) for v in counts.values())
        out[len(leaves),C]+=1
    return out

def main():
    checks=0
    for n in range(3,9):
        predicted=formula(n)
        observed=brute(n)
        assert predicted==observed,(n,predicted,observed)
        assert sum(observed.values())==n**(n-2)
        for ell in range(2,n):
            m=n-ell
            if m==1:
                assert observed[ell,comb(ell,2)]==n
                continue
            tot=sum(v for (l,c),v in observed.items() if l==ell)
            assert tot==comb(n,ell)*factorial(m)*stirling(n-2,m)
            fac1=sum(c*v for (l,c),v in observed.items() if l==ell)
            fac2=sum(c*(c-1)*v for (l,c),v in observed.items() if l==ell)
            expected1=comb(n,ell)*comb(ell,2)*factorial(m)*stirling(n-3,m)
            expected2=comb(n,ell)*(ell*(ell-1)*(ell-2)*(ell+1)//4)*factorial(m)*stirling(n-4,m)
            assert fac1==expected1,(n,ell,fac1,expected1)
            assert fac2==expected2,(n,ell,fac2,expected2)
            # Support is exactly realizable leaf-load profiles with at least two positive entries.
            support=set()
            def compositions(rem,k,used,score):
                if k==m:
                    if rem==0 and used>=2:support.add(score)
                    return
                for a in range(rem+1):
                    compositions(rem-a,k+1,used+(a>0),score+comb(a,2))
            compositions(ell,0,0,0)
            obs={c for (l,c),v in observed.items() if l==ell and v>0}
            assert obs==support,(n,ell,obs,support)
            checks+=4+len(obs)
        print('n=%d trees=%d leaf/cherry-cells=%d PASS'%(n,n**(n-2),len(observed)))
    print('PASS: %d independent exact table, moment, and support checks'%checks)
if __name__=='__main__':main()
