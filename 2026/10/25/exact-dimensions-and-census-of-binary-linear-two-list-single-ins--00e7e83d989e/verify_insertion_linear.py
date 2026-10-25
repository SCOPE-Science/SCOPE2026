#!/usr/bin/env python3
"""Exact finite-dimensional one-insertion, two-list code computation.

Run with Python 3.9 or newer. No nonstandard dependencies.
"""
from itertools import combinations, product


def gaussian_binomial_2(n, k):
    if k < 0 or k > n:
        return 0
    # Do not divide termwise: integrality may emerge only at the end.
    top = bot = 1
    for i in range(k):
        top *= 2**(n-i)-1
        bot *= 2**(k-i)-1
    return top // bot


def rref_bases(n, k):
    for pivots in combinations(range(n), k):
        rights = [tuple(j for j in range(p+1, n) if j not in pivots) for p in pivots]
        candidates = []
        for p, cols in zip(pivots, rights):
            candidates.append([1 << p | sum((1 << col) for j, col in enumerate(cols)
                                                    if mask & (1 << j))
                               for mask in range(1 << len(cols))])
        yield from product(*candidates)


def codewords(rows):
    words = [0]
    for r in rows:
        words += [c ^ r for c in words]
    return words


def deletion_word(received, position):
    return ((received & ((1 << position)-1)) |
            ((received >> (position+1)) << position))


def all_parent_masks(n):
    masks = []
    for received in range(1 << (n+1)):
        m = 0
        for pos in range(n+1):
            m |= 1 << deletion_word(received, pos)
        if m.bit_count() > 2:
            masks.append((received, m))
    return masks


def good_code(n, rows, witnesses):
    words = codewords(rows)
    assert len(set(words)) == 1 << len(rows)
    membership = sum(1 << c for c in words)
    for received, parent_mask in witnesses:
        if (membership & parent_mask).bit_count() > 2:
            return False
    return True


def independently_check_witness(n, rows):
    # Independent forward-channel implementation: insert either bit at
    # each of n+1 positions, deduplicating identical received words.
    arrivals = {}
    for c in codewords(rows):
        for pos in range(n+1):
            for bit in (0, 1):
                received = ((c & ((1 << pos) - 1)) |
                            (bit << pos) | ((c >> pos) << (pos+1)))
                arrivals.setdefault(received, set()).add(c)
    peak = max(map(len, arrivals.values()), default=0)
    histogram = [0] * (peak+1)
    histogram[0] = (1 << (n+1)) - len(arrivals)
    for parents in arrivals.values():
        histogram[len(parents)] += 1
    return peak, histogram


def main():
    known = (1, 1, 2, 2, 3, 4, 4, 5, 6)
    expected_optimal_counts = (1, 3, 4, 29, 49, 17, 3238, 5534, 1786)
    for n, optimum in enumerate(known, start=1):
        masks = all_parent_masks(n)
        upper = optimum + 1
        if upper <= n:
            tried = 0
            for rows in rref_bases(n, upper):
                tried += 1
                if good_code(n, rows, masks):
                    raise AssertionError(('upper counterexample', n, upper, rows))
            expected = gaussian_binomial_2(n, upper)
            if tried != expected:
                raise AssertionError(('incomplete search', n, tried, expected))
        else:
            tried = 0
            expected = 0
        found = None
        scanned = 0
        optimal_count = 0
        for rows in rref_bases(n, optimum):
            scanned += 1
            if good_code(n, rows, masks):
                optimal_count += 1
                if found is None:
                    found = rows
        assert scanned == gaussian_binomial_2(n, optimum)
        assert optimal_count == expected_optimal_counts[n-1], (n, optimal_count)
        if found is None:
            raise AssertionError(('no lower witness', n))
        peak, histogram = independently_check_witness(n, found)
        if peak > 2 or sum(histogram) != (1 << (n+1)):
            raise AssertionError(('bad witness', n, peak, histogram))
        print(f'n={n} K={optimum} optimal_count={optimal_count}/{scanned} upper_k={upper} excluded={tried}/{expected} witness={list(found)} verified_max_list={peak} list_histogram={histogram}', flush=True)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
