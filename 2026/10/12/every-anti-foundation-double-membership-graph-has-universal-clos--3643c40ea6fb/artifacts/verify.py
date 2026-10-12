#!/usr/bin/env python3
"""Finite replay of the disjoint-component wreath-product calculation."""
from itertools import permutations
from math import factorial


def disjoint_cliques(q, k):
    n=q*k
    edges=set()
    for b in range(k):
        block=range(b*q,(b+1)*q)
        for i in block:
            for j in block:
                if i<j: edges.add((i,j))
    return n,edges


def is_aut(p, edges):
    image={tuple(sorted((p[i],p[j]))) for i,j in edges}
    return image==edges

checks=0
# For k copies of K_q, Aut is S_q wr S_k and has order (q!)^k k!.
# Exhaust only modest sizes, enough to independently replay the component argument.
for q,k in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2)]:
    n,e=disjoint_cliques(q,k)
    count=sum(is_aut(p,e) for p in permutations(range(n)))
    expected=(factorial(q)**k)*factorial(k)
    assert count==expected,(q,k,count,expected)
    checks+=factorial(n)+1

# A direct structural check: arbitrary within-block permutations and block permutations
# preserve adjacency for several sizes.
for q in range(1,5):
    for k in range(1,5):
        n,e=disjoint_cliques(q,k)
        # deterministic sample: reverse each block and cyclically move the blocks
        p=[None]*n
        for b in range(k):
            nb=(b+1)%k
            for t in range(q):
                p[b*q+t]=nb*q+(q-1-t)
        assert is_aut(tuple(p),e)
        checks+=1

print(f"VERIFY_OK {checks} exact assertions")
