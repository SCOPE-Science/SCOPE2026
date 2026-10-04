#!/usr/bin/env python3
from itertools import combinations
from math import comb


def original_graph(a,b):
    n=a+b
    A=set(range(a)); B=set(range(a,n))
    adj=[set() for _ in range(n)]
    for u in A:
        for v in B:
            adj[u].add(v); adj[v].add(u)
    return adj,A,B


def switch(adj,S):
    n=len(adj); S=set(S); T=set(range(n))-S
    out=[set(x) for x in adj]
    for u in S:
        for v in T:
            if v in out[u]:
                out[u].remove(v); out[v].remove(u)
            else:
                out[u].add(v); out[v].add(u)
    return out


def complete_bipartite_sizes(adj):
    n=len(adj)
    if n==0:
        return (0,0)
    if all(len(nei)==0 for nei in adj):
        return (0,n)
    # Connected bipartite test, then exact completeness.
    color=[None]*n
    color[0]=0; q=[0]
    for u in q:
        for v in adj[u]:
            if color[v] is None:
                color[v]=1-color[u]; q.append(v)
            elif color[v]==color[u]:
                return None
    if any(c is None for c in color):
        return None
    P={i for i,c in enumerate(color) if c==0}
    Q=set(range(n))-P
    if any((v in adj[u]) != (v in Q) for u in P for v in range(n) if v!=u):
        return None
    if any((v in adj[u]) != (v in P) for u in Q for v in range(n) if v!=u):
        return None
    return tuple(sorted((len(P),len(Q))))


def subsets(n):
    for mask in range(1<<n):
        yield {i for i in range(n) if (mask>>i)&1}


def main():
    cases=0; selectors=0; iss=0
    for a in range(1,7):
        for b in range(1,7):
            if a+b>10: continue
            adj,A,B=original_graph(a,b)
            good=0
            for S in subsets(a+b):
                selectors+=1
                x=len(S&A); y=len(S&B); d=x-y
                H=switch(adj,S)
                got=complete_bipartite_sizes(H)
                predicted=tuple(sorted((b+d,a-d)))
                assert got==predicted, (a,b,S,got,predicted)
                iso=(got==tuple(sorted((a,b))))
                criterion=(d==0 or d==a-b)
                assert iso==criterion, (a,b,S,d,got)
                if iso: good+=1
            expected=comb(a+b,a)*(1 if a==b else 2)
            assert good==expected,(a,b,good,expected)
            iss+=good; cases+=1

    # Explicit failure of closure in K_{2,3}.
    a,b=2,3
    adj,A,B=original_graph(a,b)
    a0=0; b0=2
    S={b0}; T={a0,b0}; U=S^T
    target=tuple(sorted((a,b)))
    assert complete_bipartite_sizes(switch(adj,S))==target
    assert complete_bipartite_sizes(switch(adj,T))==target
    assert complete_bipartite_sizes(switch(adj,U))!=target

    print(f"ALL CHECKS PASSED; parameter_cases={cases}; selectors={selectors}; iss_selectors={iss}; a,b_range=1..6 with a+b<=10")

if __name__=='__main__':
    main()
