#!/usr/bin/env python3
"""Small exact consistency census for adjacency-nullity-one graph theorem.

Requires Python 3 standard library only. Finite checks are not proofs.
"""
from fractions import Fraction
from itertools import combinations


def rank(a):
    m = [[Fraction(t) for t in row] for row in a]
    n = len(m)
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, n) if m[i][c]), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        t = m[r][c]
        m[r] = [x / t for x in m[r]]
        for i in range(n):
            if i == r or not m[i][c]:
                continue
            t = m[i][c]
            m[i] = [m[i][j] - t * m[r][j] for j in range(n)]
        r += 1
    return r


def connected(a):
    seen = {0}
    todo = [0]
    while todo:
        v = todo.pop()
        for w, b in enumerate(a[v]):
            if b and w not in seen:
                seen.add(w)
                todo.append(w)
    return len(seen) == len(a)


def bipartition(a):
    sign = {0: 0}
    todo = [0]
    while todo:
        v = todo.pop()
        for w, b in enumerate(a[v]):
            if b:
                if w in sign and sign[w] == sign[v]:
                    return None
                if w not in sign:
                    sign[w] = 1 - sign[v]
                    todo.append(w)
    return sign


def checks(a):
    n = len(a)
    twins = [(i, j) for i in range(n) for j in range(i + 1, n) if a[i] == a[j]]
    assert len(twins) <= 1, (n, twins)
    if twins:
        i, j = twins[0]
        assert not a[i][j]
        assert rank(a) == n - 1
    deg = [sum(row) for row in a]
    s = bipartition(a)
    good = len(set(deg)) == 1 or (s is not None and all(len({deg[i] for i in range(n) if s[i] == z}) == 1 for z in (0, 1)))
    return bool(twins), good


def main():
    counts = {'with_twins': 0, 'twin_free': 0, 'regular_or_biregular': 0, 'neither': 0}
    for n in range(3, 7):
        edges = list(combinations(range(n), 2))
        for mask in range(1 << len(edges)):
            a = [[0] * n for _ in range(n)]
            for k, (i, j) in enumerate(edges):
                if (mask >> k) & 1:
                    a[i][j] = a[j][i] = 1
            if not connected(a) or rank(a) != n - 1:
                continue
            twins, good = checks(a)
            counts['with_twins' if twins else 'twin_free'] += 1
            counts['regular_or_biregular' if good else 'neither'] += 1
    # The diamond is K4 minus the {2,3} edge; its rank is three,
    # it has exactly one false-twin pair, and it is not regular.
    diamond = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 0]]
    assert rank(diamond) == 3 and checks(diamond) == (True, False)
    path5 = [[int(abs(i - j) == 1) for j in range(5)] for i in range(5)]
    assert rank(path5) == 4 and checks(path5) == (False, False)
    # K1,3 has adjacency-nullity two, outside the theorem's scope.
    star = [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
    assert rank(star) == 2
    print('VERIFY_OK', counts)


if __name__ == '__main__':
    main()
