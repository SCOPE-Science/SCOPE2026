#!/usr/bin/env python3
"""Finite exact checks for strong antagonistic paired-spin update."""
from itertools import product
from fractions import Fraction


def graphs(n):
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for mask in range(1 << len(edges)):
        neigh = [[] for _ in range(n)]
        for k, (u, v) in enumerate(edges):
            if (mask >> k) & 1:
                neigh[u].append(v)
                neigh[v].append(u)
        yield neigh


def advance(a, b, ga, gb, strength):
    n = len(a)
    aa, bb = [], []
    for i in range(n):
        ha = sum(a[j] for j in ga[i]) - strength * b[i]
        hb = sum(b[j] for j in gb[i]) - strength * a[i]
        assert ha != 0 and hb != 0
        aa.append(1 if ha > 0 else -1)
        bb.append(1 if hb > 0 else -1)
    return tuple(aa), tuple(bb)


for n in range(1, 4):
    states = list(product((-1, 1), repeat=n))
    for ga in graphs(n):
        for gb in graphs(n):
            delta = max([len(v) for v in ga + gb])
            j = delta + 1
            fixed = 0
            period_two = set()
            for a in states:
                for b in states:
                    state = a, b
                    expected = tuple(-t for t in b), tuple(-t for t in a)
                    result = advance(a, b, ga, gb, j)
                    assert result == expected
                    assert advance(*result, ga, gb, j) == state
                    assert tuple(x-y for x,y in zip(a,b)) == tuple(x-y for x,y in zip(*result))
                    if result == state:
                        fixed += 1
                    else:
                        period_two.add(frozenset((state, result)))
            assert fixed == 2**n
            assert len(period_two) == (4**n - 2**n)//2
    for r in [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)]:
        q = r*r + (1-r)*(1-r)
        direct_fixed = Fraction(0)
        direct_polar = Fraction(0)
        for a in states:
            for b in states:
                pr = Fraction(1)
                for x,y in zip(a,b):
                    pr *= (r if x == 1 else 1-r) * (1-r if y == 1 else r)
                if all(x == -y for x,y in zip(a,b)):
                    direct_fixed += pr
                if (all(x == 1 for x in a) and all(y == -1 for y in b)) or (all(x == -1 for x in a) and all(y == 1 for y in b)):
                    direct_polar += pr
        assert direct_fixed == q**n
        assert direct_polar == r**(2*n) + (1-r)**(2*n)

# Sharpness of the state-uniform guarantee: j<=Delta fails for all-positive states.
n=4
g=[ [v for v in range(n) if v!=i] for i in range(n)]
allpos=(1,)*n
assert advance(allpos,allpos,g,g,2) != ((-1,)*n,(-1,)*n)
assert sum(allpos[k] for k in g[0]) - 3*allpos[0] == 0
print('VERIFY_OK: exact complete microstate census, sharpness and biased-ensemble probabilities')
