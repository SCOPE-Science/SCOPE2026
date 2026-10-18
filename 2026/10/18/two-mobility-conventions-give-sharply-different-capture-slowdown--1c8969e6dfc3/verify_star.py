"""Exact rational checks for independently moving capture on finite star graphs.

Only Python's standard library is required. Each vertex-to-vertex transition
is built directly from the labeled Cartesian-product graph, not a lumped model.
"""
from fractions import Fraction as F


def solve(A, rhs):
    """Solve a square rational linear system by exact elimination."""
    A = [list(row) + [b] for row, b in zip(A, rhs)]
    n = len(A)
    for col in range(n):
        pivot = next(k for k in range(col, n) if A[k][col] != 0)
        A[col], A[pivot] = A[pivot], A[col]
        scale = A[col][col]
        for j in range(col, n + 1):
            A[col][j] /= scale
        for k in range(n):
            if k == col:
                continue
            scale = A[k][col]
            if scale:
                for j in range(col, n + 1):
                    A[k][j] -= scale * A[col][j]
    return [row[n] for row in A]


def predicted(m, a, b, mode):
    x = b / a
    denominator = (1 + x) * (1 + 2*m*x + x*x)
    if mode == "edge":
        numerator = 1 + m*(m+1)*x + m*x*x
    elif mode == "vertex":
        numerator = 1 + (4*m-2)*x + (2*m-1)*x*x
    else:
        raise ValueError(mode)
    return numerator / denominator / a


def graph_result(m, a, b, mode):
    vertices = list(range(m + 1))  # 0 = hub, 1..m = leaves
    nbr = {0: list(range(1, m+1))}
    for i in range(1, m+1):
        nbr[i] = [0]
    pairs = [(u, v) for u in vertices for v in vertices if u != v]
    idx = {p: i for i, p in enumerate(pairs)}
    n = len(pairs)
    A = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, (u, v) in enumerate(pairs):
        for w in nbr[u]:
            rate = a / (len(nbr[u]) if mode == "vertex" else 1)
            A[i][i] += rate
            if w != v:
                A[i][idx[(w, v)]] -= rate
        for w in nbr[v]:
            rate = b / (len(nbr[v]) if mode == "vertex" else 1)
            A[i][i] += rate
            if w != u:
                A[i][idx[(u, w)]] -= rate
    ans = solve(A, [F(1) for _ in range(n)])
    return ans[idx[(1,0)]], A, ans, pairs


def main():
    checks = 0
    equations = 0
    for m in range(2, 7):
        for a, b in [(F(1), F(0)), (F(1), F(1,3)),
                     (F(1), F(1)), (F(3,2), F(5,4))]:
            for mode in ("edge", "vertex"):
                actual, A, ans, pairs = graph_result(m, a, b, mode)
                wanted = predicted(m, a, b, mode)
                assert actual == wanted, (m, a, b, mode, actual, wanted)
                checks += 1
                for row, val in zip(A, [F(1)] * len(pairs)):
                    assert sum(q * t for q, t in zip(row, ans)) == val
                    equations += 1
                # Exchange of identical rates swaps the two agents.
                if a == b:
                    lookup = dict(zip(pairs, ans))
                    assert all(lookup[(u,v)] == lookup[(v,u)] for u,v in pairs)
    print(f"PASS: {checks} exact full-generator formula comparisons, "
          f"{equations} individual first-step equations")

if __name__ == "__main__":
    main()
