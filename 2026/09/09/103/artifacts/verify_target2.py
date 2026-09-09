"""Lane 484 TARGET — part 2: direct K homology, K freeness, RP^2 cup square.

K = D*D*P where D=Delta_{4,3} (12v, faces 12/36/24), P=Delta_{4,1} (4v).
Direct F2 boundary-rank computation => H1(K)=H2(K)=0 (2-acyclic input to
Volovikov/Thm 3.1 with n=rank C=3). Direct V4-freeness on all K-simplices.
RP^2 (6-vertex triangulation): H^1 generator a with a^2 != 0 in H^2
(e^2 != 0 input to Intersection Lemma 3.2 with k=2).
"""
import json, itertools, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "target_machine_log2.json")

def rank_f2_int(rows):
    basis = {}
    r = 0
    for v in rows:
        x = v
        while x:
            b = x.bit_length() - 1
            if b in basis:
                x ^= basis[b]
            else:
                basis[b] = x
                r += 1
                break
    return r

# ---------- build D faces ----------
R, C = 4, 3
Dv = [(0, i, j) for i in range(R) for j in range(C)]  # tag factor later
def batt_faces(verts):
    F = { -1: [()], 0: [(v,) for v in verts], 1: [], 2: []}
    for a, b in itertools.combinations(verts, 2):
        if a[1] != b[1] and a[2] != b[2]:
            F[1].append((a, b))
    for a, b, c in itertools.combinations(verts, 3):
        if len({a[1], b[1], c[1]}) == 3 and len({a[2], b[2], c[2]}) == 3:
            F[2].append(tuple(sorted((a, b, c))))
    F[1] = [tuple(sorted(e)) for e in F[1]]
    return F
D1v = [(1, i, j) for i in range(R) for j in range(C)]
D2v = [(2, i, j) for i in range(R) for j in range(C)]
Pv = [(3, t) for t in range(4)]
F1, F2, FP = batt_faces(D1v), batt_faces(D2v), {-1: [()], 0: [(v,) for v in Pv]}
# join faces by dim: dim(f1*f2*f3)=d1+d2+d3+2 (empty=-1)
from collections import defaultdict
K = defaultdict(list)
for d1 in (-1, 0, 1, 2):
    for d2 in (-1, 0, 1, 2):
        for d3 in (-1, 0):
            L1 = F1[d1] if d1 in F1 else []
            L2 = F2[d2] if d2 in F2 else []
            L3 = FP[d3]
            d = d1 + d2 + d3 + 2
            for a in L1:
                for b in L2:
                    for c in L3:
                        K[d].append(a + b + c)
counts = {d: len(K[d]) for d in sorted(K)}
n_all = sum(counts.values())
assert sum(counts.values()) == 73 * 73 * 5 - 1 + 1 - 1 + 1 - 1 + 1, counts
# faces incl empty should be 73*73*5 = 26645? recompute: (73+1? ) D incl empty = 1+12+36+24=73.
assert n_all == 73 * 73 * 5, (n_all, 73 * 73 * 5)
# chain complex C0..C6 over F2; boundary via deleting one vertex (sorted order => sign irrelevant)
dims = sorted(d for d in counts if d >= 0)
Cdim = {d: len(K[d]) for d in dims}
assert dims == [0, 1, 2, 3, 4, 5, 6], dims
idx = {d: {s: k for k, s in enumerate(K[d])} for d in dims}
ranks = {}
for d in dims:
    if d == 0:
        continue
    rows = []
    low = idx[d - 1]
    for s in K[d]:
        m = 0
        for k in range(len(s)):
            f = s[:k] + s[k + 1:]
            m |= 1 << low[f]
        rows.append(m)
    # transpose to column space? rank(rows) as row vectors = rank of matrix. Boundary
    # matrix is (dim C_{d-1}) x (dim C_d); rows here = columns transposed; row-rank=col-rank.
    ranks[d] = rank_f2_int(rows)
bet = {}
prev = {d: ranks.get(d, 0) for d in dims}
for d in dims:
    bd = ranks.get(d + 1, 0)
    ker = Cdim[d] - ranks.get(d, 0) if d > 0 else Cdim[d]
    bet[d] = ker - bd
H1 = bet[1]; H2 = bet[2]
# ---------- V4 freeness on K ----------
V4 = [(0, 0), (1, 0), (0, 1), (1, 1)]
def act(g, v):
    if v[0] == 3:
        return (3, v[1] ^ (g[0] + 2 * g[1]))
    return (v[0], v[1] ^ (g[0] + 2 * g[1]), v[2])
