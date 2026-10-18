"""Exact rational quadratic-field count of cyclic axes of three binary polyhedral groups.

Run: python verify_spinor_coefficients.py
Only standard-library modules are used. This checks finite axis incidences; the
classification of arbitrary coefficient kernels is established analytically.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product


def z(a=0, b=0):
    return (F(a), F(b))


def sub(x, y):
    return x[0] - y[0], x[1] - y[1]


def mul(x, y, d):
    return (x[0] * y[0] + d * x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def cross(a, b, d):
    return tuple(sub(mul(a[(k + 1) % 3], b[(k + 2) % 3], d),
                     mul(a[(k + 2) % 3], b[(k + 1) % 3], d)) for k in range(3))


def even(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2 == 0


def roots(which):
    d = {'T': 5, 'O': 2, 'I': 5}[which]
    zero = z()
    out = []
    for i in range(4):
        for sign in (-1, 1):
            q = [zero] * 4
            q[i] = z(sign)
            out.append(tuple(q))
    for signs in product((-1, 1), repeat=4):
        out.append(tuple(z(F(t, 2)) for t in signs))
    if which == 'O':
        for i, j in combinations(range(4), 2):
            for a, b in product((-1, 1), repeat=2):
                q = [zero] * 4
                q[i] = z(0, F(a, 2))
                q[j] = z(0, F(b, 2))
                out.append(tuple(q))
    if which == 'I':
        values = [zero, z(F(1, 2)), z(F(1, 4), F(1, 4)),
                  z(-F(1, 4), F(1, 4))]
        for p in permutations(range(4)):
            if even(p):
                for signs in product((-1, 1), repeat=3):
                    q = [values[k] for k in p]
                    it = iter(signs)
                    q = [mul(z(next(it)), v, d) if v != zero else zero for v in q]
                    out.append(tuple(q))
    assert len(out) == {'T': 24, 'O': 48, 'I': 120}[which]
    assert len(set(out)) == len(out)
    for q in out:
        square = tuple(sum(mul(v, v, d)[i] for v in q) for i in (0, 1))
        assert square == z(1)
    return out, d


def axis_census(which):
    rr, d = roots(which)
    directions = []
    for q in rr:
        v = q[1:]
        if all(t == z() for t in v):
            continue
        if not any(all(t == z() for t in cross(v, axis, d)) for axis in directions):
            directions.append(v)
    counts = Counter()
    for axis in directions:
        order = sum(all(t == z() for t in cross(q[1:], axis, d)) for q in rr)
        assert order > 2
        counts[order] += 1
    expect = {'T': Counter({4: 3, 6: 4}),
              'O': Counter({4: 6, 6: 4, 8: 3}),
              'I': Counter({4: 15, 6: 10, 10: 6})}[which]
    assert counts == expect, (which, counts)
    size = len(rr)
    cosets = sum(a * (size // order) for order, a in counts.items())
    total = 1 + size // 2 + cosets
    expected = {'T': 47, 'O': 147, 'I': 783}[which]
    assert total == expected
    print(which, 'axes:', dict(counts), 'distinct zero sets:', total,
          'projective rigid coefficient rays:', 2 * cosets)


def dic_multiply(n, x, y):
    a, b = x
    c, d = y
    return ((a + (-1) ** b * c + n * b * d) % (2 * n), (b + d) % 2)


def dic_cyclic(n, g):
    identity = (0, 0)
    acc = identity
    out = set()
    while acc not in out:
        out.add(acc)
        acc = dic_multiply(n, acc, g)
    assert acc == identity
    return frozenset(out)


def dic_census(n):
    elements = [(a, b) for a in range(2 * n) for b in (0, 1)]
    cyclic = {dic_cyclic(n, g) for g in elements}
    maximal = {c for c in cyclic if len(c) > 2 and not any(c < h for h in cyclic)}
    assert Counter(map(len, maximal)) == Counter([2 * n] + [4] * n)
    cosets = set()
    for c in maximal:
        for g in elements:
            cosets.add(frozenset(dic_multiply(n, g, h) for h in c))
    expected = 2 + n * n
    assert len(cosets) == expected
    assert 1 + (2 * n) + len(cosets) == n * n + 2 * n + 3
    print('Dic', n, 'axes:', dict(Counter(map(len, maximal))),
          'distinct zero sets:', 1 + 2 * n + len(cosets),
          'projective rigid coefficient rays:', 2 * len(cosets))


if __name__ == '__main__':
    for kind in ('T', 'O', 'I'):
        axis_census(kind)
    for degree in range(2, 13):
        dic_census(degree)
    print('PASS exact finite axis and coset certificates')
