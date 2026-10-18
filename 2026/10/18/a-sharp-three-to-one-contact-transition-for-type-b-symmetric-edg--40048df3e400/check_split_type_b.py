"""Exact standalone checks for Euclidean contact formulas of type-B split-graph polytopes.

Run with: python3 check_split_type_b.py
Uses only the standard library. Finite enumeration does not replace the proof.
"""
from fractions import Fraction as F
from itertools import combinations, product


def edges(p, q):
    return list(combinations(range(p), 2)) + [
        (i, p + j) for i in range(p) for j in range(q)
    ]


def inequalities(p, q):
    n = p + q
    rows = []
    for i in range(n):
        v = [0] * n
        v[i] = -1
        rows.append((v, 0))
        v = [0] * n
        v[i] = 1
        rows.append((v, 1))
    for i, j in edges(p, q):
        v = [0] * n
        v[i] = v[j] = 1
        rows.append((v, 1))
    return rows


def solve(rows, n):
    A = [[F(z) for z in v] + [F(b)] for v, b in rows]
    for col in range(n):
        pivot = next((r for r in range(col, n) if A[r][col]), None)
        if pivot is None:
            return None
        A[col], A[pivot] = A[pivot], A[col]
        d = A[col][col]
        A[col] = [z / d for z in A[col]]
        for r in range(n):
            if r != col:
                mult = A[r][col]
                if mult:
                    A[r] = [a - mult * b for a, b in zip(A[r], A[col])]
    return tuple(A[i][-1] for i in range(n))


def enumerate_vertices(p, q):
    n = p + q
    rows = inequalities(p, q)
    vertices = set()
    for ids in combinations(range(len(rows)), n):
        v = solve([rows[i] for i in ids], n)
        if v is None:
            continue
        if all(sum(a * z for a, z in zip(normal, v)) <= bound
               for normal, bound in rows):
            vertices.add(v)
    return vertices


def predicted_maximizers(p, q):
    n = p + q
    target = max(F(q), F(n, 4))
    candidates = set()
    if F(q) == target:
        candidates.add((F(0),) * p + (F(1),) * q)
    if F(n, 4) == target:
        candidates.add((F(1, 2),) * n)
    return target, candidates


def check_finite_vertices():
    tested = [(2, 2), (2, 3), (3, 2), (3, 1)]
    total = 0
    for p, q in tested:
        verts = enumerate_vertices(p, q)
        assert verts
        scores = {v: sum(z * z for z in v) for v in verts}
        maximum = max(scores.values())
        optimizers = {v for v in verts if scores[v] == maximum}
        target, expected = predicted_maximizers(p, q)
        assert maximum == target, (p, q, maximum, target)
        # q=1, p=3 has other singleton maximizers; the theorem is for q>=2.
        if q >= 2:
            assert optimizers == expected, (p, q, optimizers, expected)
        total += len(verts)
        print('p=%d q=%d: orthant polar vertices=%d, squared extremal norm=%s, optimal magnitude vectors=%d' %
              (p, q, len(verts), maximum, len(optimizers)))
    print('Exact small-dimensional polar vertices checked:', total)


def check_witnesses():
    count = 0
    for p in range(2, 22):
        for q in range(2, 12):
            n = p + q
            B = inequalities(p, q)
            val, examples = predicted_maximizers(p, q)
            for v in examples:
                assert sum(z * z for z in v) == val
                assert all(sum(a * z for a, z in zip(normal, v)) <= bound
                           for normal, bound in B)
                count += 1
            assert val in (F(q), F(n, 4))
            if p < 3 * q:
                assert val == q
            elif p > 3 * q:
                assert val == F(n, 4)
            else:
                assert val == q == F(n, 4)
    print('Exact feasible extremal witnesses checked:', count,
          'across', 20 * 10, 'profiles')


def check_outer_sphere():
    # Distinct signed edges lie on the squared-radius-two sphere.
    total = 0
    for p in range(2, 10):
        for q in range(2, 7):
            n = p + q
            seen = set()
            for i, j in edges(p, q):
                for s, t in product((-1, 1), repeat=2):
                    v = [0] * n
                    v[i], v[j] = s, t
                    v = tuple(v)
                    assert sum(z * z for z in v) == 2
                    seen.add(v)
            assert len(seen) == 4 * (p * (p - 1) // 2 + p * q)
            total += len(seen)
    print('Distinct outer-sphere graph-root contacts checked:', total)


if __name__ == '__main__':
    check_finite_vertices()
    check_witnesses()
    check_outer_sphere()
    print('All checks passed. Analytical proof is required for arbitrary dimensions.')
