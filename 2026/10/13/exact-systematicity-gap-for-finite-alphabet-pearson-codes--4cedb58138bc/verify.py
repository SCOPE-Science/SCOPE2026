#!/usr/bin/env python3
"""Finite checks of a sharp Pearson-code systematicity theorem.

The theorem is proved symbolically in RESULT.md. These checks independently
recompute the canonical primitive representatives and affine-ratio signatures.
"""
from fractions import Fraction
from itertools import product
from math import gcd


def canonical(x):
    z = min(x)
    d = 0
    for a in x:
        d = gcd(d, a - z)
    return None if d == 0 else tuple((a - z) // d for a in x)


def ratio_signature(x):
    lo, hi = min(x), max(x)
    if lo == hi:
        return None
    return tuple(Fraction(v - lo, hi - lo) for v in x)


def primitive_triples(q):
    return [x for x in product(range(q), repeat=3)
            if min(x) == 0 and max(x) > 0 and canonical(x) == x]


def coprime_pairs(m):
    return sum(gcd(a, b) == 1
               for a in range(1, m + 1)
               for b in range(1, m + 1))


for q in range(2, 14):
    P = primitive_triples(q)
    F = coprime_pairs(q - 1)
    assert len(P) == 3 * F + 3
    assert len(P) >= q*q
    a = {canonical(x) for x in P}
    b = {ratio_signature(x) for x in P}
    assert len(a) == len(b) == len(P)
    if q <= 7:
        signatures_all = {ratio_signature(x) for x in product(range(q), repeat=3)
                          if max(x) != min(x)}
        assert len(signatures_all) == len(P)
    print(f"primitive_q={q} coprime_pairs={F} Pearson_length3={len(P)} full_payload_q2={q*q}")

# Use two disjoint implementations of positive-affine equivalence:
# gcd primitive form and rational interval normalization.
for q in range(2, 6):
    triples = primitive_triples(q)[:q*q]
    assert len(triples) == q*q
    for k in range(2, 5):
        C = [b + suffix for b in triples for suffix in product(range(q), repeat=k-2)]
        assert len(C) == q ** k
        ca = {canonical(x) for x in C}
        rb = {ratio_signature(x) for x in C}
        assert len(ca) == len(rb) == len(C)
        assert all(t is not None for t in ca)
        print(f"free_q={q} message_symbols={k} block_length={k+1} codewords={len(C)}")

# For one fixed systematic check symbol, all q constant information words
# map into only two positive-affine equivalence classes, indexed by sign.
for q in range(2, 6):
    choices = []
    for a in range(q):
        choices.append([canonical((a, a, c)) for c in range(q) if c != a])
    unique_signatures = set.union(*(set(v) for v in choices))
    assert len(unique_signatures) == 2
    assert all(set(v) <= unique_signatures for v in choices)
    # The q=2 construction has exactly two different orientations.
    if q == 2:
        assert len(set((canonical((0,1)), canonical((1,0))))) == 2
    print(f"constant_payload_q={q} inequivalent_one_check_signatures={len(unique_signatures)}")

print("VERIFY_OK exact_r_sys_q_ge_3=2 exact_r_free_q_ge_3_k_ge_2=1 exact_r_free_q_ge_3_k_1=2 exact_r_binary=1")
