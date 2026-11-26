"""Finite exact checks for statewise payoff blindness; run with Python 3."""
from fractions import Fraction as F
from itertools import product


def gaps(groups, r):
    n = len(groups)
    d = len(groups[0]) - 1
    result = set()
    for s in product((0, 1), repeat=n):
        pay = [0] * n
        for group in groups:
            benefit = r * F(sum(s[u] for u in group), len(group))
            for v in group:
                pay[v] += benefit - s[v]
        for v in range(n):
            for u in groups[v]:
                if s[u] != s[v]:
                    result.add(abs(pay[u] - pay[v]))
    assert all(len(group) == d + 1 for group in groups)
    return result


def verify_boundary(groups, r, expected):
    possible = gaps(groups, r)
    assert max(possible) == expected
    def blind(cutoff):
        return all(delta == 0 or delta < cutoff for delta in possible)
    assert blind(expected) == (expected == 0)
    assert blind(expected + F(1, 100))


def verify_torus(L):
    vertices = list(product(range(L), repeat=2))
    steps = ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1))
    groups = [{((u+a) % L, (v+b) % L) for a, b in steps}
              for u, v in vertices]
    x, y = (0, 0), (1, 0)
    h = {v: sum((int(x in g) - int(y in g)) for g in groups if v in g)
         for v in vertices}
    assert sorted(k for k in h.values() if k > 0) == [1, 1, 1, 1, 2, 2, 3]
    assert sorted(abs(k) for k in h.values() if k < 0) == [1, 1, 1, 1, 2, 2, 3]
    assert (h[x], h[y]) == (3, -3)
    free = [h[v] for v in vertices if v not in (x, y) and h[v]]
    contrasts = {h[x] + sum(c*s for c, s in zip(free, bits))
                 for bits in product((0, 1), repeat=len(free))}
    assert len(free) == 12 and (min(contrasts), max(contrasts)) == (-5, 11)
    for r in (F(1), F(9), F(25, 3), F(30)):
        assert max(abs(r * c/5 - 5) for c in contrasts) == max(5+r, abs(r * 11/5 - 5))


if __name__ == '__main__':
    cycle4 = [{i, (i-1) % 4, (i+1) % 4} for i in range(4)]
    clique5 = [set(range(5)) for _ in range(5)]
    for r in (F(1), F(9), F(19, 2)):
        verify_boundary(cycle4, r, abs(r/3-3))
        verify_boundary(clique5, r, F(5))
    for side in (6, 7, 10):
        verify_torus(side)
    print('PASS: C4 and K5 boundary checks; exhaustive nonzero torus stencils for L=6,7,10')
