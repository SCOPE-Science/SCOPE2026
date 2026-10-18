#!/usr/bin/env python3
"""Standalone exact integer enumeration for clique Euler and partition statistic."""
from functools import lru_cache
from itertools import groupby
from collections import defaultdict
from math import comb

@lru_cache(None)
def partitions(n, cap):
    if n==0: return ((),)
    return tuple((k,)+v for k in range(min(n,cap),0,-1) for v in partitions(n-k,k))

def partition_statistic(lam):
    m=[len(tuple(g)) for _,g in groupby(lam)]
    t=len(m)
    return 0 if t < 3 else (t-2)*(t-3)//2 + sum(u>=2 for u in m[1:-1])

def graph_of_partitions(n):
    vs=partitions(n,n)
    idx={v:i for i,v in enumerate(vs)}
    adj=[set() for _ in vs]
    for i,lam in enumerate(vs):
        a=list(lam)
        for donor in range(len(a)):
            for recipient in range(len(a)+1):
                if recipient==donor:continue
                b=a[:]
                b[donor]-=1
                if recipient==len(a):b.append(1)
                else:b[recipient]+=1
                next_lam=tuple(sorted((x for x in b if x>0),reverse=True))
                if next_lam!=lam:
                    j=idx[next_lam];adj[i].add(j);adj[j].add(i)
    return vs,adj

def clique_euler(adj):
    # Extend cliques by strictly larger vertex labels; sign 1,-1,+1,...
    total=0
    counts=defaultdict(int)
    def expand(candidates, sign, dim):
        nonlocal total
        for j,u in enumerate(candidates):
            total+=sign;counts[dim]+=1
            expand([v for v in candidates[j+1:] if v in adj[u]],-sign,dim+1)
    expand(list(range(len(adj))),1,1)
    return total,dict(counts)

def directed_link_statistic(vs,adj):
    # Independent, graph-level Euler contributions from height-directed links.
    heights=[sum((i+1)*v for i,v in enumerate(lam)) for lam in vs]
    total=0
    for i,lam in enumerate(vs):
        lower=sorted(u for u in adj[i] if heights[u]<heights[i]); S=set(lower)
        # count cliques in subgraph induced on lower neighbors
        mapping={v:j for j,v in enumerate(lower)}
        lower_adj=[{mapping[y] for y in adj[x]&S} for x in lower]
        chi,_=clique_euler(lower_adj)
        local=1-chi
        t=sum(1 for _ in groupby(lam))
        m=[len(tuple(g)) for _,g in groupby(lam)]
        expected=(1 if len(lam)==1 else 0) if t==1 else ((t-1)*(t-2)//2 -sum(x==1 for x in m[1:-1]))
        if local!=expected: raise AssertionError((lam,local,expected,lower))
        total+=local
    return total

def qseries_b(nmax):
    # Formal-power-series verification of the stated Euler-product identity.
    def multiples_product(sizes):
        poly=[1]+[0]*nmax
        for d in sizes:
            for j in range(d,nmax+1):poly[j]+=poly[j-d]
        return poly
    def convolution(a,b):
        c=[0]*(nmax+1)
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b[:nmax+1-i]):c[i+j]+=x*y
        return c
    P=multiples_product(range(1,nmax+1))
    # Coefficients of 1 - sum_{i>=1} q^i + sum_{1<=i<j} q^(i+j).
    R=[0]*(nmax+1);R[0]=1
    for k in range(1,nmax+1):R[k]=-1+max(0,(k-1)//2)
    outcome=convolution(P,R)
    outcome[0]-=1
    smaller=[[1]+[0]*nmax]
    for k in range(1,nmax+1):
        old=smaller[-1][:]
        for i in range(k,nmax+1):old[i]+=old[i-k]
        smaller.append(old)
    greater=[[0]*(nmax+1) for _ in range(nmax+1)]
    greater[nmax][0]=1
    for k in range(nmax-1,-1,-1):
        a=greater[k+1][:]
        d=k+1
        for i in range(d,nmax+1):a[i]+=a[i-d]
        greater[k]=a
    for k in range(1,nmax+1):
        A=smaller[k-1][:];A[0]-=1
        B=greater[k][:];B[0]-=1
        C=convolution(A,B)
        for i in range(nmax+1-k):outcome[k+i]-=C[i]
    return outcome

PUBLISHED=[1,1,1,1,1,1,1,2,3,6,11,20,33,56,88,138,208,311,452,653,922,1294,1788,2454,3325]

def main():
    print('Exact graph/clique checks:')
    for n in range(1,16):
        vs,adj=graph_of_partitions(n)
        chi,clique_counts=clique_euler(adj)
        b=sum(partition_statistic(lam) for lam in vs)
        localchi=directed_link_statistic(vs,adj)
        assert chi==1+b==localchi==PUBLISHED[n-1],(n,chi,b,localchi)
        print('n=%2d partitions=%3d Euler=%3d b=%3d cliques=%d'% (n,len(vs),chi,b,sum(clique_counts.values())))
    print('Partition-statistic checks against independent published Euler table:')
    for n in range(16,26):
        vs=partitions(n,n)
        b=sum(partition_statistic(lam) for lam in vs)
        assert b+1==PUBLISHED[n-1]
        print('n=%2d partitions=%4d Euler=%4d b=%4d'%(n,len(vs),b+1,b))
    print('Formal q-series and monotonicity checks:')
    bseries=qseries_b(35)
    assert bseries[0]==0
    for n in range(1,36):
        b=sum(partition_statistic(lam) for lam in partitions(n,n))
        assert bseries[n]==b,(n,bseries[n],b)
        if n <= 7:assert b==0
        if n>=8:assert b>bseries[n-1],(n,b,bseries[n-1])
        if n in (8,9,10,25,26,30,35):print('n=%2d b=%d'%(n,b))
    print('PASS')

if __name__=='__main__':main()
