"""Exact rational verification of complete tripartite mixing formulas.

Run: python3 verify.py
Only the Python standard library is required. These finite checks supplement,
not replace, the argument applying to every admissible pair of part sizes.
"""
from fractions import Fraction as F
from itertools import combinations


def parameters(p, q):
    assert p >= 2 and q >= 2
    k = F(2 * p, q)
    if k <= F(1, 2):
        y, mu = F(1), F(1) - k
        return k, y, mu, F(0), F(0)
    if k <= 2:
        y, mu = F(2) / (1 + 2 * k), F(1) / (1 + 2 * k)
        low = max(F(0), 1 - y - mu)
        high = min(1 - y, (1 - y + mu) / 2)
        return k, y, mu, low, high
    if k <= 4:
        y, mu = F(4) / (4 + 3 * k), k / (4 + 3 * k)
    else:
        y, mu = 1 / k, (k - 1) / (3 * k)
    x = F(2) * (1 - y) / 3
    return k, y, mu, x, x


def spectral_values(k, x, y):
    return (1 - x - y, 1 - k * y, 1 - 2 * x - y, 1 - (1 + k) * y)


def feasible(k, x, y, mu):
    if not (x >= 0 and y >= 0 and x + y <= 1 and k * y <= 1 and mu >= 0):
        return False
    return all(abs(z) <= mu for z in spectral_values(k, x, y))


def matrix_eigen_checks(p, q, x, y, mu):
    k = F(2 * p, q)
    a, b = x / p, y / q
    n = 2 * p + q
    P = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ai = 0 if i < p else (1 if i < 2 * p else 2)
            aj = 0 if j < p else (1 if j < 2 * p else 2)
            if i == j:
                P[i][j] = 1 - x - y if ai < 2 else 1 - k * y
            elif ai != aj:
                P[i][j] = a if ai < 2 and aj < 2 else b
        assert sum(P[i]) == 1
        assert all(z >= 0 for z in P[i])
    assert all(P[i][j] == P[j][i] for i in range(n) for j in range(n))
    vectors = []
    vectors.append(([F(1)] * n, F(1)))
    for base, count in ((0, p), (p, p), (2 * p, q)):
        for i in range(1, count):
            v = [F(0)] * n
            v[base] = 1
            v[base + i] = -1
            vectors.append((v, 1 - x - y if base < 2 * p else 1 - k * y))
    vectors.append(([F(1)] * p + [F(-1)] * p + [F(0)] * q, 1 - 2 * x - y))
    vectors.append(([F(q)] * (2 * p) + [F(-2 * p)] * q, 1 - (1 + k) * y))
    assert len(vectors) == n
    checks = 0
    for v, e in vectors:
        for i in range(n):
            assert sum(P[i][j] * v[j] for j in range(n)) == e * v[i]
            checks += 1
    assert max(abs(z) for z in spectral_values(k, x, y)) == mu
    return checks


def solve3(A, b):
    a = [[F(u) for u in row] + [F(v)] for row, v in zip(A, b)]
    for j in range(3):
        r = next((i for i in range(j, 3) if a[i][j]), None)
        if r is None:
            return None
        a[j], a[r] = a[r], a[j]
        t = a[j][j]
        a[j] = [v / t for v in a[j]]
        for i in range(3):
            if i != j:
                t = a[i][j]
                a[i] = [a[i][s] - t * a[j][s] for s in range(4)]
    return tuple(a[i][-1] for i in range(3))


def enumerated_linear_optimum(k):
    # Eleven inequalities A dot (X,Y,mu) <= b.
    A = ((1, 1, 0), (0, k, 0), (-1, 0, 0), (0, -1, 0),
         (0, 0, -1), (-1, -1, -1), (0, -k, -1),
         (-2, -1, -1), (2, 1, -1), (0, -1-k, -1), (0, 1+k, -1))
    b = (1, 1, 0, 0, 0, -1, -1, -1, 1, -1, 1)
    best = None
    for ids in combinations(range(len(A)), 3):
        sol = solve3([A[i] for i in ids], [b[i] for i in ids])
        if sol is not None and all(sum(F(t) * v for t, v in zip(row, sol)) <= bound for row, bound in zip(A, b)):
            if best is None or sol[2] < best:
                best = sol[2]
    assert best is not None
    return best


def run():
    tests = [(p, q) for p in range(2, 13) for q in range(2, 15)]
    tests += [(2, 50), (2, 100), (3, 17), (4, 16), (7, 2), (11, 2), (25, 4), (40, 12)]
    nmatrix, nvertices, ncases = 0, 0, 0
    for p, q in tests:
        k, y, mu, low, high = parameters(p, q)
        assert low <= high
        for x in (low, (low + high) / 2, high):
            assert feasible(k, x, y, mu)
            nmatrix += matrix_eigen_checks(p, q, x, y, mu)
            ncases += 1
        assert enumerated_linear_optimum(k) == mu
        nvertices += 1
    print(f'VERIFY_OK {ncases} exact matrix designs, {nmatrix} eigen-equation coordinates, {nvertices} independent LP vertex enumerations')

if __name__ == '__main__':
    run()
