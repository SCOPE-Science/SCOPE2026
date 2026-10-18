#!/usr/bin/env python3
"""Independent finite-state and arithmetic checks for a cyclotomic digit-sum theorem."""
from collections import deque


def semigroup_membership(base, bound):
    generators = (3, base + 2, 2 * base + 1)
    possible = [False] * (bound + 1)
    possible[0] = True
    for total in range(1, bound + 1):
        possible[total] = any(total >= generator and possible[total - generator]
                              for generator in generators)
    return possible


def digit_automaton_sums(base, bound):
    modulus = base * base + base + 1
    powers = (1, base, base * base)
    queue = deque([(0, 0, 0)])  # used digit sum, residue, next position class
    visited = {(0, 0, 0)}
    reachable = [False] * (bound + 1)
    while queue:
        total, residue, phase = queue.popleft()
        if total:
            if residue == 0:
                reachable[total] = True
        for digit in range(min(base - 1, bound - total) + 1):
            state = (total + digit,
                     (residue + digit * powers[phase]) % modulus,
                     (phase + 1) % 3)
            if state not in visited:
                visited.add(state)
                queue.append(state)
    return reachable, len(visited)


def main():
    checks = 0
    states = 0
    for base in list(range(2, 17)) + [18, 20, 23]:
        bound = 4 * base + 21
        expected = semigroup_membership(base, bound)
        actual, n_states = digit_automaton_sums(base, bound)
        states += n_states
        for total in range(1, bound + 1):
            assert actual[total] == expected[total], (base, total)
            checks += 1
        assert all(x % 3 == 0 for x in range(1, bound + 1)
                   if expected[x]) if base % 3 == 1 else True
        if base % 3 != 1:
            gaps = [x for x in range(1, 2 * base + 2) if not expected[x]]
            assert len(gaps) == base, (base, gaps)
            assert max(gaps) == 2 * base - 2, (base, gaps)
            assert all(expected[x] for x in range(2 * base - 1, bound + 1))
    print('PASS: 18 bases; %d digit-sum membership comparisons; %d finite-state visits.' % (checks, states))
    print('Checks include the exact gap count, Frobenius bound, and the divisible-by-three branch.')


if __name__ == '__main__':
    main()
