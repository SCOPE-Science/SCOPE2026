#!/usr/bin/env python3
"""Exact checks for smooth torus-fixed point counts of bipartite graphic fans.

Reproducible with Python 3 standard library: python verify_graphical_zonotope.py
The symbolic theorem for all parameters is proved separately; this finite
calculation tests canonical source layers and the predicted enumerator.
"""
from collections import deque
from itertools import product
from math import factorial


def falling(n, k):
    return factorial(n) // factorial(n-k)


def predicted(a, b):
    s = 2 * sum(falling(a, r-1) * falling(b, r-1)
                for r in range(2, min(a, b) + 1))
    if a >= b + 1:
        s += falling(a, b-1)*factorial(b)*(2**(a-b+1)-2)
    if b >= a + 1:
        s += falling(b, a-1)*factorial(a)*(2**(b-a+1)-2)
    return s


def examine(a, b):
    n = a+b
    edges = [(i, a+j) for i in range(a) for j in range(b)]
    total = good = 0
    for bits in product((0,1), repeat=len(edges)):
        out = [set() for _ in range(n)]
        indeg = [0]*n
        for (u,v),bit in zip(edges,bits):
            if not bit: u,v=v,u
            out[u].add(v)
            indeg[v]+=1
        todo = [i for i,d in enumerate(indeg) if d==0]
        blocks = []
        removed=0
        while todo:
            layer=tuple(sorted(todo))
            blocks.append(layer)
            removed+=len(layer)
            nxt=[]
            for u in layer:
                for v in out[u]:
                    indeg[v]-=1
                    if indeg[v]==0: nxt.append(v)
            todo=nxt
        if removed!=n:
            continue
        total+=1
        # Rebuild the transitively reduced edge set by testing alternate paths.
        covers = set()
        for u in range(n):
            for v in out[u]:
                todo = deque(w for w in out[u] if w!=v)
                seen=set(todo)
                while todo and v not in seen:
                    z=todo.popleft()
                    for w in out[z]:
                        if w not in seen:
                            seen.add(w)
                            todo.append(w)
                if v not in seen:
                    covers.add((u,v))
        expected=set()
        for c,d in zip(blocks, blocks[1:]):
            for u in c:
                for v in d:
                    expected.add((u,v))
        assert covers==expected, (a,b,blocks,covers,expected)
        assert all(all(i<a for i in layer) or all(i>=a for i in layer)
                   for layer in blocks)
        assert all((blocks[i][0]<a)!=(blocks[i+1][0]<a)
                   for i in range(len(blocks)-1))
        smooth=len(covers)==n-1
        combinatorial=(len(blocks)>=3 and
                       all(len(layer)==1 for layer in blocks[1:-1]))
        assert smooth==combinatorial, (a,b,blocks,smooth,combinatorial)
        good+=smooth
    assert good==predicted(a,b), (a,b,good,predicted(a,b))
    return total,good


if __name__=='__main__':
    for a,b in ((2,2),(2,3),(2,4),(3,3),(3,4),(4,4)):
        t,s=examine(a,b)
        print(f'K({a},{b}): acyclic={t}, smooth={s}, formula={predicted(a,b)}, PASS')
    # Exact symmetric specialization: sum_{j=1}^{m-1}(j!)^{-2}.
    for m in range(2,15):
        num=sum((factorial(m)//factorial(j))**2 for j in range(1,m))
        assert predicted(m,m)==2*num
    print('balanced factorial-square identity: m=2..14 PASS')
