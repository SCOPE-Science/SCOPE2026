"""Exact finite-state verification of two-particle encounter laws on balanced complete multipartite graphs.

Run with: python3 meeting_checker.py
No third-party packages are required. This checks examples, not the general proof.
"""
from fractions import Fraction as F


def solve(M, b):
    n = len(b)
    A = [[F(z) for z in row] + [F(b[i])] for i, row in enumerate(M)]
    for j in range(n):
        k = next(k for k in range(j, n) if A[k][j])
        A[j], A[k] = A[k], A[j]
        inv = 1 / A[j][j]
        A[j] = [z * inv for z in A[j]]
        for k in range(n):
            if k != j:
                factor = A[k][j]
                if factor:
                    A[k] = [a - factor * b for a, b in zip(A[k], A[j])]
    return [row[-1] for row in A]


def check(r, m):
    n, deg = r * m, (r - 1) * m
    vertices = range(n)
    pairs = [(u, v) for u in vertices for v in vertices if u != v]
    index = {xy: i for i, xy in enumerate(pairs)}
    d = len(pairs)
    G = [[F(0) for _ in range(d)] for _ in range(d)]
    for (u, v), i in index.items():
        G[i][i] -= 2
        for w in vertices:
            if w // m != u // m and w != v:
                G[i][index[(w, v)]] += F(1, deg)
            if w // m != v // m and w != u:
                G[i][index[(u, w)]] += F(1, deg)
    minus_G = [[-z for z in row] for row in G]
    mu = solve(minus_G, [F(1)] * d)
    mom2 = solve(minus_G, [2 * x for x in mu])
    for (u, v), i in index.items():
        same = u // m == v // m
        pred_mu = F(n if same else n - 1, 2)
        pred_var = F(n * n - 2 * deg - (not same), 4)
        assert mu[i] == pred_mu, (r, m, u, v, mu[i], pred_mu)
        assert mom2[i] - mu[i] ** 2 == pred_var
    for s in [F(1, 3), F(1), F(5, 2)]:
        resolvent = [[minus_G[i][j] + (s if i == j else 0) for j in range(d)] for i in range(d)]
        absorb = [ -sum(G[i]) for i in range(d) ]
        transform = solve(resolvent, absorb)
        for (u, v), i in index.items():
            same = u // m == v // m
            pred = F(4 if same else 2, 1) * (F(1) if same else (s + 2)) / (deg * s * s + 2 * n * s + 4)
            assert transform[i] == pred, (r, m, u, v, s, transform[i], pred)
    return 2 * len(pairs) + 3 * len(pairs)


def main():
    tests = [(3, 1), (4, 1), (5, 1), (2, 2), (3, 2), (4, 2), (2, 3), (3, 3)]
    total = sum(check(r, m) for r, m in tests)
    print(f'PASS: {len(tests)} graph families, {total} exact rational moment/transform identities.')
    print('This finite check is corroborative, not an all-size proof.')


if __name__ == '__main__':
    main()
