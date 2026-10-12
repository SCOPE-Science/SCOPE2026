#!/usr/bin/env python3
"""Independent finite tests for random two-agent S5 grid modal-type theorem.

Standard library only. Exhaustive cases are explicitly bounded; the limit
law and the probability convergence are proved mathematically, not by tests.
"""
import itertools
import math
import random
from collections import Counter


def modal_type_count(n, bits):
    """Refine one-proposition modal types by the two S5 accessibility sets."""
    m = n*n
    t = [int((bits >> k) & 1) for k in range(m)]
    last = len(set(t))
    for depth in range(m+1):
        rows = [tuple(sorted(set(t[i*n:(i+1)*n]))) for i in range(n)]
        cols = [tuple(sorted(set(t[j::n]))) for j in range(n)]
        ids = {}
        v = []
        for i in range(n):
            for j in range(n):
                key = (t[i*n+j], rows[i], cols[j])
                if key not in ids: ids[key] = len(ids)
                v.append(ids[key])
        if len(ids) == last:
            return last, depth
        last = len(ids)
        t = v
    raise RuntimeError('No stabilization')


def regular_condition(n, bits):
    """Sufficient exact one-round pattern theorem, not a random assumption."""
    row = [sum((bits >> (i*n+j)) & 1 for j in range(n)) for i in range(n)]
    col = [sum((bits >> (i*n+j)) & 1 for i in range(n)) for j in range(n)]
    active_r = sum(v != 0 for v in row)
    active_c = sum(v != 0 for v in col)
    if not active_r or not active_c: return None
    if any(v >= active_c for v in row if v) or any(v >= active_r for v in col if v):
        return None
    a = int(active_r < n)
    b = int(active_c < n)
    return 2 + a + b + a*b


def closure_size(n, bits):
    """Directly close subsets under complement, union and row/column diamonds."""
    universe = (1 << (n*n)) - 1
    p = bits
    sets = {0, universe, p, universe ^ p}
    def diam(x, by_row):
        result = 0
        for i in range(n):
            for j in range(n):
                group = (sum(1 << (i*n+k) for k in range(n)) if by_row
                         else sum(1 << (k*n+j) for k in range(n)))
                if x & group: result |= group
        return result
    while True:
        old = len(sets)
        new = set(sets)
        for x in sets:
            new.add(universe ^ x)
            new.add(diam(x, True))
            new.add(diam(x, False))
        for x in sets:
            for y in sets:
                new.add(x | y)
        sets = new
        if len(sets) == old: return len(sets)
        assert len(sets) <= 2**(n*n)


def factorial_moment(n, c, a, b):
    p = (math.log(n) + c)/n
    fall = lambda x,k: math.prod(x-j for j in range(k))
    return fall(n,a)*fall(n,b)*(1-p)**(n*(a+b)-a*b)


def run():
    exhaustive = cases = closures = 0
    for n in (2,3,4):
        for b in range(1 << (n*n)):
            exhaustive += 1
            predicted = regular_condition(n,b)
            if predicted is not None:
                cases += 1
                k,depth = modal_type_count(n,b)
                assert k == predicted and depth <= 2, (n,b,k,predicted,depth)
            if n <= 2 or (n == 3 and (b % 19 == 0)):
                k,_ = modal_type_count(n,b)
                assert closure_size(n,b) == (1 << k)
                closures += 1
    rng = random.Random(123456)
    trial_check = 0
    hist = Counter()
    for n in (25,70,140):
        p = math.log(n)/n
        for rep in range(160):
            bits = sum(1 << (i*n+j)
                       for i in range(n) for j in range(n) if rng.random() < p)
            expected = regular_condition(n,bits)
            actual,depth = modal_type_count(n,bits)
            if expected is not None:
                assert expected == actual and depth <= 2
                hist[(n,expected)] += 1
            trial_check += 1
    for n in (100,300,1000,5000):
        for a in range(3):
            for b in range(3):
                m = factorial_moment(n,0.,a,b)
                assert math.isfinite(m)
                if n == 5000: assert abs(m-1.) < .03,(a,b,m)
    print('VERIFY_OK exhaustive_binary_matrices',exhaustive,
          'structural_cases',cases,'direct_boolean_closures',closures,
          'random_refinements',trial_check,'factorial_moment_checks',36)
    print('SIMULATED_COUNTS',sorted((str(k),v) for k,v in hist.items()))

if __name__ == '__main__':
    run()
