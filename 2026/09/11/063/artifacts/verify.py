"""Independent verifier for the m2(9) adjoint-H2 ledger (stdlib only).

Rebuilds the structure constants, the Chevalley-Eilenberg matrices
d1: C^1 -> C^2 (324 x 81) and d2: C^2 -> C^3 (756 x 324), checks d2*d1 = 0,
computes exact rational ranks per N-homogeneous weight block, extracts
17 quotient representatives, and checks the distinguished non-coboundary
certificate. Prints VERIFY_OK on success.
"""
from fractions import Fraction

N = 9
# --- structure constants of m2(9), 0-indexed: e0..e8 ---
C = [[[0] * N for _ in range(N)] for _ in range(N)]


def set_br(i, j, k, v=1):
    C[i][j][k] += v
    C[j][i][k] -= v


for j in range(1, 8):
    set_br(0, j, j + 1)  # [x1,xi] = x_{i+1}
for k in range(2, 7):
    set_br(1, k, k + 2)  # [x2,xj] = x_{j+2}

PAIRS = [(i, j) for i in range(N) for j in range(i + 1, N)]
TRIPLES = [(i, j, k) for i in range(N) for j in range(i + 1, N)
           for k in range(j + 1, N)]
PIdx = {p: t for t, p in enumerate(PAIRS)}
TIdx = {t: i for i, t in enumerate(TRIPLES)}
W = list(range(1, 10))  # deg(xi) = i
C1W = [W[q] - W[p] for p in range(N) for q in range(N)]
C2W = [-W[t] + W[a] + W[b] for t in range(N) for (a, b) in PAIRS]
C3W = [-W[s] + W[i] + W[j] + W[k] for s in range(N) for (i, j, k) in TRIPLES]

R1, K1 = N * len(PAIRS), N * N          # 324 x 81
R2, K2 = N * len(TRIPLES), N * len(PAIRS)  # 756 x 324


def build_d1():
    M = [[0] * K1 for _ in range(R1)]
    for p in range(N):
        for q in range(N):
            c = p * N + q
            for (i, j) in PAIRS:
                base = PIdx[(i, j)]
                for r in range(N):
                    v = 0
                    if i == q:
                        v += C[p][j][r]
                    if j == q:
                        v += C[i][p][r]
                    if r == p:
                        v -= C[i][j][q]
                    if v:
                        M[r * len(PAIRS) + base][c] = v
    return M


def build_d2():
    Mc = [[0] * K2 for _ in range(R2)]
    for t in range(N):
        for (a, b) in PAIRS:
            cc = t * len(PAIRS) + PIdx[(a, b)]

            def E(u, v):
                return ((1 if (u == a and v == b) else 0)
                        - (1 if (u == b and v == a) else 0))
            for (i, j, k) in TRIPLES:
                ejk, eki, eij = E(j, k), E(k, i), E(i, j)
                base = TIdx[(i, j, k)]
                for s in range(N):
                    v = (ejk * C[i][t][s] + eki * C[j][t][s]
                         + eij * C[k][t][s])
                    if s == t:
                        w = 0
                        for m in range(N):
                            w += (C[i][j][m] * E(m, k)
                                  + C[j][k][m] * E(m, i)
                                  + C[k][i][m] * E(m, j))
                        v -= w
                    if v:
                        Mc[s * len(TRIPLES) + base][cc] = v
    return Mc


def fr_rank(rows):
    """Exact rank of a list of integer rows (list of lists)."""
    A = [[Fraction(x) for x in row] for row in rows]
    m = len(A)
    n = len(A[0]) if m else 0
    r = 0
    for c in range(n):
        p = -1
        for i in range(r, m):
            if A[i][c] != 0:
                p = i
                break
        if p < 0:
            continue
        A[r], A[p] = A[p], A[r]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                for j in range(c, n):
                    A[i][j] -= f * A[r][j]
        r += 1
    return r


def nullspace(rows, ncols):
    M = [[Fraction(x) for x in row] for row in rows]
    m = len(M)
    where = [-1] * ncols
    for c in range(ncols):
        p = -1
        for i in range(sum(1 for _ in range(m))):
            pass
        piv = -1
        # find pivot at/below current rank
        rk = sum(1 for w in where if w >= 0)
        for i in range(rk, m):
            if M[i][c] != 0:
                piv = i
                break
        if piv < 0:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        inv = M[rk][c]
        for j in range(c, ncols):
            M[rk][j] /= inv
        for i in range(m):
            if i != rk and M[i][c] != 0:
                f = M[i][c]
                for j in range(c, ncols):
                    M[i][j] -= f * M[rk][j]
        where[c] = rk
    free = [c for c in range(ncols) if where[c] < 0]
    basis = []
    for f in free:
        v = [Fraction(0)] * ncols
        v[f] = Fraction(1)
        for c in range(ncols):
            if where[c] >= 0:
                v[c] = -M[where[c]][f]
        basis.append(v)
    return where, basis


