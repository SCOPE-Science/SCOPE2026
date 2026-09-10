"""Build symmetric LP(B,B) 3x5 array, L=7, and structural checks.
Writes artifacts; prints log. Pure stdlib.
Ring-level LP: A=B=3x5 over F2[C7], entries x^{E[i][j]}.
  H_X = [A otimes I5 | I3 otimes B*]   (15x34 over R -> 105x238 binary)
  H_Z = [I5 otimes B | A* otimes I3]
Block1 cols: (j1,q,b), j1,q in 0..4, b in 0..6 -> idx (j1*5+q)*7+b (0..174)
Block2 cols: (s,l,b), s,l in 0..2 -> 175+(s*3+l)*7+b (175..237)
H_X rows: (i1,p,a) -> (i1*5+p)*7+a
H_Z rows: (p',q',a) -> (p'*3+q')*7+a
"""
import json, itertools, os

ART = os.path.dirname(os.path.abspath(__file__))
L = 7
E = [[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,1]]

def b1(j1,q,b): return (j1*5+q)*7+b
def b2(s,l,b): return 175+(s*3+l)*7+b
def hx_row(i1,p,a): return (i1*5+p)*7+a
def hz_row(p,q,a): return (p*3+q)*7+a

# ---- binary base B (21x35) ----
# Brow (i,a); Bcol (j,b): 1 iff b-a == E[i][j]
B_rows = []
for i in range(3):
    for a in range(7):
        v = 0
        for j in range(5):
            b = (a+E[i][j]) % 7
            v |= 1 << (j*7+b)
        B_rows.append(v)

def ctz(x):
    return (x & -x).bit_length()-1 if x else None

def ref_basis(rows):
    """Reduced row-echelon basis: dict pivot->row (each row has single bit at its pivot)."""
    basis = {}
    for v in rows:
        w = v
        for p in sorted(basis):
            if (w >> p) & 1:
                w ^= basis[p]
        if w:
            piv = ctz(w)
            for p in list(basis):
                if (basis[p] >> piv) & 1:
                    basis[p] ^= w
            basis[piv] = w
    return basis

def in_span(basis, v):
    w = v
    for p in sorted(basis):
        if (w >> p) & 1:
            w ^= basis[p]
    return w == 0

def rank_of(rows):
    return len(ref_basis(rows))

def nullspace_basis(rows, ncols):
    basis = ref_basis(rows)
    pivs = set(basis)
    free = [c for c in range(ncols) if c not in pivs]
    ns = []
    for f in free:
        v = 1 << f
        for p in pivs:
            if (basis[p] >> f) & 1:
                v |= 1 << p
        ns.append(v)
    # verify
    for v in ns:
        for r in rows:
            assert bin(r & v).count('1') % 2 == 0, "nullspace fail"
    return ns, free, pivs

def wt(v): return bin(v).count('1')

# ---- H_X, H_Z binary ----
HX = []
for i1 in range(3):
    for p in range(5):
        for a in range(7):
            v = 0
            for j1 in range(5):            # A otimes I: I part p==q
                v |= 1 << b1(j1, p, (a+E[i1][j1]) % 7)
            for l in range(3):            # I otimes B*: (B*)_{p,l} = x^{-E[l][p]}
                v |= 1 << b2(i1, l, (a-E[l][p]) % 7)
            HX.append(v)
HZ = []
for p_ in range(5):
    for q_ in range(3):
        for a in range(7):
            v = 0
            for q in range(5):            # I otimes B: (B)_{q_,q} = x^{E[q_][q]}
                v |= 1 << b1(p_, q, (a+E[q_][q]) % 7)
            for s in range(3):            # A* otimes I: (A*)_{p_,s} = x^{-E[s][p_]}
                v |= 1 << b2(s, q_, (a-E[s][p_]) % 7)
            HZ.append(v)

assert len(HX) == 105 and len(HZ) == 105
assert all(wt(v) == 8 for v in HX), "HX row weights"
assert all(wt(v) == 8 for v in HZ), "HZ row weights"

# CSS orthogonality: HX @ HZ^T == 0
HZcols = []
for c in range(238):
    m = 0
    for r in range(105):
        if (HZ[r] >> c) & 1:
            m |= 1 << r
    HZcols.append(m)
orth = all(bin(HX[r] & 0 or 0) == 0 or True for r in range(105))  # placeholder
bad = 0
for r in range(105):
    s = 0
    v = HX[r]
    # syndrome of HX[r] under HZ = parity of (HZ[r2] & HX[r]) for each r2
    for r2 in range(105):
        if bin(HZ[r2] & v).count('1') % 2:
            bad += 1
            break
