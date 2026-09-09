"""Standalone stdlib-only verifier for the certified vanishing-obstruction record.
Checks: full 3718-class logs for both nominated triples (term consistency,
class-size sum, S=0, g=0), full-row tallies and <=3-row vanishing family,
box-distance neighbourhood census, ray sparse-log consistency, tensor-dimension
identity. Uses only stdlib + committed JSON logs; recomputes no characters.
Usage: python3 verify.py
"""
import json
import math
import os

A = os.path.dirname(os.path.abspath(__file__))


def hook_dim(lam):
    n = sum(lam)
    r = len(lam)
    d = 1
    for i, row in enumerate(lam):
        for j in range(row):
            leg = sum(1 for k in range(i + 1, r) if lam[k] > j)
            d *= (row - j - 1) + leg + 1
    return math.factorial(n) // d


def partitions(n, max_part=None):
    if max_part is None:
        max_part = n
    if n == 0:
        yield ()
        return
    for first in range(min(max_part, n), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def boxdist(p, q):
    L = max(len(p), len(q))
    pp = list(p) + [0] * (L - len(p))
    qq = list(q) + [0] * (L - len(q))
    return sum(abs(a - b) for a, b in zip(pp, qq)) // 2


fn28 = math.factorial(28)
assert str(fn28) == "304888344611713860501504000000", fn28
assert len(list(partitions(28))) == 3718

# (a) full-class logs for both nominated triples
for name, nu in [("plus", [16, 8, 4]), ("minus", [17, 8, 3])]:
    d = json.load(open(os.path.join(A, f"full_{name}.json")))
    assert d["n"] == 28 and d["nu"] == nu, name
    assert d["rho"] == [7, 6, 5, 4, 3, 2, 1] and d["alpha"] == [14, 14], name
    assert d["fact_n"] == str(fn28), name
    rows = d["rows"]
    assert len(rows) == 3718, (name, len(rows))
    seen = set()
    csum = 0
    S = 0
    for r in rows:
        cl, z, a, b, c, t = r
        key = tuple(cl)
        assert key not in seen, (name, cl)
        seen.add(key)
        assert sum(cl) == 28 and all(cl[i] >= cl[i + 1] for i in range(len(cl) - 1)), (name, cl)
        assert z > 0 and fn28 % z == 0, (name, cl, z)
        assert t == (fn28 // z) * a * b * c, (name, cl)
        csum += fn28 // z
        S += t
    assert csum == fn28, (name, csum)
    assert str(S) == d["S"] and S == 0, (name, S)
    assert d["g"] == 0 and S // fn28 == 0, name
    nnz = sum(1 for r in rows if r[5] != 0)
    print(f"{name}: 3718 classes, class-size sum=28!, S=0, g=0, nnz={nnz}  CERT_OK")

# (b) full-row tallies + <=3-row vanishing family (80/80)
row = json.load(open(os.path.join(A, "fullrow_rho_alpha.json")))
assert row["n"] == 28 and len(row["entries"]) == 3718
e = {tuple(p): g for p, g in row["entries"]}
assert e[(16, 8, 4)] == 0 and e[(17, 8, 3)] == 0, "row mismatch on targets"
nzb = sum(1 for g in e.values() if g > 0)
nzz = sum(1 for g in e.values() if g == 0)
assert nzb == 2557 and nzz == 1161, (nzb, nzz)
assert all(g >= 0 for g in e.values()), "negative Kronecker value impossible"
le3 = [p for p in e if len(p) <= 3]
assert len(le3) == 80, len(le3)
assert all(e[p] == 0 for p in le3), "nonzero <=3-row entry"
print(f"full row: 3718 entries, {nzb} positive / {nzz} zero, 80/80 <=3-row zeros  ROW_OK")

# (c) box-distance neighbourhood census around (16,8,4)
t = (16, 8, 4)
near = [p for p in e if boxdist(p, t) <= 2]
assert len(near) == 43, len(near)
assert all(e[p] == 0 for p in near), "nonzero entry within distance 2"
d3pos = sorted(p for p in e if boxdist(p, t) == 3 and e[p] > 0)
assert len(d3pos) == 9, len(d3pos)
assert all(boxdist(p, t) >= 3 for p in e if e[p] > 0), "positive closer than distance 3"
print(f"neighbourhood: 43/43 zero within distance<=2, 9 positives at distance 3  NBHD_OK")

# (d) ray sparse logs: term consistency + sparse sums
for fname, n, rho, alpha, nu, nclasses in [
    ("rayk1.json", 29, [8, 6, 5, 4, 3, 2, 1], [15, 14], [17, 8, 4], 4565),
    ("rayk2.json", 30, [9, 6, 5, 4, 3, 2, 1], [16, 14], [18, 8, 4], 5604),
]:
    r = json.load(open(os.path.join(A, fname)))
    assert r["n"] == n and r["rho"] == rho and r["alpha"] == alpha and r["nu"] == nu
    fn = math.factorial(n)
    assert r["fact_n"] == str(fn) and r["nclasses"] == nclasses
    S = 0
    for cl, z, a, b, c, tt in r["rows"]:
        assert sum(cl) == n, (fname, cl)
        assert tt == (fn // z) * a * b * c, (fname, cl)
        S += tt
    assert S == 0 and str(S) == r["S"] and r["g"] == 0, fname
    print(f"{fname}: n={n}, sparse terms consistent, S=0, g=0  RAY_OK")

# tensor-dimension identity
dim_rho = hook_dim((7, 6, 5, 4, 3, 2, 1))
dim_a = hook_dim((14, 14))
assert dim_rho == 48608795688960 and dim_a == 2674440
S = sum(g * hook_dim(p) for p, g in e.items())
assert S == dim_rho * dim_a == 130001307542382182400, S
print("tensor-dimension identity: sum_nu g*dim = dim(rho)*dim(alpha)  DIM_OK")
print("VERIFY_OK")