def in_span(v, G):
    g = len(G)
    if g == 0:
        return all(x == 0 for x in v)
    A = [[G[j][i] for j in range(g)] + [v[i]] for i in range(len(v))]
    m = len(A)
    r = 0
    for c in range(g):
        p = -1
        for i in range(r, m):
            if A[i][c] != 0:
                p = i
                break
        if p < 0:
            continue
        A[r], A[p] = A[p], A[r]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                for j in range(c, g + 1):
                    A[i][j] -= f * A[r][j]
        r += 1
    for i in range(m):
        if all(A[i][j] == 0 for j in range(g)) and A[i][g] != 0:
            return False
    return True


def main():
    # Jacobi check
    for a in range(N):
        for b in range(a + 1, N):
            for c in range(b + 1, N):
                for L in range(N):
                    s = 0
                    for m in range(N):
                        s += (C[a][b][m] * C[m][c][L]
                              + C[b][c][m] * C[m][a][L]
                              + C[c][a][m] * C[m][b][L])
                    assert s == 0, ("jacobi", a, b, c, L)
    d1 = build_d1()
    d2 = build_d2()
    assert all(abs(v) <= 1 for row in d1 for v in row)
    assert all(abs(v) <= 1 for row in d2 for v in row)
    # weight-homogeneity: no off-block nonzeros
    assert all(d1[r][c] == 0 or C2W[r] == C1W[c]
               for r in range(R1) for c in range(K1)
               if d1[r][c] != 0)
    assert all(d2[r][c] == 0 or C3W[r] == C2W[c]
               for r in range(R2) for c in range(K2)
               if d2[r][c] != 0)
    # d2*d1 = 0 via sparse columns
    d1col = []
    for c in range(K1):
        d1col.append([(r, d1[r][c]) for r in range(R1) if d1[r][c] != 0])
    d2row = []
    for r in range(R2):
        d2row.append({c: d2[r][c] for c in range(K2) if d2[r][c] != 0})
    for c in range(K1):
        col = dict(d1col[c])
        for r in range(R2):
            row = d2row[r]
            if len(row) < len(col):
                s = sum(v * col.get(k, 0) for k, v in row.items())
            else:
                s = sum(v * row.get(k, 0) for k, v in col.items())
            assert s == 0, ("d2d1", r, c)
    # exact per-weight ranks
    rk1 = rk2 = 0
    for k in sorted(set(C1W) | set(C2W) | set(C3W)):
        r1 = [i for i in range(R1) if C2W[i] == k]
        c1 = [j for j in range(K1) if C1W[j] == k]
        r2 = [i for i in range(R2) if C3W[i] == k]
        c2 = [j for j in range(K2) if C2W[j] == k]
        if r1 and c1:
            rk1 += fr_rank([[d1[i][j] for j in c1] for i in r1])
        if r2 and c2:
            rk2 += fr_rank([[d2[i][j] for j in c2] for i in r2])
    assert rk1 == 66, rk1
    assert rk2 == 241, rk2
    dimh2 = K2 - rk2 - rk1
    assert dimh2 == 17, dimh2
    # quotient representatives, counted per block
    total = 0
    for k in sorted(set(C2W)):
        rows2 = [i for i in range(R2) if C3W[i] == k]
        cols2 = [j for j in range(K2) if C2W[j] == k]
        rows1 = [i for i in range(R1) if C2W[i] == k]
        cols1 = [j for j in range(K1) if C1W[j] == k]
        B2 = [[d2[i][j] for j in cols2] for i in rows2] if rows2 else []
        _, ns = nullspace(B2, len(cols2))
        c2set = cols2
        pos = {v: t for t, v in enumerate(rows1)}
        order = [c2set.index(r) for r in rows1]
        inv = [0] * len(order)
        for t, o in enumerate(order):
            inv[o] = t
        G = []
        if cols1:
            B1 = [[d1[i][j] for j in cols1] for i in rows1]
            for j in range(len(cols1)):
                g = [Fraction(B1[i][j]) for i in range(len(rows1))]
                G.append([g[inv[t]] for t in range(len(cols2))])
        kept = 0
        for v in ns:
            assert all(sum(d2[i][cols2[t]] * v[t] for t in range(len(cols2))) == 0
                       for i in rows2), ("closed", k)
            if not in_span(v, G):
                G.append(list(v))
                kept += 1
        total += kept
    assert total == 17, total
    # distinguished cocycle phi(x1,x3) = x8, 0-indexed e8 <- (e0,e2)
    phi = [0] * K2
    phi[7 * 36 + PIdx[(0, 2)]] = 1
    assert all(sum(d2[r][c] * phi[c] for c in range(K2)) == 0
               for r in range(R2)), "phi not closed"
    y = [Fraction(0)] * R1
    y[253] = Fraction(-1)
    y[290] = Fraction(-1)
    y[296] = Fraction(1)
    assert all(sum(y[i] * d1[i][j] for i in range(R1)) == 0
               for j in range(K1)), "y not a left null vector"
    assert sum(y[i] * phi[i] for i in range(R1)) == -1, "pairing"
    print("rank(d1)=66 rank(d2)=241 dimH2=17 reps=17 phi-cert OK")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
