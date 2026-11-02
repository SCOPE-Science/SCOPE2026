"""Finite direct checks for persistent, glut-free bilateral valuations.

The proof of the first-order asymptotic statements is mathematical, not
based on these finite enumeration tests.
"""
from itertools import product
from fractions import Fraction
from math import log2

N, T, F = 0, 1, 2

def classify(a, b):
    counts = [0, 0, 0]
    for s in product((N, T, F), repeat=a+b):
        bottom, top = s[:a], s[a:]
        if not all(x == N or x == y for x in bottom for y in top):
            continue
        colors = set(bottom)
        if colors == {N}:
            counts[0] += 1
        elif T in colors:
            assert F not in colors
            counts[1] += 1
        else:
            assert F in colors and T not in colors
            counts[2] += 1
    return tuple(counts)

cases = 0
models = 0
for a in range(1, 6):
    for b in range(1, 6):
        c = classify(a, b)
        assert c == (3**b, 2**a-1, 2**a-1), (a, b, c)
        z = sum(c)
        assert Fraction(c[1] + c[2], z) == Fraction(2*(2**a-1), 3**b+2*(2**a-1))
        cases += 1
        models += z

# Stable bounded finite arithmetic checks of the scaling identity.
alpha = log2(3)
for b in (20, 60, 100, 1000):
    a = int(alpha*b)
    delta = a-alpha*b
    w = 2*(2**a-1)/(3**b+2*(2**a-1))
    critical = 2**(delta+1)/(1+2**(delta+1))
    assert abs(w-critical) < 3e-6, (a,b,w,critical)
    assert 0.49 <= w <= 0.68
print('ALL_CHECKS_OK', 'size_pairs='+str(cases), 'admissible_models='+str(models), 'scales=4')
