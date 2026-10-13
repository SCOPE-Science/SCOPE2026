#!/usr/bin/env python3
"""Finite Boolean-filter regression for an omega-accumulation classification.

This only tests the abstract Boolean ultrafilter lemma on finite sets.  It
cannot test the infinite topological statement or existence of a free ultrafilter.
"""
from itertools import product


def check(n):
    top = (1 << n) - 1
    candidates = 0
    identities = 0
    for kernel in range(1, top + 1):
        # Every proper filter on a finite set is the principal filter of one
        # nonempty kernel.  The Boolean form of omega-positivity is positive(A)
        # iff the complement of A is NOT in this filter.
        in_filter = lambda a: (kernel & a) == kernel
        positive = lambda a: not in_filter(top ^ a)
        is_ultra = (kernel.bit_count() == 1)
        preserves_meets = True
        for a, b in product(range(top + 1), repeat=2):
            pa, pb = positive(a), positive(b)
            if positive(a | b) != (pa or pb):
                raise AssertionError(('union', n, kernel, a, b))
            if positive(a & b) != (pa and pb):
                preserves_meets = False
            identities += 1
        if preserves_meets != is_ultra:
            raise AssertionError(('ultrafilter boundary', n, kernel))
        candidates += 1
    return candidates, identities


def main():
    total_filters = total_pairs = 0
    for n in range(1, 6):
        fil, pairs = check(n)
        total_filters += fil
        total_pairs += pairs
        print(f'n={n}: filters={fil}, tested ordered valuation pairs={pairs}')
    print(f'PASS: {total_filters} finite filters, {total_pairs} pair-tests.')
    print('Scope: finite Boolean abstraction only; infinite conclusions are proved in RESULT.md.')


if __name__ == '__main__':
    main()
