#!/usr/bin/env python3
"""Finite symbolic-reduction checks for a period-five binomid construction."""
from itertools import product

PERIOD = 5
A = (0, 1, 1, 0, 2)
EXPECTED = (
    (0, 1, 1, 0, 2),
    (0, 1, 0, 1, 1),
    (0, 0, 1, 0, 1),
    (0, 2, 1, 1, 2),
    (0, 0, 0, 0, 0),
)


def column_exponents(word, c):
    period = len(word)
    base = sum(word[i % period] for i in range(c))
    return tuple(sum(word[(start+i) % period] for i in range(c)) - base
                 for start in range(period))


def is_periodic_binomid(word):
    period = len(word)
    return all(sum(word[i] for i in range(r)) <=
               sum(word[(start+i) % period] for i in range(r))
               for r in range(1, period)
               for start in range(period))


def is_periodic_divisible(word):
    period = len(word)
    return all(word[(i-1) % period] <= word[(j-1) % period]
               for j in range(1, period*period+1)
               for i in range(1, j+1) if j % i == 0)


for c in range(1, 6):
    assert column_exponents(A, c) == EXPECTED[c - 1], c
    for r in range(1, PERIOD):
        b = EXPECTED[c - 1]
        initial = sum(b[:r])
        cyclic_sums = [sum(b[(start+i) % PERIOD] for i in range(r))
                       for start in range(PERIOD)]
        assert initial == min(cyclic_sums), (c, r, cyclic_sums)

for c in range(1, 101):
    assert column_exponents(A, c) == EXPECTED[(c-1) % PERIOD], c

bounded_small_words = 0
for period in range(1, 5):
    for word in product(range(5), repeat=period):
        all_levels = all(is_periodic_binomid(column_exponents(word, c))
                         for c in range(1, period+1))
        if all_levels:
            assert is_periodic_divisible(word), (period, word)
        bounded_small_words += 1

# Independent direct factorial-ratio exponent checks, all integers up to n=120.
checked_pairs = 0
for c in range(1, 36):
    b = [sum(A[(n - 1 + j) % PERIOD] for j in range(c))
         - sum(A[j % PERIOD] for j in range(c))
         for n in range(1, 121)]
    assert min(b) >= 0
    ps = [0]
    for exponent in b:
        ps.append(ps[-1] + exponent)
    for n in range(1, 121):
        for k in range(n + 1):
            assert ps[n] - ps[n-k] - ps[k] >= 0, (c, n, k)
            checked_pairs += 1

for q in (2, 3, 4, 6, 9):
    f = [q ** A[(n-1) % PERIOD] for n in range(1, 46)]
    assert f[1] == q and f[3] == 1 and f[1] > f[3]
    assert f[:5] == [1, q, q, 1, q*q]

print('VERIFY_OK')
print('period_five_column_patterns=5')
print('cyclic_minimum_inequalities=100')
print('columns_modulo_period_checked=100')
print('small_period_valuation_words_checked=', bounded_small_words)
print('direct_column_integer_exponent_checks=', checked_pairs)
print('full_infinite_proof_depends_on_period_reduction_and_symbolic_lemmas=True')
