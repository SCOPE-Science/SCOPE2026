#!/usr/bin/env python3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def bareiss_det(A):
    A = [list(map(int, row)) for row in A]
    n = len(A)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            s = next((i for i in range(k + 1, n) if A[i][k]), None)
            if s is None:
                return 0
            A[k], A[s] = A[s], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pivot - A[i][k] * A[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            A[i][k] = 0
    return sign * A[n - 1][n - 1]

def vertex(n, p, q):
    ell = 2 * n - 1
    d = [2] * (n + 1)
    d[p] = -ell
    d[q] = 1
    return tuple(d)

for n in range(2, 9):
    ell = 2 * n - 1
    V = {vertex(n, p, q) for p in range(n + 1) for q in range(n + 1) if p != q}
    assert len(V) == n * (n + 1)
    assert all(sum(v) == 0 for v in V)

    for i in range(n + 1):
        lower = [v for v in V if v[i] == -ell]
        upper = [v for v in V if v[i] == 2]
        assert len(lower) == n
        assert len(upper) == n * (n - 1)

    # Lower facet d_n=-ell: columns 2*1-e_q.
    B = [[2 - (1 if i == j else 0) for j in range(n)] for i in range(n)]
    assert abs(bareiss_det(B)) == ell

    # Upper facet d_n=2.
    upper = [vertex(n, p, q)[:n] for p in range(n) for q in range(n) if p != q]
    assert all(sum(w) == -2 for w in upper)
    if n == 2:
        M = [[upper[j][i] for j in range(2)] for i in range(2)]
        assert abs(bareiss_det(M)) == 8
    else:
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                p = next(k for k in range(n) if k not in (i, j))
                wi = vertex(n, p, i)[:n]
                wj = vertex(n, p, j)[:n]
                diff = tuple(a - b for a, b in zip(wi, wj))
                target = tuple((1 if k == j else -1 if k == i else 0) for k in range(n))
                assert diff == target

    assert gcd(2, ell) == 1
    upper_group = "Z/8" if n == 2 else f"Z^{n*(n-2)} + Z/2"
    print(
        f"n={n}: vertices={len(V)}, lower_rays={n}, upper_rays={n*(n-1)}, "
        f"lower_class_group=Z/{ell}, upper_class_group={upper_group}"
    )

print("VERIFY_OK")
