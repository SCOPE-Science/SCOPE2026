#!/usr/bin/env python3
"""Exact finite certificate for a Stern-sequence residue-discrepancy theorem.

All arithmetic is integer arithmetic. Usage: python3 verify.py
Optionally place CERTIFICATE.tsv beside this file for comparison with a saved table.
"""
from pathlib import Path

P = 5
STATES = [(a, b) for a in range(P) for b in range(P) if a or b]
assert len(STATES) == 24
INDEX = {pair: k for k, pair in enumerate(STATES)}

def left(pair):
    a, b = pair
    return (a, (a + b) % P)

def right(pair):
    a, b = pair
    return ((a + b) % P, b)

LEFT = [INDEX[left(pair)] for pair in STATES]
RIGHT = [INDEX[right(pair)] for pair in STATES]
WEIGHT = [int(a == 1) - int(a == 4) for a, b in STATES]

def next_level(level):
    sums, minima, maxima = level
    new_sums = []
    new_minima = []
    new_maxima = []
    for i in range(len(STATES)):
        j, k = LEFT[i], RIGHT[i]
        new_sums.append(sums[j] + sums[k])
        new_minima.append(min(minima[j], sums[j] + minima[k]))
        new_maxima.append(max(maxima[j], sums[j] + maxima[k]))
    return new_sums, new_minima, new_maxima

levels = []
level = (WEIGHT, [min(0, w) for w in WEIGHT], [max(0, w) for w in WEIGHT])
for r in range(53):
    levels.append(level)
    level = next_level(level)

assert levels[5][0] == levels[1][0], 'signed block totals need period four'
assert all(levels[28][1][i] == levels[16][1][i] - 4
           for i in range(24)), 'twelve-step minimum shift'
assert all(levels[28][2][i] == levels[16][2][i] + 4
           for i in range(24)), 'twelve-step maximum shift'

for r in range(16, 41):
    assert levels[r + 12][0] == levels[r][0]
    assert all(levels[r + 12][1][i] == levels[r][1][i] - 4
               for i in range(24))
    assert all(levels[r + 12][2][i] == levels[r][2][i] + 4
               for i in range(24))

base = INDEX[(0, 1)]
# The root-state drift begins earlier than the simultaneous all-state drift.
for r in range(8, 16):
    assert levels[r + 12][1][base] == levels[r][1][base] - 4
    assert levels[r + 12][2][base] == levels[r][2][base] + 4
assert levels[19][1][base] != levels[7][1][base] - 4
expected = [(-4, 9), (-4, 9), (-5, 9), (-5, 9),
            (-5, 11), (-5, 11), (-6, 11), (-6, 11),
            (-6, 12), (-6, 12), (-8, 12), (-8, 12)]
assert [(levels[r][1][base], levels[r][2][base])
        for r in range(16, 28)] == expected

header = 'a\tb\tS1\tS5\tL16\tL28\tH16\tH28\n'
rows = [f'{a}\t{b}\t{levels[1][0][i]}\t{levels[5][0][i]}\t'
        f'{levels[16][1][i]}\t{levels[28][1][i]}\t'
        f'{levels[16][2][i]}\t{levels[28][2][i]}\n'
        for i, (a, b) in enumerate(STATES)]
certificate = header + ''.join(rows)
certfile = Path(__file__).with_name('CERTIFICATE.tsv')
if certfile.exists():
    assert certfile.read_text(encoding='utf-8') == certificate, 'saved table differs'

# Independent direct enumeration from the defining recurrence, not the 24-state
# block recursion. This checks actual signed sums and prefix extrema.
limit = 1 << 17
stern = [0] * (limit + 1)
stern[1] = 1
for n in range(2, limit + 1):
    stern[n] = (stern[n // 2] if n % 2 == 0
                else stern[n // 2] + stern[n // 2 + 1])
D, low, high = 0, 0, 0
for n in range(limit):
    if n == 0 or (n & (n - 1)) == 0:
        r = n.bit_length() - 1
        if n == 0:
            assert (D, low, high) == (0, 0, 0)
        else:
            assert (D, low, high) == (levels[r][0][base],
                                       levels[r][1][base],
                                       levels[r][2][base]), (n, D, low, high)
    D += int(stern[n] % P == 1) - int(stern[n] % P == 4)
    low = min(low, D)
    high = max(high, D)
assert (D, low, high) == (levels[17][0][base],
                           levels[17][1][base], levels[17][2][base])
# Monroe's representation counts: for i bits, b_i(n)=stern[2**i-n].
# The first row and column of signed-digit counts can also be checked
# independently by direct ternary-word enumeration for small i.
from itertools import product
for i in range(1, 7):
    cnt = [0] * (1 << i)
    for digits in product((-1, 0, 1), repeat=i):
        n = sum(digits[j] * (1 << j) for j in range(i))
        if 0 <= n < (1 << i):
            cnt[n] += 1
    assert cnt == [stern[(1 << i)-n] for n in range(1 << i)]
for r in range(8, 18):
    nmax = 1 << r
    e, low_bsd, high_bsd = 0, 0, 0
    for n in range(nmax):
        value = stern[nmax-n] % P
        e += int(value == 1) - int(value == 4)
        low_bsd, high_bsd = min(low_bsd, e), max(high_bsd, e)
    target_low = levels[r][0][base] + 1 - levels[r][2][base]
    target_high = levels[r][0][base] + 1 - levels[r][1][base]
    assert (low_bsd, high_bsd) == (target_low, target_high)
assert [(levels[r][0][base]+1-levels[r][2][base],
         levels[r][0][base]+1-levels[r][1][base]) for r in range(8,20)] == [
    (-4,4),(-5,3),(-4,5),(-3,6),(-5,5),(-6,4),
    (-5,7),(-4,8),(-6,7),(-7,6),(-6,8),(-5,9)]
print('VERIFY_OK states=24 levels=53 total_period=4 from=1 '
      'root_shift_start=8 all_states_start=16 '
      'increment=4 direct_stern_terms=131072 '
      'direct_BSD_widths=8..17 enumeration_widths=1..6 certificate_rows=24')
