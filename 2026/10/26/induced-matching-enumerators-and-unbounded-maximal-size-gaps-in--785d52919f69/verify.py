#!/usr/bin/env python3
"""Exact independent checks for maximal induced matchings of S(K_{p,q}).

Uses raw graph adjacency, not the bijection in the proof. No dependencies.
"""
from itertools import combinations
from math import comb, factorial


def stirling(n,k):
    if k < 0 or k > n: return 0
    a=[1]
    for i in range(1,n+1):
        b=[0]*(i+1)
        for j in range(1,i+1):
            b[j]=(j*a[j] if j<len(a) else 0)+a[j-1]
        a=b
    return a[k]


def formulas(p,q):
    degree=p+q-2
    all_c=[0]*(degree+1); maximal=[0]*(degree+1)
    for a in range(p+1):
        for b in range(q+1):
            k=a+b
            if k>degree:continue
            all_c[k]+=comb(p,a)*comb(q,b)*(q-b)**a*(p-a)**b
            if a<p and b<q:
                u=p-a; v=q-b
                maximal[k]+=comb(p,a)*comb(q,b)*factorial(u)*stirling(b,u)*factorial(v)*stirling(a,v)
    maximal[p]+=q**p
    maximal[q]+=p**q
    return all_c,maximal


def make_graph(p,q):
    n=p+q
    pairs=[(a,p+b) for a in range(p) for b in range(q)]
    N=n+len(pairs)
    adj=[[False]*N for _ in range(N)]
    for idx,(a,b) in enumerate(pairs):
        v=n+idx
        adj[a][v]=adj[v][a]=True
        adj[b][v]=adj[v][b]=True
    edges=[(u,v) for u in range(N) for v in range(u+1,N) if adj[u][v]]
    return adj,edges


def brute(p,q):
    adj,edges=make_graph(p,q)
    E=len(edges)
    assert E==2*p*q
    conflict=[0]*E
    for i,(a,b) in enumerate(edges):
        for j,(c,d) in enumerate(edges):
            if i==j or len({a,b,c,d})<4 or adj[a][c] or adj[a][d] or adj[b][c] or adj[b][d]:
                conflict[i]|=1<<j
    bound=p+q-2
    full=(1<<E)-1
    all_c=[0]*(bound+1); maximal=[0]*(bound+1)
    trials=0
    for k in range(bound+1):
        for subset in combinations(range(E),k):
            trials+=1
            chosen=0
            valid=True
            for j in subset:
                if chosen&conflict[j]:
                    valid=False
                    break
                chosen|=1<<j
            if valid:
                all_c[k]+=1
                blocked=0
                for j in subset: blocked|=conflict[j]
                if blocked==full: maximal[k]+=1
    return all_c,maximal,trials


def main():
    tested=0
    cases=[(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4)]
    for p,q in cases:
        expected=formulas(p,q)
        actualI,actualM,trials=brute(p,q)
        assert expected==(actualI,actualM),(p,q,expected,(actualI,actualM))
        support=[k for k,v in enumerate(actualM) if v]
        assert support==([p]+list(range(q,p+q-1)) if p<q else list(range(p,2*p-1)))
        tested+=trials
        print(f'p={p},q={q}, tested={trials}, all={actualI}, maximal={actualM}')
    for p in range(2,21):
        for q in range(p,27):
            I,M=formulas(p,q)
            support={k for k,v in enumerate(M) if v}
            assert support==({p}|set(range(q,p+q-1)))
            assert M[p]==(q**p if p<q else 2*p**p+factorial(p)*(2**p-2))
            assert M[-1]==p*q if p+q-2>q else (p*q+p**q if p==2 and q>2 else p*q + (2*p**p if p==q==2 else 0))
            assert I[0]==1
    print(f'PASS: independent adjacency enumeration for {len(cases)} graphs ({tested} candidate edge subsets); exact support and boundary checks for 2<=p<=20 and p<=q<=26.')

if __name__=='__main__':main()
