"""Lane 434: exact rank-4 Haemers fitting matrices for C7 over GF(2), GF(3).
Stdlib only. Prints VERIFY_OK iff: each M fits C7 (diag 1, zero on nonedges),
and rank(M)==4 by explicit elimination with logged pivots.
"""
def rank_cert(M, p):
    A = [r[:] for r in M]
    n = len(A)
    r = 0
    pivs = []
    for c in range(n):
        piv = None
        for i in range(r, n):
            if A[i][c] % p != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c] % p, -1, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(n):
            if i != r and A[i][c] % p != 0:
                f = A[i][c] % p
                A[i] = [(a - f * b) % p for a, b in zip(A[i], A[r])]
        pivs.append(c)
        r += 1
    assert all(all(v % p == 0 for v in row) for row in A[r:])
    return r, pivs


def build(x, p):
    E = set()
    for i in range(7):
        E.add((i, (i + 1) % 7))
        E.add((i, (i - 1) % 7))
    M = [[0] * 7 for _ in range(7)]
    for i in range(7):
        M[i][i] = 1 % p
    for i in range(7):
        j = (i + 1) % 7
        M[i][j] = x[i] % p
        M[j][i] = x[i] % p
    for i in range(7):
        assert M[i][i] % p == 1
        for j in range(7):
            if i != j and (i, j) not in E:
                assert M[i][j] % p == 0, (i, j)
    return M


if __name__ == "__main__":
    cases = [
        (2, [0, 1, 0, 1, 0, 0, 1]),
        (3, [0, 2, 0, 1, 0, 0, 2]),
    ]
    for p, x in cases:
        M = build(x, p)
        r, pivs = rank_cert(M, p)
        print("GF(%d) edge-values=%s rank=%d pivots=%s" % (p, x, r, pivs))
        for row in M:
            print("   ", row)
        assert r == 4, "expected rank 4"
    print("fitting + rank-4 checks passed")
    print("VERIFY_OK")
