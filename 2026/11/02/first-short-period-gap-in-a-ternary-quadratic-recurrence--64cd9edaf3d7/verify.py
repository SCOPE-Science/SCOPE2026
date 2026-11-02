#!/usr/bin/env python3
"""Independent exact finite certificate for the small-period classification.
For each m<=9, the lag k acts modulo m. Two enumerators reconstruct the complete cycle table.
"""
from itertools import product

def fundamental_period(word):
    n = len(word)
    return next(d for d in range(1, n + 1) if n % d == 0 and
                all(word[i] == word[i % d] for i in range(n)))

def relation(word, r):
    n = len(word)
    return all((word[i] - word[(i - 1) % n]) % 3 ==
               (word[(i - r) % n] != 0) for i in range(n))

def brute():
    tab = {}
    for n in range(1, 10):
        for word in product(range(3), repeat=n):
            if fundamental_period(word) != n:
                continue
            for r in range(n):
                if relation(word, r):
                    tab[(n, r)] = tab.get((n, r), 0) + 1
    return tab

def compositions(total, parts):
    if parts == 1:
        if total >= 1:
            yield (total,)
        return
    for x in range(1, total - parts + 2):
        for rest in compositions(total - x, parts - 1):
            yield (x,) + rest

def six_run():
    output = {}
    expected_compositions = {8: 21, 9: 56}
    for n in (8, 9):
        comps = list(compositions(n, 6))
        assert len(comps) == expected_compositions[n]
        hits = []
        for co in comps:
            word = tuple(v for j, size in enumerate(co)
                         for v in (j % 3,) * size)
            assert len(word) == n
            for r in range(n):
                if relation(word, r):
                    hits.append((co, r, fundamental_period(word)))
        output[n] = sorted(hits)
    return output

expected = {(1, 0): 1, (4, 2): 4, (4, 3): 4, (9, 4): 9, (9, 6): 9}
actual = brute()
assert actual == expected, (actual, expected)
census = six_run()
assert census[8] == sorted([
    ((1, 1, 2, 1, 1, 2), 3, 4),
    ((1, 1, 2, 1, 1, 2), 7, 4),
    ((1, 2, 1, 1, 2, 1), 2, 4),
    ((1, 2, 1, 1, 2, 1), 6, 4),
]), census[8]
assert census[9] == sorted([
    ((1, 1, 1, 2, 1, 3), 4, 9),
    ((1, 3, 1, 2, 1, 1), 6, 9),
    ((2, 1, 1, 1, 3, 1), 6, 9),
    ((2, 1, 3, 1, 1, 1), 4, 9),
]), census[9]
print('VERIFY_OK ternary_words_through=9 nonzero_primitive_periods=4,9 '
      'four_cycle_lags=2,3 nine_cycle_lags=4,6 sixrun_compositions=77 '
      'independent_enumerators=yes')
