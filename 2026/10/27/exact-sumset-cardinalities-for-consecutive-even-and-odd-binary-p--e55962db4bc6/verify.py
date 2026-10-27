"""Exact finite-state certificate for adjacent-length binary palindrome sumsets.

Runs with Python 3 standard library only.
"""
from collections import deque
from itertools import product

BITS = (0, 1)
LABELS = tuple(product(BITS, repeat=2))


def successor(subset, output):
    lower_bit, upper_bit = output
    result = set()
    for lower_carry, upper_carry, preceding_digit in subset:
        for a, b, next_upper_carry in product(BITS, repeat=3):
            low_total = a + b + lower_carry
            upper_total = preceding_digit + b + next_upper_carry
            if (low_total % 2 == lower_bit and
                    upper_total % 2 == upper_bit and
                    upper_total // 2 == upper_carry):
                result.add((low_total // 2, next_upper_carry, a))
    return frozenset(result)


def middle_outputs(subset):
    outputs = set()
    for lower_carry, upper_carry, preceding_digit in subset:
        for center in BITS:
            total = preceding_digit + center + lower_carry
            if total // 2 == upper_carry:
                outputs.add(total % 2)
    return len(outputs)


def automaton():
    starts = tuple(frozenset(((1, upper_carry, 1),))
                   for upper_carry in BITS)
    reachable = set(starts)
    queue = deque(starts)
    while queue:
        subset = queue.popleft()
        for label in LABELS:
            next_subset = successor(subset, label)
            if next_subset and next_subset not in reachable:
                reachable.add(next_subset)
                queue.append(next_subset)
    states = sorted(reachable, key=lambda s: (len(s), str(sorted(s))))
    ids = {state: index for index, state in enumerate(states)}
    matrix = [[0] * len(states) for _ in states]
    for state in states:
        for label in LABELS:
            next_subset = successor(state, label)
            if next_subset:
                matrix[ids[state]][ids[next_subset]] += 1
    initial = [0] * len(states)
    for start in starts:
        initial[ids[start]] += 1
    terminal = [middle_outputs(state) for state in states]
    return initial, matrix, terminal


def step(vector, matrix):
    output = [0] * len(vector)
    for i, coefficient in enumerate(vector):
        if coefficient:
            for j, weight in enumerate(matrix[i]):
                if weight:
                    output[j] += coefficient * weight
    return output


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def palindromes(length):
    result = []
    for low_half in product(BITS, repeat=(length + 1) // 2 - 1):
        first_half = (1,) + low_half
        digits = first_half + tuple(reversed(first_half[:length // 2]))
        result.append(int(''.join(map(str, digits)), 2))
    return result


def direct_count(m):
    even = palindromes(2 * m)
    odd = palindromes(2 * m + 1)
    return len({a + b for a in even for b in odd})


def verify():
    initial, matrix, terminal = automaton()
    dimension = len(initial)
    assert dimension == 37, dimension
    rows = [initial]
    for _ in range(dimension + 8):
        rows.append(step(rows[-1], matrix))
    counts = [dot(row, terminal) for row in rows]
    first_eight = [2, 7, 27, 95, 345, 1259, 4629, 17019]
    assert counts[:8] == first_eight
    for m in range(1, 9):
        assert counts[m - 1] == direct_count(m), (m, counts[m - 1], direct_count(m))
    # P(X) = X^8 - 7X^7 + 14X^6 - 4X^5 - 22X^4
    #         + 56X^3 - 36X^2 - 16X + 16.
    polynomial = (16, -16, -36, 56, -22, -4, 14, -7, 1)
    for k in range(dimension):
        assert sum(polynomial[j] * counts[k+j] for j in range(9)) == 0, k
    print("VERIFY_OK: 37 reachable subset states; direct counts m=1..8; "
          "37 Cayley-Hamilton recurrence checks")
    print('first_eight:', counts[:8])


if __name__ == '__main__':
    verify()
