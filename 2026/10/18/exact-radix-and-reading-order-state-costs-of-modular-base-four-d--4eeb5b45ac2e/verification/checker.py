#!/usr/bin/env python3
"""Finite checks for exact automaton state counts of modular base-four digit counts.

This script verifies concrete instances only; the companion mathematical proof
establishes the uniform theorems for every modulus.
"""
from collections import deque


def digit_3_count(n):
    count = 0
    while n > 0:
        count += n % 4 == 3
        n //= 4
    return count


def msd_next(st, digit, modulus):
    u, v, prev = st
    return ((v + prev * digit) % modulus, u, digit)


def lsd_next(st, digit, modulus):
    residue, pending = st
    if pending == 2:  # no low bit pending
        return residue, digit
    return (residue + pending * digit) % modulus, 2


def base4_next(st, digit, modulus):
    return (st + (digit == 3)) % modulus


def count_minimal(start, alphabet, transition, output):
    found = {start}
    queue = deque([start])
    edges = {}
    while queue:
        st = queue.popleft()
        edges[st] = tuple(transition(st, d) for d in alphabet)
        for dest in edges[st]:
            if dest not in found:
                found.add(dest)
                queue.append(dest)
    blocks = [frozenset(s for s in found if output(s) == value)
              for value in (False, True)]
    blocks = [b for b in blocks if b]
    while True:
        membership = {s: i for i, group in enumerate(blocks) for s in group}
        new_blocks = []
        for group in blocks:
            signatures = {}
            for state in group:
                signature = tuple(membership[nxt] for nxt in edges[state])
                signatures.setdefault(signature, set()).add(state)
            new_blocks.extend(frozenset(v) for v in signatures.values())
        if len(new_blocks) == len(blocks):
            return len(found), len(blocks)
        blocks = new_blocks


def visit(start, transition, word):
    state = start
    for digit in word:
        state = transition(state, digit)
    return state


def digits(n, base):
    if n == 0:
        return [0]
    result = []
    while n:
        result.append(n % base)
        n //= base
    return result[::-1]


def check(modulus, limit=512):
    msd = lambda state, digit: msd_next(state, digit, modulus)
    lsd = lambda state, digit: lsd_next(state, digit, modulus)
    quad = lambda state, digit: base4_next(state, digit, modulus)
    sizes = {
        'binary_msd': count_minimal((0, 0, 0), (0, 1), msd,
                                     lambda state: state[0] == 0),
        'binary_lsd': count_minimal((0, 2), (0, 1), lsd,
                                     lambda state: state[0] == 0),
        'base4_msd': count_minimal(0, (0, 1, 2, 3), quad,
                                   lambda state: state == 0)
    }
    assert sizes == {
        'binary_msd': (2 * modulus * modulus, 2 * modulus * modulus),
        'binary_lsd': (3 * modulus, 3 * modulus),
        'base4_msd': (modulus, modulus)
    }, (modulus, sizes)
    tested = 0
    for n in range(limit):
        correct = digit_3_count(n) % modulus == 0
        binary = digits(n, 2)
        quaternary = digits(n, 4)
        for zero_pad in range(4):
            assert (visit((0, 0, 0), msd, [0]*zero_pad + binary)[0] == 0) == correct
            assert (visit((0, 2), lsd, list(reversed(binary)) + [0]*zero_pad)[0] == 0) == correct
            assert (visit(0, quad, [0]*zero_pad + quaternary) == 0) == correct
            tested += 3
    print(f'modulus={modulus}: base4(msd)={modulus}, binary(msd)={2*modulus**2}, '
          f'binary(lsd)={3*modulus}; digit-output checks={tested}')


if __name__ == '__main__':
    for m in range(2, 10):
        check(m)
    print('ALL MODULAR BASE-CHANGE CHECKS PASSED')
