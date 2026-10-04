#!/usr/bin/env python3
"""Coefficient regression for the L9a20 twist-family Alexander polynomials."""

from collections import defaultdict

K_TERMS = [
    (4,2,1),(4,1,-1),(3,2,-3),(3,1,4),(3,0,-1),
    (2,2,3),(2,1,-7),(2,0,3),(1,2,-1),(1,1,4),
    (1,0,-3),(0,1,-1),(0,0,1),
]
J_TERMS = [
    (2,4,1),(2,3,-3),(2,2,3),(2,1,-1),(1,4,-1),
    (1,3,4),(1,2,-7),(1,1,4),(1,0,-1),(0,3,-1),
    (0,2,3),(0,1,-3),(0,0,1),
]

def expand(terms, k):
    d = defaultdict(int)
    for a,b,c in terms:
        d[a*k+b] += c
    return {e:c for e,c in d.items() if c}

expected_K = {-2:7, -1:13, 1:9, 2:7}
expected_J = {-4:7, -3:7, -2:5, -1:13, 1:9, 2:7, 3:7}

for k, want in expected_K.items():
    got = max(abs(c) for c in expand(K_TERMS, k).values())
    assert got == want, (k, got, want)

for k, want in expected_J.items():
    got = max(abs(c) for c in expand(J_TERMS, k).values())
    assert got == want, (k, got, want)

for m in list(range(-500, -2)) + list(range(3, 501)):
    p = expand(K_TERMS, m)
    assert len(p) == 13
    assert 7 in {abs(c) for c in p.values()}

for n in list(range(-500, -4)) + list(range(4, 501)):
    p = expand(J_TERMS, n)
    assert len(p) == 13
    assert 7 in {abs(c) for c in p.values()}

print(
    "VERIFY_OK "
    "K_exceptional=4 "
    "J_exceptional=7 "
    "sampled_K=996 "
    "sampled_J=993 "
    "all_have_coefficient_abs_gt_1=true"
)
