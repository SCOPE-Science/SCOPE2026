"""Reproduce sharp-simplex constructions and numerical stress tests for conical frusta.

Standard library only. Numerical experiments corroborate the exact proof but
are not used to establish the universal theorem.
"""
import math
import random


def c(k):
    assert k >= 1
    return 1.0 if k == 1 else k ** (k / 2) / (k - 1) ** ((k - 1) / 2)


def candidates(d, t):
    assert d >= 2 and 0 <= t <= 1
    return [c(d + 1 - j) * c(j) * t ** (j - 1) / math.factorial(d)
            for j in range(1, d + 1)]


def determinant(M):
    n = len(M)
    A = [list(map(float, row)) for row in M]
    det = 1.0
    for j in range(n):
        p = max(range(j, n), key=lambda i: abs(A[i][j]))
        if abs(A[p][j]) < 1.e-14:
            return 0.0
        if p != j:
            A[p], A[j] = A[j], A[p]
            det = -det
        pivot = A[j][j]
        det *= pivot
        for i in range(j + 1, n):
            q = A[i][j] / pivot
            for k in range(j + 1, n):
                A[i][k] -= q * A[j][k]
            A[i][j] = 0.0
    return det


def volume(vertices):
    d = len(vertices) - 1
    A = [[vertices[i + 1][j] - vertices[0][j] for j in range(d)]
         for i in range(d)]
    return abs(determinant(A)) / math.factorial(d)


def helmert_simplex(k):
    """The vertices of a regular (k-1)-simplex of circumradius one."""
    if k == 1:
        return [[]]
    # Row j of a Helmert matrix is orthonormal and perpendicular to all-ones.
    verts = [[] for _ in range(k)]
    for j in range(1, k):
        v = 1 / math.sqrt(j * (j + 1))
        for i in range(k):
            verts[i].append(math.sqrt(k / (k - 1)) *
                            (v if i < j else (-j * v if i == j else 0)))
    return verts


def optimal_vertices(d, t, j):
    k = d + 1 - j
    low = helmert_simplex(k)
    high = helmert_simplex(j)
    return ([v + [0.0] * (j - 1) + [0.0] for v in low] +
            [[0.0] * (k - 1) + [t * z for z in v] + [1.0]
             for v in high])


def random_point(d, t, rng):
    z = rng.random()
    radius = 1 - (1 - t) * z
    v = [rng.gauss(0.0, 1.0) for _ in range(d - 1)]
    n = math.sqrt(sum(x*x for x in v))
    size = radius * rng.random() ** (1 / (d - 1))
    return [size * x / n for x in v] + [z]


def check():
    rng = random.Random(938716)
    num_random = 0
    for d in range(2, 11):
        for t in (0.0, 0.1, 0.25, 0.5, 0.6, 0.7, 0.8, 0.95, 1.0):
            score = candidates(d, t)
            m = max(score)
            for j in range(1, d + 1):
                v = volume(optimal_vertices(d, t, j))
                assert math.isclose(v, score[j - 1], rel_tol=2e-11,
                                    abs_tol=2e-12), (d, t, j, v, score[j - 1])
            if d <= 6:
                for _ in range(120):
                    test = [random_point(d, t, rng) for _ in range(d + 1)]
                    assert volume(test) <= m * (1 + 2e-11)
                    num_random += 1
        # Each dimension has strictly ordered transitions inside (0,1).
        thresholds = [c(d + 1 - j) * c(j) /
                      (c(d - j) * c(j + 1))
                      for j in range(1, (d - 1) // 2 + 1)]
        assert all(0 < s < 1 for s in thresholds)
        assert all(x < y for x, y in zip(thresholds, thresholds[1:]))
        # At a threshold precisely the two adjacent layer splits tie.
        for j, t in enumerate(thresholds, 1):
            scores = candidates(d, t)
            assert math.isclose(scores[j - 1], scores[j], rel_tol=3e-13)
            assert max(scores) <= scores[j - 1] * (1 + 2e-12)
    assert math.isclose(c(3) / (c(2) * c(2)),
                        3 * math.sqrt(3) / 8, rel_tol=1e-14)
    assert math.isclose(c(4) / (c(3) * c(2)), 16 / 27, rel_tol=1e-14)
    # Check discrete high-dimensional limit away from an infinite threshold.
    t = 0.7
    assert all(max(range(1, d + 1), key=lambda j: candidates(d, t)[j-1]) == 2
               for d in (25, 40, 70))
    print('PASS: 486 constructed layer configurations,', num_random,
          'random contained simplices, 9 dimension phase lists, and'
          ' high-dimensional consistency checks.')


if __name__ == '__main__':
    check()
