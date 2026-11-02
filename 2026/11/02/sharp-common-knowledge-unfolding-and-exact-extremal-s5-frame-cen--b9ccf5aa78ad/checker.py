"""Independently check extremal common-knowledge depth on finite S5 frames.

No external dependencies.  Agent relations are equivalence relations on a labeled carrier.
"""
from itertools import product
from math import factorial


def partitions(n):
    def rec(prefix, mx):
        if len(prefix) == n:
            blocks = {}
            for i, b in enumerate(prefix):
                blocks.setdefault(b, []).append(i)
            yield tuple(tuple(v) for v in blocks.values())
            return
        for value in range(mx + 2):
            yield from rec(prefix + (value,), max(mx, value))
    yield from rec((0,), 0)


def edges_for_partition(blocks, n):
    mask = [0]*n
    for block in blocks:
        for i in block:
            for j in block:
                if i != j:
                    mask[i] |= 1 << j
    return mask


def diameter_of_union(edges):
    n = len(edges)
    diam = 0
    for root in range(n):
        seen = {root}
        frontier = {root}
        dist = 0
        while frontier:
            nxt = set()
            for a in frontier:
                nxt |= {b for b in range(n) if (edges[a] >> b)&1 and b not in seen}
            if not nxt:
                break
            seen |= nxt
            frontier = nxt
            dist += 1
        diam = max(diam, dist)
    return diam


def transfer(k, n):
    if n == 1:
        return 1
    u = [0] + [1]*k
    for _ in range(n-2):
        u = [0] + [sum(__import__('math').comb(k-s,t)*u[t] for t in range(1,k-s+1)) for s in range(1,k+1)]
    from math import comb
    c = sum(comb(k,s)*u[s] for s in range(1,k+1))
    return factorial(n)*c//2


def run():
    cases = [(2,1),(3,1),(4,1),(5,1),(2,2),(3,2),(4,2),(5,2),(6,2),(2,3),(3,3),(4,3),(5,3)]
    expected = {}
    for n,k in cases:
        p = [edges_for_partition(z,n) for z in partitions(n)]
        hits=0
        for tup in product(p, repeat=k):
            e = [0]*n
            for rows in tup:
                for i in range(n):
                    e[i] |= rows[i]
            if diameter_of_union(e)==n-1:
                hits+=1
                if n>=3:
                    assert sum(x.bit_count() for x in e)==2*(n-1), (n,k,e)
        formula=transfer(k,n)
        assert hits==formula, (n,k,hits,formula)
        expected[n,k]=hits
    assert expected[5,2]==120
    assert expected[3,3]==36
    assert expected[4,3]==360
    assert expected[5,3]==4320
    assert expected[6,2]==720
    print('ALL_CHECKS_OK',expected)


if __name__=='__main__':
    run()
