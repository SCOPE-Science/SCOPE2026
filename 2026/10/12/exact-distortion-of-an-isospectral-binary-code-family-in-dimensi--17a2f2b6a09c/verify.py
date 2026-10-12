"""Finite checks for a parameterized dimension-three binary code-distortion example.

Run: python3 verify.py  (standard library only).
The all-parameter proof is the weight-class/dependency argument in RESULT.md.
"""
from fractions import Fraction
from itertools import product

A0 = (0, 0, 0, 1, 1, 1, 3)
B0 = (0, 0, 0, 0, 2, 2, 2)
P = tuple(range(1, 8))

def weight_vector(multiplicities):
    return tuple(sum(multiplicities[p-1] for p in P
                     if (p & u).bit_count() % 2) for u in P)

def gl3():
    for basis in product(P, repeat=3):
        images = tuple(__import__('functools').reduce(
            int.__xor__, (basis[i] for i in range(3) if u & (1 << i)), 0)
            for u in P)
        if len(set(images)) == 7:
            yield images

maps = list(gl3())
assert len(maps) == 168
assert weight_vector(A0) == (4, 4, 2, 6, 2, 2, 4)
assert weight_vector(B0) == (4, 4, 4, 6, 2, 2, 2)
assert 3 ^ 5 ^ 6 == 0 and 5 ^ 6 ^ 7 != 0

for t in (0, 1, 2, 3, 5, 10, 100):
    a = tuple(x+t for x in A0)
    b = tuple(x+t for x in B0)
    assert sum(a) == sum(b) == 6+7*t
    wa, wb = weight_vector(a), weight_vector(b)
    assert sorted(wa) == sorted(wb) == sorted((4*t+2,)*3+(4*t+4,)*3+(4*t+6,))
    distortions = []
    for m in maps:
        ratios = [Fraction(wb[m[u-1]-1], wa[u-1]) for u in P]
        distortions.append(max(ratios)/min(ratios))
    predicted = Fraction((2*t+2)**2, (2*t+1)**2)
    assert min(distortions) == predicted
    assert distortions.count(predicted) == 60

print('VERIFY_OK')
