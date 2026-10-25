"""Exact symbolic checks for conductance-normalized wheel projections.

Requires Python 3.10+ and SymPy. Run: python wheel_verification.py
The theorem for all parameters is proved separately; these are finite tests.
"""
import sympy as sp


def verify(n, t):
    t = sp.Rational(t)
    vertices = list(range(n)) + [n]  # n is the hub
    edges = [(n, k) for k in range(n)] + [(k, (k + 1) % n) for k in range(n)]
    weights = [t] * n + [sp.Integer(1)] * n
    D = sp.zeros(n, 2 * n)  # grounded vertex-edge incidence
    for j, (a, b) in enumerate(edges):
        if a != n:
            D[a, j] -= 1
        if b != n:
            D[b, j] += 1
    W = sp.diag(*weights)
    S = sp.diag(*[sp.sqrt(w) for w in weights])
    T = D * W * D.T
    G = T.inv()
    P = S * D.T * G * D * S
    R = sp.eye(2 * n) - P
    assert P.T == P and P * P == P and R * R == R
    g = [G[k, 0] for k in range(n)]
    m = n // 2
    a = sp.simplify(1 + 2 * sp.sqrt(t) * (g[0] - g[m]))
    b = sp.simplify(2 * (1 - t * g[0]) + 2 * sp.sqrt(t) * (g[0] - g[m]))
    def col_norm(M, j):
        return sp.simplify(sum(abs(M[k, j]) for k in range(2 * n)))
    for j in range(2 * n):
        expect_P = a if j < n else b
        expect_R = b if j < n else a
        assert sp.simplify(col_norm(P, j) - expect_P) == 0, (n, t, j, 'P')
        assert sp.simplify(col_norm(R, j) - expect_R) == 0, (n, t, j, 'R')
    assert sp.simplify((b - a) - (1 - 2 * t * g[0])) == 0
    assert sp.simplify(t * sum(g) - 1) == 0
    assert g[m] == min(g)  # rational exact comparison
    return 2 * n


def verify_green_formula(n, t):
    t = sp.Rational(t)
    root = sp.sqrt(t * (t + 4))
    rho = (t + 2 - root) / 2
    d = sp.sqrt(t * (t + 4)) * (1 - rho**n)
    T = (t + 2) * sp.eye(n)
    for j in range(n):
        T[j, (j - 1) % n] -= 1
        T[j, (j + 1) % n] -= 1
    g = sp.Matrix([(rho**k + rho**(n-k)) / d for k in range(n)])
    assert all(sp.simplify(z) == 0 for z in T * g - sp.eye(n)[:, 0])


def main():
    cases = 0
    columns = 0
    for n in range(3, 12):
        for t in [sp.Rational(1, 10), sp.Rational(1, 2), 1, sp.Rational(4, 3), 2, 5, 50]:
            columns += verify(n, t)
            cases += 1
    for n in range(3, 9):
        for t in [sp.Rational(1, 2), 1, 2]:
            verify_green_formula(n, t)
    print(f'PASS: {cases} exact-rational parameter instances, {columns} edge columns, 18 radical Green checks')


if __name__ == '__main__':
    main()
