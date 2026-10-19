"""Finite exact-arithmetic checks accompanying the sharp shift-radius theorem.

These checks are sanity tests of finite algebra; the paper's infinite-product
claims are proved analytically using independent blocks and Borel--Cantelli.
"""
from fractions import Fraction as F


def finite_weight(K):
    return sum((F(1, 2) ** abs(j) for j in range(-K, K+1)), F(0))


def support_threshold(a, b):
    assert F(0) <= a <= b <= F(1)
    return F(3, 2) * (b-a)


for K in range(51):
    assert finite_weight(K) == 3 - F(2, 2**K)
    assert finite_weight(K) <= 3
assert support_threshold(F(0), F(1)) == F(3, 2)
assert support_threshold(F(1, 4), F(3, 4)) == F(3, 4)
for m in range(1, 201):
    a, b = F(1, 2)-F(1, 4*m), F(1, 2)+F(1, 4*m)
    assert support_threshold(a, b) == F(3, 4*m)
    assert max(abs(F(1, 2)-a), abs(F(1, 2)-b))*3 == support_threshold(a, b)
    for eps in (F(1, 10000), F(1, 3000)):
        if support_threshold(a, b) > eps:
            assert any((F(1, 2)-F(1, 100000))*finite_weight(k) > eps
                       for k in range(20))
# Explicit mass of the m-th component, and partial-sum check.
assert sum((F(1, 2**(m+1)) for m in range(1, 101)), F(0)) == F(1, 2)-F(1, 2**101)
for radius in (F(1, 2), F(1, 10), F(1, 100), F(1, 1000)):
    m = 1
    while F(3, 4*m) > radius:
        m += 1
    assert F(3, 4*m) <= radius
    assert F(1, 2**(m+1)) > 0
print("PASS: 51 exact weighted sums, 200 interval thresholds, mixture normalization and witness radii")
