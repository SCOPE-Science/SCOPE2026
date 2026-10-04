#!/usr/bin/env python3
from pathlib import Path
from itertools import product
import json

ROOT = Path(__file__).resolve().parent.parent
cert = json.loads((ROOT / "artifacts" / "certificate.json").read_text(encoding="utf-8"))

def paldup(w, i):
    b = w[i:i+2]
    return w[:i+2] + b[::-1] + w[i+2:]

def desc2(w):
    out = set()
    for i in range(len(w)-1):
        w1 = paldup(w, i)
        for j in range(len(w1)-1):
            out.add(paldup(w1, j))
    return out

expected = {2:4,3:8,4:14,5:20,6:28,7:42,8:66}

for n, optimum in expected.items():
    row = cert["values"][str(n)]
    assert row["maximum"] == optimum
    words = [''.join(p) for p in product('01', repeat=n)]
    D = {w: desc2(w) for w in words}

    witness = row["witness"]
    assert len(witness) == optimum
    assert len(set(witness)) == optimum
    assert all(w in D for w in witness)
    for i, a in enumerate(witness):
        for b in witness[:i]:
            assert D[a].isdisjoint(D[b])

    groups = row["conflict_clique_cover"]
    assert len(groups) == optimum
    flat = [w for g in groups for w in g]
    assert len(flat) == len(words)
    assert sorted(flat) == words
    for g in groups:
        assert g
        for i, a in enumerate(g):
            for b in g[:i]:
                assert D[a] & D[b]

# The first two cases are genuinely collision-free.
for n in (2,3):
    words = [''.join(p) for p in product('01', repeat=n)]
    D = [desc2(w) for w in words]
    for i in range(len(words)):
        for j in range(i):
            assert D[i].isdisjoint(D[j])

print("VERIFY_OK")
