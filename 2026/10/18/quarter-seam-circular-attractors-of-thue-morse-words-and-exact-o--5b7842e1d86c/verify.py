"""Recompute exact cyclic Thue--Morse factor-cover constraints and four-point transversals.

Python 3 standard library; no input files or third-party packages needed.
"""
from collections import Counter
from itertools import product

BASES = {(0, 4, 8, 12), (2, 4, 10, 12), (2, 5, 10, 13),
         (3, 6, 11, 14), (4, 6, 12, 14)}


def word(n):
    w = '0'
    for _ in range(n):
        w += ''.join('1' if a == '0' else '0' for a in w)
    return w


def masks(w):
    N = len(w)
    double = w + w
    full = (1 << N) - 1
    cover = set()
    for length in range(1, N + 1):
        seen = {}
        window = (1 << length) - 1
        for start in range(N):
            factor = double[start:start + length]
            positions = window << start
            positions = (positions & full) | (positions >> N)
            seen[factor] = seen.get(factor, 0) | positions
        cover.update(seen.values())
    # Every factor set containing another can be dropped without changing transversals.
    ordered = sorted(cover, key=lambda x: x.bit_count())
    essential = []
    for c in ordered:
        if not any((c & d) == d for d in essential):
            essential.append(c)
    return essential


def optimal_sets(constraints, N, limit):
    # Complete branching: in any hitting set, a currently missed constraint
    # must be hit by one of its positions. Memoization removes duplicate branches.
    # A solution found before the depth limit is extended to all supersets.
    solutions = set()
    visited = set()
    def visit(mask, depth):
        state = mask, depth
        if state in visited:
            return
        visited.add(state)
        missing = None
        smallest = N + 1
        for c in constraints:
            if c & mask == 0 and c.bit_count() < smallest:
                missing = c
                smallest = c.bit_count()
        if missing is None:
            if depth == limit:
                solutions.add(mask)
            else:
                for i in range(N):
                    bit = 1 << i
                    if not mask & bit:
                        visit(mask | bit, depth + 1)
            return
        if depth == limit:
            return
        options = missing & ~mask
        while options:
            bit = options & -options
            options -= bit
            visit(mask | bit, depth + 1)
    visit(0, 0)
    return solutions


def expected_families(n):
    N = 1 << n
    h = N // 16
    output = set()
    for boundaries in BASES:
        for sides in product((0, 1), repeat=4):
            positions = [(j * h - side) % N for j, side in zip(boundaries, sides)]
            output.add(sum(1 << p for p in positions))
    return output


def check():
    expected = {2: (2, 2), 3: (2, 2), 4: (4, 151), 5: (4, 96),
                6: (4, 96), 7: (4, 80), 8: (4, 80)}
    critical = {2: 4, 3: 4, 4: 14, 5: 20, 6: 28, 7: 36, 8: 44}
    for n in range(2, 9):
        w = word(n)
        constraints = masks(w)
        assert len(constraints) == critical[n], (n, len(constraints))
        k, count = expected[n]
        for smaller in range(1, k):
            assert not optimal_sets(constraints, len(w), smaller), (n, smaller)
        actual = optimal_sets(constraints, len(w), k)
        assert len(actual) == count, (n, len(actual))
        if n >= 4:
            m = len(w) // 4
            quarter = set()
            for side in product((0, 1), repeat=4):
                quarter.add(sum(1 << ((j * m - e) % len(w))
                                for j, e in enumerate(side)))
            assert len(quarter) == 16 and quarter <= actual, n
        if n in (7, 8):
            wanted = expected_families(n)
            assert len(wanted) == 80
            assert actual == wanted, n
        print(f'order={n} length={len(w)} constraints={len(constraints)} ' 
              f'minimum={k} optimizers={len(actual)}')
    w = word(6)
    linear_factors = {w[i:i+13] for i in range(len(w) - 12)}
    assert len(linear_factors) == 40
    print('length-13 linear factors in order-6 word=40')
    print('ALL CHECKS PASS')


if __name__ == '__main__':
    check()
