"""Verify target obstruction at K0 (Limonchenko-Panov Thm 2 main example).

Steps:
 1. Transcribe the 15 minimal non-faces verbatim (1-indexed in paper; 0-indexed here).
 2. Define K0 by "contains no minimal non-face as subset".
 3. Assert every subset of size <=2 is a face (full 1-skeleton) since every
    minimal non-face has size >=3.
 4. Exact-Q reduced homology of every induced subcomplex K_I (512 subsets)
    via Fraction boundary-rank; aggregate Hochster H^p(Z_K0).
 5. Assert H^3(Z_K0;Q)=0 (kills nonzero degree-3 a,b,c,d).
 6. Assert every I with |I|<=2 has vanishing reduced (co)homology
    (=> every nonzero multigraded component needs |I|>=3 => no four nonzero
    pairwise-disjointly supported classes on 9 vertices).
 7. Cross-check the three published triple supports carry nonzero classes.
Repro: python3 verify_target_obstruction.py
Stdlib only.
"""
from fractions import Fraction
from itertools import combinations

N = 9
# Paper's 15 minimal non-faces, 1-indexed -> 0-indexed, sorted.
MIN_NONFACES_1 = [
    (1,2,3),(4,5,6),(7,8,9),(1,4,7),
    (1,2,4,5),(5,6,7,8),(2,3,7,8),
    (2,3,5,6,7),
    (1,2,4,6,8,9),(1,3,4,5,8,9),(1,3,5,6,7,9),
    (2,3,4,5,7,9),(2,3,4,5,8,9),(2,3,4,6,7,9),(2,3,5,6,8,9),
]
MIN_NONFACES = [frozenset(x-1 for x in t) for t in MIN_NONFACES_1]
assert len(MIN_NONFACES) == 15, len(MIN_NONFACES)
assert len(set(MIN_NONFACES)) == 15, "list must have 15 distinct items"

def is_face(s):
    fs = frozenset(s)
    for m in MIN_NONFACES:
        if m <= fs:
            return False
    return True

# --- Step 3: full 1-skeleton ---
min_size = min(len(m) for m in MIN_NONFACES)
print("minimal non-face sizes:", sorted(len(m) for m in MIN_NONFACES))
assert min_size >= 3
for i in range(N):
    assert is_face((i,)), f"vertex {i} must be a face"
for i, j in combinations(range(N), 2):
    assert is_face((i, j)), f"edge {(i,j)} must be a face"
print("FULL_1_SKELETON_OK: all 9 vertices and all 36 edges are faces")

def rank_q(rows):
    """Exact rank of integer matrix given as list of rows (lists of int/Fraction)."""
    M = [[Fraction(x) for x in r] for r in rows]
    m = len(M)
    n = len(M[0]) if m else 0
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, m):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = 1 / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r

def reduced_betti(I):
    """Reduced Betti dict {dim: betti} over Q for full subcomplex K_I.
    I: sorted tuple of vertices. Chain groups C_n, n=-1..d."""
    I = tuple(sorted(I))
    k = len(I)
    if k == 0:
        return {-1: 1}  # void complex {empty}: \tilde H_{-1}=Q
    # enumerate faces by dimension
    faces = {}  # dim -> list of sorted tuples
    for r in range(1, k+1):
        dim = r - 1
        fl = [c for c in combinations(I, r) if is_face(c)]
        faces[dim] = fl
    # index maps
    idx = {dim: {s: j for j, s in enumerate(faces[dim])} for dim in faces}
    maxdim = max(faces) if faces else -1
    # boundary ranks: rank(d_n) for n>=0, plus rank(d_0 : C0 -> C_{-1})
    drank = {}
    # d_0 is the 1 x k all-ones matrix (augmentation); rank 1 if k>0
    drank[0] = 1
    for n in range(1, maxdim+1):
        dom, cod = faces[n], faces.get(n-1, [])
        if not dom or not cod:
            drank[n] = 0
            continue
        # rows = cod, cols = dom
        mat = [[Fraction(0)]*len(dom) for _ in range(len(cod))]
        for j, s in enumerate(dom):
            for t in range(n+1):
                f = tuple(v for u, v in enumerate(s) if u != t)
                i = idx[n-1][f]
                mat[i][j] += Fraction((-1)**t)
        drank[n] = rank_q(mat)
    betti = {}
    # n = -1
    b_1 = 1 - drank[0]
    if b_1:
        betti[-1] = b_1
    for n in range(0, maxdim+1):
        dimc = len(faces[n])
        rn = drank.get(n, 0)
        rnp1 = drank.get(n+1, 0)
        b = dimc - rn - rnp1
        if b:
            betti[n] = b
    return betti

# --- Step 4: full Hochster sweep ---
Hp = {}   # p -> total dim
support_witness = {}  # p -> list of (I, q, b)
small_support_violation = []
for mask in range(1 << N):
    I = tuple(i for i in range(N) if mask & (1 << i))
    b = reduced_betti(I)
    if 1 <= len(I) <= 2 and any(v != 0 for v in b.values()):
        small_support_violation.append((I, b))
    for q, d in b.items():
        p = q + len(I) + 1
        Hp[p] = Hp.get(p, 0) + d
        if p in (3, 5):
            support_witness.setdefault(p, []).append((I, q, d))

print("HOCHSTER_BETTI_Z (p: dim):", {p: Hp.get(p, 0) for p in range(0, 16)})
print("total dim H*(Z) =", sum(Hp.values()))
assert not small_support_violation, small_support_violation[:5]
print("SMALL_SUPPORT_VANISHING_OK: every K_I with |I|<=2 has zero reduced homology")
h3 = Hp.get(3, 0)
assert h3 == 0, f"H^3 must vanish, got {h3}"
print("H3_VANISHING_OK: H^3(Z_K0;Q) = 0")

# --- Step 7: triple-support cross-check ---
for S1 in [(0,1,2),(3,4,5),(6,7,8)]:
    b = reduced_betti(S1)
    print(f"K_{tuple(x+1 for x in S1)} reduced Betti:", b)
    assert b.get(1, 0) == 1, (S1, b)
print("TRIPLE_SUPPORTS_OK: each of {123},{456},{789} carries \\tilde H^1=Q (H^5 summand)")

# --- Quadruple-disjointness obstruction arithmetic ---
# Every nonzero multigraded component needs |I|>=3 (just proved for all 512 I).
# Four pairwise-disjoint nonempty supports each of size>=3 need >=12 vertices.
print("QUADRUPLE_DISJOINT_IMPOSSIBLE: 4 x 3 = 12 > 9 vertices")
print("ALL_TARGET_OBSTRUCTION_CHECKS_PASS")
