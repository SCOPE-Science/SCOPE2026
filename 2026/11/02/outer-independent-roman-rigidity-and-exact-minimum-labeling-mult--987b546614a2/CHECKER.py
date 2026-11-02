#!/usr/bin/env python3
"""Self-contained exact small-case and explicit-witness checks for outer-independent Roman domination on clique chains."""
from itertools import product
from collections import defaultdict
from math import ceil

def neighbors(m,n,cyclic):
    G=[set() for _ in range(m*n)]
    def edge(u,v):G[u].add(v);G[v].add(u)
    for j in range(n):
        for a in range(m):
            for b in range(a+1,m):edge(j*m+a,j*m+b)
        if j+1<n:
            for a in range(m):edge(j*m+a,(j+1)*m+a)
    if cyclic and n>=3:
        for a in range(m):edge((n-1)*m+a,a)
    return G

def valid(labels,G,require_total=True):
    for v,x in enumerate(labels):
        if x==0:
            if any(labels[u]==0 for u in G[v]):return False
            if not any(labels[u]==2 for u in G[v]):return False
        if require_total and x>0 and not any(labels[u]>0 for u in G[v]):return False
    return True

def expected(m,n,cyclic):
    return m*n-(1 if cyclic and n==3 else (2*n)//3)

def constructive(m,n,cyclic):
    assert m>=3 and n>=1 and (not cyclic or n>=3)
    labels=[[1]*m for _ in range(n)]
    if cyclic and n==3:
        labels[0][0]=0;labels[0][1]=2;labels[1][1]=0
        return tuple(x for col in labels for x in col)
    if not cyclic:
        if n==1:centers=[0]
        else:
            centers=list(range(1,n,3))
            if n%3==1:centers.append(n-1)
        assert len(centers)==ceil(n/3) and len(set(centers))==len(centers)
    else:
        k=ceil(n/3)
        gaps=[2]*(3*k-n)+[3]*(n-2*k)
        assert k>=2 and sum(gaps)==n
        centers=[0]
        for g in gaps[:-1]:centers.append(centers[-1]+g)
    k=len(centers)
    colors=[(i%2) for i in range(k)]
    if cyclic and k%2==1:colors[-1]=2
    assert all(colors[i]!=colors[i+1] for i in range(k-1))
    if cyclic:assert colors[0]!=colors[-1]
    rows=[None]*n
    if not cyclic:
        for j in range(centers[0]):rows[j]=colors[0]
        for j in range(k-1):
            dist=centers[j+1]-centers[j]
            assert dist in (2,3)
            rows[centers[j]+1]=colors[j]
            if dist==3:rows[centers[j]+2]=colors[j+1]
        for j in range(centers[-1]+1,n):rows[j]=colors[-1]
    else:
        for j in range(k):
            dist=(centers[(j+1)%k]-centers[j])%n
            if dist==0:dist=n
            assert dist in (2,3)
            rows[(centers[j]+1)%n]=colors[j]
            if dist==3:rows[(centers[j]+2)%n]=colors[(j+1)%k]
    for j,c in enumerate(centers):
        forbidden={colors[j]}
        if c>0:forbidden.add(rows[c-1])
        elif cyclic:forbidden.add(rows[-1])
        if c<n-1:forbidden.add(rows[c+1])
        elif cyclic:forbidden.add(rows[0])
        b=next(i for i in range(m) if i not in forbidden)
        rows[c]=b
        labels[c][colors[j]]=2
    assert all(x is not None for x in rows)
    for j,r in enumerate(rows):
        assert labels[j][r]==1,(j,r,labels[j])
        labels[j][r]=0
    return tuple(x for col in labels for x in col)

def exact_dp(m,n,cyclic):
    """Unrestricted column-state dynamic program, tracking exact minima and multiplicities."""
    states=[s for s in product((0,1,2),repeat=m) if s.count(0)<=1]
    S=len(states)
    wt=[sum(s) for s in states]
    adj=[[not any(states[i][r]==states[j][r]==0 for r in range(m)) for j in range(S)] for i in range(S)]
    good=[[[False]*S for _ in range(S)] for _ in range(S)]
    for i in range(S):
        for j in range(S):
            if not adj[i][j]:continue
            for k in range(S):
                if not adj[j][k]:continue
                zero=states[j].index(0) if 0 in states[j] else -1
                good[i][j][k]=(zero==-1 or (2 in states[j] or states[i][zero]==2 or states[k][zero]==2))
    def start_good(a,b):
        z=states[a].index(0) if 0 in states[a] else -1
        return z==-1 or 2 in states[a] or states[b][z]==2
    def end_good(a,b):
        z=states[b].index(0) if 0 in states[b] else -1
        return z==-1 or 2 in states[b] or states[a][z]==2
    def insert(d,key,w,c):
        if key not in d or w<d[key][0]:d[key]=(w,c)
        elif w==d[key][0]:d[key]=(w,d[key][1]+c)
    answer=None
    for a in range(S):
        for b in range(S):
            if not adj[a][b] or (not cyclic and not start_good(a,b)):continue
            d={(a,b):(wt[a]+wt[b],1)}
            for t in range(2,n):
                nd={}
                for (i,j),(w,c) in d.items():
                    for k in range(S):
                        if good[i][j][k]:insert(nd,(j,k),w+wt[k],c)
                d=nd
            for (i,j),(w,c) in d.items():
                ok=(good[i][j][a] and good[j][a][b]) if cyclic else end_good(i,j)
                if ok:
                    if answer is None or w<answer[0]:answer=(w,c)
                    elif w==answer[0]:answer=(w,answer[1]+c)
    return answer

def direct_bruteforce(m,n,cyclic):
    G=neighbors(m,n,cyclic)
    best=None;count=0
    for f in product((0,1,2),repeat=m*n):
        if not valid(f,G,False):continue
        w=sum(f)
        if best is None or w<best:best=w;count=1
        elif w==best:count+=1
    return best,count

def run():
    w=0
    for cyc in (False,True):
        for m in range(3,9):
            for n in range(3 if cyc else 1,80):
                f=constructive(m,n,cyc)
                assert valid(f,neighbors(m,n,cyc)),(m,n,cyc,'invalid witness')
                assert sum(f)==expected(m,n,cyc),(m,n,cyc,'wrong weight')
                w+=1
    print('WITNESSES_OK',w,flush=True)
    cases=[(3,n,False) for n in range(2,11)]+[(3,n,True) for n in range(3,11)]
    cases += [(4,2,False),(4,3,False),(4,3,True)]
    for m,n,cyc in cases:
        ans=exact_dp(m,n,cyc)
        assert ans[0]==expected(m,n,cyc),(m,n,cyc,ans,expected(m,n,cyc))
        if n%3==0 and (not cyc or n>=6):
            q=n//3
            if cyc:count=3*((m-1)**q+(-1)**q*(m-1))*(m-1)**q
            else:count=m*(m-1)**(2*q-1)
            assert ans[1]==count,(m,n,cyc,ans,count)
        print('DP_OK',m,n,'cycle' if cyc else 'path',ans,flush=True)
    direct_cases=[(3,3,False),(3,3,True),(4,2,False),(3,4,False)]
    for m,n,cyc in direct_cases:
        ans=direct_bruteforce(m,n,cyc)
        assert ans[0]==expected(m,n,cyc),(m,n,cyc,ans)
        print('DIRECT_GRAPH_OK',m,n,'cycle' if cyc else 'path',ans,flush=True)
    print('VERIFY_OK: %d constructed and graph-checked witnesses; %d unrestricted DP minima/counts; %d direct all-label graph enumerations' %(w,len(cases),len(direct_cases)))
if __name__=='__main__':run()
