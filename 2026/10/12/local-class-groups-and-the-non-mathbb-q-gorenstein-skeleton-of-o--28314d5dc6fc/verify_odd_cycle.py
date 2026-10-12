#!/usr/bin/env python3
"""Exact finite checks of stable-set fan data for odd cycles.

Independent evidence for a symbolic theorem; not a proof for unbounded n.
No external packages are required.
"""
from collections import Counter
from math import comb


def stable_sets(n):
    ans = []
    for mask in range(1 << n):
        if any((mask >> i) & 1 and (mask >> ((i + 1) % n)) & 1
               for i in range(n)):
            continue
        ans.append(mask)
    return ans


def facets(n):
    m = (n - 1) // 2
    fs = []
    for i in range(n):
        a = [0] * n
        a[i] = 1
        fs.append((('zero', i), tuple(a), 0))
    for i in range(n):
        a = [0] * n
        a[i] = -1
        a[(i + 1) % n] = -1
        fs.append((('edge', i), tuple(a), -1))
    fs.append((('odd', None), tuple([-1] * n), -m))
    return fs


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def active_facets(fs, n, mask):
    a = [(mask >> i) & 1 for i in range(n)]
    return {label for label, normal, minimum in fs if dot(normal, a) == minimum}


def det_bareiss(rows):
    a = [list(r) for r in rows]
    n = len(a)
    sign, divisor = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((i for i in range(k+1, n) if a[i][k]), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                t = a[i][j] * pivot - a[i][k] * a[k][j]
                assert t % divisor == 0
                a[i][j] = t // divisor
        for i in range(k+1, n):
            a[i][k] = 0
        divisor = pivot
    return sign * a[n-1][n-1]


def local_basis(n, mask):
    rows = []
    for t in range(n):
        if not mask & (1 << t):
            a = [0] * n
            a[t] = 1
            rows.append(a)
    for s in range(n):
        if mask & (1 << s):
            a = [0] * n
            a[s], a[(s+1) % n] = -1, -1
            rows.append(a)
    assert len(rows) == n
    return rows


def verify(n):
    assert n % 2 == 1 and n >= 5
    m = (n-1)//2
    fs = facets(n)
    masks = stable_sets(n)
    classes = Counter()
    for S in masks:
        k = S.bit_count()
        assert k <= m
        active = active_facets(fs, n, S)
        predicted = {('zero',t) for t in range(n) if not S & (1<<t)}
        predicted.update(('edge',t) for t in range(n)
                         if (S & (1<<t)) or (S & (1<<((t+1)%n))))
        if k == m:
            predicted.add(('odd',None))
        assert active == predicted, (n,S,'active facet mismatch')
        assert abs(det_bareiss(local_basis(n,S))) == 1
        assert len(active) - n == k + (k == m)
        h = [(-2 if S & (1<<i) else 1) for i in range(n)]
        for label, normal, minimum in fs:
            if label in active:
                actual = dot(normal,h)
                if label[0] == 'odd':
                    assert actual == m - 1
                else:
                    assert actual == 1
        classes[k + (k == m)] += 1
    expected = Counter()
    for k in range(m+1):
        expected[k + (k == m)] = 1 if k == 0 else n * comb(n-k-1,k-1) // k
        if k:
            assert n * comb(n-k-1,k-1) % k == 0
    assert classes == expected, (n, classes, expected)
    for i in range(n):
        max_not_i = [S for S in masks if S.bit_count() == m and not S & (1<<i)]
        assert len(max_not_i) == m+1
        common = set.intersection(*(active_facets(fs, n, S) for S in max_not_i))
        expected_common = {('zero',i), ('odd', None)}
        expected_common.update(('edge',(i+2*j+1)%n) for j in range(m))
        assert common == expected_common, (n,i,common,expected_common)
        # Normals e_i and -(e_{i+2j+1}+e_{i+2j+2}) form a primitive basis
        # of the (m+1)-dimensional face normal lattice.
        a = [0]*n
        a[i] = 1
        normals = [a]
        for j in range(m):
            b = [0]*n
            b[(i+2*j+1)%n] = -1
            b[(i+2*j+2)%n] = -1
            normals.append(b)
        selected_columns = [i] + [(i+2*j+1)%n for j in range(m)]
        minor = [[row[col] for col in selected_columns] for row in normals]
        assert abs(det_bareiss(minor)) == 1
        # The unique circuit among the rays is w = sum_j v_j - e_i.
        odd = tuple([-1]*n)
        right = [sum(normals[j][t] for j in range(1,m+1))-normals[0][t]
                 for t in range(n)]
        assert tuple(right) == odd
        for delta in range(1,n):
            j = (i+delta)%n
            count = sum(not (S & (1<<j)) for S in max_not_i)
            expected_count = ((delta+1)//2 if delta%2 else m-delta//2+1)
            assert count == expected_count
    print(f'n={n}: {len(masks)} torus-fixed points; '
          f'class-group ranks {dict(sorted(classes.items()))}; '
          f'{n} projective-{m}-space toric face candidates; '
          f'generic primitive canonical coefficient {m-2}; '
          f'all pairwise face intersections checked')


if __name__ == '__main__':
    for n in (5,7,9,11,13,15):
        verify(n)
    print('ALL EXACT FINITE CHECKS PASS; this does not prove the unbounded theorem.')
