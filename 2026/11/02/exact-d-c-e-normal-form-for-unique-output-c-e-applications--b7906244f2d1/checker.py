"""Finite consistency checks for unique-output selections from binary relations.

Run with Python 3. No nonstandard dependencies. These finite checks do not
prove the computability-theoretic statements for infinite enumerations.
"""

from itertools import product

N = 3


def relation(mask):
    return {(i, j) for i in range(N) for j in range(N) if mask & (1 << (N * i + j))}


def data(R):
    rows = [{j for (x, j) in R if x == i} for i in range(N)]
    first = {i: min(row) for i, row in enumerate(rows) if row}
    erased = {i for i, row in enumerate(rows) if len(row) >= 2}
    unique = {i: next(iter(row)) for i, row in enumerate(rows) if len(row) == 1}
    assert {i: v for i, v in first.items() if i not in erased} == unique
    return first, erased, unique


cases = [data(relation(mask)) for mask in range(1 << (N * N))]

for first, erased, unique in cases:
    # The converse finite representation: include the chosen output,
    # and on erased inputs introduce one different output.
    S = {(i, v) for i, v in first.items()}
    S |= {(i, (first[i] + 1) % N) for i in erased}
    assert data(S)[2] == unique

for fg, bg, f in cases:
    for hk, dh, h in cases:
        composed = {i: h[f[i]] for i in f if f[i] in h}
        l = {i: hk[fg[i]] for i in fg if fg[i] in hk}
        e = {i for i in l if i in bg or fg[i] in dh}
        assert {i: v for i, v in l.items() if i not in e} == composed

print(f"ALL_CHECKS_OK relations={len(cases)} composition_pairs={len(cases)**2}")
