#!/usr/bin/env python3
"""Finite cross-checks of the cell-coordinate classification of cyclic Hom complexes.

The two generators deliberately use different predicates: exhaustive directed-
arc extension versus cyclic anchor selection. They test finite instances only;
the all-parameter statement is established by the accompanying proof.
"""
from collections import Counter
from itertools import permutations, combinations
from math import comb


def tournament(n):
    m = (n-1)//2
    out = [sum(1 << ((v+j) % n) for j in range(1,m+1)) for v in range(n)]
    return out


def all_cells_by_arcs(n):
    out=tournament(n)
    cells=set()
    def add(x):
        if x in cells:
            return
        cells.add(x)
        used=x[0]|x[1]|x[2]
        for v in range(n):
            bit=1<<v
            if used&bit:
                continue
            for k in range(3):
                nxt=(k+1)%3
                prv=(k+2)%3
                if (out[v]&x[nxt]) != x[nxt]:
                    continue
                if any(not (out[u]&bit) for u in range(n) if x[prv]&(1<<u)):
                    continue
                y=list(x)
                y[k] |= bit
                add(tuple(y))
    for a,b,c in permutations(range(n),3):
        if (out[a] >> b)&1 and (out[b] >> c)&1 and (out[c] >> a)&1:
            add((1<<a,1<<b,1<<c))
    return cells


def all_cells_by_anchors(n):
    m=(n-1)//2
    answer=set()
    for a in range(n):
        for x in range(1,m+1):
            for y in range(1,m+1):
                z=n-x-y
                if not 1<=z<=m:
                    continue
                b=(a+x)%n
                c=(b+y)%n
                choices=(
                    [(0,(a+j)%n) for j in range(1,m-z+1)]
                    +[(1,(b+j)%n) for j in range(1,m-x+1)]
                    +[(2,(c+j)%n) for j in range(1,m-y+1)]
                )
                assert len(choices)==m-1
                for mask in range(1<<(m-1)):
                    v=[1<<a,1<<b,1<<c]
                    for i,(which,pos) in enumerate(choices):
                        if mask>>i & 1:
                            v[which]|=1<<pos
                    t=tuple(v)
                    assert t not in answer, 'anchor representation not injective'
                    answer.add(t)
    return answer


def verify():
    for n in (5,7,9,11,13,15):
        cells1=all_cells_by_arcs(n)
        cells2=all_cells_by_anchors(n)
        assert cells1==cells2, (n,len(cells1),len(cells2),len(cells1^cells2))
        m=(n-1)//2
        counted=Counter(sum(b.bit_count() for b in t)-3 for t in cells1)
        expected={d:n*comb(m+1,2)*comb(m-1,d) for d in range(m)}
        assert dict(counted)==expected,(n,dict(counted),expected)
        print(f'n={n} cells={len(cells1)} f={tuple(counted[d] for d in range(m))}')
    print('BOOLEAN_CELL_ENUMERATION_OK')

if __name__=='__main__':
    verify()
