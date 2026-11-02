"""Reproducible finite checks for rearranged optical-coordinate search.

All assertions are finite diagnostics; the theorem's continuum and universal
quantifiers follow from the written analytic proof, not these tests.
"""
import itertools
import math
import random


TESTS = 0


def check(condition, explanation):
    global TESTS
    assert condition, explanation
    TESTS += 1


def integral_prefix(values, a):
    total = 0.0
    for i, v in enumerate(values):
        total += v * min(1.0, max(0.0, a - i))
    return total


def upper_reflected_path(initial, ymax, increments):
    pos_free = initial
    running_max = initial
    positions = []
    for inc in increments:
        pos_free += inc
        running_max = max(running_max, pos_free)
        positions.append(pos_free - max(0.0, running_max-ymax))
    return positions


def first_sample_hit(initial, ymax, increments):
    values = upper_reflected_path(initial, ymax, increments)
    return next((j for j, x in enumerate(values) if x <= 0), math.inf)


def constant_reset_sample_hit(initial, ymax, segments):
    for cycle, increments in enumerate(segments):
        index = first_sample_hit(initial, ymax, increments)
        if index < math.inf:
            return cycle * len(increments) + index
    return math.inf


def laplace_no_reset(initial, ymax, s):
    return math.cosh(math.sqrt(s) * (ymax - initial)) / math.cosh(math.sqrt(s) * ymax)


def mean_poisson(initial, ymax, rate):
    return (1.0 / laplace_no_reset(initial, ymax, rate) - 1.0) / rate


def check_arrangements():
    pieces = (0.5, 0.75, 1.0, 1.25, 1.5, 2.0)
    start_length = 2.5
    lo = integral_prefix(pieces, start_length)
    hi = integral_prefix(tuple(reversed(pieces)), start_length)
    for p in itertools.permutations(pieces):
        u = integral_prefix(p, start_length)
        check(lo - 1e-12 <= u <= hi + 1e-12, "equimeasurable-prefix bound")
        check(abs(sum(p) - sum(pieces)) <= 1e-12, "invariant optical length")
    # Continuous shifts of the monotone profile attain the full interval.
    endpoints = []
    for step in range(101):
        s = (6 - start_length) * step/100
        shift = s
        total = 0.0
        for j, g in enumerate(pieces):
            intersect = max(0.0, min(j+1, shift+start_length) - max(j, shift))
            total += g*intersect
        endpoints.append(total)
    check(abs(endpoints[0]-lo) < 1e-12, "cyclic sliding lower endpoint")
    check(abs(endpoints[-1]-hi) < 1e-12, "cyclic sliding upper endpoint")
    for a,b in zip(endpoints,endpoints[1:]):
        check(a <= b+1e-12, "monotone sliding window")


def check_coupling():
    rng = random.Random(41807)
    ymax = 0.75
    for _ in range(800):
        steps = [rng.gauss(0, 0.015) for j in range(40)]
        ua, ub = 0.15, 0.38
        a = upper_reflected_path(ua, ymax, steps)
        b = upper_reflected_path(ub, ymax, steps)
        for pa, pb in zip(a,b):
            check(pa <= pb + 1e-12, "reflected monotonicity")
            check(pb-pa <= ub-ua + 1e-12, "Skorokhod nonexpansiveness")
        check(first_sample_hit(ua,ymax,steps) <= first_sample_hit(ub,ymax,steps), "first-passage sample ordering")
    for _ in range(200):
        segments = [[rng.gauss(0,0.06) for j in range(20)] for i in range(15)]
        check(constant_reset_sample_hit(0.2,ymax,segments) <=
              constant_reset_sample_hit(0.4,ymax,segments),
              "restart sample ordering")


def check_formula():
    ymax=0.75
    for j in range(1, 75):
        s=0.05*j
        a=laplace_no_reset(0.2,ymax,s)
        b=laplace_no_reset(0.4,ymax,s)
        check(0<b<a<1,"Laplace transform initial-state ordering")
        check(mean_poisson(0.2,ymax,s)<mean_poisson(0.4,ymax,s),"Poisson mean ordering")
    check(abs(mean_poisson(0.2,ymax,1)-0.12083949413114192)<1e-12, "fast numerical reference")
    check(abs(mean_poisson(0.4,ymax,1)-0.2192394090177916)<1e-12, "slow numerical reference")
    for initial in [0.1,0.2,0.5,0.7]:
        noreset = initial*(2*ymax-initial)/2
        check(abs(mean_poisson(initial,ymax,1e-5)-noreset)<1e-5, "zero-reset limit")


if __name__ == "__main__":
    check_arrangements()
    check_coupling()
    check_formula()
    print(f"PASS: {TESTS} finite assertions (rearrangement, reflection coupling, resetting, means)")
