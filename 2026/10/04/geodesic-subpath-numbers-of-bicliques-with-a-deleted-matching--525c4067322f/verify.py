#!/usr/bin/env python3
from collections import deque


def graph(a,b,t):
    n=a+b
    A=range(a); B=range(a,a+b)
    adj=[set() for _ in range(n)]
    for i in A:
        for j0 in range(b):
            if i < t and j0 == i:
                continue
            j=a+j0
            adj[i].add(j); adj[j].add(i)
    return adj

def all_pairs_gpn(adj):
    n=len(adj); total=n
    for s in range(n):
        dist=[-1]*n; ways=[0]*n
        dist[s]=0; ways[s]=1
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if dist[v] < 0:
                    dist[v]=dist[u]+1; ways[v]=ways[u]; q.append(v)
                elif dist[v] == dist[u]+1:
                    ways[v]+=ways[u]
        assert all(d>=0 for d in dist)
        total += sum(ways[s+1:])
    return total

def formula(a,b,t):
    return a+b + (a*b*(a+b))//2 + t*(a*b-2*a-2*b+3)-t*t

def best_t_formula(a,b):
    m=min(a,b); C=a*b-2*a-2*b+3
    vals=[t*(C-t) for t in range(m+1)]
    M=max(vals)
    return {t for t,v in enumerate(vals) if v==M}

def main():
    cases=0
    for a in range(3,9):
        for b in range(3,9):
            m=min(a,b)
            observed=[]
            for t in range(m+1):
                g=all_pairs_gpn(graph(a,b,t))
                f=formula(a,b,t)
                assert g==f,(a,b,t,g,f)
                observed.append(g)
                cases+=1
            mx=max(observed)
            got={t for t,v in enumerate(observed) if v==mx}
            assert got==best_t_formula(a,b),(a,b,got,best_t_formula(a,b))
    # Balanced corollaries.
    for n in range(3,9):
        vals=[formula(n,n,t) for t in range(n+1)]
        C=n*n-4*n+3
        assert {t for t,v in enumerate(vals) if v==max(vals)} == best_t_formula(n,n)
        if n>=5:
            assert formula(n,n,n) > formula(n,n,0)
        if n>=6:
            assert best_t_formula(n,n)=={n}
    print(f"ALL CHECKS PASSED; parameter_cases={cases}; a,b_range=3..8; balanced_n_range=3..8")

if __name__=='__main__':
    main()
