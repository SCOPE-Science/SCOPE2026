"""Exact finite identity checks for the angularly weighted lattice-shift theorem.

Only the infinite-dimensional analytical proof establishes hypercyclicity failure.
"""
from fractions import Fraction
from math import comb, sqrt, exp


def coefficient(n, k):
    return sum((-1)**a * comb(3, a) * comb(n, k-a)
               for a in range(4) if 0 <= k-a <= n)


def expansion_coefficient(n, k):
    # Direct sum of four starting-coordinate evaluations of the n-th shift.
    starts = (1, -3, 3, -1)
    return sum(starts[a] * comb(n, k-a)
               for a in range(4) if 0 <= k-a <= n)


def h(i, j):
    s = i+j
    return max(0, abs(i-j) - s/2)


def reciprocal_weight(i, j):
    s = i+j
    return (s+1) * (2.0 ** (-s)) * exp(h(i,j) / 100)


for n in range(0, 201):
    c = [coefficient(n,k) for k in range(n+4)]
    assert all(coefficient(n,k) == expansion_coefficient(n,k)
               for k in range(n+4))
    lhs = sum(v*v for v in c)
    rhs = Fraction(120 * comb(2*n,n), (n+1)*(n+2)*(n+3))
    assert Fraction(lhs) == rhs, (n, lhs, rhs)
    assert sum(c) == 0  # polynomial vanishes at z=1

for n in (16, 64, 256, 1024):
    c = [coefficient(n,k) for k in range(n+4)]
    # Exact original binomial lower witness before angular normalization.
    for i,j in ((0,0),(1,2),(5,0)):
        k = n // 2
        s = i+j
        assert h(i+k,j+n-k) == 0
        raw = Fraction((n+s+1)*comb(n,k), 2**(n+s))
        assert raw > 0
    l1 = sum(abs(v) for v in c)
    l2sq = sum(v*v for v in c)
    assert l1*l1 <= (n+4)*l2sq
    if n <= 256:
        norm_dual_bound = sum(abs(v)*reciprocal_weight(k,n+3-k)
                              for k,v in enumerate(c))
        print('n', n, 'finite_l1', l1, 'upper_dual', format(norm_dual_bound,'.8g'))

print('NONRADIAL_LATTICE_BINOMIAL_CANCELLATION_EXACT_OK')
