"""Standalone exhaustive check of outer-independent double Roman weight enumerators.

Run with Python 3.9 or newer, without third-party libraries.
"""
from collections import Counter
from itertools import product


def times(a, b):
    c = Counter()
    for i, x in a.items():
        for j, y in b.items():
            c[i+j] += x*y
    return c


def power_base(m):
    a = Counter({0: 1})
    for _ in range(m):
        a = times(a, Counter({1:1, 2:1, 3:1}))
    return a


def formula(sizes):
    out = Counter()
    for hub in range(4):
        term = Counter({hub: 1})
        for m in sizes:
            base = power_base(m)
            less = power_base(m-1)
            if hub == 0:
                blade = base - Counter({m: 1})
            elif hub == 1:
                blade = base - Counter({m: 1})
                extra = less - Counter({m-1: 1, m: m-1})
                for d, count in extra.items():
                    blade[d] += m*count
            elif hub == 2:
                blade = base.copy()
                for d, count in less.items():
                    blade[d] += m*count
                blade[m-1] -= m
            else:
                blade = base.copy()
                for d, count in less.items():
                    blade[d] += m*count
            term = times(term, blade)
        for d, count in term.items():
            out[d] += count
    return +out


def actual(sizes):
    n = 1 + sum(sizes)
    neighbors = [set(range(1, n))]
    start = 1
    for m in sizes:
        block = set(range(start, start+m))
        for vertex in range(start, start+m):
            neighbors.append(({0}|block) - {vertex})
        start += m
    assert len(neighbors) == n
    result = Counter()
    for f in product(range(4), repeat=n):
        zeros = [u for u, v in enumerate(f) if v == 0]
        if any((v in neighbors[u]) for index, u in enumerate(zeros) for v in zeros[index+1:]):
            continue
        allowed = True
        for u, value in enumerate(f):
            if value == 0 and not(any(f[v] == 3 for v in neighbors[u]) or sum(f[v] == 2 for v in neighbors[u]) >= 2):
                allowed = False; break
            if value == 1 and not any(f[v] >= 2 for v in neighbors[u]):
                allowed = False; break
        if allowed:
            result[sum(f)] += 1
    return +result


def check(sizes):
    observed = actual(sizes)
    predicted = formula(sizes)
    assert observed == predicted, (sizes, observed, predicted)
    weight = 3 + sum(m-1 for m in sizes)
    minimum_count = 1
    for m in sizes: minimum_count *= m
    assert min(observed) == weight, (sizes, min(observed), weight)
    assert observed[weight] == minimum_count, (sizes, observed[weight], minimum_count)
    near_count = 0
    for i, m in enumerate(sizes):
        prod = 1
        for j, other in enumerate(sizes):
            if i != j:
                prod *= other
        near_count += (1+m*(m-1))*prod
    if len(sizes) == 2:
        prod2 = 1
        for m in sizes:
            prod2 *= (1+m*(m-1))
        near_count += prod2 + minimum_count
    assert observed[weight+1] == near_count, (sizes,observed[weight+1],near_count)
    print('PASS', sizes, 'vertices=',1+sum(sizes),'labelings=',sum(observed.values()),'minimum=',weight,'minimum_count=',minimum_count)

if __name__ == '__main__':
    test_sizes = [(2,2),(2,3),(3,2),(3,3),(2,4),(2,2,2),(2,3,2),(3,2,2),(2,2,2,2),(2,2,3)]
    for sizes in test_sizes:
        check(sizes)
    print('ALL 10 CASES PASSED')
