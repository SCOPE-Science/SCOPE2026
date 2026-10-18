"""Exhaustive metric-based checks of commuting nilpotents in finite stars.

Run with Python 3; uses the standard library only. For n = 1,...,6,
construct all partial metric isometries and independently test their products.
"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial


def distance(a, b):
    if a == b:
        return 0
    return 1 if 0 in (a, b) else 2


def partial_isometries(n):
    points = tuple(range(n))
    for k in range(n + 1):
        for domain in combinations(points, k):
            for image in combinations(points, k):
                for bijection in permutations(image):
                    if all(distance(domain[i], domain[j]) ==
                           distance(bijection[i], bijection[j])
                           for i in range(k) for j in range(i)):
                        out = [-1] * n
                        for x, y in zip(domain, bijection):
                            out[x] = y
                        yield tuple(out)


def nilpotency_index(f):
    n = len(f)
    max_power = 0
    for x in range(n):
        seen = set()
        y = x
        power = 0
        while f[y] != -1:
            if y in seen:
                return None
            seen.add(y)
            y = f[y]
            power += 1
        max_power = max(max_power, power)
    return max_power + 1


def partitions(m, smallest=1):
    if m == 0:
        yield ()
        return
    for a in range(smallest, m + 1):
        for suffix in partitions(m - a, a):
            yield (a,) + suffix



def compose(f, g):
    """First f, then g, with -1 for undefined."""
    return tuple(-1 if y == -1 else g[y] for y in f)


def commuting_count(maps):
    total = 0
    for i, a in enumerate(maps):
        total += 1  # a commutes with itself
        for b in maps[:i]:
            if compose(a,b) == compose(b,a):
                total += 2
    return total


def leaf_maps(nilpotents):
    return [f for f in nilpotents if f[0] == -1 and all(y != 0 for y in f)]


def correction_formula(m):
    c1 = c2 = 0
    for shape in partitions(m):
        weight = factorial(m)
        for v in Counter(shape).values():
            weight //= factorial(v)
        c = len(shape)
        a1 = shape.count(1)
        c1 += weight * c
        c2 += weight * (c*c - a1)
    return 4*c1 + 2*c2 + 2*m*m + m*(m-1), c1, c2


def verify(max_n=6):
    for n in range(1, max_n + 1):
        nilpotents = [f for f in partial_isometries(n)
                      if nilpotency_index(f) is not None]
        leaf = leaf_maps(nilpotents)
        base = commuting_count(leaf)
        full = commuting_count(nilpotents)
        delta, c1, c2 = correction_formula(n-1)
        assert full-base == delta, (n, full, base, delta)
        print('n',n,'leaf nilpotents',len(leaf),'all nilpotents',len(nilpotents),
              'commuting leaf pairs',base,'commuting star pairs',full,
              'excess',delta,'terminal sum',c1,'source-terminal distinct sum',c2)

if __name__ == "__main__":
    verify()
