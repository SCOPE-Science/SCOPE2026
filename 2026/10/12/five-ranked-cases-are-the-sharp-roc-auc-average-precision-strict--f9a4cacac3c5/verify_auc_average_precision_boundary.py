#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction

def rankings(n, p):
    for pos in combinations(range(n), p):
        s = [0] * n
        for i in pos:
            s[i] = 1
        yield tuple(s)

def positive_ranks(seq):
    return tuple(i + 1 for i, x in enumerate(seq) if x)

def auc(seq):
    p = sum(seq)
    q = len(seq) - p
    ranks = positive_ranks(seq)
    displacement = sum(r - j for j, r in enumerate(ranks, 1))
    return Fraction(p * q - displacement, p * q)

def average_precision(seq):
    p = sum(seq)
    ranks = positive_ranks(seq)
    return sum((Fraction(j, r) for j, r in enumerate(ranks, 1)), Fraction(0, 1)) / p

def sign(x):
    return (x > 0) - (x < 0)

weak = {}
strict = {}
ranking_counts = {}

for n in range(2, 6):
    weak[n] = []
    strict[n] = []
    ranking_counts[n] = 0
    for p in range(1, n):
        seqs = list(rankings(n, p))
        ranking_counts[n] += len(seqs)
        for a, b in combinations(seqs, 2):
            da = sign(auc(a) - auc(b))
            dp = sign(average_precision(a) - average_precision(b))
            if da != dp:
                weak[n].append((p, a, b))
            if da * dp < 0:
                strict[n].append((p, a, b))

assert ranking_counts == {2: 2, 3: 6, 4: 14, 5: 30}
assert weak[2] == []
assert weak[3] == []
assert strict[2] == []
assert strict[3] == []
assert strict[4] == []

assert weak[4] == [
    (2, (1,0,0,1), (0,1,1,0))
]
a = (1,0,0,1)
b = (0,1,1,0)
assert auc(a) == auc(b) == Fraction(1,2)
assert average_precision(a) == Fraction(3,4)
assert average_precision(b) == Fraction(7,12)

expected_strict_5 = [
    (2, (1,0,0,0,1), (0,1,1,0,0)),
    (3, (1,0,0,1,1), (0,1,1,1,0)),
]
assert strict[5] == expected_strict_5

a = (1,0,0,0,1)
b = (0,1,1,0,0)
assert auc(a) == Fraction(1,2)
assert auc(b) == Fraction(2,3)
assert average_precision(a) == Fraction(7,10)
assert average_precision(b) == Fraction(7,12)

a = (1,0,0,1,1)
b = (0,1,1,1,0)
assert auc(a) == Fraction(1,3)
assert auc(b) == Fraction(1,2)
assert average_precision(a) == Fraction(7,10)
assert average_precision(b) == Fraction(23,36)

# Positive-label complement maps the P=2 strict pair to the P=3 strict pair,
# with pair order exchanged.
assert tuple(1-x for x in expected_strict_5[0][1]) == expected_strict_5[1][2]
assert tuple(1-x for x in expected_strict_5[0][2]) == expected_strict_5[1][1]

print("VERIFY_OK")
print("ranking_counts", ranking_counts)
print("first_weak_total", 4)
print("first_weak_layer", weak[4])
print("first_strict_total", 5)
print("first_strict_layer", strict[5])
