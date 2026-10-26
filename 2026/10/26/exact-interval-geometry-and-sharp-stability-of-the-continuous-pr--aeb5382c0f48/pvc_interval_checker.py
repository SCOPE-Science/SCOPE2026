"""Exact arithmetic checks of the one-dimensional uniform epsilon-veto-core endpoint theorem.

Run: python pvc_interval_checker.py
The finite tests are corroboration of the theorem, not a proof of its universal form.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from random import Random


def bounds(peaks, epsilon=F(0)):
    """Return predicted exact epsilon-veto-core endpoints on [0,1]."""
    p = sorted(map(F, peaks))
    n = len(p)
    assert n > 0 and epsilon >= 0 and all(F(0) <= t <= 1 for t in p)
    lower = max([F(0)] + [min(F(n-j+1, n)-epsilon,
                                 p[j-1]-F(j-1, 2*n)-epsilon/2)
                            for j in range(1, n+1)])
    upper = min([F(1)] + [max(F(n-j, n)+epsilon,
                                 p[j-1]+F(n-j, 2*n)+epsilon/2)
                            for j in range(1, n+1)])
    assert lower <= upper
    return lower, upper


def brute_membership(peaks, x, epsilon=F(0)):
    """Check every nonempty voter coalition, using its exact preferred-set measure."""
    peaks = list(map(F, peaks))
    n = len(peaks)
    x = F(x)
    for mask in range(1, 1 << n):
        left, right = F(0), F(1)
        for i, p in enumerate(peaks):
            if mask >> i & 1:
                if p == x:
                    right = left
                    break
                t = 2*p-x
                left = max(left, min(t, x))
                right = min(right, max(t, x))
        measure = max(F(0), right-left)
        if measure + F(mask.bit_count(), n) > 1 + epsilon:
            return False
    return True


def run():
    count=0
    for n in range(1, 7):
        for ints in combinations_with_replacement([0, 2, 4, 6, 8], n):
            p=[F(t, 8) for t in ints]
            for eps in (F(0), F(1, 8), F(1, 4), F(1, 2), F(1), F(3, 2)):
                lo, hi = bounds(p, eps)
                for k in range(9):
                    x=F(k, 8)
                    assert (lo <= x <= hi) == brute_membership(p, x, eps), (p, x, eps, lo, hi)
                    count += 1
    rng=Random(260316751)
    for n in range(1, 10):
        for _ in range(160):
            p = sorted(F(rng.randint(0, 32), 32) for __ in range(n))
            eps=F(rng.randint(0, 16), 32)
            lo, hi = bounds(p, eps)
            x = F(rng.randint(0, 64), 64)
            assert (lo <= x <= hi) == brute_membership(p, x, eps), (p, x, eps, lo, hi)
            count += 1
    for n in range(1, 10):
        for _ in range(60):
            p = sorted(F(rng.randint(0, 64), 64) for __ in range(n))
            q = sorted(min(F(1), max(F(0), v + F(rng.randint(-8, 8), 64))) for v in p)
            eps = F(rng.randint(0, 16), 32)
            lp, up = bounds(p, eps)
            lq, uq = bounds(q, eps)
            d = max(abs(a-b) for a,b in zip(p,q))
            assert max(abs(lp-lq),abs(up-uq)) <= d
            count += 1
    print('PASS', count, 'exact checks (coalition equivalence plus stability)')
    for p in [(F(0), F(0), F(1)), (F(2,5), F(3,5)), (F(0), F(1)), (F(1,4), F(1,2), F(3,4))]:
        print('example',str(p),'PVC',str(bounds(p)))

if __name__ == '__main__':
    run()
