"""Exact finite-dimensional rank checks for cone-direction examples.

The analytic classification for all convex bodies is proved separately.
Run: python verify_cones.py (requires SymPy).
"""
from sympy import Matrix


def affine_rank(vertices):
    base = Matrix(vertices[0])
    return Matrix.hstack(*(Matrix(v) - base for v in vertices[1:])).rank()


def apex_count(vertices, dimension):
    assert affine_rank(vertices) == dimension
    return sum(affine_rank(vertices[:i] + vertices[i + 1:]) == dimension - 1
               for i in range(len(vertices)))


def examples(n, k):
    m = n - k
    vs = []
    for j in range(m):
        plus = [0] * n
        minus = [0] * n
        plus[j] = 1
        minus[j] = -1
        vs.extend((plus, minus))
    for j in range(m, n):
        e = [0] * n
        e[j] = 1
        vs.append(e)
    return vs


def simplex(n):
    return [[0] * n] + [[int(j == i) for j in range(n)] for i in range(n)]


def run():
    checks = 0
    for n in range(2, 9):
        for k in range(n - 1):
            vertices = examples(n, k)
            assert apex_count(vertices, n) == k, (n, k)
            checks += 1
        assert apex_count(simplex(n), n) == n + 1
        checks += 1
    print(f"VERIFY_OK exact_integer_rank_cases={checks}")


if __name__ == "__main__":
    run()
