"""Independent exact-arithmetic checks for electrical projection norms on Hamming-product networks.

No third-party packages are required. Run: python verification/check_exact.py
"""
from fractions import Fraction
from itertools import product


def inverse(matrix):
    n = len(matrix)
    a = [[Fraction(v) for v in row] + [Fraction(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = next((p for p in range(k, n) if a[p][k]), None)
        assert pivot is not None, "Grounded Laplacian must be invertible"
        a[k], a[pivot] = a[pivot], a[k]
        t = a[k][k]
        a[k] = [v/t for v in a[k]]
        for i in range(n):
            if i == k:
                continue
            t = a[i][k]
            if t:
                a[i] = [x - t*y for x, y in zip(a[i], a[k])]
    return [row[n:] for row in a]


def run_case(qs, roots=None):
    if roots is None:
        roots = (1,) * len(qs)
    cs = tuple(v*v for v in roots)
    vertices = list(product(*(range(q) for q in qs)))
    vi = {v: i for i, v in enumerate(vertices)}
    edges = []
    for v in vertices:
        for j, q in enumerate(qs):
            for value in range(v[j] + 1, q):
                w = list(v)
                w[j] = value
                edges.append((vi[v], vi[tuple(w)], j))
    n = len(vertices)
    lap = [[0] * (n - 1) for _ in range(n - 1)]
    for a, b, j in edges:
        if a < n - 1:
            lap[a][a] += cs[j]
        if b < n - 1:
            lap[b][b] += cs[j]
        if a < n - 1 and b < n - 1:
            lap[a][b] -= cs[j]
            lap[b][a] -= cs[j]
    inv = inverse(lap)
    counts = 0
    predicted = []
    for i, q in enumerate(qs):
        predicted.append(2 * Fraction(q - 1, q) +
                         2 * sum((Fraction((qs[j] - 1) * roots[i] * roots[j],
                                           q * cs[i] + qs[j] * cs[j])
                                  for j in range(len(qs)) if j != i), Fraction(0)))
    for a, b, j in edges:
        rhs = [0] * (n - 1)
        if a < n - 1:
            rhs[a] += 1
        if b < n - 1:
            rhs[b] -= 1
        u = [sum(inv[i][k] * rhs[k] for k in range(n - 1))
             for i in range(n - 1)] + [Fraction(0)]
        row = [Fraction(roots[j] * roots[k]) * (u[x] - u[y])
               for x, y, k in edges]
        norm = sum(map(abs, row), Fraction(0))
        assert norm == predicted[j], (qs, roots, j, norm, predicted[j])
        extremal_signs = [1 if v >= 0 else -1 for v in row]
        assert sum((v*s for v, s in zip(row, extremal_signs)), Fraction(0)) == norm
        counts += 1
    exact_norm = max(predicted)
    if len(set(roots)) == 1:
        k = min(range(len(qs)), key=lambda i: qs[i])
        assert exact_norm == predicted[k]
        assert all(predicted[i] < exact_norm for i in range(len(qs)) if qs[i] > qs[k])
    return counts, exact_norm


def main():
    cases = [(2,), (3,), (4,), (2, 2), (2, 3), (2, 4), (3, 3),
             (2, 2, 2), (2, 2, 3), (2, 3, 3), (2, 2, 4),
             (2, 2, 2, 2), (2, 3, 2), (3, 2, 2), (3, 2, 3)]
    total_edges = 0
    for qs in cases:
        comparisons, value = run_case(qs)
        print(f"{qs}: norm={value}, exact edge rows={comparisons}")
        total_edges += comparisons
    weighted_cases = [((2, 2), (1, 2)), ((2, 3), (1, 10)),
                      ((2, 3), (3, 2)), ((2, 2, 2), (1, 2, 3)),
                      ((2, 3, 2), (1, 2, 3)), ((2, 3, 3), (2, 1, 3)),
                      ((3, 2, 2), (1, 2, 2)), ((2, 4), (3, 1)),
                      ((2, 2, 2, 2), (1, 2, 1, 2))]
    for qs, roots in weighted_cases:
        comparisons, value = run_case(qs, roots)
        print(f"{qs}, roots={roots}: norm={value}, exact edge rows={comparisons}")
        total_edges += comparisons
    print(f"PASS: {len(cases) + len(weighted_cases)} profiles; {total_edges} independent exact edge-row comparisons")


if __name__ == '__main__':
    main()
