#!/usr/bin/env python3
"""Check cycle strong-discrete-Morse face enumeration (Python standard library)."""
from collections import Counter
from itertools import permutations, product


def poly_add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return c


def poly_multiply(a, b):
    if not a or not b:
        return []
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return c


def matmul(a, b):
    d = len(a)
    out = [[[] for _ in range(d)] for _ in range(d)]
    for i in range(d):
        for j in range(d):
            out[i][j] = poly_multiply(a[i][0], b[0][j])
            for k in range(1, d):
                out[i][j] = poly_add(out[i][j], poly_multiply(a[i][k], b[k][j]))
    return out


def matrix_power(m, n):
    d = len(m)
    ans = [[[1] if i == j else [] for j in range(d)] for i in range(d)]
    while n:
        if n & 1:
            ans = matmul(ans, m)
        m = matmul(m, m)
        n >>= 1
    return ans


def face_coefficients(n):
    assert n >= 3
    t = [[[1], [0, 1], [0, 1]],
         [[1], [0, 1], []],
         [[1], [], [0, 1]]]
    u = [[[], [0, 1]], [[1], [0, 1]]]
    tn, un = matrix_power(t, n), matrix_power(u, n)
    a = [0]
    for i in range(3):
        a = poly_add(a, tn[i][i])
    b = [0]
    for i in range(2):
        b = poly_add(b, un[i][i])
    a = poly_add(a, [-2 * k for k in b])
    while a and a[-1] == 0:
        a.pop()
    return a


def faces_from_orders(n):
    """Generate subsets of strong matchings from every vertex filtration."""
    out = set()
    for order in permutations(range(n)):
        rank = [0] * n
        for t, i in enumerate(order):
            rank[i] = t
        marks = []
        for i in range(n):
            left, right = (i - 1) % n, (i + 1) % n
            if rank[left] < rank[i] < rank[right]:
                marks.append((i, 1))
            elif rank[right] < rank[i] < rank[left]:
                marks.append((i, 2))
        for mask in range(1 << len(marks)):
            out.add(frozenset(marks[j] for j in range(len(marks)) if mask & (1 << j)))
    return out


def faces_from_local_rules(n):
    out = set()
    for labels in product((0, 1, 2), repeat=n):
        if any(labels[i] and labels[(i + 1) % n] and
               labels[i] != labels[(i + 1) % n] for i in range(n)):
            continue
        used_colors = set(labels) - {0}
        all_edges_covered = all(labels[i] or labels[(i + 1) % n]
                                for i in range(n))
        if len(used_colors) == 1 and all_edges_covered:
            continue
        out.add(frozenset((i, labels[i]) for i in range(n) if labels[i]))
    return out


def reduced_euler(coefficients):
    return -sum((-1) ** j * a for j, a in enumerate(coefficients))


def euler_from_residue(n):
    # Exact root-of-unity trace values, with no floating-point arithmetic.
    t = ((2, 0, -2, 0)[n % 4])
    u = ((2, -1, -1)[n % 3])
    return -((-1) ** n) - t + 2 * u


def run():
    for n in range(3, 9):
        order_faces = faces_from_orders(n)
        local_faces = faces_from_local_rules(n)
        assert order_faces == local_faces, f'filtration/local mismatch n={n}'
        counts = Counter(len(face) for face in order_faces)
        coeff = face_coefficients(n)
        assert [counts[j] for j in range(len(coeff))] == coeff, f'trace mismatch n={n}'
        assert len(coeff) == n - 1 and coeff[-1] == n * (n - 1)
        assert reduced_euler(coeff) == euler_from_residue(n)
        print(f'n={n}, coefficients={coeff}, all_faces={len(order_faces)}')
    for n in list(range(9, 23)) + [24, 30, 50, 100]:
        f = face_coefficients(n)
        assert f[0] == 1 and len(f) == n - 1 and f[-1] == n * (n - 1)
        assert reduced_euler(f) == euler_from_residue(n)
        if n in (12, 22, 24, 50, 100):
            print(f'n={n}, nonempty_faces={sum(f) - 1}, reduced_euler={reduced_euler(f)}')
    assert sum(face_coefficients(22)) - 1 == 263593440
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    run()
