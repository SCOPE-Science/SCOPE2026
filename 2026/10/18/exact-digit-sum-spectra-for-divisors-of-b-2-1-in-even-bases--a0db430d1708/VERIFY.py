#!/usr/bin/env python3
"""Independent finite-state reachability check of a digit-sum spectrum theorem.

All accepted digit strings may have arbitrary length. The sum coordinate is bounded
by the checked target-sum cutoff, so every state graph is finite.
"""
from collections import deque


def reachable_digit_sums(base, modulus, maximum):
    seen = bytearray(modulus * (maximum + 1))
    todo = deque()
    for first in range(1, min(base, maximum + 1)):
        r = first % modulus
        idx = first * modulus + r
        if not seen[idx]:
            seen[idx] = 1
            todo.append((r, first))
    while todo:
        residue, total = todo.popleft()
        for digit in range(base):
            next_total = total + digit
            if next_total > maximum:
                break
            next_residue = (residue * base + digit) % modulus
            idx = next_total * modulus + next_residue
            if not seen[idx]:
                seen[idx] = 1
                todo.append((next_residue, next_total))
    return {t for t in range(1, maximum + 1) if seen[t * modulus]}


def main():
    count = 0
    for base in range(2, 25, 2):
        for divisor in range(1, base):
            if (base - 1) % divisor:
                continue
            modulus = divisor * (base + 1)
            maximum = base + 3 * divisor + 5
            actual = reachable_digit_sums(base, modulus, maximum)
            predicted = {
                t for t in range(1, maximum + 1)
                if t % divisor == 0 and (t % 2 == 0 or t > base - 1)
            }
            assert actual == predicted, (base, divisor, actual ^ predicted)
            count += 1
    assert count == 28, count
    print(f'PASS: {count} parameter pairs; arbitrary-length reachability '
          'up to each specified digit-sum cutoff')


if __name__ == '__main__':
    main()
