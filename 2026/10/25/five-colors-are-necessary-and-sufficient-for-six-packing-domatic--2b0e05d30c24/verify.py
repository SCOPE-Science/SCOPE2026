"""Finite local obstruction and periodic upper witness for packing-domatic colorings of the two-way path."""
from math import ceil
from fractions import Fraction

# Period-six packing coloring and six broadcast-domatic blocks, modulo 30.
color_period = (5, 1, 2, 4, 1, 3)
blocks = (
    (1, 4, 7, 10, 13, 16, 19, 22, 25, 28),
    (0, 8, 15, 23),
    (2, 9, 17, 24),
    (3, 11, 18, 26),
    (5, 12, 20, 27),
    (6, 14, 21, 29),
)

def color(i):
    return color_period[i % 6]

lookup = {}
for g, rows in enumerate(blocks):
    for r in rows:
        assert 0 <= r < 30 and r not in lookup
        lookup[r] = g
assert set(lookup) == set(range(30))

# Packing is a condition on all infinite pairs. Periodicity reduces it
# to finite shifts: repetitions for each color and their nearest gaps.
for c in range(1, 6):
    places = [i for i in range(-30, 61) if color(i) == c]
    assert len(places) >= 2
    assert min(v - u for u, v in zip(places, places[1:])) > c

# Every block broadcasts to every integer: check one period and all
# transmitters at distance <= 5 (only nearby translates can matter).
coverage_table = []
for x in range(30):
    counts = []
    for g in range(6):
        sources = [v for v in range(x - 5, x + 6)
                   if lookup[v % 30] == g and abs(x - v) <= color(v)]
        assert sources, (x, g)
        counts.append(len(sources))
    coverage_table.append(tuple(counts))
assert min(min(row) for row in coverage_table) >= 1

# For a hypothetic packing coloring with palette {1,2,3,4} and six
# disjoint dominating broadcasts, every one of N consecutive vertices
# needs at least six distinct transmitters from its radius-four window.
N = 367
M = N + 8
max_counts = {j: ceil(M / (j + 1)) for j in (2, 3, 4)}
upper_incidence = 3 * M + sum(2 * (j - 1) * max_counts[j] for j in (2, 3, 4))
assert upper_incidence == 2201
assert 6 * N == 2202
assert upper_incidence < 6 * N

# Asymptotic version of the obstruction.
capacity = Fraction(3) + sum(Fraction(2 * (j - 1), j + 1) for j in (2, 3, 4))
assert capacity == Fraction(88, 15)
assert capacity < 6
print('PACKING_COLORS_OK; PERIOD=6')
print('PARTITION_AND_BROADCAST_OK; PERIOD=30; PARTS=6')
print('COVERAGE_COUNTS_MINIMUM=', min(min(row) for row in coverage_table), sep='')
print(f'FINITE_OBSTRUCTION_OK; N={N}; WINDOW={M}; CAPACITY={upper_incidence}; DEMAND={6*N}')
print('ASYMPTOTIC_CAPACITY=88/15 < 6')
print('VERIFY_OK')
