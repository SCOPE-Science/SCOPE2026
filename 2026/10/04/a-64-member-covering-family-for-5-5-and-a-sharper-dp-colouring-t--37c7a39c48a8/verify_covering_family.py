#!/usr/bin/env python3
import itertools
import json
import sys
from collections import Counter

path = sys.argv[1] if len(sys.argv) > 1 else "covering_family_5.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

assert data["l"] == 5
family = data["family"]
assert len(family) == 64

normalized = []
for member in family:
    assert len(member) == 5
    row = []
    for perm in member:
        assert len(perm) == 5
        assert sorted(perm) == [1, 2, 3, 4, 5]
        row.append(tuple(perm))
    normalized.append(tuple(row))

assert len(set(normalized)) == 64

hist = Counter()
for x in itertools.product(range(1, 6), repeat=5):
    multiplicity = 0
    for member in normalized:
        images = [member[i][x[i] - 1] for i in range(5)]
        if len(set(images)) == 5:
            multiplicity += 1
    assert multiplicity >= 1, f"uncovered tuple: {x}"
    hist[multiplicity] += 1

assert sum(hist.values()) == 5 ** 5
print(
    "ALL CHECKS PASSED; "
    f"family_size={len(normalized)}; "
    f"tuples={sum(hist.values())}; "
    f"minimum_coverage={min(hist)}; "
    f"maximum_coverage={max(hist)}"
)
