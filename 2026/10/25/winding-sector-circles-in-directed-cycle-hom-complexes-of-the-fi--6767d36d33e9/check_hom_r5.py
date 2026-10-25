#!/usr/bin/env python3
"""Exact finite-cell checks for Hom(oriented C_k, R_5), k=3,...,10.

The general all-k theorem uses a separate topological proof; these tests
independently enumerate the finite regular CW complexes and their boundaries.
Only the Python standard library is required.
"""
from collections import Counter, defaultdict
from math import comb


def hom_cells(k):
    masks = (1 << 5) - 1
    out_single = [(1 << ((i + 1) % 5)) | (1 << ((i + 2) % 5)) for i in range(5)]
    out = [masks] * 32
    for a in range(1, 32):
        low = a & -a
        out[a] = out[a ^ low] & out_single[low.bit_length() - 1]
    subsets = [[] for _ in range(32)]
    for a in range(1, 32):
        b = a
        while b:
            subsets[a].append(b)
            b = (b - 1) & a
    groups = defaultdict(list)
    def visit(prefix):
        if len(prefix) == k:
            if prefix[0] & ~out[prefix[-1]]:
                return
            q = sum(a.bit_count() - 1 for a in prefix)
            groups[q].append(tuple(prefix))
            return
        for nxt in subsets[out[prefix[-1]]]:
            if len(prefix) == k - 1 and prefix[0] & ~out[nxt]:
                continue
            visit(prefix + [nxt])
    for a in range(1, 32):
        visit([a])
    return groups


def bits(a):
    return [i for i in range(5) if a & (1 << i)]


def cell_sector(c):
    k = len(c)
    flexibility = [i for i, a in enumerate(c) if a.bit_count() == 2]
    assert all(not ((i + 1) % k in flexibility) for i in flexibility)
    radii = set()
    for selections in __import__('itertools').product(*(bits(a) for a in c)):
        steps = [(selections[(i + 1) % k] - selections[i]) % 5 for i in range(k)]
        assert set(steps) <= {1, 2}
        radii.add(steps.count(2))
        for i in flexibility:
            assert steps[i - 1] != steps[i]
    assert len(radii) == 1
    return radii.pop()


def matching_count(k, q):
    if q == 0:
        return 1
    if q > k // 2:
        return 0
    return k * comb(k - q, q) // (k - q)


def boundary(groups, d):
    lower = {c: j for j, c in enumerate(groups.get(d-1, []))}
    columns = []
    for c in groups.get(d, []):
        faces = []
        parity = 0
        for i, A in enumerate(c):
            for j, v in enumerate(bits(A)):
                B = A ^ (1 << v)
                if B:
                    face = list(c)
                    face[i] = B
                    faces.append((lower[tuple(face)], (-1)**(parity + j)))
            parity += A.bit_count() - 1
        columns.append(faces)
    return columns


def rank_mod(columns, p):
    pivots = {}
    for col in columns:
        v = {i: x % p for i, x in col if x % p}
        while v:
            row = min(v)
            if row not in pivots:
                z = pow(v[row], -1, p)
                pivots[row] = {i: a*z % p for i, a in v.items()}
                break
            scalar = v[row]
            for i, a in pivots[row].items():
                z = (v.get(i, 0) - scalar*a) % p
                if z:
                    v[i] = z
                else:
                    v.pop(i, None)
    return len(pivots)


def check(k):
    groups = hom_cells(k)
    count_by_sector = Counter()
    for q, cells in groups.items():
        for c in cells:
            r = cell_sector(c)
            count_by_sector[r, q] += 1
    for r in range(k + 1):
        if (k + r) % 5:
            assert not any(rr == r for rr, q in count_by_sector)
            continue
        for q in range(k // 2 + 1):
            predicted = 5 * matching_count(k, q) * (comb(k-2*q, r-q) if 0 <= r-q <= k-2*q else 0)
            assert count_by_sector[r, q] == predicted, (k, r, q, count_by_sector[r, q], predicted)
    for p in [2, 3]:
        ranks = {d: rank_mod(boundary(groups, d), p) for d in groups if d}
        betti = {d:len(groups[d]) - ranks.get(d,0) - ranks.get(d+1,0) for d in groups}
        circles = sum((k < 5*w < 2*k) for w in range((2*k)//5+1))
        points = 10 if k % 5 == 0 else 0
        expected_b0 = circles + points
        assert betti.get(0,0) == expected_b0, (k,p,betti,expected_b0)
        assert betti.get(1,0) == circles, (k,p,betti,circles)
        assert all(v == 0 for d,v in betti.items() if d >= 2), (k,p,betti)
    return {'k':k, 'f_vector':tuple(len(groups.get(d,[])) for d in range(max(groups)+1)), 'sectors':sorted(set(r for r,q in count_by_sector)), 'circles':sum((k < 5*w < 2*k) for w in range((2*k)//5+1)), 'isolated_points':10 if k % 5 == 0 else 0}


if __name__ == '__main__':
    for k in range(3, 11):
        print(check(k))
    print('ALL_CHECKS_PASSED')
