#!/usr/bin/env python3
import json
from pathlib import Path

def complement(w):
    return "".join("1" if c == "0" else "0" for c in w)

def suffix_encounters_cube(w):
    n = len(w)
    for m in range(1, n // 3 + 1):
        s = w[n - 3*m:]
        a, b, c = s[:m], s[m:2*m], s[2*m:]
        ar = a[::-1]
        if b in (a, ar) and c in (a, ar):
            return True
    return False

def contains_cube_direct(w):
    n = len(w)
    for i in range(n):
        for m in range(1, (n - i) // 3 + 1):
            a = w[i:i+m]
            b = w[i+m:i+2*m]
            c = w[i+2*m:i+3*m]
            ar = a[::-1]
            if b in (a, ar) and c in (a, ar):
                return True
    return False

root = Path(__file__).resolve().parent
cert = json.loads((root / "certificate.json").read_text(encoding="utf-8"))

survivors = [""]
counts = [1]
level9 = None
for n in range(1, 11):
    nxt = []
    for w in survivors:
        for bit in "01":
            q = w + bit
            if not suffix_encounters_cube(q):
                nxt.append(q)
    survivors = nxt
    counts.append(len(survivors))
    if n == 9:
        level9 = sorted(survivors)

assert counts == cert["survivor_counts_by_length_0_to_10"]
assert level9 == sorted(cert["length_9_extremizers"])
assert counts[9] == 6
assert counts[10] == 0

# Whole-word recheck of the boundary cases without relying on prefix pruning.
assert all(not contains_cube_direct(w) for w in level9)

def orbit(w):
    c = complement(w)
    return {w, w[::-1], c, c[::-1]}

remaining = set(level9)
computed = []
while remaining:
    w = min(remaining)
    o = orbit(w) & set(level9)
    computed.append(sorted(o))
    remaining -= o
computed = sorted(computed)
expected = sorted(sorted(o) for o in cert["symmetry_orbits"])
assert computed == expected
assert sorted(len(o) for o in computed) == [2, 4]

# The two-element orbit consists of complementary palindromes.
assert level9[0] == level9[0][::-1]
assert complement(level9[0]) == "110010011"
assert "110010011" == "110010011"[::-1]

print(
    "VERIFY_OK max=9 count9=6 count10=0 orbits=2 orbit_sizes=2,4 counts="
    + ",".join(str(x) for x in counts)
)
