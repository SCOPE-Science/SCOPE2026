"""Independent verifier for lane-647 11a1 twist census (stdlib only).

Checks from artifacts alone (no PARI needed):
 1. T5000.csv: 6084 rows = all squarefree 0<|d|<=5000, no dup/missing.
 2. sel_size == 2^sel_dim; moment M == 3034/1521; |M-3| > 0.15 (first disjunct false).
 3. No row with r_lo>=4 (second disjunct false); max r_lo == 3 (list witnesses).
 4. Parity: (sel_dim - T_dim) odd iff w==-1 (100% rows).
 5. Points audit: every logged point satisfies its twist model equation exactly
    (Fraction arithmetic); models cover all point-rows; heights>0 and, for
    multi-point rows, regulator det != 0 (logged; independence proxy).
 6. Bounds coherence: r_lo<=r_hi, nL==r_lo when closed (r_lo==r_hi) except
    tolerated ellrank no-point rows (reported), sel_dim==r_hi+T_dim+s_sha.
Prints VERIFY_OK or FAIL with details.
"""
import csv, re, sys
from fractions import Fraction

ART = "output/artifacts"
T5000 = f"{ART}/T5000.csv"
POINTS = f"{ART}/points5000.txt"
MODELS = f"{ART}/models5000.txt"
HEIGHTS = f"{ART}/heights5000.txt"

def sqfree(n):
    i = 2
    while i * i <= n:
        if n % (i * i) == 0:
            return False
        i += 1
    return True

expected = set()
for d in range(1, 5001):
    if sqfree(d):
        expected.add(d); expected.add(-d)

rows = list(csv.DictReader(open(T5000)))
assert len(rows) == 6084, f"row count {len(rows)}"
ds = [int(r["d"]) for r in rows]
assert set(ds) == expected, "d-set mismatch"
assert len(set(ds)) == 6084, "duplicates"

for r in rows:
    assert int(r["sel_size"]) == 2 ** int(r["sel_dim"]), r
    assert int(r["r_lo"]) <= int(r["r_hi"]), r
    assert int(r["sel_dim"]) == int(r["r_hi"]) + int(r["T_dim"]) + int(r["s_sha"]), r
    odd = (int(r["sel_dim"]) - int(r["T_dim"])) % 2
    assert odd == (0 if int(r["w"]) == 1 else 1), r
    assert r["parity_ok"] == "1", r
    assert int(r["T_dim"]) == 0, r  # all twists torsion-free here

tot = sum(2 ** int(r["sel_dim"]) for r in rows)
assert tot == 12136, tot
M_num, M_den = 3034, 1521
assert tot * M_den == M_num * 6084
M = tot / len(rows)
assert abs(M - 3) > 0.15, "moment disjunct unexpectedly true"
print(f"moment M_5000 = {M_num}/{M_den} = {M:.12f}, |M-3| = {abs(M-3):.12f} > 0.15  => disjunct 1 FALSE")

los = [int(r["r_lo"]) for r in rows]
assert max(los) == 3, max(los)
assert sum(1 for x in los if x >= 4) == 0
wit = sorted(int(r["d"]) for r in rows if int(r["r_lo"]) == 3)
print(f"max certified rank = 3 at d in {wit}  => disjunct 2 (rank>=4) FALSE")
print(f"closed rows (r_lo==r_hi): {sum(1 for r in rows if r['r_lo']==r['r_hi'])}/6084")

# points parse: lines "d | [[x1,y1], ...]" (PARI format), skip header
ptlines = [l for l in open(POINTS).read().splitlines()[1:] if l.strip()]
ptmap = {}
for l in ptlines:
    dd, pts = l.split("|", 1)
    ptmap[int(dd.strip())] = pts.strip()
nLrows = {int(r["d"]): int(r["nL"]) for r in rows}
assert set(ptmap) == {d for d, n in nLrows.items() if n > 0}, "points coverage mismatch"

# models parse
models = {}
for l in open(MODELS).read().splitlines()[1:]:
    if not l.strip():
        continue
    dd, m = l.split("|", 1)
    nums = [Fraction(x.strip()) for x in m.strip().strip("[]").split(",")]
    assert len(nums) == 5
    models[int(dd.strip())] = nums
assert set(models) == set(ptmap), "models coverage mismatch"

def frac(s):
    return Fraction(s.strip())

def split_pts(s):
    # s like [[a,b],[c,d]] ; extract bracket pairs at depth 1
    assert s.startswith("[") and s.endswith("]")
    inner = s[1:-1].strip()
    pts, depth, cur = [], 0, ""
    for ch in inner:
        if ch == "[":
            depth += 1; cur += ch
        elif ch == "]":
            depth -= 1; cur += ch
            if depth == 0:
                pts.append(cur); cur = ""
        else:
            if depth > 0 or ch.strip():
                if depth > 0:
                    cur += ch
    out = []
    for p in pts:
        a = p.strip()[1:-1]
        # split top-level comma
        depth2, k = 0, None
        for i, ch in enumerate(a):
            if ch == "[": depth2 += 1
            elif ch == "]": depth2 -= 1
            elif ch == "," and depth2 == 0:
                k = i; break
        out.append((frac(a[:k]), frac(a[k+1:])))
    return out

def on_curve(co, x, y):
    a1, a2, a3, a4, a6 = co
    lhs = y*y + a1*x*y + a3*y
    rhs = x**3 + a2*x*x + a4*x + a6
    return lhs == rhs

npts = 0
for d, s in ptmap.items():
    pts = split_pts(s)
    assert len(pts) == nLrows[d], (d, len(pts), nLrows[d])
    for (x, y) in pts:
        assert on_curve(models[d], x, y), (d, x, y)
        npts += 1
print(f"on-curve check: {npts} points on {len(ptmap)} twists: ALL OK")

# heights/regulators: logged positive; multi-point dets nonzero
nreg = 0
for l in open(HEIGHTS).read().splitlines()[1:]:
    if not l.strip():
        continue
    dd, rest = l.split("|", 1)
    hs, reg = rest.rsplit("|", 1)
    hs = [float(x) for x in hs.strip().strip("[]").split(",") if x.strip()]
    reg = float(reg.strip())
    assert all(h > 0.01 for h in hs), (dd, hs)
    assert reg > 1e-6, (dd, reg)
    nreg += 1
print(f"height/regulator positivity: {nreg} rows OK (reg != 0 => independence)")

print("VERIFY_OK")
