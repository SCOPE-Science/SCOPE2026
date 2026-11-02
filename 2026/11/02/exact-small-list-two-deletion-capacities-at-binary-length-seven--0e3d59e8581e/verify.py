#!/usr/bin/env python3
"""Exact finite verification for a binary two-deletion list-decoding profile.

Uses only Python's standard library; certificate entries use exact rational arithmetic.
"""
import itertools
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "certificates.json").read_text(encoding="utf-8"))
WORDS = ["".join(bits) for bits in itertools.product("01", repeat=7)]
READS = ["".join(bits) for bits in itertools.product("01", repeat=5)]
assert len(WORDS) == 128 and len(READS) == 32


def shadows_combinations(word):
    return {"".join(word[j] for j in positions)
            for positions in itertools.combinations(range(7), 5)}


def shadows_deletions(word):
    return {word[:i] + word[i+1:j] + word[j+1:]
            for i in range(7) for j in range(i+1, 7)}


SHADOW = {}
for w in WORDS:
    s1, s2 = shadows_combinations(w), shadows_deletions(w)
    assert s1 == s2
    assert s1 <= set(READS)
    SHADOW[w] = s1

expected = {1: 5, 2: 11, 3: 16, 4: 21, 5: 26, 6: 32}
assert len(DATA) == len(expected)
for item in DATA:
    L, optimum = item["L"], item["optimum"]
    assert L in expected and optimum == expected[L]
    code = item["code"]
    assert len(code) == optimum and len(set(code)) == len(code)
    assert set(code) <= set(WORDS)
    multiplicities = {v: 0 for v in READS}
    for w in code:
        for v in SHADOW[w]:
            multiplicities[v] += 1
    assert max(multiplicities.values()) <= L

    assert item["received"] == READS
    assert len(item["y"]) == len(READS)
    assert len(item["z"]) == len(WORDS)
    y = {v: Fraction(item["y"][i]) for i, v in enumerate(READS)}
    z = {w: Fraction(item["z"][i]) for i, w in enumerate(WORDS)}
    assert all(weight >= 0 for weight in y.values())
    assert all(weight >= 0 for weight in z.values())
    for w in WORDS:
        assert sum((y[v] for v in SHADOW[w]), Fraction(0)) + z[w] >= 1
    bound = L * sum(y.values()) + sum(z.values())
    assert bound == Fraction(item["rational_bound"])
    assert optimum <= bound < optimum + 1
    print(f"PASS L={L} construction={len(code)} peak_list={max(multiplicities.values())} "
          f"rational_upper={bound} integer_upper={int(bound)}")

print(f"PASS {len(DATA)} profiles; 128 source words, 32 received words, "
      f"128 dual constraints per profile, 128 independent deletion-shadow crosschecks")
