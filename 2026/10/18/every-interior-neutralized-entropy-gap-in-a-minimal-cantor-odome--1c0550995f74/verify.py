"""Finite exact-rational checks of the scale/combinatorial lemmas.

This is not a proof of the asymptotic statements; see RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from math import log


def audit():
    # A finite heterogeneous-level Cantor odometer; both contraction regimes occur.
    N = 7
    c = [Fraction(1, 9)] * 2 + [Fraction(1, 3)] * (N - 2)
    a = [Fraction(1)]
    for factor in c:
        a.append(a[-1] * factor)
    delta = Fraction(1, 3)
    points = []
    for state in range(1 << N):
        points.append(sum((1 - c[k]) * a[k] for k in range(N)
                          if state & (1 << k)))
    checked = 0
    for x, y in combinations(range(1 << N), 2):
        k = ((x ^ y) & -(x ^ y)).bit_length()  # first different digit (one-indexed)
        ultra = a[k-1]
        for t in (0, 1, 2, 3, 13, 37):
            xx = (x + t) % (1 << N)
            yy = (y + t) % (1 << N)
            assert ((xx ^ yy) & -(xx ^ yy)).bit_length() == k
            dist = abs(points[xx] - points[yy])
            assert delta * ultra <= dist <= ultra
            checked += 3
    for block in range(1, 9):
        lengths = [2 ** (j*j) for j in range(1, block + 1)]
        total = sum(lengths)
        S = sum(m * log(9 if j % 2 else 3) for j,m in enumerate(lengths,1))
        d = total * log(2) / S
        target = log(2) / log(9 if block % 2 else 3)
        assert log(2)/log(9) - 1e-12 <= d <= log(2)/log(3) + 1e-12
        if block >= 5:
            assert abs(d - target) < 0.01
        checked += 2
    print(f'PASS {checked} finite exact-rational/computed endpoint assertions')


if __name__ == '__main__':
    audit()
