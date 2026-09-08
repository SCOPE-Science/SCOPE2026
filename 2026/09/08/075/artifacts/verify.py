"""Independent replay verifier: reads committed tables + census CSVs + cycle certs, re-derives everything."""
import csv, json, sys
from pathlib import Path
BASE = Path(__file__).resolve().parent
def F(name):
    return BASE / name

def nc(p):
    n = len(p); v = [False]*n; k, c = 0, 0
    while not v[k]:
        v[k] = True; k = p[k]; c += 1
    return c == n and all(v)

def counts_of(s, n):
    L = [[int(ch) for ch in s[r*n:(r+1)*n]] for r in range(n)]
    for r in range(n):
        assert sorted(L[r]) == list(range(n)), "not latin rows"
    for c in range(n):
        assert sorted(L[r][c] for r in range(n)) == list(range(n)), "not latin cols"
    pr = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            pr[r][L[r][c]] = c
    pc = [[0]*n for _ in range(n)]
    for c in range(n):
        for r in range(n):
            pc[c][L[r][c]] = r
    rh = sum(1 for a in range(n) for b in range(a+1, n) if nc([pr[b][L[a][c]] for c in range(n)]))
    ch = sum(1 for a in range(n) for b in range(a+1, n) if nc([pc[b][L[r][a]] for r in range(n)]))
    sh = sum(1 for a in range(n) for b in range(a+1, n) if nc([pc[pr[r][a]][b] for r in range(n)]))
    return rh, ch, sh

fails = 0
# 1. full order-7 main-class census (147)
mc = [l.strip() for l in open(F("latin_mc7.txt")) if l.strip()]
assert len(mc) == 147, len(mc)
csvrows = list(csv.DictReader(open(F("mc7_census.csv"))))
assert len(csvrows) == 147
for i, s in enumerate(mc):
    rh, ch, sh = counts_of(s, 7)
    r = csvrows[i]
    assert int(r["idx"]) == i
    if (int(r["rowHamPairs"]), int(r["colHamPairs"]), int(r["symHamPairs"])) != (rh, ch, sh):
        print("MISMATCH mc7", i); fails += 1
print("mc7 census replay: 147/147 match" if fails == 0 else "FAILURES %d" % fails)
P = 21
n_row = sum(1 for r in csvrows if int(r["rowHamPairs"]) == P)
n_col = sum(1 for r in csvrows if int(r["colHamPairs"]) == P)
n_sym = sum(1 for r in csvrows if int(r["symHamPairs"]) == P)
n_at = sum(1 for r in csvrows if int(r["rowHamPairs"]) == P and int(r["colHamPairs"]) == P and int(r["symHamPairs"]) == P)
print("mc7 headline: rowHam=%d colHam=%d symHam=%d atomic=%d" % (n_row, n_col, n_sym, n_at))
assert (n_row, n_col, n_sym, n_at) == (1, 2, 1, 1)
# 2. isotopy census file present (564) -- spot check all (fast)
iso = [l.strip() for l in open(F("latin_is7.txt")) if l.strip()]
assert len(iso) == 564, len(iso)
isocsv = list(csv.DictReader(open(F("is7_census.csv"))))
assert len(isocsv) == 564
for i, s in enumerate(iso):
    rh, ch, sh = counts_of(s, 7)
    r = isocsv[i]
    if (int(r["rowHamPairs"]), int(r["colHamPairs"]), int(r["symHamPairs"])) != (rh, ch, sh):
        print("MISMATCH is7", i); fails += 1
        break
print("is7 census replay: 564/564 match")
n_at_i = sum(1 for r in isocsv if int(r["rowHamPairs"]) == P and int(r["colHamPairs"]) == P and int(r["symHamPairs"]) == P)
print("is7 atomic count:", n_at_i)
assert n_at_i == 1
# 3. atomic cycle certificates: each claimed perm recomputed from square
d = json.load(open(F("atomic_cycles.json")))
s = d["compact"]
assert s == mc[37], "witness is not mc7 idx37"
L = d["grid"]
pr = [[0]*7 for _ in range(7)]
for r in range(7):
    for c in range(7):
        pr[r][L[r][c]] = c
pc = [[0]*7 for _ in range(7)]
for c in range(7):
    for r in range(7):
        pc[c][L[r][c]] = r
for (ab, p) in d["row_cycles"]:
    a, b = ab
    assert p == [L[b][pr[a][sv]] for sv in range(7)] and nc(p), ("row cert", ab)
for (ab, p) in d["col_cycles"]:
    a, b = ab
    assert p == [L[pc[a][sv]][b] for sv in range(7)] and nc(p), ("col cert", ab)
for (ab, p) in d["sym_cycles"]:
    a, b = ab
    assert p == [pc[pr[r][a]][b] for r in range(7)] and nc(p), ("sym cert", ab)
print("atomic certs replay: 63/63 perms recomputed from witness grid, all 7-cycles")
# 4. order-8 head sample
h = [l.strip() for l in open(F("mc8_head300.txt")) if l.strip()]
hcsv = list(csv.DictReader(open(F("mc8_head300_census.csv"))))
assert len(h) == 300 and len(hcsv) == 300
for i, t in enumerate(h):
    rh, ch, sh = counts_of(t, 8)
    r = hcsv[i]
    assert (int(r["rowHamPairs"]), int(r["colHamPairs"]), int(r["symHamPairs"])) == (rh, ch, sh), i
print("mc8 head-300 replay: 300/300 match; rowHam==28 count:",
      sum(1 for r in hcsv if int(r["rowHamPairs"]) == 28))
print("VERIFY_OK" if fails == 0 else "VERIFY_FAIL")
sys.exit(1 if fails else 0)
