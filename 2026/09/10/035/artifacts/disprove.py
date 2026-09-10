"""Lift classical low-weight codewords to quantum logicals; test TARGET d>=9.
Exact integer-bit arithmetic. Rebuilds everything from (E,L) — no imports from build.py.
"""
import json, os

ART = os.path.dirname(os.path.abspath(__file__))
L = 7
E = [[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,1]]

def b1(j1,q,b): return (j1*5+q)*7+b
def b2(s,l,b): return 175+(s*3+l)*7+b

B_rows = []
for i in range(3):
    for a in range(7):
        v = 0
        for j in range(5):
            v |= 1 << (j*7+(a+E[i][j]) % 7)
        B_rows.append(v)

HX = []
for i1 in range(3):
    for p in range(5):
        for a in range(7):
            v = 0
            for j1 in range(5):
                v |= 1 << b1(j1, p, (a+E[i1][j1]) % 7)
            for l in range(3):
                v |= 1 << b2(i1, l, (a-E[l][p]) % 7)
            HX.append(v)
HZ = []
for p_ in range(5):
    for q_ in range(3):
        for a in range(7):
            v = 0
            for q in range(5):
                v |= 1 << b1(p_, q, (a+E[q_][q]) % 7)
            for s in range(3):
                v |= 1 << b2(s, q_, (a-E[s][p_]) % 7)
            HZ.append(v)

def ctz(x): return (x & -x).bit_length()-1
def wt(v): return bin(v).count('1')

def ref_basis(rows):
    basis = {}
    for v in rows:
        w = v
        for p in sorted(basis):
            if (w >> p) & 1: w ^= basis[p]
        if w:
            piv = ctz(w)
            for p in list(basis):
                if (basis[p] >> piv) & 1: basis[p] ^= w
            basis[piv] = w
    return basis

def remainder(basis, v):
    w = v
    for p in sorted(basis):
        if (w >> p) & 1: w ^= basis[p]
    return w

basisB = ref_basis(B_rows)
pivB = set(basisB); freeB = [c for c in range(35) if c not in pivB]
nsB = []
for f in freeB:
    v = 1 << f
    for p in pivB:
        if (basisB[p] >> f) & 1: v |= 1 << p
    nsB.append(v)
assert len(nsB) == 16
for v in nsB:
    for r in B_rows: assert bin(r & v).count('1') % 2 == 0

cw = {}
for mask in range(1, 1 << 16):
    v = 0; m = mask; i = 0
    while m:
        if m & 1: v ^= nsB[i]
        i += 1; m >>= 1
    cw.setdefault(wt(v), []).append(v)
print("classical weight classes:", {w: len(cw[w]) for w in sorted(cw)})
assert min(cw) == 6 and len(cw[6]) == 21

def synd(H, v):
    s = 0
    for i, r in enumerate(H):
        if bin(r & v).count('1') % 2: s |= 1 << i
    return s

basisX = ref_basis(HX); basisZ = ref_basis(HZ)
print("rank HX:", len(basisX), "rank HZ:", len(basisZ))

def supp35(v): return [(c // 7, c % 7) for c in range(35) if (v >> c) & 1]
def supp238(v): return [c for c in range(238) if (v >> c) & 1]

# X-logical candidates from ker(B), all weights <=8
results = {}
witness = None
for w in sorted(cw):
    if w > 8: break
    n_log = 0; n_stab = 0
    for c in cw[w]:
        for j in range(5):
            v = 0
            for t in range(35):
                if (c >> t) & 1:
                    v |= 1 << b1(j, t // 7, t % 7)
            assert wt(v) == w
            assert synd(HZ, v) == 0, "lift must be in ker(HZ)"
            if remainder(basisX, v) == 0:
                n_stab += 1
            else:
                n_log += 1
                if witness is None:
                    witness = (w, c, j, v)
    results[w] = {"logical": n_log, "stabilizer": n_stab}
    print(f"weight {w}: logical={n_log} stabilizer={n_stab} (of {len(cw[w])*5} lifts)")

assert witness is not None, "no logical found"
w, c, j, v = witness
print(f"\nwitness: classical wt={w}, block j={j}")
print("classical support (var,shift):", supp35(c))
print("quantum support:", supp238(v))
# independent rank-augmentation check
assert len(ref_basis(HX + [v])) == len(basisX) + 1, "rank must grow by 1"
print("rank(HX)=%d rank(HX+l)=%d -> l not in rowspace(HX)" % (len(basisX), len(ref_basis(HX+[v]))))
print("H_Z l = 0 verified:", synd(HZ, v) == 0)
print("wt(l) =", wt(v))
print(f"\nCONCLUSION: d(Q*) <= {wt(v)} < 9. TARGET d>=9 is FALSE.")

with open(os.path.join(ART, "disproof.json"), "w") as f:
    json.dump({
        "classical_codeword_support35": supp35(c),
        "classical_weight": w, "lift_block_j": j,
        "logical_support238": supp238(v),
        "logical_weight": wt(v),
        "rank_HX": len(basisX), "rank_HZ": len(basisZ),
        "rank_HX_plus_l": len(ref_basis(HX+[v])),
        "HZ_syndrome_zero": True,
        "lift_census_wt_le8": results,
        "conclusion": f"d(Q*)<={wt(v)}<9"},
        f, indent=1)
print("disproof.json written")
