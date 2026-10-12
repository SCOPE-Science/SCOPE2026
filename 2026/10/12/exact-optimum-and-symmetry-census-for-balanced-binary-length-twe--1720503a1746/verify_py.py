#!/usr/bin/env python3
"""Exact census of constant-composition non-overlapping one-error-correcting codes."""
import itertools
import sys
from collections import Counter

LENGTH = 12
WEIGHT = LENGTH // 2


def is_eligible(s):
    return s.count('1') == WEIGHT and all(s[:k] != s[-k:] for k in range(1, LENGTH))


def edge(s, t):
    if sum(c != d for c, d in zip(s, t)) < 4:
        return False
    return all(s[:k] != t[-k:] and t[:k] != s[-k:] for k in range(1, LENGTH))


vertices = [''.join(t) for t in itertools.product('01', repeat=LENGTH) if is_eligible(''.join(t))]
adj = [0] * len(vertices)
for i in range(len(vertices)):
    for j in range(i + 1, len(vertices)):
        if edge(vertices[i], vertices[j]):
            adj[i] |= 1 << j
            adj[j] |= 1 << i

size_profile = Counter()
solutions = []
visits = 0


def enumerate_maximal(p, x, selected):
    global visits
    visits += 1
    if not (p or x):
        k = len(selected)
        size_profile[k] += 1
        if k == 13:
            solutions.append(' '.join(vertices[j] for j in sorted(selected)))
        return
    union = p | x
    pivot = max(iter_bits(union), key=lambda i: (p & adj[i]).bit_count())
    choices = p & ~adj[pivot]
    while choices:
        bit = choices & -choices
        v = bit.bit_length() - 1
        enumerate_maximal(p & adj[v], x & adj[v], selected + (v,))
        p ^= bit
        x |= bit
        choices ^= bit


def iter_bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


enumerate_maximal((1 << len(vertices)) - 1, 0, ())
solutions.sort()
if len(sys.argv) > 1:
    with open(sys.argv[1], 'w', encoding='ascii', newline='\n') as out:
        for sol in solutions:
            out.write(sol + '\n')
print('vertices', len(vertices), 'edges', sum(x.bit_count() for x in adj) // 2)
print('visits', visits, 'maximal_profile', sorted(size_profile.items()))
print('optimizers', len(solutions), 'maximum_size', max(size_profile))
