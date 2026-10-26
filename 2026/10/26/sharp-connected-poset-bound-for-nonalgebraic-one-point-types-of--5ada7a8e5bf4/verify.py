#!/usr/bin/env python3
"""Independent finite checks for sharp connected-poset external-type bound.
Runs with Python standard library only; not a proof for unbounded size.
"""
from itertools import combinations, product
from collections import deque


def all_natural_posets(n):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        rel = frozenset(e for k, e in enumerate(pairs) if mask >> k & 1)
        if all((a, c) in rel for a,b in rel for bb,c in rel if b == bb):
            yield rel


def type_count(n, rel):
    total=0
    for state in product((0,1,2), repeat=n):
        if any(state[a]>state[b] for a,b in rel):
            continue
        low=[i for i,t in enumerate(state) if t==0]
        high=[i for i,t in enumerate(state) if t==2]
        if all((a,b) in rel for a in low for b in high):
            total+=1
    return total


def connected(n, rel):
    if n==0: return False
    neigh=[set() for _ in range(n)]
    for a,b in rel:
        neigh[a].add(b); neigh[b].add(a)
    reached={0}; todo=[0]
    for v in todo:
        for u in neigh[v]-reached:
            reached.add(u); todo.append(u)
    return len(reached)==n


def is_one_sided_star(n, rel):
    if n==1:return True
    for c in range(n):
        if all((c,i) in rel for i in range(n) if i!=c) and len(rel)==n-1:
            return True
        if all((i,c) in rel for i in range(n) if i!=c) and len(rel)==n-1:
            return True
    return False


def run():
    all_connected=0; one_sided=0; maximal_extensions=0; strict_extensions=0
    for n in range(1,7):
        posets=list(all_natural_posets(n))
        conn=0; eq=0; ext=0
        for rel in posets:
            t=type_count(n,rel)
            if connected(n,rel):
                conn+=1
                assert t<=3*(1<<(n-1)),(n,rel,t)
                expected=is_one_sided_star(n,rel)
                assert (t==3*(1<<(n-1)))==expected,(n,rel,t,expected)
                eq+=int(expected)
            if n>=2:
                B={a for a,b in rel if b==n-1}
                if B:
                    Q=frozenset((a,b) for a,b in rel if b<n-1)
                    tQ=type_count(n-1,Q)
                    assert t<=2*tQ,(n,rel,t,tQ)
                    # Equality iff B consists of a least point of Q and Q minus it is an antichain.
                    expected=False
                    if len(B)==1:
                        b=next(iter(B))
                        expected=(all((b,j) in Q for j in range(n-1) if j!=b) and
                                  all((a,c) not in Q for a,c in combinations([j for j in range(n-1) if j!=b],2)))
                    assert (t==2*tQ)==expected,(n,rel,t,tQ,expected)
                    ext+=1
        all_connected+=conn;one_sided+=eq;maximal_extensions+=ext
        print(f"n={n}; natural_posets={len(posets)}; connected={conn}; extremal_labeled={eq}; maximal_extensions={ext}")
    print(f"CONNECTED_TESTS={all_connected}; EQUALITY_TESTS={one_sided}; EXTENSION_TESTS={maximal_extensions}")
    print("ALL_CHECKS_PASS")

if __name__ == '__main__':run()
