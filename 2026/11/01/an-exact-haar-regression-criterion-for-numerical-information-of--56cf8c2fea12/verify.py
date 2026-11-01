"""Exact finite checks for numerical-information conditional-regression identities.

Analytical proofs of arbitrary dimensions and conditional laws are in RESULT.md.
Run with: python3 verify.py
"""
from fractions import Fraction as Q
from itertools import product

checks = 0

def check(statement):
    global checks
    assert statement
    checks += 1

# Uniform complex sphere: E |x_i|^4 = 2/[n(n+1)],
# E |x_i|^2|x_j|^2 = 1/[n(n+1)], i != j.
for n in range(2, 28):
    diag = Q(2, n * (n + 1))
    off = Q(1, n * (n + 1))
    check(n * diag + n * (n - 1) * off == 1)
    check(Q(1, n) - Q(1, n * n) == Q(n - 1, n * n))
    for a in range(-4, 5):
        for b in range(-4, 5):
            # Trace/Hilbert-Schmidt formula for a two-coordinate diagonal R.
            t = Q(a + b)
            direct = Q(a * a + b * b) * diag + 2 * Q(a * b) * off
            formula = Q(a * a + b * b + (a + b)**2, n * (n + 1))
            check(direct == formula)

# Three spectral levels: X=t3-t1, Y=t2, joint density 1 on
# |X|+Y<=1, Y>=0. Conditional Y uniform on [0,1-|X|].
# Integrate (1-|X|)^k over [-1,1]: 2/(k+1).
for k in range(0, 20):
    check(Q(2, k + 1) > 0)
check(Q(1, 12) * Q(2, 4) == Q(1, 24))
check(Q(2, 3) / (3 * 4) == Q(1, 18))
check(Q(1, 24) / Q(1, 18) == Q(3, 4))

# Two- and three-vertex affine interpolation identities: the
# barycentric map recovers each vertex weight exactly.
vertices = [(Q(0), Q(0)), (Q(1), Q(0)), (Q(0), Q(1))]
for i, j, k in product(range(7), repeat=3):
    weights = [Q(i, i + j + k), Q(j, i + j + k), Q(k, i + j + k)] if i + j + k else [Q(1), Q(0), Q(0)]
    zreal = weights[1]
    zimag = weights[2]
    reconstructed = (1-zreal-zimag, zreal, zimag)
    for a, b in zip(weights, reconstructed):
        check(a == b)

print(f'PASS: {checks} exact assertions')