Kfree = True
for g in V4[1:]:
    for d in dims:
        for s in K[d]:
            if frozenset(act(g, v) for v in s) == frozenset(s):
                Kfree = False
                break
# ---------- RP^2 cup square ----------
T = [(0,1,2),(0,2,3),(0,3,4),(0,4,5),(0,1,5),(1,2,4),(2,3,5),(3,4,1),(4,5,2),(5,1,3)]
E = sorted({tuple(sorted(e)) for t in T for e in itertools.combinations(t,2)})
eix = {e: k for k, e in enumerate(E)}
assert len(E) == 15
# coboundary d0: C0->C1, d1: C1->C2
d0 = []
for i in range(6):
    m = 0
    for (a, b) in E:
        if (i == a) != (i == b):
            m |= 1 << eix[(a, b)]
    d0.append(m)
r_d0 = rank_f2_int(d0)
d1 = []
for (a, b) in E:
    m = 0
    for t in T:
        if a in t and b in t:
            m |= 1 << T.index(t)
    d1.append(m)
r_d1 = rank_f2_int(d1)
dimH1 = 15 - r_d0 - r_d1
dimH2 = 10 - r_d1
# find H1 generator: vector in ker d1 not in im d0. im d0 row space; use complement search.
# brute force over F2^15 is 32768: fine.
def mat_rows_vec(rows, ncols):
    return rows
ker = []
for v in range(1 << 15):
    ok = True
    # v in ker d1: for each triangle, sum of v on its 3 edges = 0
    for t in T:
        s = 0
        for e in itertools.combinations(t, 2):
            if v >> eix[tuple(sorted(e))] & 1:
                s ^= 1
        if s:
            ok = False; break
    if ok:
        ker.append(v)
# quotient by im d0: reduce each by row space of d0 (6 rows in F2^15)
basis = {}
for w in d0:
    x = w
    while x:
        bb = x.bit_length() - 1
        if bb in basis:
            x ^= basis[bb]
        else:
            basis[bb] = x; break
def red(v):
    x = v
    while x:
        bb = x.bit_length() - 1
        if bb in basis:
            x ^= basis[bb]
        else:
            break
    return x
classes = {}
for v in ker:
    r = red(v)
    classes.setdefault(r, v)
reps = [v for r, v in classes.items() if r != 0 or v == 0]
gen = [v for r, v in classes.items() if r != 0]
a = gen[0]
# cup square: (a cup a)(t) = a(v0v1)*a(v1v2) with t sorted v0<v1<v2
def cup(aa, bb, t):
    v0, v1, v2 = sorted(t)
    return ((aa >> eix[(v0, v1)] & 1) & (bb >> eix[(v1, v2)] & 1))
a2 = [(cup(a, a, t)) for t in T]
# a^2 is a 2-cocycle automatically (a closed, char 2: d(a cup a)=0); check nonzero class:
# H^2 = C^2/im d1, dim should be 1; a2 != 0 vector and H2 dim 1 => nonzero class iff a2 not in im d1.
# im d1 = row space of d1 rows (15 rows in F2^10)
basis2 = {}
for w in d1:
    x = w
    while x:
        bb = x.bit_length() - 1
        if bb in basis2:
            x ^= basis2[bb]
        else:
            basis2[bb] = x; break
def red2(v):
    x = v
    while x:
        bb = x.bit_length() - 1
        if bb in basis2:
            x ^= basis2[bb]
        else:
            break
    return x
a2v = sum(c << k for k, c in enumerate(a2))
nonzero = red2(a2v) != 0
log = {
    "K_faces_by_dim": counts, "K_chain_dims": Cdim,
    "K_boundary_ranks": ranks, "K_betti_F2": {d: bet[d] for d in dims},
    "H1K": H1, "H2K": H2, "K_V4_free": Kfree,
    "RP2": {"nE": 15, "dimH1": dimH1, "dimH2": dimH2,
            "cup_square_nonzero": nonzero, "a2_triangle_values": a2},
}
with open(OUT, "w") as f:
    json.dump(log, f, indent=2)
print("K faces:", counts, "| betti:", {d: bet[d] for d in dims})
print("H1(K) =", H1, " H2(K) =", H2, " V4-free:", Kfree)
print("RP2: dimH1 =", dimH1, " dimH2 =", dimH2, " a^2 != 0:", nonzero)
ok = (H1 == 0 and H2 == 0 and Kfree and dimH1 == 1 and dimH2 == 1 and nonzero)
print("VERIFY_OK" if ok else "VERIFY_FAIL")
