"""Independent verifier: recomputes all invariants from committed generators only,
using a different code path (gcd + bounded membership sieve + Apéry minima),
and checks counts, W>=0, and extremal optimality per (g,m)."""
import json, math, sys
from functools import reduce

rows = json.load(open("output/artifacts/census.json"))
ext = json.load(open("output/artifacts/extremals.json"))

assert len(rows) == 1386
expected = {6: 23, 7: 39, 8: 67, 9: 118, 10: 204, 11: 343, 12: 592}
from collections import Counter
cnt = Counter(r["g"] for r in rows)
assert dict(cnt) == expected, cnt

def verify_row(r):
    gens = r["gens"]; m = r["m"]
    assert m == min(gens)
    assert reduce(math.gcd, gens) == 1
    F = r["F"]; c = F + 1
    assert c == r["c"]
    B = c + m * max(gens)
    inS = [False] * (B + 1)
    inS[0] = True
    for n in range(1, B + 1):
        for g_ in gens:
            if g_ > n:
                break
            if inS[n - g_]:
                inS[n] = True
                break
    gaps = [n for n in range(c) if not inS[n]]
    assert len(gaps) == r["g"], (gens, len(gaps), r["g"])
    assert max(gaps) == F
    # Apery: smallest element in S per residue
    Ap = []
    for i in range(m):
        w = next(n for n in range(B + 1) if n % m == i and inS[n])
        Ap.append(w)
    assert Ap == r["Ap"], (gens, Ap, r["Ap"])
    kunz = [(Ap[i] - i) // m for i in range(1, m)]
    assert kunz == r["kunz"] and sum(kunz) == r["g"]
    Lsize = sum(1 for n in range(c) if inS[n])
    assert Lsize == r["Lsize"] == c - r["g"]
    # minimality of gens
    for j, gj in enumerate(gens):
        others = gens[:j] + gens[j+1:]
        if not others:
            continue
        mB = gj + max(others) * gj
        reach = [False] * (mB + 1)
        reach[0] = True
        for n in range(1, mB + 1):
            for h in others:
                if h <= n and reach[n - h]:
                    reach[n] = True
                    break
        assert not reach[gj], (gens, gj)
    e = len(gens)
    assert e == r["e"]
    PF = [x for x in gaps if all(inS[x + g_] for g_ in gens)]
    assert len(PF) == r["t"]
    W = e * Lsize - c
    assert W == r["W"] and W >= 0
    return True

for r in rows:
    verify_row(r)

# extremal optimality per (g,m)
for key, E in ext.items():
    g, m = E["g"], E["m"]
    sub = [r for r in rows if r["g"] == g and r["m"] == m]
    assert len(sub) == E["N"]
    assert all(E["S_high"]["t"] >= r["t"] for r in sub)
    assert all(E["S_low"]["W"] <= r["W"] for r in sub)
    verify_row(E["S_high"])
    verify_row(E["S_low"])

# global boundary facts
assert min(r["W"] for r in rows) == 0
assert max(r["t"] for r in rows) == 12
for g in range(6, 13):
    sub = [r for r in rows if r["g"] == g]
    assert max(r["t"] for r in sub) == g  # ordinary semigroup attains t=g
    assert min(r["W"] for r in sub) == 0

print(f"VERIFY_OK: {len(rows)} rows, all invariants replayed from generators; W>=0 everywhere; extremals optimal in all 63 strata")
