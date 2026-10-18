#!/usr/bin/env python3
"""Direct exhaustive check of optimal-attractor classification for periodic distinct-letter prefixes.
The factor coverage masks are computed from explicit substring occurrences, independently
of the mathematical characterization being tested.
"""
from itertools import product


def run_case(q, m, r, verbose=False):
    word = tuple(range(q)) * m + tuple(range(r))
    n = len(word)
    masks = {}
    for i in range(n):
        interval = 0
        for j in range(i, n):
            interval |= 1 << j
            factor = word[i:j+1]
            masks[factor] = masks.get(factor, 0) | interval
    cover_masks = list(masks.values())
    options = [range(m + (j < r)) for j in range(q)]
    valid_count, bad_count, check_count = 0, 0, 0
    for ranks in product(*options):
        selected = sum(1 << (j + q * ranks[j]) for j in range(q))
        actual = all(selected & z for z in cover_masks)
        if m == 1 or r == q - 1:
            predicted = True
        else:
            bad = (ranks[q-1] == m-1 and ranks[r] == 0
                   and all(ranks[j] in (0, m) for j in range(r)))
            predicted = not bad
        assert actual == predicted, (q, m, r, ranks, actual, predicted)
        check_count += 1
        valid_count += actual
        bad_count += not actual
    if m == 1:
        expected = 2 ** r
    elif r == q - 1:
        expected = (m + 1)**r * m
    else:
        expected = (m + 1)**r * m**(q-r) - 2**r * m**(q-r-2)
    assert valid_count == expected, (q, m, r, valid_count, expected)
    if verbose:
        print(f'q={q} m={m} r={r} candidates={check_count} valid={valid_count} bad={bad_count} factors={len(masks)}')
    return check_count, len(masks)


def main():
    cells = candidates = factors = 0
    for q in range(2, 7):
        for m in range(1, 5):
            for r in range(q):
                ct, fc = run_case(q, m, r)
                cells += 1; candidates += ct; factors += fc
    print(f'PASS q=2..6, m=1..4, r=0..q-1: cells={cells}, candidate_sets={candidates}, cumulative_distinct_factors={factors}')
    for args in ((3,2,0), (3,3,1), (4,3,2), (5,4,3), (6,4,5)):
        run_case(*args, verbose=True)

if __name__ == '__main__':
    main()
