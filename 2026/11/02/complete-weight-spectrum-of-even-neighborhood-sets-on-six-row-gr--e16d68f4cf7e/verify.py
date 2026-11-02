"""Exact six-row closed-neighborhood kernel checks (Python standard library)."""
from collections import Counter

BASE = {0: 1, 18: 4, 20: 12, 22: 12, 24: 3,
        26: 12, 28: 15, 30: 4, 36: 1}


def predicted(n):
    if (n + 1) % 9:
        return {0: 1}
    q = (n + 1) // 9
    return {q * weight: count for weight, count in BASE.items()}


def neighboring_cells(n, col, row):
    result = 1 << (6 * col + row)
    for dc, dr in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        x, y = col + dc, row + dr
        if 0 <= x < n and 0 <= y < 6:
            result |= 1 << (6 * x + y)
    return result


def independent_kernel(n):
    dim = 6 * n
    original = [neighboring_cells(n, col, row)
                for col in range(n) for row in range(6)]
    matrix = original.copy()
    pivots = []
    rank = 0
    for col in range(dim):
        pivot = next((i for i in range(rank, dim) if (matrix[i] >> col) & 1), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        for i in range(dim):
            if i != rank and ((matrix[i] >> col) & 1):
                matrix[i] ^= matrix[rank]
        pivots.append(col)
        rank += 1
    free_cols = sorted(set(range(dim)) - set(pivots))
    basis = []
    for free in free_cols:
        b = 1 << free
        for r, pivot in enumerate(pivots):
            if (matrix[r] >> free) & 1:
                b |= 1 << pivot
        assert all((b & row).bit_count() % 2 == 0 for row in original)
        basis.append(b)
    weights = Counter()
    for choice in range(1 << len(basis)):
        word = 0
        for j, b in enumerate(basis):
            if (choice >> j) & 1:
                word ^= b
        weights[word.bit_count()] += 1
    return dict(weights), len(basis)


def apply_B(bits):
    return bits ^ ((bits << 1) & 63) ^ (bits >> 1)


def chased(n):
    weights = Counter()
    for first in range(64):
        prev, curr = 0, first
        columns = []
        for _ in range(n):
            columns.append(curr)
            prev, curr = curr, apply_B(curr) ^ prev
        if curr:
            continue
        word = sum(bits << (6 * j) for j, bits in enumerate(columns))
        assert all((word & neighboring_cells(n, c, r)).bit_count() % 2 == 0
                   for c in range(n) for r in range(6))
        weights[sum(bits.bit_count() for bits in columns)] += 1
    return dict(weights)


def block_table():
    groups = {}
    for first in range(64):
        prev, curr, weight = 0, first, 0
        for _ in range(8):
            weight += curr.bit_count()
            prev, curr = curr, apply_B(curr) ^ prev
        assert curr == 0
        groups.setdefault(weight, []).append(first)
    assert {w: len(v) for w, v in groups.items()} == BASE
    assert len({x for values in groups.values() for x in values}) == 64
    print('EXHAUSTIVE_64_INITIAL_COLUMNS_OK')


def main():
    block_table()
    for n in range(1, 55):
        weights, dimension = independent_kernel(n)
        assert weights == predicted(n), (n, weights, predicted(n))
        assert dimension == (6 if (n + 1) % 9 == 0 else 0)
    print('INDEPENDENT_GF2_MATRIX_ELIMINATION_OK', 54)
    for n in range(1, 145):
        assert chased(n) == predicted(n), (n, chased(n), predicted(n))
    print('COLUMN_RECURRENCE_AND_DIRECT_PARITY_OK', 144)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
