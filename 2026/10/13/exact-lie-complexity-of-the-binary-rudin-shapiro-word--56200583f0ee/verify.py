#!/usr/bin/env python3
"""Finite checks for a symbolic proof of the Rudin--Shapiro Lie complexity.
This script only checks finite certificates; the all-length argument is in RESULT.md.
"""
from collections import defaultdict
import json
from pathlib import Path

SIGMA = {"a": "ab", "b": "ac", "c": "db", "d": "dc"}
TAU = {"a": "0", "b": "0", "c": "1", "d": "1"}
ALPHABET = tuple(SIGMA)

def substitute(word):
    return "".join(SIGMA[x] for x in word)

def phi(word):
    return "".join(TAU[x] for x in word)

def high_block(x, k):
    word = x
    for _ in range(k):
        word = substitute(word)
    return phi(word)

def bigram_closure():
    # Start from the prefix sigma(a)=ab. Under substitution, every old
    # bigram xy creates the boundary sigma(x)[-1]sigma(y)[0].
    pairs = {"ab"}
    for _ in range(20):
        nxt = set(pairs)
        for x in SIGMA:
            nxt.add(SIGMA[x])
        for xy in pairs:
            nxt.add(SIGMA[xy[0]][-1] + SIGMA[xy[1]][0])
        if nxt == pairs:
            return pairs
        pairs = nxt
    raise AssertionError("bigram closure did not stabilize")

PAIRS = bigram_closure()
assert PAIRS == {"ab", "ac", "ba", "bd", "ca", "cd", "db", "dc"}
assert {phi(SIGMA[x]) for x in SIGMA} == {"00", "01", "10", "11"}

# Every factor length <= 2^k is inside sigma^k(xy) with xy a legal
# two-letter factor of the four-letter fixed point. Conversely every
# listed xy occurs, so these are EXACT finite factor sets.
def complete_factors(n, supertile_power=None):
    k = max(1, (n - 1).bit_length()) if supertile_power is None else supertile_power
    width = 1 << k
    assert width >= n
    blocks = {x: high_block(x, k) for x in SIGMA}
    by_phase = (set(), set())
    for xy in PAIRS:
        encoded = blocks[xy[0]] + blocks[xy[1]]
        for offset in range(width):
            by_phase[offset & 1].add(encoded[offset : offset + n])
    return by_phase

def lie_classes(n, factors):
    good = set()
    for word in factors:
        conjugates = [word[j:] + word[:j] for j in range(n)]
        if all(v in factors for v in conjugates):
            good.add(min(conjugates))
    return good

def cyclic_min(word):
    return min(word[j:] + word[:j] for j in range(len(word)))

# Verify definition of the classical Rudin--Shapiro bits by adjacent
# binary digit pairs (not just by a downloaded/prefabricated prefix).
s = "a"
for _ in range(16):
    s = substitute(s)
w = phi(s)
def digit_rs(i):
    return ((i & (i >> 1)).bit_count()) % 2
assert len(w) == 1 << 16
assert all(int(w[i]) == digit_rs(i) for i in range(len(w)))
assert all(s[i] in ("a", "d") if i % 2 == 0 else s[i] in ("b", "c") for i in range(len(s)))

# Exact phase certificate, not sampled: sigma^4 supertiles and the
# closed legal-bigram set cover all 8-bit factors at all positions.
even8, odd8 = complete_factors(8, supertile_power=4)
assert (len(even8), len(odd8), len(even8 & odd8)) == (24, 32, 0)

expected = {1: 2, 2: 3, 3: 4, 4: 6, 5: 2, 6: 3, 7: 0, 8: 4}
small_classes = {}
for n, count in expected.items():
    factors = set.union(*complete_factors(n))
    cls = lie_classes(n, factors)
    assert len(cls) == count, (n, count, cls)
    small_classes[str(n)] = sorted(cls)

assert small_classes == {
    "1": ["0", "1"],
    "2": ["00", "01", "11"],
    "3": ["000", "001", "011", "111"],
    "4": ["0000", "0001", "0011", "0101", "0111", "1111"],
    "5": ["00001", "01111"],
    "6": ["000111", "001001", "011011"],
    "7": [],
    "8": ["00001001", "00010111", "00011101", "01101111"],
}

# Compare against the embedded small exhaustive certificate.
cert = json.loads(Path(__file__).with_name("certificate.json").read_text(encoding="utf-8"))
assert cert["all_four_letter_bigrams"] == sorted(PAIRS)
assert cert["phase_certificate"]["all_even_eight_factors"] == sorted(even8)
assert cert["phase_certificate"]["all_odd_eight_factors"] == sorted(odd8)
assert cert["short_lie_representatives"] == small_classes
assert cert["dyadic_representatives_k3"] == {x: high_block(x,3) for x in SIGMA}

# Independent boundary test: exact factor sets from all source bigrams
# agree with those seen in a long directly coded prefix for n<=24.
for n in range(1, 25):
    factors = set.union(*complete_factors(n))
    direct = {w[i:i+n] for i in range(len(w)-n+1)}
    assert direct == factors, (n,len(direct),len(factors))

# Check all short lengths, using exact full factor sets, rather than
# extrapolating from a prefix. These are diagnostic checks, not a proof
# of the all-length sparsity theorem.
for n in range(1, 129):
    F = set.union(*complete_factors(n))
    L = len(lie_classes(n, F))
    target = expected.get(n, 4 if n & (n - 1) == 0 else 0)
    assert L == target, (n,L,target)

# For the four long dyadic witnesses, every cut is exhibited inside
# one of the eight legal two-block concatenations. All four cyclic
# classes are checked distinct for k=3..9.
NEXT = {"a": "b", "b": "a", "c": "d", "d": "c"}
PREV = {"a": "c", "b": "d", "c": "a", "d": "b"}
for k in range(1, 10):
    B = {x: high_block(x, k) for x in SIGMA}
    width = 1 << k
    for x in SIGMA:
        assert x + NEXT[x] in PAIRS and PREV[x] + x in PAIRS
        low = B[x] + B[NEXT[x]]
        high = B[PREV[x]] + B[x]
        for t in range(width):
            rot = B[x][t:] + B[x][:t]
            witness = (low if t <= width//2 else high)[t:t+width]
            assert rot == witness,(x,k,t)
    if k >= 3:
        assert len({cyclic_min(B[x]) for x in SIGMA}) == 4

print("VERIFY_OK sigmabigrams=8 coded_blocks=4 8phase=24+32_disjoint "
      "exact_base_n=1..8 exact_factors_prefix_n<=24 "
      "exact_Lie_n<=128 witnesses_k=1..9 dyadic_classes_k=3..9")
