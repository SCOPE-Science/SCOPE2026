#!/usr/bin/env python3
"""Step 5: independent verifier (fresh code path): recompute rank oracles from sorted
line triples, recompute T(2,0) by subset-sum formula, verify census sums + maximizer gap
+ Fano cert + replay files."""
import json
from itertools import combinations

N = 8
reps = json.load(open("output/artifacts/reps.json"))
rows = json.load(open("output/artifacts/tutte_table.json"))

assert reps["ntypes"] == 68 and len(rows) == 68
assert sum(d["count"] for d in rows) == 433038
assert all(40320 % d["count"] == 0 for d in rows)

def T20(lines):
    tot = 0
    for a in range(1 << N):
        pc = bin(a).count("1")
        if pc <= 2:
            rk = pc
        else:
            rk = 2 if any((a & ~ln) == 0 for ln in lines) else 3
        tot += (-1) ** (pc - rk)
    return tot

for d in rows:
    v = T20(d["lines"])
    assert v == d["t20"], (d["type"], v, d["t20"])
    # bases check
    nb = 0
    for b in combinations(range(N), 3):
        m = (1 << b[0]) | (1 << b[1]) | (1 << b[2])
        if not any((m & ~ln) == 0 for ln in d["lines"]):
            nb += 1
    assert nb == d["nbases"], (d["type"], nb, d["nbases"])

rs = sorted(rows, key=lambda d: (-d["t20"], d["type"]))
assert rs[0]["type"] == 0 and rs[0]["t20"] == 58 and rs[0]["lines"] == []
assert rs[1]["t20"] == 56 and rs[0]["t20"] - rs[1]["t20"] == 2
vals = sorted(set(d["t20"] for d in rows), reverse=True)
assert vals == [58,56,54,52,50,48,46,44,42,40,38,36,28]

# Fano cert
F = [frozenset(L) for L in [[1,2,5],[0,3,5],[0,2,6],[1,3,6],[0,1,7],[2,3,7],[5,6,7]]]
t66 = [d for d in rows if d["type"] == 66][0]
assert set(map(int, t66["lines"])) == set([sum(1 << x for x in L) for L in F])
seen = set()
for L in F:
    L = sorted(L)
    for a in range(3):
        for b in range(a+1, 3):
            p = (L[a], L[b])
            assert p not in seen
            seen.add(p)
assert len(seen) == 21

# replay files
for lab, exp in [("W", 58), ("runnerup", 56)]:
    rp = json.load(open(f"output/artifacts/replay_{lab}.json"))
    v = sum(c * 2**i for (i, j, c) in rp["poly"] if j == 0)
    assert v == exp, (lab, v)
    assert sum(c * 2**i * 2**j for (i, j, c) in rp["poly"]) == 256

print("VERIFIER: ALL CHECKS PASSED")
print("types=68 labeled=433038 max T(2,0)=58 (U(3,8)) runner-up=56 gap=2")
print("Fano minor in type-66 certified (delete 4); replay files consistent")
