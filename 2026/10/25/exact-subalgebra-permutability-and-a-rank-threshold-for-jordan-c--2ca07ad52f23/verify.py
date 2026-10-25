"""Finite-field tests for subalgebra permutability of Jordan-chain Lie algebras.

Run: python3 verify.py
All tests use explicit subspace enumeration and Lie brackets; the
unbounded mathematical statements require the separate written proof.
"""
from itertools import combinations, product
from math import prod


def reduced_rowspace(rows, p, n):
    a = [list(x) for x in rows if any(x)]
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, len(a)) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[pivot], a[rank] = a[rank], a[pivot]
        t = pow(a[rank][col], -1, p)
        a[rank] = [(t * u) % p for u in a[rank]]
        for i in range(len(a)):
            if i != rank:
                t = a[i][col]
                a[i] = [(u - t * v) % p for u, v in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return tuple(tuple(x) for x in a[:rank])


def subspaces(n, p):
    spaces = []
    for rank in range(n + 1):
        for pivots in combinations(range(n), rank):
            free = [(i, j) for i, c in enumerate(pivots)
                    for j in range(c + 1, n) if j not in pivots]
            for vals in product(range(p), repeat=len(free)):
                a = [[0] * n for _ in range(rank)]
                for i, c in enumerate(pivots):
                    a[i][c] = 1
                for (i, j), value in zip(free, vals):
                    a[i][j] = value
                spaces.append(tuple(tuple(x) for x in a))
    assert len(spaces) == len(set(spaces))
    return spaces


def bracket(x, y, p, r, scalar):
    # h is coordinate zero; J(e_i) = e_{i-1}, with J(e_1) = 0.
    z = [0] * (r + 1)
    for i in range(1, r + 1):
        t = x[0] * y[i] - y[0] * x[i]
        z[i] = (z[i] + scalar * t) % p
        if i > 1:
            z[i - 1] = (z[i - 1] + t) % p
    return tuple(z)


def in_span(v, rows, p):
    v = list(v)
    for row in rows:
        col = next(i for i, x in enumerate(row) if x)
        scale = v[col]
        v = [(u - scale * x) % p for u, x in zip(v, row)]
    return not any(v)


def direct_census(r, p, scalar):
    n = r + 1
    spaces = subspaces(n, p)
    subs = [a for a in spaces
            if all(in_span(bracket(x, y, p, r, scalar), a, p)
                   for x, y in combinations(a, 2))]
    permutable = set()
    for i, a in enumerate(subs):
        for j, b in enumerate(subs):
            joined = reduced_rowspace(a + b, p, n)
            if all(in_span(bracket(x, y, p, r, scalar), joined, p)
                   for x in a for y in b):
                permutable.add((i, j))
    return len(spaces), tuple(subs), permutable


def gaussian(n, k, q):
    numerator = prod(q ** (n - i) - 1 for i in range(k))
    denominator = prod(q ** (k - i) - 1 for i in range(k))
    return numerator // denominator


def predicted_counts(r, q):
    t = sum(gaussian(r, k, q) for k in range(r + 1))
    s = sum(q ** j for j in range(r + 1))
    h = [sum(gaussian(j, k, q) * q ** ((ell - j) * (j - k))
             for ell in range(j, r + 1) for k in range(j + 1))
         for j in range(r + 1)]
    mixed = sum(q ** (r - j) * h[j] for j in range(r + 1))
    both_outside = (sum((2 * ell - 1) * q ** (ell + 1)
                        for ell in range(1, r + 1)) + 2 * s - 1)
    return t + s, t * t + 2 * mixed + both_outside


def verify():
    for r, p in [(1, 2), (2, 2), (2, 3), (2, 5),
                 (3, 2), (3, 3), (4, 2)]:
        nspaces, subs, good = direct_census(r, p, 1)
        n, g = predicted_counts(r, p)
        assert len(subs) == n and len(good) == g, (r, p, n, g)
        print(f'r={r}, q={p}: linear_spaces={nspaces}, '
              f'Lie_subalgebras={n}, ordered_permutable_pairs={g}')
        # Changing the scalar part of the operator must leave both
        # the subalgebra set and the permutability relation unchanged.
        if (r, p) in [(2, 2), (2, 3), (3, 2), (3, 3)]:
            for scalar in range(p):
                _, other_subs, other_good = direct_census(r, p, scalar)
                assert other_subs == subs
                assert other_good == good
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
