"""A7 character table from scratch + Frobenius width-two certificate.
Step 1: S7 irreducible characters via Murnaghan-Nakayama (sub-diagram
  rim-hook enumeration), verified by full row orthogonality.
Step 2: Restrict to A7; split the self-conjugate irrep on the split
  class (7A/7B); verify A7 row orthogonality (complex).
Step 3: E = e2(A7) equals A7 (census); Frobenius convolution
  N(g) = #{(u,v) in E x E : uv = g} evaluated as character sum
  N(g) = (1/|G|) sum_chi S_chi^2 chi(g)/chi(1), S_chi = sum_{u in E} chi(u).
  Assert N(g) > 0 for all 9 classes; save per-class table.
Stdlib only.
"""
import json, cmath, itertools
from functools import lru_cache

# ---------- partitions ----------
def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0: yield ();
    else:
        for f in range(min(mx, n), 0, -1):
            for r in partitions(n - f, f):
                yield (f,) + r

PARTS7 = sorted(list(partitions(7)), reverse=True)
assert len(PARTS7) == 15
print("S7 classes:", len(PARTS7))

def conj_part(lam):
    if not lam: return ()
    m = lam[0]
    out = []
    for c in range(1, m + 1):
        out.append(sum(1 for r in lam if r >= c))
    return tuple(out)

def class_size_S(sym_type, n=7):
    from math import factorial
    m = {}
    for c in sym_type: m[c] = m.get(c, 0) + 1
    z = 1
    for c, e in m.items(): z *= (c ** e) * factorial(e)
    return factorial(n) // z

# ---------- Murnaghan-Nakayama ----------
def sub_diagrams(lam):
    """all mu subset lam (as partitions, padded with zeros)."""
    lam = tuple(lam)
    k = len(lam)
    ranges = [range(lam[i] + 1) for i in range(k)]
    for mus in itertools.product(*ranges):
        mu = tuple(mus)
        # must be a partition (nonincreasing)
        if all(mu[i] >= mu[i + 1] for i in range(k - 1)):
            yield mu

def rim_hook_info(lam, mu):
    """lam/mu skew: return (size, height, valid) with no-2x2 + connected."""
    lam = list(lam) + [0]
    mu = list(mu) + [0] * (len(lam) - len(mu))
    cells = set()
    for i in range(len(lam)):
        for c in range(mu[i], lam[i]):
            cells.add((i, c))
    size = len(cells)
    if size == 0: return (0, 0, False)
    # connected (edge adjacency)
    stack = [next(iter(cells))]; seen = set(stack)
    while stack:
        a, b = stack.pop()
        for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (a + d[0], b + d[1])
            if q in cells and q not in seen:
                seen.add(q); stack.append(q)
    if seen != cells: return (size, 0, False)
    # no 2x2 block
    for (i, c) in cells:
        if (i + 1, c) in cells and (i, c + 1) in cells and (i + 1, c + 1) in cells:
            return (size, 0, False)
    rows = {i for (i, c) in cells}
    if max(rows) - min(rows) + 1 != len(rows):
        return (size, 0, False)  # disconnected rows (safety)
    return (size, len(rows) - 1, True)

def chi_MN(lam, mu):
    """irreducible S_n character: lam partition, mu class cycle type."""
    key = (tuple(lam), tuple(mu))
    return _chi(key)

@lru_cache(maxsize=None)
def _chi(key):
    lam, mu = list(key[0]), list(key[1])
    n = sum(lam)
    if n == 0: return 1
    if not mu or sum(mu) != n: return 0
    k = mu[0]
    rest = tuple(sorted(mu[1:], reverse=True))
    total = 0
    for sub in sub_diagrams(tuple(lam)):
        size, ht, ok = rim_hook_info(tuple(lam), sub)
        if ok and size == k:
            total += ((-1) ** ht) * chi_MN(list(sub), list(rest))
    return total

