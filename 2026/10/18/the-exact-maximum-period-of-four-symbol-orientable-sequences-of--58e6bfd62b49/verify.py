#!/usr/bin/env python3
"""Exact checks for a cyclic orientable word over four symbols (stdlib only)."""
from itertools import product
from pathlib import Path

ALPHABET = "0123"
N = 4
s = Path(__file__).with_name("WITNESS.txt").read_text(encoding="utf-8").strip()
assert len(s) == 106 and set(s) == set(ALPHABET)

# First method: direct windows, with cyclic wraparound; normalize orientation.
windows = ["".join(s[(i + j) % len(s)] for j in range(N)) for i in range(len(s))]
assert all(w != w[::-1] for w in windows)
assert len(set(windows)) == len(s)
classes = [min(w, w[::-1]) for w in windows]
assert len(set(classes)) == len(s)
assert all(w[::-1] not in windows for w in windows)

# Second method: independently enumerate all reversal classes in the full graph.
all_words = ("".join(w) for w in product(ALPHABET, repeat=N))
all_nonpal = {w for w in all_words if w != w[::-1]}
assert len(all_nonpal) == 240
all_classes = {min(w, w[::-1]) for w in all_nonpal}
assert len(all_classes) == 120
unused = sorted(all_classes.difference(classes))
assert len(unused) == 14

# Check the sharpness pattern of the omissions used in the upper-bound proof.
uniform = {min(a * 3 + b, b + a * 3)
           for a in ALPHABET for b in ALPHABET if a != b}
exceptional = {min(a + a + b + b, b + b + a + a)
               for a in ALPHABET for b in ALPHABET if a != b}
unused_uniform = sorted(set(unused).intersection(uniform))
unused_exceptional = sorted(set(unused).intersection(exceptional))
assert len(unused_uniform) == 4
assert len(unused_exceptional) == 6
assert len(unused) == 6 + 2 * len(unused_uniform)

# Verify the elementary full-graph degree facts at all twelve aab vertices.
for a in ALPHABET:
    for b in ALPHABET:
        if a == b:
            continue
        vertex = a + a + b
        inc = sum((c + vertex) in all_nonpal for c in ALPHABET)
        out = sum((vertex + c) in all_nonpal for c in ALPHABET)
        assert (inc, out) == (3, 4)

print("alphabet=4 window_order=4 period=106")
print("all_nonpalindromic_reversal_classes=120")
print("used_classes=106 missing_classes=14")
print("missing_reversal_class_representatives=" + ",".join(unused))
print("missing_uniform_vertex_classes=" + ",".join(unused_uniform))
print("missing_doublet_pair_classes=" + ",".join(unused_exceptional))
print("UNIQUE_ORIENTABLE_WINDOWS_OK")
