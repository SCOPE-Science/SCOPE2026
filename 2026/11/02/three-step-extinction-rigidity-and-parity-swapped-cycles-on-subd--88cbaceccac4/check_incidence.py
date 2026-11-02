#!/usr/bin/env python3
"""Independent bit-vector verification of mod-2 neighbor parity on edge subdivisions."""
from itertools import combinations


def mul(rows, v):
    return sum(((r & v).bit_count() & 1) << i for i,r in enumerate(rows))


def rank(rows):
    basis = {}
    for row in rows:
        x = row
        while x:
            k=x.bit_length()-1
            if k not in basis:
                basis[k]=x
                break
            x ^= basis[k]
    return len(basis)


def power_rows(rows,t):
    q=len(rows)
    out=[]
    for j in range(q):
        v=1<<j
        for _ in range(t):v=mul(rows,v)
        out.append(v)
    return [sum(((out[j]>>i)&1)<<j for j in range(q)) for i in range(q)]


def subdivision(rows):
    n=len(rows)
    edges=[(i,j) for i in range(n) for j in range(i+1,n) if (rows[i]>>j)&1]
    N=n+len(edges)
    adj=[0]*N
    for e,(u,v) in enumerate(edges,n):
        adj[e] |= (1<<u)|(1<<v)
        adj[u] |= 1<<e
        adj[v] |= 1<<e
    return adj


def connected(rows):
    n=len(rows); seen=1
    while True:
        nxt=seen
        for i in range(n):
            if (seen>>i)&1:nxt |= rows[i]
        if nxt==seen:break
        seen=nxt
    return seen==(1<<n)-1


def base_from_mask(n,mask):
    rows=[0]*n
    for k,(i,j) in enumerate(combinations(range(n),2)):
        if mask>>k&1:
            rows[i]|=1<<j;rows[j]|=1<<i
    return rows


def complete(n):
    return [(1<<n)-1 ^ (1<<i) for i in range(n)]


def main():
    graph_counts={}
    for n in range(2,7):
        tested=0; good=0
        for mask in range(1<<(n*(n-1)//2)):
            rows=base_from_mask(n,mask)
            if not connected(rows):continue
            tested+=1
            F=subdivision(rows)
            is_nil=all(x==0 for x in power_rows(F,3))
            wanted = (n%2==0 and mask==(1<<(n*(n-1)//2))-1)
            assert is_nil==wanted, (n,mask,is_nil,wanted)
            good+=is_nil
        graph_counts[n]=(tested,good)
    print('connected graph rigidity exhaustive n=2..6:',graph_counts)
    for n in range(2,15):
        F=subdivision(complete(n))
        N=len(F)
        rr=[rank(power_rows(F,t)) for t in range(4)]
        if n%2==0:
            assert rr==[N,2*(n-1),n-1,0],(n,rr)
        else:
            assert rr==[N,2*(n-1),2*(n-1),2*(n-1)],(n,rr)
            assert power_rows(F,3)==F
            dim_fix=N-rank([F[i]^(1<<i) for i in range(N)])
            assert dim_fix==n-1,(n,dim_fix)
        print(f'n={n} vertices={N} ranks={rr} OK')
    for n in range(2,6):
        F=subdivision(complete(n)); N=len(F)
        if N>15:continue
        entry={};periods={}
        for x in range(1<<N):
            seen={};v=x;t=0
            while v not in seen:
                seen[v]=t;v=mul(F,v);t+=1
            pre=seen[v];p=t-pre
            entry[pre]=entry.get(pre,0)+1
            periods[p]=periods.get(p,0)+1
        if n%2==0:
            rr=[N,2*(n-1),n-1,0]
            predicted={0:1}
            prev=1
            for t in range(1,4):
                curr=1<<(N-rr[t]);predicted[t]=curr-prev;prev=curr
            assert entry==predicted,(n,entry,predicted)
            assert periods=={1:1<<N}
        else:
            assert entry=={0:1<<(2*(n-1)),1:(1<<N)-(1<<(2*(n-1)))}
            assert periods=={1:1<<(N-(n-1)),2:(1<<N)-(1<<(N-(n-1)))}
        print(f'exhaustive n={n} states={1<<N} entry={entry} eventual_periods={periods} OK')
    print('VERIFICATION_OK')

if __name__=='__main__':main()