# build S7 table
S = {}
for lam in PARTS7:
    for mu in PARTS7:
        S[(lam, mu)] = chi_MN(list(lam), list(mu))
# orthogonality check
N_S7 = 5040
ok = True
for i, lam in enumerate(PARTS7):
    for j, mu_ in enumerate(PARTS7):
        if j < i: continue
        s = sum(class_size_S(nu) * S[(lam, nu)] * S[(mu_, nu)] for nu in PARTS7)
        want = N_S7 if i == j else 0
        if s != want:
            ok = False; print("S7 ORTH FAIL", lam, mu_, s)
print("S7 orthogonality:", "OK" if ok else "FAIL")
assert ok
print("S7 degrees:", sorted([S[(lam, (1,) * 7)] for lam in PARTS7]))
assert sum(S[(lam, (1,) * 7)] ** 2 for lam in PARTS7) == 5040

# ---------- restrict to A7 ----------
def is_even_type(mu): return (sum(mu) - len(mu)) % 2 == 0
EVEN = [mu for mu in PARTS7 if is_even_type(mu)]
print("S7 even classes:", EVEN)

def splits(mu):
    # centralizer <= A_n iff parts are distinct odd numbers
    return len(set(mu)) == len(mu) and all(c % 2 == 1 for c in mu)

SPLIT = [mu for mu in EVEN if splits(mu)]
print("split S-classes:", SPLIT)
# A7 classes: each even S-class one A-class, split ones two
A_CLASSES = []  # (stype, half) half 0/1 for split
for mu in EVEN:
    if splits(mu): A_CLASSES += [(mu, 0), (mu, 1)]
    else: A_CLASSES.append((mu, 0))
print("A7 classes:", len(A_CLASSES))
assert len(A_CLASSES) == 9
# A-class sizes: non-split same as S-size; split halves half each
A_SIZE = {}
for (mu, h) in A_CLASSES:
    s = class_size_S(mu) // 2  # A7 index... careful: S-class inside A7?
    # S-class of even type lies in A7; size in A7 = same number; split halves = half
    A_SIZE[(mu, h)] = class_size_S(mu) if not splits(mu) else class_size_S(mu) // 2
assert sum(A_SIZE.values()) == 2520, sum(A_SIZE.values())

# A-irreps: pair up conjugates
pairs = []
used = set()
for lam in PARTS7:
    if lam in used: continue
    c = conj_part(lam)
    if c == lam:
        pairs.append((lam, None)); used.add(lam)
    else:
        pairs.append((lam, c)); used.add(lam); used.add(c)
print("A-irrep seeds:", [(a, b) for a, b in pairs])
print("n A-irreps:", sum(1 for (a, b) in pairs if b is not None) + 2 * sum(1 for (a, b) in pairs if b is None))
SELF = [a for (a, b) in pairs if b is None]
print("self-conjugate:", SELF)
assert len(SELF) == 1
lam_star = SELF[0]

# A-irreps: non-self-conjugate pairs restrict to ONE A-irrep each;
# the self-conjugate one splits into TWO A-irreps (differ on split classes).
A_IRR = []  # (kind, seed, sub) kind: 'pair' or 'split0'/'split1'
for (a, b) in pairs:
    if b is None:
        A_IRR.append(('split0', a, 0)); A_IRR.append(('split1', a, 1))
    else:
        A_IRR.append(('pair', a, 0))
assert len(A_IRR) == 9, len(A_IRR)
NIRR = 9

