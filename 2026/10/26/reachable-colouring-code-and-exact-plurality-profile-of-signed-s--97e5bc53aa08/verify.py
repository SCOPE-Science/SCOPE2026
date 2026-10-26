#!/usr/bin/env python3
"""Exact finite verification of signed-star two-colour burning.

The ignition occurs AFTER synchronous spread, with persistent burned colours.
No external packages. Sign array gives center-to-leaf edge signs.
"""
from itertools import product
from collections import Counter


def reachable(signs):
    n = len(signs)
    N = n+1
    # 0 unburned, +/-1 burning; center is coordinate 0
    initial=(0,)*N
    frontier={initial}
    finals=set()
    while frontier:
        next_states=set()
        for state in frontier:
            if all(state):
                finals.add(state)
                continue
            spread=list(state)
            for v in range(N):
                if state[v]:
                    continue
                if v==0:
                    h=sum(s*state[j+1] for j,s in enumerate(signs))
                else:
                    h=signs[v-1]*state[0]
                if h:
                    spread[v]=1 if h>0 else -1
            if all(spread):
                finals.add(tuple(spread))
            else:
                for v,x in enumerate(spread):
                    if x==0:
                        for c in (-1,1):
                            q=spread.copy();q[v]=c
                            next_states.add(tuple(q))
        frontier=next_states
    return finals


def expected(signs):
    n=len(signs)
    if n==1:
        return {(a,a*signs[0]) for a in (-1,1)}
    ans=set()
    for a in (-1,1):
        base=(a,)+(tuple(a*s for s in signs))
        ans.add(base)
        for j in range(n):
            v=list(base);v[j+1]=-v[j+1]
            ans.add(tuple(v))
    return ans


def polynomial(signs):
    p=sum(s==1 for s in signs)
    q=len(signs)-p
    c=Counter()
    # Canonical center +/- and one flippable leaf if at least two leaves.
    if len(signs)==1:
        for a in (-1,1):
            c[int(a==1)+int(a*signs[0]==1)]+=1
    else:
        c[p+1]+=1; c[p]+=p; c[p+2]+=q
        c[q]+=1; c[q-1]+=q; c[q+1]+=p
    return +c


def main():
    total=0
    for n in range(1,8):
        for signs in product((-1,1),repeat=n):
            actual=reachable(signs)
            prediction=expected(signs)
            assert actual==prediction,(n,signs,actual^prediction)
            poly=Counter(sum(c==1 for c in v) for v in actual)
            assert poly==polynomial(signs),(n,signs,poly,polynomial(signs))
            p=signs.count(1);q=n-p
            if n==1:
                Y=(2 if p else 1)
            else:
                Y=max(1+p+int(q>0),q+int(p>0))
            assert max(poly)==Y,(n,signs,max(poly),Y)
            assert len(actual)==(2 if n==1 else 2*(n+1))
            total+=1
        # Covering radius of all-positive star's reachable-coloring code.
        code=expected((1,)*n)
        rho=max(min(sum(u!=v for u,v in zip(x,w)) for w in code)
                for x in product((-1,1),repeat=n+1))
        theoretical=(1 if n<=2 else (n-1)//2)
        assert rho==theoretical,(n,rho,theoretical)
        # Every signing is a switching of all-positive on a tree.
        observed=min(max(sum(v==1 for v in x) for x in expected(signs))
                     for signs in product((-1,1),repeat=n))
        assert observed==n+1-rho,(n,observed,rho)
        print(f'n={n}: signings={2**n}; reachable/signing={len(code)}; covering_radius={rho}; worst_plurality={observed}')
    print(f'VERIFY_OK: {total} signing cases; full reachable sets, colour-count distributions, plurality, covering radii, and worst signing')

if __name__=='__main__':
    main()
