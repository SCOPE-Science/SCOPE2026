"""Exact rational checks for a three-party finite-house apportionment boundary.

No numerical experiment is used as a proof of the continuum theorem.
Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement


def allocate(p, seats):
    q = tuple(seats * v for v in p)
    whole = [v.numerator // v.denominator for v in q]
    rem = [v - k for v, k in zip(q, whole)]
    awarded = seats - sum(whole)
    order = sorted(range(3), key=lambda i: rem[i], reverse=True)
    if 0 < awarded < 3 and rem[order[awarded-1]] == rem[order[awarded]]:
        return None  # cutoff tie: omitted from strict-region check
    for i in order[:awarded]:
        whole[i] += 1
    return tuple(whole)


def is_strict(p):
    return all(allocate(p, h) is not None for h in (1, 2, 3, 4))

# Vertex and area certificate, computed by exact integration.
lo, mid, hi = F(1, 9), F(5, 36), F(1, 6)
area1 = F(3, 4) * (mid-lo)**2
area2 = F(3, 4) * (hi-mid)**2
assert area1 == area2 == F(1, 1728)
assert 6 * 2 * (area1 + area2) == F(1, 72)

p = (F(4, 9), F(5, 12), F(5, 36))
assert tuple(allocate(p, h) for h in (1,2,3,4)) == (
    (1,0,0), (1,1,0), (1,1,1), (2,2,0))

checked = 0
losses = 0
for total in range(3, 181):
    for small in range(1, total//3 + 1):
        for medium in range(small, (total-small)//2 + 1):
            large = total - medium - small
            if not large >= medium:
                continue
            p = (F(large, total), F(medium, total), F(small, total))
            if not is_strict(p):
                continue
            a1, a2, a3, a4 = (allocate(p, h) for h in (1, 2, 3, 4))
            assert all(u <= v for u, v in zip(a1, a2))
            assert all(u <= v for u, v in zip(a2, a3))
            lost = any(u > v for u, v in zip(a3, a4))
            predicted = (p[0]-p[2] < F(1,3) and p[1]-p[2] > F(1,4))
            assert lost == predicted, (p, a3, a4, predicted)
            if lost:
                assert a3 == (1,1,1) and a4 == (2,2,0)
                losses += 1
            checked += 1
print('PASS exact area=1/72, first witness, strict rational profiles=',checked,
      'three-to-four losses=', losses)
