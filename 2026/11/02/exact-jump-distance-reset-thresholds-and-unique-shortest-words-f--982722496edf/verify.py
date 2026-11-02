#!/usr/bin/env python3
"""Finite checks for the cyclic unitary jump automaton. Run with python3 verify.py."""
from collections import deque
from math import gcd


def letter_image(mask, n, d, letter):
    if letter == 'a':
        return (mask & ~1) | (((mask & 1) != 0) << d)
    allbits = (1 << n) - 1
    return ((mask << 1) & allbits) | (mask >> (n - 1))


def shortest_and_count(n, d):
    first = (1 << n) - 1
    distance = {first: 0}
    count = {first: 1}
    queue = deque([first])
    while queue:
        mask = queue.popleft()
        if mask.bit_count() == 1:
            continue
        for letter in 'ab':
            next_mask = letter_image(mask, n, d, letter)
            if next_mask not in distance:
                distance[next_mask] = distance[mask] + 1
                count[next_mask] = count[mask]
                queue.append(next_mask)
            elif distance[next_mask] == distance[mask] + 1:
                count[next_mask] += count[mask]
    finals = [(distance[mask], count[mask]) for mask in distance if mask.bit_count() == 1]
    if not finals:
        return None, 0
    best = min(distance for distance, _ in finals)
    return best, sum(number for distance, number in finals if distance == best)


def witness_check(n, d):
    mask = (1 << n) - 1
    for j in range(n - 1):
        mask = letter_image(mask, n, d, 'a')
        if j < n - 2:
            for _ in range(n - d):
                mask = letter_image(mask, n, d, 'b')
    assert mask.bit_count() == 1, (n, d, mask)
    assert mask == 1 << d, (n, d, mask)


def main():
    cases = 0
    synchronizing = 0
    nonsynchronizing = 0
    for n in range(2, 12):
        for d in range(1, n):
            shortest, number = shortest_and_count(n, d)
            if gcd(n, d) == 1:
                desired = 1 + (n - 2) * (n - d + 1)
                assert (shortest, number) == (desired, 1), (n, d, shortest, number, desired)
                witness_check(n, d)
                synchronizing += 1
            else:
                assert (shortest, number) == (None, 0), (n, d, shortest, number)
                nonsynchronizing += 1
            cases += 1
    for n in range(12, 101):
        for d in range(1, n):
            if gcd(n, d) == 1:
                witness_check(n, d)
    print(f'VERIFY_OK exhaustive_n=2..11 cases={cases} sync={synchronizing} nonsync={nonsynchronizing} witness_n=2..100 shortest_word_multiplicity=1')


if __name__ == '__main__':
    main()
