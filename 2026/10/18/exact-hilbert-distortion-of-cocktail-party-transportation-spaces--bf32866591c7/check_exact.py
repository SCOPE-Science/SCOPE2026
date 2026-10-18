"""Reproduce exact ellipsoidal distortion calculations for matching-deleted cliques.

Python standard library only. This checker confirms finite instances;
the universal theorem requires the separate analytic proof.
"""
from fractions import Fraction as F
from collections import deque


def squared_components(y):
    k = len(y) // 2
    total = sum(y)
    # Subtracting a global constant changes neither pair differences nor U.
    u2 = sum(F((y[2*i] - y[2*i + 1]) ** 2, 2) for i in range(k))
    s = [y[2*i] + y[2*i + 1] for i in range(k)]
    w2 = (sum(F(v*v, 2) for v in s) - F(sum(s)**2, 2*k))
    return u2, w2


def cut_vertex(mask, k):
    return tuple((mask >> j) & 1 for j in range(2*k))


def special_vertices(k):
    for i in range(k):
        for sg in (1, -1):
            y = [0] * (2*k)
            y[2*i] = sg
            y[2*i+1] = -sg
            yield tuple(y)


def connected_tight(y):
    n = len(y)
    seen = {0}
    todo = deque([0])
    while todo:
        v = todo.popleft()
        for u in range(n):
            if u // 2 != v // 2 and abs(y[u] - y[v]) == 1 and u not in seen:
                seen.add(u)
                todo.append(u)
    return len(seen) == n


def alpha(k):
    return F(2, 3) if k == 2 else F(3, 5) if k == 3 else F(1, 2)


def expected(k):
    return F(3) if k == 2 else F(10, 3) if k == 3 else F(k)


def verify(k):
    a = alpha(k)
    maxval = F(0)
    count = 0
    contact = 0
    all_cuts = 0
    for m in range(1, (1 << (2*k)) - 1):
        y = cut_vertex(m, k)
        all_cuts += 1
        if not connected_tight(y):
            continue
        count += 1
        u2, w2 = squared_components(y)
        v = u2 / a + w2 / (1-a)
        if v > maxval:
            maxval = v
            contact = 1
        elif v == maxval:
            contact += 1
    for y in special_vertices(k):
        assert connected_tight(y), ('not tight special', k, y)
        count += 1
        u2, w2 = squared_components(y)
        v = u2 / a + w2 / (1-a)
        if v > maxval:
            maxval = v
            contact = 1
        elif v == maxval:
            contact += 1
    assert maxval == expected(k), (k, maxval, expected(k))
    expected_count = 6 if k == 2 else 2**(2*k) - 2 - 2*k
    assert count == expected_count, (k, count, expected_count)
    return k, count, maxval, contact


if __name__ == '__main__':
    for k in range(2, 9):
        print('k=%d: tight_vertices=%d distortion_squared=%s limiting_contacts=%d' % verify(k))
    print('EXACT_COCKTAIL_DISTORTION_CHECKS_PASS: k=2..8')
