#!/usr/bin/env python3
"""Exact finite-state checks for the two-level Van der Laan classification.

Run: python3 verify.py
Only the Python standard library is required.
"""
from itertools import product
from math import gcd


def valid_block(word):
    values = sorted(word)
    return values[-1] == values[0] + values[1]


def matrix_multiply(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def matrix_trace(a):
    return sum(a[i][i] for i in range(len(a)))


def build_matrix():
    m = [[0] * 8 for _ in range(8)]
    for s in range(8):
        for next_digit in (0, 1):
            if s.bit_count() + next_digit in (2, 3):
                t = ((s << 1) & 7) | next_digit
                m[s][t] += 1
    return m


def count_words(n):
    # 1 codes the small value and 0 the large value.
    if n < 3:
        return 1 << n
    v = [1] * 8
    for _ in range(n - 3):
        w = [0] * 8
        for s, coefficient in enumerate(v):
            for t, adjacency in enumerate(M[s]):
                w[t] += coefficient * adjacency
        v = w
    return sum(v)


M = build_matrix()
assert M == [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
]

# Check every binary word of lengths 0 through 13 by direct max/min.
for n in range(14):
    brute = 0
    for bits in product((1, 2), repeat=n):
        if all(valid_block(bits[i:i + 4]) for i in range(n - 3)):
            brute += 1
    assert brute == count_words(n), (n, brute, count_words(n))

# Characteristic polynomial via exact Newton identities and matrix traces.
traces = []
power = [[int(i == j) for j in range(8)] for i in range(8)]
for _ in range(8):
    power = matrix_multiply(power, M)
    traces.append(matrix_trace(power))
coeff = [1]
for k in range(1, 9):
    numerator = -sum(coeff[k - j] * traces[j - 1] for j in range(1, k + 1))
    assert numerator % k == 0
    coeff.append(numerator // k)
assert coeff == [1, 0, -1, -1, -2, -1, 1, 1, 0]

# Independent rational-function verification at 120 Taylor coefficients.
# Q(t) = 1-t-t^3-t^4+t^6; N(t) as in the theorem.
Q = (1, -1, 0, -1, -1, 0, 1)
N = (1, 1, 2, 3, -1, 0, -2, -2, 0, 1)
c = [count_words(n) for n in range(120)]
for n in range(120):
    coefficient = sum(Q[j] * c[n - j] for j in range(min(n, 6) + 1))
    assert coefficient == (N[n] if n < len(N) else 0), (n, coefficient)
assert c[:18] == [1, 2, 4, 8, 10, 16, 25, 39, 61, 95, 149, 233,
                  364, 569, 890, 1392, 2176, 3402]

# The seven non-dead states are strongly connected.
states = range(1, 8)
def reachable(start, reverse=False):
    found = {start}
    frontier = [start]
    while frontier:
        v = frontier.pop()
        for w in states:
            has_edge = M[w][v] if reverse else M[v][w]
            if has_edge and w not in found:
                found.add(w)
                frontier.append(w)
    return found
assert reachable(1) == set(states)
assert reachable(1, reverse=True) == set(states)
assert M[3][6] and M[6][5] and M[5][3]       # three-cycle
assert M[1][3] and M[3][6] and M[6][4] and M[4][1]  # four-cycle
assert gcd(3, 4) == 1

# Compare all two-level 4-blocks with the claimed dichotomy.
for u, v in ((0, 1), (0, 8), (1, 2), (3, 6), (2, 5), (5, 5)):
    if not u < v:
        continue
    for word in product((u, v), repeat=4):
        predicted = ((word.count(u) == 4 or word.count(u) == 1)
                     if u == 0 else
                     (v == 2 * u and word.count(u) in (2, 3)))
        assert valid_block(word) == predicted, (u, v, word)

# Directly verify the 0/v infinite-type restrictions at all lengths up to 11.
for n in range(4, 12):
    candidates = [bits for bits in product((0, 5), repeat=n)
                  if all(valid_block(bits[i:i + 4]) for i in range(n - 3))]
    expected = {(0,) * n}
    for phase in range(4):
        expected.add(tuple(0 if (i - phase) % 4 == 0 else 5 for i in range(n)))
    assert set(candidates) == expected, n

# Perron root of x^6-x^5-x^3-x^2+1, strictly bracketed.
def f(x):
    return x**6 - x**5 - x**3 - x**2 + 1
lo, hi = 1.5636106955918, 1.5636106955921
assert f(lo) < 0 < f(hi)

print('VERIFY_OK')
print('exhaustive_binary_words_lengths=0..13')
print('exact_characteristic_polynomial=PASS')
print('rational_generating_function_coefficients=0..119_PASS')
print('positive_and_zero_alphabet_four_window_tests=PASS')
print('zero_case_full_word_census_lengths=4..11_PASS')
print('essential_seven_state_strong_connectivity=PASS')
print('aperiodic_three_and_four_cycles=PASS')
print('perron_root_bracket=1.5636106955918..1.5636106955921')
