#!/usr/bin/env python3
import json
import itertools
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "certificates.json").read_text(encoding="utf-8"))


def legal_matchings(n):
    edges = range(n - 1)
    out = []
    for r in range(n // 2 + 1):
        for s in itertools.combinations(edges, r):
            if all(s[j + 1] > s[j] + 1 for j in range(len(s) - 1)):
                out.append(s)
    return out


MATCHINGS = legal_matchings(6)
assert len(MATCHINGS) == 13


def ball(word):
    ans = set()
    for matching in MATCHINGS:
        a = list(word)
        for i in matching:
            a[i], a[i + 1] = a[i + 1], a[i]
        ans.add("".join(a))
    return ans


def orbit(multiset_word):
    return {"".join(p) for p in itertools.permutations(multiset_word)}


for typ, rec in DATA["types"].items():
    universe = orbit(rec["canonical_multiset"])
    centers = rec["centers"]
    assert len(centers) == len(set(centers)) == rec["claimed_cover_number"]
    assert set(centers) <= universe

    covered = set()
    for center in centers:
        b = ball(center)
        assert b <= universe
        covered |= b
    assert covered == universe, (typ, len(covered), len(universe))

    weights = {w: Fraction(v) for w, v in rec["dual_weights"].items()}
    assert set(weights) <= universe
    assert all(v >= 0 for v in weights.values())
    total = sum(weights.values(), Fraction(0))
    assert total == rec["claimed_cover_number"], (typ, total)

    max_ball_weight = Fraction(0)
    for center in universe:
        bw = sum((weights.get(w, Fraction(0)) for w in ball(center)), Fraction(0))
        max_ball_weight = max(max_ball_weight, bw)
        assert bw <= 1, (typ, center, bw)

    print(f"{typ}: universe={len(universe)} centers={len(centers)} dual_total={total} max_ball_weight={max_ball_weight}")

print("VERIFY_OK")
