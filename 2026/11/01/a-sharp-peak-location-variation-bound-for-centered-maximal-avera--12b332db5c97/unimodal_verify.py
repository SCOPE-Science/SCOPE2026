"""Exact-rational consistency checks for a centered path maximal-function bound.

Run with Python 3 (standard library only): python unimodal_verify.py
The universal claim is proved analytically; finite checks only test implementation and examples.
"""
from fractions import Fraction
from itertools import product
from random import Random


def is_unimodal(a):
    return any(all(a[i] <= a[i + 1] for i in range(k))
               and all(a[i] >= a[i + 1] for i in range(k, len(a) - 1))
               for k in range(len(a)))


def mode(a):
    return next(k for k in range(len(a))
                if all(a[i] <= a[i + 1] for i in range(k))
                and all(a[i] >= a[i + 1] for i in range(k, len(a) - 1)))


def centered_maximum(a):
    n = len(a)
    p = [0]
    for x in a:
        p.append(p[-1] + x)
    result = []
    for i in range(n):
        best = Fraction(a[i])
        for r in range(1, max(i, n - 1 - i) + 1):
            lo, hi = max(0, i-r), min(n, i+r+1)
            best = max(best, Fraction(p[hi]-p[lo], hi-lo))
        result.append(best)
    return result


def tv(a):
    return sum(abs(a[i+1]-a[i]) for i in range(len(a)-1))


def check(a):
    n = len(a)
    k = mode(a)
    H, left, right = a[k], a[0], a[-1]
    b = centered_maximum(a)
    assert all(b[i] <= b[i+1] for i in range(k)), (a, b, k)
    assert all(b[i] >= b[i+1] for i in range(k, n-1)), (a, b, k)
    assert b[k] == H
    assert tv(b) == 2*H-b[0]-b[-1]
    endpoint_gain = Fraction(H-left,k+1) + Fraction(H-right,n-k)
    assert (b[0]-left) + (b[-1]-right) >= endpoint_gain, (a, b)
    assert tv(b) <= tv(a) - endpoint_gain, (a, b)
    assert n*tv(b) <= (n-1)*tv(a), (a, b)
    if 0<k<n-1 and H>left and H>right:
        assert n*tv(b) < (n-1)*tv(a), (a, b)


def main():
    total=0
    for n in range(3,9):
        for a in product(range(4), repeat=n):
            if is_unimodal(a):
                check(a)
                total += 1
    rng = Random(23917)
    random_count=0
    for n in [9, 12, 20, 35]:
        for _ in range(1200):
            k = rng.randrange(n)
            prefix = sorted(rng.randrange(100) for _ in range(k))
            suffix = sorted((rng.randrange(100) for _ in range(n-k-1)), reverse=True)
            a = tuple(prefix+[100]+suffix)
            check(a)
            random_count += 1
    spikes=0
    for n in range(3,101):
        for k in range(n):
            a = [0]*n
            a[k]=1
            b = centered_maximum(a)
            assert b[0] == Fraction(1,k+1)
            assert b[-1] == Fraction(1,n-k)
            check(a)
            spikes += 1
    print('exhaustive_unimodal_integer_sequences:',total)
    print('deterministic_unimodal_samples:',random_count)
    print('exact_single_spike_sharpness_cases:',spikes)
    print('all_checks_passed')

if __name__ == '__main__':
    main()
