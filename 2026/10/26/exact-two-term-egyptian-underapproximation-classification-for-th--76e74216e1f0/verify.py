#!/usr/bin/env python3
"""Exact-arithmetic verification of the finite competitor table in RESULT.md."""
from fractions import Fraction
from collections import defaultdict

def ceil_fraction(x):
    return -((-x.numerator) // x.denominator)

candidates = []
for u in range(5, 8):
    v = 7
    while Fraction(v, 1) < Fraction(4*u, u-4):
        C = Fraction(1, u) + Fraction(1, v)
        A = ceil_fraction(1 / (C - Fraction(1, 4)))
        G = Fraction(1, 4) + Fraction(1, A)
        upper = Fraction(1, 4) + Fraction(1, A-1)
        assert G <= C < upper
        candidates.append((u, v, A, C, G))
        v += 1

assert len(candidates) == 21
assert [(u,v) for u,v,_,_,_ in candidates] == (
    [(5,v) for v in range(7,20)] +
    [(6,v) for v in range(7,12)] +
    [(7,v) for v in range(7,10)]
)

groups = defaultdict(list)
for row in candidates:
    if row[2] >= 13:
        groups[row[2]].append(row)

tie = sorted(a for a, rows in groups.items()
             if all(C == G for _,_,_,C,G in rows))
strict = sorted(a for a, rows in groups.items()
                if any(C > G for _,_,_,C,G in rows))
assert tie == [20,24,28,30,36,56,60,80,132,180,252,380]
assert strict == [14,17,25,38,47,114]

threshold = {
    14: Fraction(13,40), 17: Fraction(13,42),
    25: Fraction(16,55), 38: Fraction(18,65),
    47: Fraction(19,70), 114: Fraction(22,85)
}
for a, c in threshold.items():
    observed = min(row[3] for row in groups[a])
    assert observed == c
    assert Fraction(1,4)+Fraction(1,a) < c < Fraction(1,4)+Fraction(1,a-1)
for a in tie:
    assert all(C == Fraction(1,4)+Fraction(1,a)
               for _,_,_,C,_ in groups[a])

print("VERIFY_OK: 21 candidate pairs; 19 relevant greedy denominators; "
      "6 strict-failure denominators; 12 tie denominators.")
