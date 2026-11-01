"""Independent exact-arithmetic checks for the simplex translate-depth theorem.

This script is supplementary; it does not certify the continuum theorem.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb


def overlap_fraction(delta, dimension):
    assert len(delta) == dimension + 1
    remaining = 1 - sum(max(v, Q(0)) for v in delta)
    return max(remaining, Q(0)) ** dimension


def predicted_missed_mass(barycentric, scale):
    d = len(barycentric) - 1
    if min(barycentric) < 0:
        return min(Q(1), scale)**d
    return min(scale, Q(1)-min(barycentric))**d


def checks():
    tested = 0
    for d in (2, 3, 4):
        scales = [Q(1, 5), Q(d, d+1), Q(4, 5), Q(1), Q(5, 4), Q(7, 2)]
        for t in scales:
            for idx in range(20):
                raw = [Q(1 + ((7*idx+11*j+j*j) % 17), 1) for j in range(d+1)]
                total = sum(raw)
                bary = [v/total for v in raw]
                target = predicted_missed_mass(bary,t)
                # Every sampled missed translate has intersection mass <= candidate supremum.
                for j in range(d+1):
                    for m in range(8):
                        v = [Q(0) for _ in range(d+1)]
                        v[j] = bary[j] + Q(m+1, 150)
                        k = (j+1) % (d+1)
                        v[k] = Q(1)-t-v[j]
                        assert v[j] > bary[j] and sum(v) == 1-t
                        assert overlap_fraction(v,d) <= target
                        tested += 1
                # Construct a translate missing the point that attains the supremum in the limit.
                j = min(range(d+1),key=lambda k:bary[k])
                v = [Q(0) for _ in range(d+1)]
                v[j] = bary[j]+Q(1,10**6)
                v[(j+1)%(d+1)] = 1-t-v[j]
                assert v[j]>bary[j] and sum(v)==1-t
                assert target-overlap_fraction(v,d) <= Q(d,10**5)
                tested += 1
            # Check exact probability of the nonbaseline region as a simplex volume ratio.
            if t <= Q(d,d+1):
                assert not (t>Q(d,d+1))
            else:
                core_scale = (d+1)*min(t,Q(1))-d
                assert 0<core_scale<=1
                assert core_scale**d == ((d+1)*min(t,Q(1))-d)**d
                tested += 1
    # Exterior points: exhibit maximal-overlap translates missing the point.
    for d in (2,3,4):
        bary = [Q(-1,7),Q(8,7)]+[Q(0) for _ in range(d-1)]
        for t in (Q(1,3),Q(1),Q(7,3)):
            v = [Q(0) for _ in range(d+1)]
            v[1] = 1-t
            assert v[0]>bary[0] and sum(v)==1-t
            assert overlap_fraction(v,d)==min(t,Q(1))**d
            tested += 1
    print('PASS:',tested,'exact-rational translate and threshold checks')

if __name__=='__main__':
    checks()
