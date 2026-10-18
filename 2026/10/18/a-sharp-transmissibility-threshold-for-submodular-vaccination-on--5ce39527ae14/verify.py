#!/usr/bin/env python3
"""Independent exact-integer checks for cycle-immunization threshold identities."""
from itertools import combinations, product
from fractions import Fraction
from math import comb

def reached(n, edges, live, blocked):
    if blocked & 1:
        raise ValueError('The index case cannot be vaccinated')
    active = 1
    changed = True
    while changed:
        changed = False
        for j, (u, v) in enumerate(edges):
            if not (live >> j & 1) or (blocked >> u & 1) or (blocked >> v & 1):
                continue
            if (active >> u & 1) and not (active >> v & 1):
                active |= 1 << v
                changed = True
            if (active >> v & 1) and not (active >> u & 1):
                active |= 1 << u
                changed = True
    return active.bit_count()

def all_infections(n, edges, numerator, denominator):
    weight = [(numerator ** live.bit_count()) * ((denominator - numerator)**(len(edges)-live.bit_count())) for live in range(1 << len(edges))]
    out = {}
    for blocked in range(1 << n):
        if blocked & 1:
            continue
        out[blocked] = sum(weight[live]*reached(n,edges,live,blocked) for live in range(1 << len(edges)))
    return out  # numerators, denominator ** |E|

def delta(tab,blocked,a,b):
    ia,ib=1 << a,1 << b
    return tab[blocked|ia]+tab[blocked|ib]-tab[blocked|ia|ib]-tab[blocked]

def cycle_check(n,p,q):
    E=[(i,(i+1)%n) for i in range(n)]
    t=all_infections(n,E,p,q)
    one=q**n
    for a,b in combinations(range(1,n),2):
        A=a;C=n-b
        rhs=(n-1)*Fraction(p,q)**n - sum((Fraction(p,q)**k for k in range(n-A,n)),Fraction(0)) - sum((Fraction(p,q)**k for k in range(n-C,n)),Fraction(0))
        assert delta(t,0,a,b)==rhs*one,(n,p,q,a,b,delta(t,0,a,b),rhs*one)
        for S in t:
            if S & ((1<<a)|(1<<b)): continue
            d=delta(t,S,a,b)
            if S:
                assert d<=0,(n,p,q,S,a,b,d)
            if p*(n-1)<=2*q:
                assert d<=0,(n,p,q,S,a,b,d)
    if n>=4 and p*(n-1)>2*q:
        assert delta(t,0,1,n-1)>0
    return len(t),len(list(combinations(range(1,n),2)))

def prufer_tree(n,seq):
    deg=[1]*n
    for u in seq:deg[u]+=1
    E=[]
    for u in seq:
        v=next(i for i in range(n) if deg[i]==1)
        E.append((u,v));deg[u]-=1;deg[v]-=1
    x,y=[i for i in range(n) if deg[i]==1]
    E.append((x,y))
    return E

def check_tree(n,seq):
    E=prufer_tree(n,seq)
    p,q=2,5
    tab=all_infections(n,E,p,q)
    # independent path-coverage expression for every vaccination set
    neigh=[[] for _ in range(n)]
    for u,v in E:neigh[u].append(v);neigh[v].append(u)
    parent=[-1]*n; depth=[0]*n
    seen={0};stack=[0]
    while stack:
        v=stack.pop()
        for u in neigh[v]:
            if u not in seen:
                seen.add(u);parent[u]=v;depth[u]=depth[v]+1;stack.append(u)
    for S in tab:
        expect=0
        for v in range(1,n):
            u=v
            while u>0:
                if (S>>u)&1:
                    expect+=p**depth[v]*q**(n-1-depth[v]);break
                u=parent[u]
        assert tab[0]-tab[S]==expect,(n,seq,S)
    return len(tab)

def main():
    ct=0
    for n in range(3,9):
        for p,q in [(1,4),(1,2),(3,4),(9,10)]:
            v,k=cycle_check(n,p,q)
            ct+=1
    print('Cycle tests: %s complete numerator tables at 4 rational probabilities; n=3..8, all vaccination sets and pairs.'%ct)
    nt=0
    for n in range(2,7):
        for seq in product(range(n),repeat=n-2):
            check_tree(n,seq)
            nt+=1
    print('Tree tests:',nt,'labeled Prüfer-sequence trees, each checked against independent path coverage for all vaccination sets.')
    print('All exact-integer checks PASSED')

if __name__=='__main__':main()
