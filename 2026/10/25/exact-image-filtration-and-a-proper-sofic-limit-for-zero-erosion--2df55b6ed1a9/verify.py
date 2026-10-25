#!/usr/bin/env python3
"""Finite consistency tests for a binary zero-erosion cellular automaton.

Every assertion concerns periodic rings or finite words; analytical claims
on arbitrary bi-infinite sequences are proved separately.
"""
from itertools import product

def update(state, r):
    length = len(state)
    return tuple(
        1 if state[i] == 0 and state[(i + 1) % length] == 1
             and all(state[(i - j) % length] == 0 for j in range(1, r))
        else state[i]
        for i in range(length)
    )

def admissible_ring(state, r, n):
    length = len(state)
    if len(set(state)) <= 1:
        return True
    for start in range(length):
        if state[(start - 1) % length] != 1 or state[start] != 0:
            continue
        z = 0
        while state[(start + z) % length] == 0:
            z += 1
        if z >= r:
            ones = 0
            while state[(start + z + ones) % length] == 1:
                ones += 1
            if ones <= n:
                return False
    return True

def avoids_finite_word(word, r):
    for j in range(1, len(word) + 1):
        token = (0,) * r + (1,) * j + (0,)
        if any(word[i:i + len(token)] == token
               for i in range(len(word) - len(token) + 1)):
            return False
    return True

def automaton_accepts(word, r):
    state = 0
    # Z_0,...,Z_r indexed 0..r; P indexed r+1.
    for bit in word:
        if state == r + 1:
            if bit == 0:
                return False
        elif bit == 0:
            state = min(r, state + 1)
        elif state == r:
            state = r + 1
        else:
            state = 0
    return True

def run():
    ring_checks = 0
    for r in range(2, 6):
        for length in range(r + 2, 13):
            strings = list(product((0, 1), repeat=length))
            reachable = set(strings)
            for n in range(1, 5):
                reachable = {update(x, r) for x in reachable}
                prediction = {x for x in strings if admissible_ring(x, r, n)}
                assert reachable == prediction, (r, length, n)
                ring_checks += 1
    word_checks = 0
    for r in range(2, 6):
        for length in range(0, 13):
            for word in product((0, 1), repeat=length):
                assert automaton_accepts(word, r) == avoids_finite_word(word, r), (r, length, word)
                word_checks += 1
    for r in range(2, 8):
        for n in range(0, 11):
            word = (0,) * r + (1,) * (n + 1)
            assert admissible_ring(word, r, n)
            assert not admissible_ring(word, r, n + 1)
    print(f"VERIFY_OK: {ring_checks} exhaustive ring image comparisons; {word_checks} finite-word automaton checks; 66 strict-descent witnesses")

if __name__ == '__main__':
    run()
