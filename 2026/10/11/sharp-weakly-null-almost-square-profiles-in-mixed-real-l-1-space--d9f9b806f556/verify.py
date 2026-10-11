#!/usr/bin/env python3
"""Exact-rational tests of the algebraic identities in the analytic theorem."""
from fractions import Fraction as F

identity = 0
for u_num in range(-12, 13):
    for v_num in range(-12, 13):
        u, v = F(u_num, 6), F(v_num, 8)
        assert (abs(u + v) + abs(u - v)) / 2 == max(abs(u), abs(v))
        identity += 1

profiles = 0
distances = 0
for k in range(11):
    a, b = F(k, 10), F(10-k, 10)
    for j in range(41):
        t = F(j, 10)
        # Two balanced diffuse signs: each isotype has half the diffuse mass.
        # This is algebraic and makes no finite-dimensional weak-null claim.
        if b:
            c = t / b
            signed_plus = a + b * (abs(1 + c) + abs(1 - c)) / 2
            signed_minus = signed_plus
        else:
            signed_plus = signed_minus = a + t
        envelope = max(F(1), a + t)
        assert signed_plus == signed_minus == envelope
        profiles += 1
    # A unit diffuse function has distance a + (1-b) from the
    # proportional diffuse point; disjoint support covers b=0.
    if b:
        candidate_distance = a + abs(b - 1)
    else:
        candidate_distance = F(2)
    assert candidate_distance == 2*a
    distances += 1
print(f"VERIFY_OK scalar_identities={identity} two_sign_profiles={profiles} distances={distances} arithmetic=exact")