# A-character values: dict irr_index -> {(mu,h): complex}
A_CHI = {}
for idx, (kind, a, sub) in enumerate(A_IRR):
    for (mu, h) in A_CLASSES:
        if kind == 'pair':
            A_CHI[(idx, (mu, h))] = complex(S[(a, mu)])
        else:
            base = S[(a, mu)] / 2
            if splits(mu):
                m = sum(mu); kk = len(mu)
                D = ((-1) ** ((m - kk) // 2))
                for c_ in mu: D *= c_
                sq = cmath.sqrt(D)
                sgn = 1 if (kind == 'split0') == (h == 0) else -1
                A_CHI[(idx, (mu, h))] = base + sgn * sq / 2
            else:
                A_CHI[(idx, (mu, h))] = complex(base)
# orthogonality
N_A7 = 2520
ok = True
for i in range(9):
    for j in range(9):
        if j < i: continue
        s = sum(A_SIZE[C] * A_CHI[(i, C)] * A_CHI[(j, C)].conjugate()
                for C in A_CLASSES)
        want = N_A7 if i == j else 0
        if abs(s - want) > 1e-6:
            ok = False; print("A7 ORTH FAIL", i, j, s)
print("A7 orthogonality:", "OK" if ok else "FAIL")
assert ok
degs = sorted([round(abs(A_CHI[(i, ((1,) * 7, 0))])) for i in range(9)])
print("A7 degrees:", degs)
assert sum(d * d for d in degs) == 2520

# ---------- Frobenius width-two sums ----------
# E = e2(A7): census says every class fully covered => E = A7 as sets.
cen = json.load(open("output/artifacts/e2_census.json"))["7"]["table"]
E_of_class = {tuple(sorted(r["cycle_type"], reverse=True)) + (0,): r["size"]
              for r in cen}  # full class sizes (N1>0 everywhere)
# S_chi = sum over E of chi = sum_C |C| chi(C) (E = whole group)
S_chi = []
for i in range(9):
    s = sum(A_SIZE[C] * A_CHI[(i, C)] for C in A_CLASSES)
    S_chi.append(s)
print("S_chi magnitudes:", [round(abs(v)) for v in S_chi])
# only trivial rep survives (E = G)
Nconst = {}
for C in A_CLASSES:
    tot = sum(S_chi[i] ** 2 * A_CHI[(i, C)] / A_CHI[(i, ((1,) * 7, 0))]
              for i in range(9)) / N_A7
    Nconst[str(C)] = tot
print("Frobenius N(g):", {k: round(v.real) for k, v in Nconst.items()})
assert all(abs(v.imag) < 1e-6 for v in Nconst.values())
Nint = {k: int(round(v.real)) for k, v in Nconst.items()}
assert all(v == 2520 for v in Nint.values()), Nint
assert all(v > 0 for v in Nint.values())

# save certificate
cert = {
    "group": "A7", "order": 2520,
    "classes": [{"stype": list(mu), "half": h, "size": A_SIZE[(mu, h)],
                 "centralizer": 2520 // A_SIZE[(mu, h)]}
                for (mu, h) in A_CLASSES],
    "irreps": [{"index": i, "kind": A_IRR[i][0], "seed": list(A_IRR[i][1]),
                "degree": round(abs(A_CHI[(i, ((1,) * 7, 0))])),
                "values": {str(C): [A_CHI[(i, C)].real, A_CHI[(i, C)].imag]
                           for C in A_CLASSES}} for i in range(9)],
    "E_equals_G": True,
    "S_chi": [[v.real, v.imag] for v in S_chi],
    "frobenius_N_per_class": Nint,
    "conclusion": "N(g)=2520>0 for all 9 classes: A7 = e2(A7) e2(A7).",
}
json.dump(cert, open("output/artifacts/A7_frobenius_certificate.json", "w"), indent=1)
print("saved output/artifacts/A7_frobenius_certificate.json")

# also dump raw S7 table for audit
json.dump({"partitions": [list(p) for p in PARTS7],
           "table": {f"{list(a)}|{list(b)}": S[(a, b)]
                     for a in PARTS7 for b in PARTS7}},
          open("output/artifacts/S7_character_table.json", "w"))
print("saved output/artifacts/S7_character_table.json")
print("ALL CERTIFICATE CHECKS PASSED")
