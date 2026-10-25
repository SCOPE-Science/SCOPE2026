#!/usr/bin/env python3
"""Exact finite checks for the binary block-language union family.

The proof is symbolic for every d >= 2. This script independently computes
right quotients for small d and checks the predicted rank profile and count.
Only the Python standard library is required.
"""
from itertools import product

A = {"00", "10"}
B = {"01", "10"}

def words_from_blocks(blocks, d):
    return {"".join(t) for t in product(sorted(blocks), repeat=d)}

def language(d):
    return words_from_blocks(A, d) | words_from_blocks(B, d)

def nonempty_quotient_counts(d):
    L = language(d)
    counts = []
    for t in range(2*d + 1):
        suffix_len = 2*d - t
        suffixes = ["".join(x) for x in product("01", repeat=suffix_len)]
        quotients = set()
        for pref_tuple in product("01", repeat=t):
            p = "".join(pref_tuple)
            residual = frozenset(s for s in suffixes if p+s in L)
            if residual:
                quotients.add(residual)
        counts.append(len(quotients))
    return counts

def expected_profile(d):
    out = []
    for t in range(2*d + 1):
        if t % 2 == 0:
            if t == 0 or t == 2*d:
                out.append(1)
            else:
                out.append(3)
        else:
            j = (t-1)//2
            if j == 0:
                out.append(2)
            elif j == d-1:
                out.append(3)
            else:
                out.append(5)
    return out

for d in range(2, 9):
    got = nonempty_quotient_counts(d)
    exp = expected_profile(d)
    assert got == exp, (d, got, exp)
    states = sum(got) + 1  # one common dead/sink quotient
    assert states == 8*d - 5, (d, states)
    rank_bound = 5*d + 3*(d-1) + 3
    assert rank_bound == 8*d
    assert rank_bound - states == 5
    print(f"d={d}: profile={got}; sc(union)={states}; rank-bound={rank_bound}; gap={rank_bound-states}")
print("VERIFY_OK")
