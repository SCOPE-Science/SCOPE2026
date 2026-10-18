"""Finite exact checks for facet enumeration of the squared-path graph metric.

Run: python3 verify_facets.py
Uses only the Python standard library. Its finite tests are not a proof of the
all-dimensional generating function; that proof accompanies the result.
"""
from itertools import product

STATES = tuple((d, c) for d in (-1, 0, 1) for c in (0, 1))
TRANSFER = (
    (0, 0, 1, 0, 0, 0),
    (0, 0, 0, 1, 0, 1),
    (0, 1, 0, 0, 0, 1),
    (0, 1, 1, 0, 0, 1),
    (0, 0, 1, 0, 0, 0),
    (0, 1, 0, 1, 0, 0),
)
INITIAL = (0, 1, 1, 0, 0, 1)
TERMINAL = (0, 1, 0, 1, 0, 1)

def transition(state, next_state):
    d, joined = state
    step, next_joined = next_state
    heights = (0, d, d + step)
    if abs(heights[2] - heights[0]) > 1:
        return False
    groups = list(range(3))
    def root(i):
        while groups[i] != i:
            i = groups[i]
        return i
    def merge(i, j):
        groups[root(i)] = root(j)
    if joined:
        merge(0, 1)
    if abs(heights[0] - heights[2]) == 1:
        merge(0, 2)
    if abs(heights[1] - heights[2]) == 1:
        merge(1, 2)
    if root(0) not in (root(1), root(2)):
        return False
    return (root(1) == root(2)) == bool(next_joined)

def multiply_row(row):
    return tuple(sum(row[i] * TRANSFER[i][j] for i in range(6)) for j in range(6))

def inner(a, b):
    return sum(x*y for x, y in zip(a, b))

def direct_count(n):
    count = 0
    for increments in product((-1, 0, 1), repeat=n-1):
        heights = (0,)
        for step in increments:
            heights += (heights[-1] + step,)
        if any(abs(heights[i] - heights[i+2]) > 1 for i in range(n-2)):
            continue
        parents = list(range(n))
        def root(i):
            while i != parents[i]:
                i = parents[i]
            return i
        for i in range(n):
            for j in range(i+1, min(i+3, n)):
                if abs(heights[i] - heights[j]) == 1:
                    parents[root(i)] = root(j)
        if len({root(i) for i in range(n)}) == 1:
            count += 1
    return count

def main():
    checks = 0
    for i in range(6):
        for j in range(6):
            assert int(transition(STATES[i], STATES[j])) == TRANSFER[i][j]
            checks += 1
    row0 = INITIAL
    row1 = multiply_row(row0)
    row2 = multiply_row(row1)
    row3 = multiply_row(row2)
    assert all(row3[j] == row2[j] + 2*row1[j] + 2*row0[j]
               for j in range(6))
    checks += 6
    row = INITIAL
    terms = []
    for n in range(2, 65):
        terms.append(inner(row, TERMINAL))
        row = multiply_row(row)
    assert terms[:12] == [2, 6, 12, 28, 64, 144, 328, 744, 1688, 3832, 8696, 19736]
    checks += 12
    for idx in range(3, len(terms)):
        assert terms[idx] == terms[idx-1] + 2*terms[idx-2] + 2*terms[idx-3]
        checks += 1
    for n in range(2, 12):
        assert direct_count(n) == terms[n-2]
        checks += 1
    print('PASS', checks, 'exact assertions; counts n=2..11:', terms[:10])

if __name__ == '__main__':
    main()
