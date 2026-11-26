"""Exact finite tests of isolated-chord crossing-count comparisons."""
from collections import Counter, defaultdict
from itertools import combinations
from math import prod


def diagrams(vertices):
    if not vertices:
        yield ()
        return
    for j in range(1, len(vertices)):
        for rest in diagrams(vertices[1:j] + vertices[j + 1:]):
            yield ((vertices[0], vertices[j]),) + rest


def tail(hist, t):
    return sum(v for k, v in hist.items() if k >= t)


ordinary = {0: Counter({0: 1})}
for n in range(1, 7):
    ordinary[n] = Counter()
    conditional = defaultdict(Counter)
    biased = Counter()
    for pairs in diagrams(tuple(range(2*n))):
        hits = [(a, b) for a, b in combinations(pairs, 2)
                if (a[0] < b[0] < a[1]) != (a[0] < b[1] < a[1])]
        k = len(hits)
        isolated = set(pairs) - {c for hit in hits for c in hit}
        ordinary[n][k] += 1
        biased[k] += len(isolated)
        for c in isolated:
            conditional[c][k] += 1
    den = ordinary[n].total()
    assert den == prod(range(1, 2*n, 2))
    if n == 1:
        continue
    assert set(conditional) == {(a,b) for a,b in combinations(range(2*n), 2)
                                if (b-a) % 2}
    previous = ordinary[n-1]
    for (a, b), hist in conditional.items():
        k = (b-a-1)//2
        split = Counter()
        for x, count_x in ordinary[k].items():
            for y, count_y in ordinary[n-1-k].items():
                split[x+y] += count_x*count_y
        assert hist == split
        for t in range(n*(n-1)//2 + 2):
            assert tail(hist,t)*previous.total() <= tail(previous,t)*hist.total()
    for t in range(n*(n-1)//2 + 2):
        assert tail(previous,t)*den <= tail(ordinary[n],t)*previous.total()
        assert tail(biased,t)*den <= tail(ordinary[n],t)*biased.total()
    assert sum(k*v for k,v in biased.items())*den < (
        sum(k*v for k,v in ordinary[n].items())*biased.total())
print('PASS: exact split histograms and stochastic tails for 2 through 6 chords')
