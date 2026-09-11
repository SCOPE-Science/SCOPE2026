"""Exact Baker-Norine rank certification for Gamma5*, D* = v0+v1+v2.

Method (exact, stdlib only):
  q-reduced representative is UNIQUE and satisfies 0 <= E(v) <= deg(v)-1
  for v != q (burning-stage bound). Enumerate all such candidates E with
  deg(E) = deg(D), test chip-firing equivalence E ~ D (exact Fraction
  solve of the reduced Laplacian system with gauge f[q] = 0) and Dhar
  burning. Exactly one candidate passes; its q-chip decides winnability.
  |F| nonempty  <=>  q-reduced form of F is effective (any q; cross-checked
  with two basepoints).
Metric points: for each edge e, split it with a formal interior vertex p_e
  (same combinatorics for any interior position; Dhar burning is
  length-independent) and compute the p_e-reduced form on the 9-vertex model.
"""
from fractions import Fraction

BASE_EDGES = [(0, 1), (1, 2), (2, 3), (3, 0),
              (0, 4), (0, 4), (1, 5), (1, 5),
              (2, 6), (2, 6), (3, 7), (3, 7)]
N = 8
DSTAR = [1, 1, 1, 0, 0, 0, 0, 0]


def degrees(edges, n):
    d = [0] * n
    for u, v in edges:
        d[u] += 1
        d[v] += 1
    return d


def laplacian(edges, n):
    L = [[0] * n for _ in range(n)]
    for u, v in edges:
        L[u][v] -= 1
        L[v][u] -= 1
    for i in range(n):
        L[i][i] = sum(1 for (u, v) in edges if u == i or v == i)
    return L


def solve_frac(A, b):
    """Solve A x = b over Q. A: kxk list, b: len-k. Returns list or None."""
    k = len(b)
    M = [[Fraction(A[i][j]) for j in range(k)] + [Fraction(b[i])]
         for i in range(k)]
    for col in range(k):
        piv = None
        for r in range(col, k):
            if M[r][col] != 0:
                piv = r
                break
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        for r in range(k):
            if r != col and M[r][col] != 0:
                f = M[r][col] / M[col][col]
                for c in range(col, k + 1):
                    M[r][c] -= f * M[col][c]
    sol = []
    for i in range(k):
        if M[i][i] == 0:
            return None
        sol.append(M[i][k] / M[i][i])
    return sol


def equivalent(D, E, edges, n, q):
    """True iff E - D = L f for some Z-valued f (gauge f[q]=0)."""
    L = laplacian(edges, n)
    idx = [i for i in range(n) if i != q]
    Lq = [[L[i][j] for j in idx] for i in idx]
    rhs = [E[i] - D[i] for i in idx]  # want L f = E - D ... see note
    f = solve_frac(Lq, rhs)
    if f is None:
        return False, None
    if not all(x.denominator == 1 for x in f):
        return False, None
    full = [0] * n
    for k, i in enumerate(idx):
        full[i] = int(f[k])
    return True, full


def burns(E, edges, n, q):
    burnt = [False] * n
    burnt[q] = True
    while True:
        moved = False
        for v in range(n):
            if burnt[v]:
                continue
            cnt = sum(1 for (u, w) in edges
                      if (u == v and burnt[w]) or (w == v and burnt[u]))
            if E[v] < cnt:
                burnt[v] = True
                moved = True
        if not moved:
            break
    return all(burnt)


def q_reduced(D, edges, n, q):
    """Exact q-reduced representative + firing script f with D - Lf = R."""
    deg = degrees(edges, n)
    others = [i for i in range(n) if i != q]
    bounds = [list(range(deg[i])) for i in others]  # 0..deg-1
    d = sum(D)
    sols = []
    # odometer enumeration
    counter = [0] * len(others)
    while True:
        E = [0] * n
        s = 0
        for k, i in enumerate(others):
            E[i] = bounds[k][counter[k]]
            s += E[i]
        E[q] = d - s
        if burns(E, edges, n, q):
            ok, f = equivalent(D, E, edges, n, q)
            if ok:
                sols.append((E, f))
        # increment
        j = 0
        while j < len(others):
            counter[j] += 1
            if counter[j] < len(bounds[j]):
                break
            counter[j] = 0
            j += 1
        if j == len(others):
            break
    assert len(sols) == 1, "q=%s: %d reduced candidates!" % (q, len(sols))
    return sols[0]


def eff_class_nonempty(F, edges, n):
    R0, _ = q_reduced(F, edges, n, 0)
    R1, _ = q_reduced(F, edges, n, 1)
    a = all(x >= 0 for x in R0)
    b = all(x >= 0 for x in R1)
    assert a == b, "basepoint disagreement: %s vs %s" % (R0, R1)
    return a


if __name__ == "__main__":
    print("genus:", len(BASE_EDGES) - N + 1)
    print("degrees:", degrees(BASE_EDGES, N))
    print("=== vertex q-reduced forms of D* ===")
    for q in range(N):
        R, f = q_reduced(DSTAR, BASE_EDGES, N, q)
        print("q=%d R=%s R[q]=%d winnable=%s fire=%s" %
              (q, R, R[q], R[q] >= 0, f))
    print("=== edge-interior points p_e (9-vertex split models) ===")
    allok = True
    for ei, (u, v) in enumerate(BASE_EDGES):
        n2 = N + 1
        p = N
        e2 = [(a, b) for k, (a, b) in enumerate(BASE_EDGES) if k != ei]
        e2 += [(u, p), (p, v)]
        D2 = DSTAR + [0]
        R, f = q_reduced(D2, e2, n2, p)
        ok = R[p] >= 0
        allok = allok and ok
        print("edge %d (%d-%d): R=%s R[p]=%d winnable=%s" % (ei, u, v, R, R[p], ok))
    print("all edge-interior singletons winnable:", allok)
    print("=== degree-2 vertex witnesses for rank<=1 ===")
    wit = []
    for a in range(N):
        for b in range(a, N):
            E = [0] * N
            E[a] += 1
            E[b] += 1
            F = [DSTAR[i] - E[i] for i in range(N)]
            if not eff_class_nonempty(F, BASE_EDGES, N):
                wit.append((a, b))
    print("empty count:", len(wit), "examples:", wit[:10])
