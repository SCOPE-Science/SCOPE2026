#!/usr/bin/env python3
"""Exhaustive verifier for chromatic-palette forcing on a clique bouquet.

For a graph with a universal center and disjoint peripheral cliques, enumerate
all partial labelled q-colour assignments and implement the defining local rule.
No theorem-specific shortcut enters the brute-force decision procedure.
"""
from itertools import product
from math import factorial, comb


def graph(sizes):
    n=1+sum(sizes)
    adj=[set() for _ in range(n)]
    start=1
    for s in sizes:
        blade=list(range(start,start+s))
        start+=s
        for u in blade:
            adj[0].add(u); adj[u].add(0)
            for v in blade:
                if u!=v: adj[u].add(v)
    return adj


def forced(q,adj,assignment):
    current=list(assignment)
    # Improper initial assignments cannot force proper final colourings.
    if any(current[u]>=0 and current[v]==current[u]
           for u in range(len(current)) for v in adj[u]):
        return False
    while True:
        candidates=[]
        for v,c in enumerate(current):
            if c>=0: continue
            used={current[w] for w in adj[v] if current[w]>=0}
            if len(used)==q-1:
                missing=set(range(q))-used
                assert len(missing)==1
                candidates.append((v,next(iter(missing))))
        if not candidates: break
        v,color=candidates[0]
        current[v]=color
    return all(c>=0 for c in current) and all(current[u]!=current[v]
           for u in range(len(current)) for v in adj[u])


def falling(a,s):
    v=1
    for i in range(s): v*=a-i
    return v


def predicted(sizes):
    q=1+max(sizes)
    a=q-1
    B=sizes.count(a)
    small=[s for s in sizes if s<a]
    S=sum(small)
    U=1
    V=1
    for s in small:
        U*=falling(a,s)
        V*=falling(a-1,s)
    base=[0]*(B+2)
    for j in range(B+1):
        val=comb(B,j)*a**(B-j)*U
        base[j]+=val
        base[j+1]+=val
    base[0]-=a*V
    multiplier=q*factorial(a)**B
    return [0]*(S+B*(q-2))+[v*multiplier for v in base]


def run():
    cases=[(2,), (2,2), (2,2,2), (2,2,2,2), (2,1), (2,2,1),
           (2,1,1), (3,), (3,1), (3,2), (3,3), (3,2,1),
           (3,3,1), (4,), (4,1), (4,2)]
    checked=0
    for sizes in cases:
        q=1+max(sizes)
        adj=graph(sizes)
        n=len(adj)
        got=[0]*(n+1)
        for ass in product(range(-1,q),repeat=n):
            checked+=1
            if forced(q,adj,ass):
                k=sum(c>=0 for c in ass)
                got[k]+=1
        want=predicted(sizes)
        assert got==want,(sizes,got,want)
        print(f'blades={sizes}, q={q}, vertices={n}, assignments={(q+1)**n}, '
              f'valid={sum(got)}, min_seed={next(i for i,a in enumerate(got) if a)}, PASS')
    print('ALL PASSED; labelled partial assignments checked:',checked)


if __name__=='__main__': run()
