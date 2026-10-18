#!/usr/bin/env python3
"""Reproducible tests for optimal run-subsequence multiplicities of two-permutation words.
Only the input permutation and combinatorial algorithms are used.
"""
from itertools import permutations
from math import factorial

def formula_count(p):
    record = -1
    total = 0
    for t, symbol in enumerate(p):
        if symbol > record:
            record = symbol
            total += 1 << (symbol-t)
    return total

def is_run_word(t):
    closed = set()
    previous = None
    for x in t:
        if x != previous:
            if x in closed:
                return False
            if previous is not None:
                closed.add(previous)
            previous = x
    return True

def brute_optima(p):
    n = len(p)
    w = tuple(range(n))+tuple(p)
    result = set()
    optimum = -1
    # Brute enumeration is independent of the formula or structural characterization.
    for bits in range(1 << (2*n)):
        subseq = tuple(w[i] for i in range(2*n) if (bits >> i) & 1)
        if len(subseq) < optimum or not is_run_word(subseq):
            continue
        if len(subseq) > optimum:
            optimum = len(subseq)
            result.clear()
        result.add(subseq)
    return optimum, len(result)

def tiled_permutations(n):
    def produce(base):
        if base == n:
            yield ()
        else:
            for tail in produce(base+1):
                yield (base,)+tail
            if base+1 < n:
                for tail in produce(base+2):
                    yield (base+1,base)+tail
    return set(produce(0))

def check():
    for n in range(1,6):
        for p in permutations(range(n)):
            expected = formula_count(p)
            maximum, count = brute_optima(p)
            assert maximum == n+1, (n,p,maximum)
            assert count == expected, (n,p,expected,count)
        print('BRUTE_INDEPENDENT', n, 'PASS')
    for n in range(1,10):
        min_count, max_count = n, 1 << (n-1)
        lows, highs = set(), set()
        for p in permutations(range(n)):
            value = formula_count(p)
            assert min_count <= value <= max_count, (n,p,value)
            if value == min_count:
                lows.add(p)
            if value == max_count:
                highs.add(p)
        assert lows == tiled_permutations(n), ('minimizers', n, lows)
        if n > 1:
            expected_maxes = {p for p in permutations(range(n))
                              if p[0] == n-1 or (p[0] == n-2 and p[1] == n-1)}
            assert highs == expected_maxes, ('maximizers', n)
            assert len(highs) == n*factorial(n-2), (n,len(highs))
        assert len(lows) == len(tiled_permutations(n))
        print('FULL_PERMUTATION_CENSUS', n, 'lower',min_count,'lower_cases',len(lows),
              'upper',max_count,'upper_cases',len(highs), 'PASS')
    print('ALL_RUN_MULTIPLICITY_TESTS_PASSED')
if __name__ == '__main__':
    check()
