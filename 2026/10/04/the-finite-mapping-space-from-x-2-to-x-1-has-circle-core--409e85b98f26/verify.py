#!/usr/bin/env python3
from pathlib import Path
import itertools
import json

HERE = Path(__file__).resolve().parent
CERT = json.loads((HERE / "beat_certificate.json").read_text(encoding="utf-8"))
SOURCE_LEVELS = tuple(CERT["source_levels"])
TARGET_LEVELS = tuple(CERT["target_levels"])

def source_le(i, j):
    return i == j or SOURCE_LEVELS[i] < SOURCE_LEVELS[j]

def target_le(a, b):
    return a == b or TARGET_LEVELS[a] < TARGET_LEVELS[b]

def monotone(f):
    return all(
        (not source_le(i, j)) or target_le(f[i], f[j])
        for i in range(len(SOURCE_LEVELS))
        for j in range(len(SOURCE_LEVELS))
    )

def map_le(f, g):
    return all(target_le(a, b) for a, b in zip(f, g))

maps = {
    tuple(f)
    for f in itertools.product(range(len(TARGET_LEVELS)), repeat=len(SOURCE_LEVELS))
    if monotone(f)
}
assert len(maps) == CERT["map_count"] == 44

alive = set(maps)
seen = set()
up_count = 0
down_count = 0

for step in CERT["deletions"]:
    point = tuple(step["point"])
    witness = tuple(step["witness"])
    assert point in alive and witness in alive and point != witness
    assert point not in seen
    seen.add(point)

    if step["type"] == "up":
        strict_upper = [g for g in alive if g != point and map_le(point, g)]
        minima = [
            g for g in strict_upper
            if not any(h != g and map_le(h, g) for h in strict_upper)
        ]
        assert minima == [witness] or set(minima) == {witness}
        up_count += 1
    elif step["type"] == "down":
        strict_lower = [g for g in alive if g != point and map_le(g, point)]
        maxima = [
            g for g in strict_lower
            if not any(h != g and map_le(g, h) for h in strict_lower)
        ]
        assert maxima == [witness] or set(maxima) == {witness}
        down_count += 1
    else:
        raise AssertionError("unknown deletion type")
    alive.remove(point)

expected_core = {tuple(x) for x in CERT["expected_core"]}
assert alive == expected_core
assert len(alive) == 4
assert len(CERT["deletions"]) == 40
assert (up_count, down_count) == (20, 20)

constants = {tuple([y] * len(SOURCE_LEVELS)) for y in range(len(TARGET_LEVELS))}
assert alive == constants

# The induced order on the four constants is exactly the target order.
for a in range(len(TARGET_LEVELS)):
    for b in range(len(TARGET_LEVELS)):
        ca = tuple([a] * len(SOURCE_LEVELS))
        cb = tuple([b] * len(SOURCE_LEVELS))
        assert map_le(ca, cb) == target_le(a, b)

# No remaining point is a beat point.
for point in alive:
    strict_upper = [g for g in alive if g != point and map_le(point, g)]
    minima = [
        g for g in strict_upper
        if not any(h != g and map_le(h, g) for h in strict_upper)
    ]
    strict_lower = [g for g in alive if g != point and map_le(g, point)]
    maxima = [
        g for g in strict_lower
        if not any(h != g and map_le(g, h) for h in strict_lower)
    ]
    assert len(minima) != 1
    assert len(maxima) != 1

print("VERIFY_OK maps=44 deletions=40 up=20 down=20 core=4")
