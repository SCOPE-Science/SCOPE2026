#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

def tables(N, P):
    Q = N - P
    for tp in range(1, P):
        fn = P - tp
        for fp in range(1, Q):
            tn = Q - fp
            yield (tp, fp, fn, tn)

def f1(t):
    tp, fp, fn, tn = t
    return Fraction(2*tp, 2*tp + fp + fn)

def balanced_accuracy(t, P, Q):
    tp, fp, fn, tn = t
    return (Fraction(tp, P) + Fraction(tn, Q)) / 2

def sign(x):
    return (x > 0) - (x < 0)

weak = {}
strict = {}
table_counts = {}

for N in range(4, 8):
    weak[N] = []
    strict[N] = []
    table_counts[N] = 0
    for P in range(2, N-1):
        Q = N - P
        ts = list(tables(N, P))
        table_counts[N] += len(ts)
        for a, b in combinations(ts, 2):
            df = sign(f1(a) - f1(b))
            db = sign(balanced_accuracy(a, P, Q) - balanced_accuracy(b, P, Q))
            if df != db:
                weak[N].append((P, a, b))
            if df * db < 0:
                strict[N].append((P, a, b))

assert table_counts == {4:1, 5:4, 6:10, 7:20}

assert weak[4] == []
assert weak[5] == []
assert strict[4] == []
assert strict[5] == []
assert strict[6] == []

assert weak[6] == [
    (3, (1,1,2,2), (2,2,1,1))
]
a = (1,1,2,2)
b = (2,2,1,1)
assert f1(a) == Fraction(2,5)
assert f1(b) == Fraction(4,7)
assert balanced_accuracy(a,3,3) == Fraction(1,2)
assert balanced_accuracy(b,3,3) == Fraction(1,2)

expected7 = [
    (3, (1,1,2,3), (2,3,1,1)),
    (4, (1,1,3,2), (2,2,2,1)),
    (4, (2,1,2,2), (3,2,1,1)),
]
assert strict[7] == expected7
assert weak[7] == expected7

checks = [
    (3, (1,1,2,3), (2,3,1,1),
     Fraction(2,5), Fraction(1,2), Fraction(13,24), Fraction(11,24)),
    (4, (1,1,3,2), (2,2,2,1),
     Fraction(1,3), Fraction(1,2), Fraction(11,24), Fraction(5,12)),
    (4, (2,1,2,2), (3,2,1,1),
     Fraction(4,7), Fraction(2,3), Fraction(7,12), Fraction(13,24)),
]
for P, a, b, fa, fb, ba, bb in checks:
    Q = 7-P
    assert f1(a) == fa and f1(b) == fb
    assert balanced_accuracy(a,P,Q) == ba
    assert balanced_accuracy(b,P,Q) == bb
    assert fa < fb and ba > bb

# Common positive scaling preserves both metrics, so the first witness
# recurs at total 7q with prevalence 3q.
for q in range(1, 8):
    a = tuple(q*x for x in (1,1,2,3))
    b = tuple(q*x for x in (2,3,1,1))
    P = 3*q
    Q = 4*q
    assert f1(a) == Fraction(2,5)
    assert f1(b) == Fraction(1,2)
    assert balanced_accuracy(a,P,Q) == Fraction(13,24)
    assert balanced_accuracy(b,P,Q) == Fraction(11,24)

print("VERIFY_OK")
print("table_counts", table_counts)
print("first_weak_total", 6)
print("first_weak_pair", weak[6])
print("first_strict_total", 7)
print("first_strict_layer", strict[7])
