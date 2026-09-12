"""Exact ordinary-line ledger for the two-circle 21-point competitor D21.

D21 = 10 points on unit circle at angles 2k*pi/10,
     + 10 points on circle radius 2 at offset angles 2k*pi/10 + pi/10,
     + the origin.  Total 21 points.

Method: exact arithmetic in the cyclotomic field Q(zeta_20), basis
1,z,...,z^7 with minimal polynomial z^8 - z^6 + z^4 - z^2 + 1,
coefficients as Fraction. Collinearity of complex points a,b,c tested by
exact vanishing of (a-b)*conj(a-c) - conj(a-b)*(a-c).
Stdlib only.
"""
import itertools
import json
import os

# ---------- cyclotomic arithmetic ----------
DEG = 8

def zero():
    return [0, 0, 0, 0, 0, 0, 0, 0]  # Fractions as int-ok; use Fraction below

from fractions import Fraction as F

def z0():
    return [F(0)] * DEG

def zone():
    return [F(1)] + [F(0)] * (DEG - 1)

def zgen():
    r = z0(); r[1] = F(1); return r

def add(a, b):
    return [x + y for x, y in zip(a, b)]

def sub(a, b):
    return [x - y for x, y in zip(a, b)]

def mul(a, b):
    t = [F(0)] * 15
    for i in range(DEG):
        for j in range(DEG):
            t[i + j] += a[i] * b[j]
    # reduce top-down with z^8 = z^6 - z^4 + z^2 - 1,
    # i.e. z^n = z^{n-2} - z^{n-4} + z^{n-6} - z^{n-8}
    for n in range(14, DEG - 1, -1):
        c = t[n]
        if c != 0:
            t[n - 2] += c
            t[n - 4] -= c
            t[n - 6] += c
            t[n - 8] -= c
            t[n] = F(0)
    return t[:DEG]

def pow_z(n):
    n %= 20
    r = zone(); g = zgen()
    for _ in range(n):
        r = mul(r, g)
    return r

def conj(a):
    r = z0()
    for k in range(DEG):
        if a[k] != 0:
            p = pow_z((-k) % 20)
            ck = a[k]
            for i in range(DEG):
                r[i] += ck * p[i]
    return r

# ---------- self-checks of the arithmetic ----------
assert mul(pow_z(20), zone()) == zone()          # z^20 = 1
assert mul(pow_z(7), pow_z(13)) == zone()        # z^7 z^13 = 1
w = pow_z(5)                                     # z^5 = i
assert mul(w, w) == [-F(1)] + [F(0)] * 7         # i^2 = -1
for k in range(20):                              # |z^k|^2 = 1
    p = pow_z(k)
    assert mul(p, conj(p)) == zone(), k
assert conj(conj(pow_z(3))) == pow_z(3)

# ---------- the point set ----------
pts = []          # complex reps
labels = []
for k in range(10):
    pts.append(pow_z(2 * k)); labels.append(f"I{k}")
for k in range(10):
    pts.append([2 * c for c in pow_z(2 * k + 1)]); labels.append(f"O{k}")
pts.append(z0()); labels.append("C")

# distinctness
seen = set()
for i, p in enumerate(pts):
    key = tuple(p)
    assert key not in seen, f"coincidence at {labels[i]}"
    seen.add(key)
assert len(seen) == 21

def coll(i, j, k):
    a, b, c = pts[i], pts[j], pts[k]
    ab = sub(a, b); ac = sub(a, c)
    d = sub(mul(ab, conj(ac)), mul(conj(ab), ac))
    return all(x == 0 for x in d)

# all collinear triples
triples = [t for t in itertools.combinations(range(21), 3) if coll(*t)]

# group pairs into spanned lines via union-find (merge pairs sharing a triple)
pairs = list(itertools.combinations(range(21), 2))
pidx = {p: n for n, p in enumerate(pairs)}
parent = list(range(len(pairs)))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x

def union(x, y):
    rx, ry = find(x), find(y)
    if rx != ry:
        parent[rx] = ry

for (i, j, k) in triples:
    union(pidx[(i, j)], pidx[(i, k)])
    union(pidx[(i, j)], pidx[(j, k)])

lines = {}
for n, p in enumerate(pairs):
    lines.setdefault(find(n), []).append(p)

line_pts = []
for plist in lines.values():
    s = set()
    for (i, j) in plist:
        s.add(i); s.add(j)
    line_pts.append(sorted(s))

# verify every line's point set is fully collinear (all triples inside coll)
for s in line_pts:
    for t in itertools.combinations(s, 3):
        assert coll(*t), f"non-collinear triple inside line {s}"

ordinary = [s for s in line_pts if len(s) == 2]
rich = [s for s in line_pts if len(s) >= 3]

def lname(i):
    return labels[i]

def kind(s):
    has_c = 20 in s
    inner = [i for i in s if 0 <= i <= 9]
    outer = [i for i in s if 10 <= i <= 19]
    if len(s) == 3 and has_c:
        if len(inner) == 2:
            return "diameter-inner-through-center"
        if len(outer) == 2:
            return "diameter-outer-through-center"
        return "through-center-mixed"
    if len(s) == 2:
        a, b = s
        ca = "C" if a == 20 else ("I" if a <= 9 else "O")
        cb = "C" if b == 20 else ("I" if b <= 9 else "O")
        return f"ordinary-{ca}{cb}"
    return "rich-other"

from collections import Counter
typecount = Counter(kind(s) for s in line_pts)

print(f"points: 21")
print(f"collinear triples: {len(triples)}")
for t in triples:
    print("  triple:", [lname(i) for i in t])
print(f"spanned lines: {len(line_pts)}")
print(f"ordinary (2-point) lines: {len(ordinary)}")
print(f"rich (>=3-point) lines: {len(rich)}")
print("line-type census:", dict(typecount))
print(f"threshold ceil(21/2) = 11; ordinary = {len(ordinary)} >= 11: "
      f"{len(ordinary) >= 11}")

# degree-4 support polynomial Q(x,y) = (x^2+y^2-1)(x^2+y^2-4):
# vanishes exactly on the two circle components carrying 20 of 21 points.
print("deg-4 support polynomial Q=(x^2+y^2-1)(x^2+y^2-4) vanishes on "
      "20/21 points (all but origin); cells: disk, annulus, exterior.")

assert len(triples) == 10
assert len(line_pts) == 190
assert len(ordinary) == 180
assert len(rich) == 10 and all(len(s) == 3 for s in rich)
assert all(20 in s for s in rich)  # every rich line passes through center
assert len(ordinary) >= 11
print("VERIFY_OK")

os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
ledger = {
    "points": labels,
    "n_spanned_lines": len(line_pts),
    "n_ordinary": len(ordinary),
    "n_rich": len(rich),
    "rich_lines": [[lname(i) for i in s] for s in rich],
    "type_census": dict(typecount),
    "threshold": 11,
    "claim_holds": len(ordinary) >= 11,
}
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "ledger.json"), "w") as f:
    json.dump(ledger, f, indent=2)
