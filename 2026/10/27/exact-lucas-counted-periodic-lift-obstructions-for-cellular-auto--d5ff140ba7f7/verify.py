#!/usr/bin/env python3
"""Finite exact checks of periodic-lift counting for elementary cellular automaton 18."""
from itertools import product
from functools import lru_cache

RULE = 18
STATES = 4
IDENTITY = tuple(1 << i for i in range(STATES))


def multiply(a, b):
    return tuple(sum(1 << j for j in range(STATES)
                     if any(((a[i] >> k) & 1) and ((b[k] >> j) & 1)
                            for k in range(STATES))) for i in range(STATES))


def has_loop(a):
    return any((a[i] >> i) & 1 for i in range(STATES))


def output_ring(x):
    n = len(x)
    return tuple((RULE >> (4*x[(i-1)%n]+2*x[i]+x[(i+1)%n])) & 1
                 for i in range(n))


def transfer(sym):
    a = [0]*STATES
    for u, v, w in product((0, 1), repeat=3):
        if ((RULE >> (4*u+2*v+w)) & 1) == sym:
            a[2*u+v] |= 1 << (2*v+w)
    return tuple(a)

T = (transfer(0), transfer(1))
assert T == ((1, 12, 2, 12), (2, 0, 1, 0))


def matrix_of(word):
    a = IDENTITY
    for bit in word:
        a = multiply(a, T[bit])
    return a

# L_n=F_{n+1}+F_{n-1}; 2*cos(pi*n/3) is exactly 6-periodic.
lucas = [2, 1]
for _ in range(15):
    lucas.append(lucas[-1]+lucas[-2])
cos2 = (2, 1, -1, -2, -1, 1)
total_cases = total_missing = trace_checks = 0
for n in range(1, 13):
    observed_odd = 0
    ring_image = {output_ring(word) for word in product((0,1), repeat=n)}
    for word in product((0,1), repeat=n):
        mat = matrix_of(word)
        has_same = has_loop(mat)
        has_twice = has_loop(multiply(mat, mat))
        # A word has a bilateral antecedent iff it is a circular cycle label.
        in_image = has_twice or has_same
        # A missing periodic lift is equivalent to an odd independent set.
        has_adjacent_ones = any(word[i] and word[(i+1)%n] for i in range(n))
        exceptional = (sum(word) % 2 == 1 and not has_adjacent_ones)
        assert in_image == (has_same or exceptional), (n, word)
        assert has_same == (in_image and sum(word) % 2 == 0), (n, word)
        assert has_twice == in_image, (n, word)
        assert has_same == (word in ring_image), (n, word)
        observed_odd += exceptional
        total_cases += 1
        trace_checks += 4
    assert observed_odd == (lucas[n] - cos2[n % 6])//2, (n, observed_odd)
    assert (lucas[n] - cos2[n % 6]) % 2 == 0
    total_missing += observed_odd
print('VERIFY_OK: n=1..12; %d exact cyclic words; %d transfer/cycle/ring checks; '
      '%d total exceptional words; 12 Lucas character formulas' %
      (total_cases, trace_checks, total_missing))