print("HX rows:", len(HX), "HZ rows:", len(HZ))
print("all row weights 8:", all(wt(v)==8 for v in HX+HZ))
print("orthogonality violations:", bad)

rx = rank_of(HX); rz = rank_of(HZ)
k = 238 - rx - rz
print(f"rank HX={rx} rank HZ={rz} k={k} N=238")
print("w0 (max row weight) = 8")

# ---- classical base code: full kernel census of B_bin ----
nsB, freeB, pivB = nullspace_basis(B_rows, 35)
dB = len(nsB)
print(f"dim ker(B)={dB}, rank(B)={21-dB+ dB if False else rank_of(B_rows)}")
rB = rank_of(B_rows)
print(f"rank(B)={rB}")
# enumerate all codewords
from itertools import product
cw = []
for mask in range(1, 1 << dB):
    v = 0
    m = mask; i = 0
    while m:
        if m & 1: v ^= nsB[i]
        i += 1; m >>= 1
    cw.append(v)
weights = sorted(wt(v) for v in cw)
print("num nonzero codewords:", len(cw), "min weight d(B)=", weights[0])
import collections
print("weight distribution:", dict(collections.Counter(weights)))
lowB = sorted([v for v in cw if wt(v) <= 8], key=wt)
print("num codewords wt<=8:", len(lowB))

# ---- B* binary (35x21): rows (p,a), cols (l,b): 1 iff b-a == -E[l][p] ----
Bs = []
for p in range(5):
    for a in range(7):
        v = 0
        for l in range(3):
            b = (a-E[l][p]) % 7
            v |= 1 << (l*7+b)
        Bs.append(v)
rBs = rank_of(Bs)
nsBs, _, _ = nullspace_basis(Bs, 21)
print(f"B* size 35x21 rank={rBs} dimker={len(nsBs)}")
if nsBs:
    # enumerate kernel of B*
    cw2 = []
    for mask in range(1, 1 << len(nsBs)):
        v = 0; m = mask; i = 0
        while m:
            if m & 1: v ^= nsBs[i]
            i += 1; m >>= 1
        cw2.append(v)
    print("min weight ker(B*):", min(wt(v) for v in cw2), "count:", len(cw2))
else:
    cw2 = []
    print("ker(B*) trivial")

# ---- Tanner expansion of B: |N(S)| >= 2|S| for |S|<=4 ----
nbrs = []
for j in range(5):
    for b in range(7):
        c = j*7+b
        s = set()
        for i in range(3):
            a = (b-E[i][j]) % 7
            s.add(i*7+a)
        nbrs.append(s)
exp_fail = []
import math
def check_sets(vars35, size):
    fails = []
    total = 0
    for S in itertools.combinations(vars35, size):
        total += 1
        N = set()
        for v in S: N |= nbrs[v]
        if len(N) < 2*size:
            fails.append((S, len(N)))
    return total, fails
for sz in (1,2,3,4):
    t, f = check_sets(range(35), sz)
    print(f"|S|={sz}: checked {t} sets, failures: {len(f)}")
    exp_fail += [(sz, S, n) for (S, n) in f]
print("expansion holds:", len(exp_fail) == 0)

# ---- save artifacts ----
def bits(v, n):
    return [(v >> i) & 1 for i in range(n)]
with open(os.path.join(ART, "B_bin.json"), "w") as f:
    json.dump({"rows21x35": [bits(v, 35) for v in B_rows],
               "E": E, "L": L, "rank": rB, "dimker": dB,
               "classical_distance": weights[0],
               "weight_distribution": dict(collections.Counter(weights))}, f)
with open(os.path.join(ART, "HX_HZ.json"), "w") as f:
    json.dump({"HX_105x238": [bits(v, 238) for v in HX],
               "HZ_105x238": [bits(v, 238) for v in HZ],
               "rank_HX": rx, "rank_HZ": rz, "k": k,
               "orth_violations": bad}, f)
with open(os.path.join(ART, "low_weight_classical.json"), "w") as f:
    json.dump({"codewords_wt_le8": [bits(v, 35) for v in lowB]}, f)
with open(os.path.join(ART, "expansion.json"), "w") as f:
    json.dump({"holds": len(exp_fail) == 0, "failures": exp_fail,
               "sets_checked": 35+595+6545+52360}, f)
print("artifacts written")
