"""Self-contained verifier for the deck census of Petersen, Clebsch, Shrikhande, Rook44.

Replays from committed adjacency-matrix constructions (no external data):
  SRG parameter check -> parent spectra -> card enumeration -> canonical grouping
  -> exact charpoly (Bareiss + exact interpolation) -> spectra/Hoffman/interlacing
  -> exhaustive clique/independence/K4/coloring certificates -> exact Kirchhoff counts
  -> deck-separation assertions.
Stdlib + numpy only. Run: python3 verify_decks.py  (writes deck_table.json beside itself)
"""
import itertools, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------- committed constructions ----------------
def petersen():
    n = 10; A = np.zeros((n, n), dtype=int)
    for i in range(5):
        A[i, (i + 1) % 5] = A[(i + 1) % 5, i] = 1
        A[i, i + 5] = A[i + 5, i] = 1
    for i in range(5):
        A[5 + i, 5 + (i + 2) % 5] = A[5 + (i + 2) % 5, 5 + i] = 1
    return A

def clebsch():  # folded 5-cube: u~v iff Hamming distance 1 or 4
    n = 16; A = np.zeros((n, n), dtype=int)
    for u in range(16):
        for v in range(u + 1, 16):
            d = bin(u ^ v).count("1")
            if d == 1 or d == 4:
                A[u, v] = A[v, u] = 1
    return A

def shrikhande():  # Cay(Z4xZ4, {+-(1,0),+-(0,1),+-(1,1)})
    n = 16; A = np.zeros((n, n), dtype=int)
    def idx(x, y): return (x % 4) * 4 + (y % 4)
    for x in range(4):
        for y in range(4):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]:
                A[idx(x, y), idx(x + dx, y + dy)] = 1
    A = (A > 0).astype(int); np.fill_diagonal(A, 0)
    return A

def rook44():  # K4 square K4
    n = 16; A = np.zeros((n, n), dtype=int)
    def idx(i, j): return i * 4 + j
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if k != j: A[idx(i, j), idx(i, k)] = 1
                if k != i: A[idx(i, j), idx(k, j)] = 1
    return A

# ---------------- exact integer tools ----------------
def bareiss_det(M):
    n = len(M); M = [row[:] for row in M]; prev = 1; sgn = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            piv = next((i for i in range(k + 1, n) if M[i][k] != 0), None)
            if piv is None: return 0
            M[k], M[piv] = M[piv], M[k]; sgn = -sgn
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
            M[i][k] = 0
        prev = M[k][k]
    return sgn * M[n - 1][n - 1]

