"""Diagram-level audit of the corrected fixed-position relative census."""
import json
import math
import runpy
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ledger = json.loads((ROOT / "ledger.json").read_text(encoding="utf-8"))
ends = (-2, -2, 1, 3)
seen = set()
counts = Counter()
totals = Counter()
quantum = defaultdict(int)
for d in ledger["diagrams"]:
    p = d["psi_position"]
    sizes, edges, attach, weights, bits = (d[x] for x in ("sizes", "edges", "attach", "w", "bits"))
    assert sorted(sizes) == [0, 1, 1, 1] and len(edges) == 3
    assert len(attach) == 4 and len(weights) == len(bits) == 3
    reached = {0}
    while True:
        new = reached | {a for a, b in edges if b in reached} | {b for a, b in edges if a in reached}
        if new == reached:
            break
        reached = new
    assert reached == set(range(4))
    key = (p, tuple(sizes), tuple(map(tuple, edges)), tuple(attach), tuple(weights), tuple(bits))
    assert key not in seen
    seen.add(key)
    thick = [0] * 4
    balance = [0] * 4
    flags = [[] for _ in range(4)]
    for (a, b), w, bit in zip(edges, weights, bits):
        assert 0 <= a < b < 4 and 1 <= w <= 4 and bit in (0, 1)
        balance[a] += w
        balance[b] -= w
        thick[a if bit == 0 else b] += 1
        flags[a].append((w, bit == 0))
        flags[b].append((-w, bit == 1))
    for i, a in enumerate(attach):
        assert a in range(4)
        balance[a] += ends[i]
        flags[a].append((ends[i], False))
    assert balance == [0] * 4
    required = [(i == p) + 2 - 2 * sizes[i] for i in range(4)]
    assert thick == required == d["t"]
    for i in range(4):
        if sizes[i] == 0:
            assert all(th for _, th in flags[i])
            assert len(flags[i]) == (3 if i == p else 2)
            if i != p:
                assert sum(w for w, _ in flags[i]) == 0
    assert d["mult"] == math.prod(weights)
    counts[p] += 1
    totals[p] += d["mult"]
    poly = {0: 1}
    for w in weights:
        next_poly = defaultdict(int)
        for e, c in poly.items():
            for k in range(w):
                next_poly[e + w - 1 - 2 * k] += c
        poly = next_poly
    for e, c in poly.items():
        quantum[e] += c
assert [counts[p] for p in range(4)] == [43, 37, 37, 43]
assert [totals[p] for p in range(4)] == [352] * 4
assert len(seen) == ledger["summed_diagrams"] == 160
assert sum(totals.values()) == ledger["sum_of_four_invariants"] == 1408
assert [quantum[e] for e in range(-9, 10)] == [4,2,18,12,54,42,132,110,236,188,236,110,132,42,54,12,18,2,4]
assert all(quantum[e] == quantum[-e] for e in quantum)
model = runpy.run_path(str(ROOT / "enumerate.py"))
expected = set()
for p in range(4):
    for d in model["census"](p):
        expected.add((p, d["sizes"], d["edges"], d["attach"], d["w"], d["bits"]))
assert seen == expected
print("VERIFY_CORRECTED_OK: 160 nonzero diagrams; fixed-position invariants 352 each; four-position sum 1408.")

