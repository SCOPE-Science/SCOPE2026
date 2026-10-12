#!/usr/bin/env python3
"""Verify the absorption-class count for fourth-level quantifier patterns.

Symbols:
  E = exists
  A = forall
  I = exists infinitely often
  J = forall eventually

The hierarchy recursion and absorption rewrites are those in Kihara,
"The arithmetical hierarchy: A realizability-theoretic perspective",
Definition 2.3 and Definition 2.6.
"""
from functools import lru_cache
from itertools import product

ALPHABET = ("E", "A", "I", "J")

def prepend(q, state):
    side, n = state
    if side == "S":
        return {
            "E": ("S", n),
            "A": ("P", n + 1),
            "I": ("P", n + 1),
            "J": ("S", n + 2),
        }[q]
    return {
        "E": ("S", n + 1),
        "A": ("P", n),
        "I": ("P", n + 2),
        "J": ("S", n + 1),
    }[q]

def hierarchy_state(word):
    state = {
        "E": ("S", 1),
        "A": ("P", 1),
        "I": ("P", 2),
        "J": ("S", 2),
    }[word[-1]]
    for q in reversed(word[:-1]):
        state = prepend(q, state)
    return state

def normalized(word):
    return all(
        not (word[i] == word[i + 1] and word[i] in ("E", "A"))
        for i in range(len(word) - 1)
    )

def collapse_ordinary_runs(word):
    out = []
    for q in word:
        if out and q in ("E", "A") and out[-1] == q:
            continue
        out.append(q)
    return "".join(out)

@lru_cache(None)
def reductions(word):
    choices = [""]
    for q in word:
        replacements = [q]
        if q == "I":
            replacements.append("AE")
        elif q == "J":
            replacements.append("EA")
        choices = [prefix + replacement
                   for prefix in choices
                   for replacement in replacements]
    return frozenset(collapse_ordinary_runs(w) for w in choices)

def is_subsequence(small, large):
    pos = 0
    for q in large:
        if pos < len(small) and small[pos] == q:
            pos += 1
    return pos == len(small)

def absorbs(source, target):
    # Exact normal form for the rewrite preorder:
    # expand any original I/J if desired, contract ordinary duplicates,
    # then use arbitrary insertions to fill out the target.
    return any(is_subsequence(r, target) for r in reductions(source))

def normalized_patterns(side, level):
    by_length = {}
    all_patterns = []
    for length in range(1, 9):
        words = []
        for tup in product(ALPHABET, repeat=length):
            word = "".join(tup)
            if normalized(word) and hierarchy_state(word)[1] <= 4:
                words.append(word)
        by_length[length] = words
        all_patterns.extend(
            w for w in words if hierarchy_state(w) == (side, level)
        )
    return by_length, all_patterns

def mutual_classes(words):
    remaining = set(words)
    result = []
    while remaining:
        seed = min(remaining, key=lambda w: (len(w), w))
        cls = {
            w for w in words
            if absorbs(seed, w) and absorbs(w, seed)
        }
        # The rewrite relation is a preorder; this is a consistency check
        # that the computed mutual class is pairwise mutual.
        for u in cls:
            for v in cls:
                assert absorbs(u, v) and absorbs(v, u)
        result.append(sorted(cls, key=lambda w: (len(w), w)))
        remaining.difference_update(cls)
    return sorted(result, key=lambda c: (len(c[0]), c[0]))

sigma_by_length, sigma4 = normalized_patterns("S", 4)
pi_by_length, pi4 = normalized_patterns("P", 4)

# Ordinary duplicate contraction is mutually reversible by insertion, so
# normalized representatives suffice.  No normalized pattern of length 8
# has hierarchy level <= 4; prepending never lowers the level, so there can
# be no longer normalized fourth-or-lower-level pattern.
assert len(sigma_by_length[8]) == 0
assert len(pi_by_length[8]) == 0

# Sanity check against the source's explicit Sigma_3 saturation:
# there are 17 normalized Sigma_3 patterns.
sigma3 = []
for length in range(1, 8):
    for tup in product(ALPHABET, repeat=length):
        word = "".join(tup)
        if normalized(word) and hierarchy_state(word) == ("S", 3):
            sigma3.append(word)
assert len(sigma3) == 17

sigma_classes = mutual_classes(sigma4)
pi_classes = mutual_classes(pi4)

assert len(sigma4) == 61
assert len(pi4) == 61
assert len(sigma_classes) == 37
assert len(pi_classes) == 37

sigma_reps = [c[0] for c in sigma_classes]
pi_reps = [c[0] for c in pi_classes]

expected_sigma_reps = [
    "JJ",
    "EAJ", "EIA", "EIJ", "EJJ", "JAJ", "JEA", "JEJ", "JIA", "JIJ", "JJA",
    "EAEA", "EAEJ", "EAIA", "EAIJ", "EAJA", "EIEA", "EIEJ", "EIJA",
    "EJEA", "EJEJ", "EJIA", "EJIJ", "EJJA",
    "JAEA", "JAEJ", "JAIA", "JAIJ", "JAJA", "JIEA", "JIEJ", "JIJA",
    "EAIJA", "EJIEA", "EJIEJ", "EJIJA", "JAIJA",
]
assert sigma_reps == expected_sigma_reps

counts = []
for length in range(1, 9):
    words = sigma_by_length[length]
    counts.append((
        length,
        len(words),
        sum(hierarchy_state(w) == ("S", 4) for w in words),
        sum(hierarchy_state(w) == ("P", 4) for w in words),
    ))

print("length,total_level_le_4,sigma4,pi4")
for row in counts:
    print(",".join(map(str, row)))
print("SIGMA3_NORMALIZED=" + str(len(sigma3)))
print("SIGMA4_NORMALIZED=" + str(len(sigma4)))
print("PI4_NORMALIZED=" + str(len(pi4)))
print("SIGMA4_MUTUAL_ABSORPTION_CLASSES=" + str(len(sigma_classes)))
print("PI4_MUTUAL_ABSORPTION_CLASSES=" + str(len(pi_classes)))
print("SIGMA4_REPRESENTATIVES=" + ",".join(sigma_reps))
print("PI4_REPRESENTATIVES=" + ",".join(pi_reps))
print("VERIFY_OK")