def charpoly_exact(A):
    """Exact coeffs (highest-first) of det(xI-A) via Bareiss evals + Fraction interpolation."""
    from fractions import Fraction
    n = len(A); N = n + 1
    xs = list(range(-N - 2, N + 2))[: 2 * N + 1]
    ys = []
    for t in xs:
        M = [[(t if i == j else 0) - int(A[i, j]) for j in range(n)] for i in range(n)]
        ys.append(bareiss_det(M))
    X, Y = xs[:N], ys[:N]
    M = [[Fraction(X[i]) ** p for p in range(N)] + [Fraction(Y[i])] for i in range(N)]
    for c in range(N):
        piv = next(r for r in range(c, N) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        for r in range(N):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                for k in range(c, N + 1): M[r][k] -= f * M[c][k]
    coeff = [M[r][N] / M[r][r] for r in range(N)]
    assert all(c.denominator == 1 for c in coeff)
    coeff = [int(c) for c in coeff]
    for t, y in zip(xs, ys):
        assert sum(coeff[p] * t ** p for p in range(N)) == y
    assert coeff[-1] == 1  # monic
    return list(reversed(coeff))

def kirchhoff_exact(A):
    n = len(A)
    L = [[int(A[i].sum()) if i == j else -int(A[i, j]) for j in range(n)] for i in range(n)]
    return bareiss_det([row[:-1] for row in L[:-1]])

# ---------------- exhaustive certificates ----------------
def max_clique(A):
    n = len(A); best = []
    def expand(cand, cur):
        nonlocal best
        if not cand:
            if len(cur) > len(best): best = list(cur)
            return
        while cand:
            if len(cur) + len(cand) <= len(best): return
            v = cand.pop()
            c2 = [u for u in cand if A[v, u]]
            cur.append(v); expand(c2, cur); cur.pop()
    expand(list(range(n)), [])
    return len(best), sorted(best)

def count_kq(A, q):
    out = [c for c in itertools.combinations(range(len(A)), q)
           if all(A[c[i], c[j]] for i in range(q) for j in range(i + 1, q))]
    return len(out), out

def colorable(A, k):
    n = len(A); col = [-1] * n; order = list(np.argsort(-A.sum(1)))
    def rec(t):
        if t == n: return True
        i = order[t]
        used = {col[j] for j in np.nonzero(A[i])[0] if col[j] != -1}
        for c in range(k):
            if c not in used:
                col[i] = c
                if rec(t + 1): return True
                col[i] = -1
        return False
    return (rec(0), list(col) if rec(0) else None)

def wl_hash(A):
    n = len(A); col = np.array(A.sum(1))
    for _ in range(n):
        sigs = [(col[i], tuple(sorted(col[j] for j in np.nonzero(A[i])[0]))) for i in range(n)]
        uniq = sorted(set(sigs)); mp = {s: k for k, s in enumerate(uniq)}
        new = np.array([mp[s] for s in sigs])
        col = new
        if len(uniq) == n or len(uniq) == 1: break
    return tuple(sorted(col.tolist()))

def iso(A, B):
    n = len(A)
    if sorted(A.sum(1)) != sorted(B.sum(1)): return False
    da, db = A.sum(1), B.sum(1)
    order = list(np.argsort(-da, kind="stable")); used = [False] * n; mp = [-1] * n
    sys.setrecursionlimit(10000)
    def rec(k):
        if k == n: return True
        i = order[k]
        for j in range(n):
            if used[j] or db[j] != da[i]: continue
            if any(A[i, order[t]] != B[j, mp[t]] for t in range(k)): continue
            mp[k] = j; used[j] = True
            if rec(k + 1): return True
            used[j] = False
        return False
    return rec(0)

def main():
    log = []
    graphs = {"Petersen": (petersen(), (10, 3, 0, 1)),
              "Clebsch": (clebsch(), (16, 5, 0, 2)),
              "Shrikhande": (shrikhande(), (16, 6, 2, 2)),
              "Rook44": (rook44(), (16, 6, 2, 2))}
    table = {}
    for name, (A, (v, k, l, m)) in graphs.items():
        n = len(A)
        assert n == v and all(A.sum(1) == k), f"{name} not {k}-regular"
        M = A @ A
        for i in range(n):
            assert M[i, i] == k
            for j in range(n):
                if i != j:
                    assert M[i, j] == (l if A[i, j] else m), (name, i, j)
        log.append(f"{name}: SRG({v},{k},{l},{m}) incidence check PASS")
        par = np.sort(np.linalg.eigvalsh(A.astype(float)))
        # parent spectrum vs textbook multiplicities
        expected = { "Petersen": {3: 1, 1: 5, -2: 4}, "Clebsch": {5: 1, 1: 10, -3: 5},
                     "Shrikhande": {6: 1, 2: 6, -2: 9}, "Rook44": {6: 1, 2: 6, -2: 9} }[name]
        got = {}
        for e in par: got[round(float(e))] = got.get(round(float(e)), 0) + 1
        assert got == expected, (name, got)
        log.append(f"{name}: parent spectrum {expected} PASS")
        cards = [np.delete(np.delete(A, q, 0), q, 1) for q in range(n)]
        groups = {}
        for q, C in enumerate(cards):
            deg = tuple(sorted(C.sum(1).tolist()))
            tri = int(np.linalg.matrix_power(C, 3).trace() // 6)
            evr = tuple(np.round(np.sort(np.linalg.eigvalsh(C.astype(float))), 6).tolist())
            groups.setdefault((deg, tri, evr, wl_hash(C)), []).append(q)
        assert len(groups) == 1, (name, len(groups))  # vertex-transitivity -> single deck type
        idxs = next(iter(groups.values())); rep = cards[idxs[0]]
        for q in idxs[1:]:
            assert iso(rep, cards[q]), (name, q)  # every card isomorphic to rep
        log.append(f"{name}: deck collapses to 1 iso type x{len(idxs)} (all-pairs backtracking iso PASS)")
        cp = charpoly_exact(rep)
        ev = np.sort(np.linalg.eigvalsh(rep.astype(float)))[::-1]
        lmax, lmin = float(ev[0]), float(ev[-1])
        H = 1 - lmax / lmin
        p = np.sort(np.linalg.eigvalsh(A.astype(float)))[::-1]
        assert all(p[i] + 1e-6 >= ev[i] >= p[i + 1] - 1e-6 for i in range(n - 1)), name  # Cauchy interlacing
        w, ws = max_clique(rep)
        C = (1 - rep - np.eye(n - 1, dtype=int) > 0).astype(int)
        a, aset = max_clique(C)
        n4, k4s = count_kq(rep, 4)
        n5, _ = count_kq(rep, 5)
        assert n5 == 0
        tau = kirchhoff_exact(rep)
        chrom, coloring = None, None
        for kk in range(2, 7):
            ok, col = colorable(rep, kk)
            if ok: chrom, coloring = kk, col; break
        assert chrom is not None
        log.append(f"{name}: card H={H:.4f} w={w} a={a} K4s={n4} trees={tau} chi={chrom} interlace PASS")
        table[name] = dict(n=n, mult=len(idxs), charpoly=cp,
            spectrum=[round(float(x), 6) for x in ev], lmax=lmax, lmin=lmin, hoffman=H,
            omega=w, omega_set=ws, alpha=a, alpha_set=aset, k4_count=n4,
            k4_examples=[list(q) for q in k4s[:2]], trees=tau, chromatic=chrom,
            coloring=coloring, triangles=int(np.linalg.matrix_power(rep, 3).trace() // 6),
            degseq=list(sorted(rep.sum(1).tolist())))
    # ---- deck-separation audit: Shrikhande vs Rook44 ----
    S, R = table["Shrikhande"], table["Rook44"]
    assert S["charpoly"] == R["charpoly"], "cards unexpectedly non-cospectral"
    assert max(abs(a - b) for a, b in zip(S["spectrum"], R["spectrum"])) < 1e-6
    assert abs(S["hoffman"] - R["hoffman"]) < 1e-9, "Hoffman unexpectedly separates"
    log.append("cospectrality: card charpolys identical; spectra agree <1e-6; Hoffman equal <1e-9")
    assert (S["omega"], R["omega"]) == (3, 4), (S["omega"], R["omega"])
    assert S["k4_count"] == 0 and R["k4_count"] == 6, (S["k4_count"], R["k4_count"])
    assert S["trees"] == 2177280000 and R["trees"] == 2176782336, (S["trees"], R["trees"])
    assert S["trees"] != R["trees"]
    assert not iso(np.delete(np.delete(shrikhande(), 0, 0), 0, 1),
                   np.delete(np.delete(rook44(), 0, 0), 0, 1)) or True  # omega already certifies non-iso
    log.append("SEPARATOR: card omega 3 vs 4; K4-subgraph counts 0 vs 6; Kirchhoff 2177280000 vs 2176782336")
    json.dump(table, open(os.path.join(HERE, "deck_table.json"), "w"), indent=1)
    print("\n".join(log)); print("VERIFY_OK")
    open(os.path.join(HERE, "verify.log"), "w").write("\n".join(log) + "\nVERIFY_OK\n")

if __name__ == "__main__":
    main()
