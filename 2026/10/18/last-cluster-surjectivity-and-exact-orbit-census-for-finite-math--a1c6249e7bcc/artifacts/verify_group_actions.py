#!/usr/bin/env python3
"""Check bounded-morphism orbit counts by actual source/target permutation actions.

Exhaustive cases are small enough that no symbolic orbit classification is used.
"""
from itertools import product
from collections import deque
from math import comb


def blocks(sizes):
    x = 0
    res = []
    for s in sizes:
        res.append(tuple(range(x,x+s)))
        x += s
    return res


def is_bounded(f, a, b):
    A,B = blocks(a),blocks(b)
    N, M = len(f),sum(b)
    if set(f)!=set(range(M)):
        return False
    sa = [frozenset(y for lev in A[i:] for y in lev) for i in range(len(A))]
    sb = [frozenset(y for lev in B[j:] for y in lev) for j in range(len(B))]
    rank = {v:j for j, block in enumerate(B) for v in block}
    for i, xs in enumerate(A):
        for x in xs:
            if {f[z] for z in sa[i]} != sb[rank[f[x]]]:
                return False
    return True


def swap_generators(a,b):
    # Image of map f under source transposition sends f(x)<->f(y)
    # and under target transposition replaces two values.
    G=[]
    for block in blocks(a):
        for x,y in zip(block,block[1:]):
            G.append(('source',x,y))
    for block in blocks(b):
        for x,y in zip(block,block[1:]):
            G.append(('target',x,y))
    return G


def move(f, gen):
    kind,x,y=gen
    g=list(f)
    if kind=='source':
        g[x],g[y]=g[y],g[x]
    else:
        g=[y if t==x else x if t==y else t for t in g]
    return tuple(g)


def compute_orbits(a,b):
    m,n=sum(a),sum(b)
    maps={f for f in product(range(n),repeat=m) if is_bounded(f,a,b)}
    remaining=maps.copy()
    gens=swap_generators(a,b)
    orbit_count=0
    while remaining:
        seed=next(iter(remaining))
        remaining.remove(seed)
        orbit_count+=1
        queue=deque([seed])
        while queue:
            f=queue.popleft()
            for g in gens:
                transformed=move(f,g)
                if transformed not in maps:
                    raise AssertionError(('action not preserving bounded morphisms',a,b,f,g))
                if transformed in remaining:
                    remaining.remove(transformed)
                    queue.append(transformed)
    return len(maps),orbit_count


def surj(n,q):
    return sum((-1)**i*comb(q,i)*(q-i)**n for i in range(q+1))


def formula(a,b):
    # Direct recursion over target level groups, independent of group actions.
    def recur(offset,j):
        if j==len(b):return int(offset==len(a))
        total=0
        for end in range(offset+1,len(a)-len(b)+j+2):
            factor=(b[j]**sum(a[offset:end-1]))*surj(a[end-1],b[j])
            total+=factor*recur(end,j+1)
        return total
    return recur(0,0)


def positive_partitions(n,k,minfirst=1):
    if k==1:
        if n>=minfirst:yield (n,)
        return
    for i in range(minfirst,n+1):
        for rest in positive_partitions(n-i,k-1,i):
            yield (i,)+rest


def main():
    cases=[((1,),(1,)),((3,),(2,)),((4,),(2,)),((4,),(3,)),
           ((1,2),(2,)),((2,2),(2,)),((2,1,2),(2,)),
           ((2,2),(1,1)),((3,2),(2,1)),((1,2,1),(2,1)),
           ((3,1,2),(2,1)),((2,2,1),(2,1)),
           ((1,2,2),(1,2)),((1,2,3),(2,1)),((2,1,2),(1,2)),
           ((2,1,2),(2,2)),((1,1,1),(1,1,1)),
           ((1,1,1),(2,1)),((3,2,1),(2,1)),((2,2,2),(2,2)),
           ((2,3),(2,1)),((3,2),(1,2))]
    for a,b in cases:
        actual,orbits=compute_orbits(a,b)
        expected=formula(a,b)
        if actual!=expected:raise AssertionError((a,b,actual,expected))
        # Canonical orbit invariant calculated from the explicit direct maps;
        # its distinct count must equal direct group-action orbit count.
        A,B=blocks(a),blocks(b)
        patterns=set()
        for f in product(range(sum(b)),repeat=sum(a)):
            if not is_bounded(f,a,b):continue
            patterns.add(tuple(tuple(sorted(tuple(sum(f[x]==v for x in block) for block in A)
                                            for v in target)) for target in B))
        if len(patterns)!=orbits:raise AssertionError(('orbits',a,b,orbits,len(patterns)))
    print('PASS explicit source/target group actions cases=',len(cases))
    print('CASE (3,2)->(2,1):',compute_orbits((3,2),(2,1)))
    print('CASE (2,2,2)->(2,2):',compute_orbits((2,2,2),(2,2)))

if __name__=='__main__':main()
