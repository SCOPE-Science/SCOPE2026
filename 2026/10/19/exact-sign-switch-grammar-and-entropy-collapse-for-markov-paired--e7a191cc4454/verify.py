#!/usr/bin/env python3
"""Finite diagnostic tests for sign itineraries of a symmetric paired tent map.
The proof of the parameter-uniform statement is analytical, not enumerative.
Only the Python standard library is required.
"""
from itertools import product
from math import exp, log


def root_bisection(fn, lo, hi, steps=90):
    assert fn(lo) < 0 < fn(hi)
    for _ in range(steps):
        mid = (lo + hi) / 2
        if fn(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def parameters(n):
    kappa = root_bisection(lambda x: x * (2 * (1 + x)) ** n - 1, 0., .5)
    slope = 2 * (1 + kappa)
    rho = root_bisection(lambda x: x**n * (x-1) - 1, 1., 2.)
    assert abs(kappa * slope**n - 1) < 2e-12
    assert abs(rho**n * (rho-1) - 1) < 2e-12
    return kappa, slope, rho


def branch_images(slope):
    return [(-1., -.5, slope, slope-1),
            (-.5, 0., -slope, -1.),
            (0., .5, -slope, 1.),
            (.5, 1., slope, 1-slope)]


def merge(intervals):
    result = []
    for a, b in sorted(intervals):
        if b-a <= 1e-12:
            continue
        if result and a < result[-1][1] + 1e-12:
            result[-1] = (result[-1][0], max(result[-1][1], b))
        else:
            result.append((a, b))
    return result


def has_positive_measure_cylinder(word, branches):
    intervals = [(0., 1.)] if word[0] else [(-1., 0.)]
    for sign in word[1:]:
        new = []
        lower, upper = (0., 1.) if sign else (-1., 0.)
        for a, b in intervals:
            for p, q, slope, intercept in branches:
                left, right = max(a, p), min(b, q)
                if right - left <= 1e-13:
                    continue
                lo, hi = sorted((slope*left+intercept, slope*right+intercept))
                lo, hi = max(lo, lower), min(hi, upper)
                if hi - lo > 1e-12:
                    new.append((lo, hi))
        intervals = merge(new)
        if not intervals:
            return False
    return bool(intervals)


def grammar(word, n):
    flips = [word[j] != word[j+1] for j in range(len(word)-1)]
    return all(not flips[i] or all(not flips[j] for j in range(i+1, min(i+n+1, len(flips))))
               for i in range(len(flips)))


def main():
    tests = 0
    for n in range(1, 7):
        kappa, slope, rho = parameters(n)
        # Endpoint equations controlling the mandatory recovery phase.
        assert 0 < kappa < .5
        assert abs((.5 - 1/slope)*slope - kappa) < 5e-14
        for i in range(1, n):
            assert 1-slope**i*kappa > .5
        assert abs(1-slope**n*kappa) < 2e-12
        br = branch_images(slope)
        for m in range(0, 10):
            count = 0
            for word in product((0, 1), repeat=m+1):
                admissible = grammar(word, n)
                actual = has_positive_measure_cylinder(word, br)
                assert actual == admissible, (n, word, actual, admissible)
                count += int(actual)
                tests += 1
            # Compare the observed sign word count with an independent recurrence.
            numbers = [1]
            for q in range(1, m+1):
                numbers.append(numbers[-1] + (numbers[q-n-1] if q>=n+1 else 1))
            assert count == 2*numbers[m], (n,m,count,2*numbers[m])
        print('n=%d kappa=%.12g slope=%.12g sign_entropy=%.12g' %
              (n, kappa, slope, log(rho)))
    print('PASS: %d finite sign-word tests, six critical-orbit identities and count recurrences.' % tests)


if __name__ == '__main__':
    main()
