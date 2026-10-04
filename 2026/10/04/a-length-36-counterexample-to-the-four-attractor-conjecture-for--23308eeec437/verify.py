#!/usr/bin/env python3
from itertools import combinations

DELTA = "00101"
THETA = "EEEER"
TARGET = "010110010101100101101001101010011010"
GAMMA = {3, 7, 15, 21, 25}


def antimorphism(w, theta):
    r = w[::-1]
    if theta == "R":
        return r
    assert theta == "E"
    return "".join("1" if c == "0" else "0" for c in r)


def closure(u, theta):
    # Shortest theta-palindrome having u as prefix, found directly.
    for cut in range(len(u) + 1):
        suffix = u[cut:]
        if antimorphism(suffix, theta) == suffix:
            prefix = u[:cut]
            out = u + antimorphism(prefix, theta)
            assert out.startswith(u)
            assert antimorphism(out, theta) == out
            # Direct minimality check among all shorter prefix extensions.
            for L in range(len(u), len(out)):
                v = out[:L]
                assert antimorphism(v, theta) != v
            return out
    raise AssertionError("closure not found")


w = ""
prefixes = []
for delta, theta in zip(DELTA, THETA):
    w = closure(w + delta, theta)
    prefixes.append(w)
assert prefixes == [
    "01",
    "0101",
    "0101100101",
    "010110010101100101",
    TARGET,
]
assert len(TARGET) == 36
assert TARGET == TARGET[::-1]

# All distinct nonempty factors and every occurrence start.
factors = {}
for i in range(len(TARGET)):
    for j in range(i + 1, len(TARGET) + 1):
        f = TARGET[i:j]
        factors.setdefault(f, []).append(i)
assert len(factors) == 500


def eligible_mask(f):
    m = 0
    for start in factors[f]:
        for p in range(start, start + len(f)):
            m |= 1 << p
    return m

masks = {f: eligible_mask(f) for f in factors}
gamma_mask = sum(1 << p for p in GAMMA)
assert all(gamma_mask & m for m in masks.values())

# Transparent lower-bound certificate.  Every attractor must hit the union
# of positions occupied by all occurrences of each listed factor.
certificate = {
    "101101": ([15], set(range(15, 21))),
    "01011001010": ([0], set(range(0, 11))),
    "1100": ([3, 11], set(range(3, 7)) | set(range(11, 15))),
    "10101100": ([7], set(range(7, 15))),
    "00110101": ([21], set(range(21, 29))),
    "0011": ([21, 29], set(range(21, 25)) | set(range(29, 33))),
    "01010011010": ([25], set(range(25, 36))),
}
for f, (starts, eligible) in certificate.items():
    assert factors[f] == starts
    actual = {p for s in starts for p in range(s, s + len(f))}
    assert actual == eligible
    mask_positions = {p for p in range(36) if (masks[f] >> p) & 1}
    assert mask_positions == eligible

A = certificate["101101"][1]
G = certificate["01011001010"][1]
E = certificate["1100"][1]
D = certificate["10101100"][1]
C = certificate["00110101"][1]
B = certificate["0011"][1]
F = certificate["01010011010"][1]
assert not (G & E & D)
assert not (C & B & F)
assert (G | E | D) <= set(range(0, 15))
assert A <= set(range(15, 21))
assert (C | B | F) <= set(range(21, 36))
# Hence any hitting set for these seven factors needs at least 2+1+2=5 positions.

# Independent exhaustive replay of the finite lower bound: no four positions
# hit every distinct factor.
checked4 = 0
for comb in combinations(range(36), 4):
    checked4 += 1
    m = sum(1 << p for p in comb)
    assert not all(m & fm for fm in masks.values())
assert checked4 == 58905

print(
    "VERIFY_OK length=36 prefixes=5 distinct_factors=500 "
    "four_sets=58905 min_attractor=5 witness=3,7,15,21,25"
)
