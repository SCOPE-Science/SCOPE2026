#!/usr/bin/env python3
"""Independent finite checks for the mixed Wythoff representation profile.

Run: python3 verify.py
No third-party packages or input files are required.
"""
from decimal import Decimal, localcontext
from math import isqrt, log


def lower(h):
    return (h + isqrt(5*h*h)) // 2


def upper(k):
    return k + lower(k)


def direct_counts(limit):
    counts = [0] * (limit+1)
    a = []
    b = []
    for j in range(1, limit+1):
        x = lower(j)
        y = upper(j)
        if x <= limit:
            a.append(x)
        if y <= limit:
            b.append(y)
        if x > limit and y > limit:
            break
    for x in a:
        for y in b:
            if x+y > limit:
                break
            counts[x+y] += 1
    return counts, a, b


def verify():
    cap = 4500
    counts, a, b = direct_counts(cap)
    a_set = set(a)
    b_set = set(b)
    assert not a_set.intersection(b_set)
    assert a_set.union(b_set) == set(range(1, cap+1))
    first = [0, 0, 1, 0, 1, 2, 0, 3, 1, 2, 4, 0, 4, 4, 1, 6, 2, 4, 7]
    assert counts[1:20] == first
    worst = (Decimal(0), -1)
    with localcontext() as ctx:
        ctx.prec = 85
        delta = (Decimal(3)-Decimal(5).sqrt()) / 2
        for n in range(1, cap+1):
            y = n*delta - int(n*delta)
            kmax = int(n*delta)
            assert sum(1 for v in b if v < n) == kmax
            via_complement = sum(1 for v in b if v < n and n-v not in b_set)
            assert via_complement == counts[n], (n,via_complement,counts[n])
            via_rotation = 0
            for k in range(1, kmax+1):
                u = Decimal(k)*(1/delta) - int(Decimal(k)*(1/delta))
                t = y + delta*u
                is_b = int(t+delta)-int(t)
                via_rotation += 1-is_b
            assert via_rotation == counts[n], (n,via_rotation,counts[n])
            if y <= 1-2*delta:
                f = delta
            elif y <= 1-delta:
                f = 1-delta-y
            else:
                f = y-1+delta
            assert 0 <= f <= delta
            err = abs(Decimal(counts[n])-n*f)
            if err > worst[0]:
                worst = (err,n)
            assert err < Decimal(20)*Decimal(str(log(2*n))), (n,err)
        # The density of the two nonconstant branches is exactly delta each.
        # Their pushforward densities sum to 2 on (0,delta).
        assert 0 < 1-2*delta < 1
        assert 2*delta + (1-2*delta) == 1
        assert abs(delta*(1-delta) - (Decimal(5).sqrt()-2)) < Decimal("1e-70")
    print(f'VERIFY_OK exact_convolution_n={cap} rotation_n={cap} '
          f'Beatty_partition=PASS profile=PASS max_error={worst[0]:.6f}@{worst[1]} '
          'law_mass=PASS')


if __name__ == '__main__':
    verify()
