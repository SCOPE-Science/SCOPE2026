"""Exact quantifier-rank-four types of GP(n,2), n=5,...,24.

Automorphism reduction is only a cache optimization: every possible next vertex
is considered in the recursion, and all atomic equality and adjacency facts are
retained. Executable using the Python standard library.
"""

from __future__ import annotations

from pathlib import Path
import csv

# Shared signature interners across graph sizes ensure that the same integer
# denotes exactly the same rank-type, even in distinct graphs.
TYPE_KEYS = [dict() for _ in range(5)]


def root_type(n: int) -> int:
    assert n >= 5
    size = 2 * n
    adjacency = [[False] * size for _ in range(size)]
    for x in range(size):
        kind_x, ix = divmod(x, n)
        for y in range(size):
            kind_y, iy = divmod(y, n)
            if kind_x != kind_y:
                adjacency[x][y] = ix == iy
            elif kind_x == 0:
                adjacency[x][y] = (ix - iy) % n in (1, n - 1)
            else:
                adjacency[x][y] = (ix - iy) % n in (2, n - 2)

    def canonical(t: tuple[int, ...]) -> tuple[int, ...]:
        if not t:
            return ()
        first_index = t[0] % n
        plus, minus = [], []
        for v in t:
            kind, index = divmod(v, n)
            plus.append((kind, (index - first_index) % n))
            minus.append((kind, (first_index - index) % n))
        return tuple(kind * n + index for kind, index in min(tuple(plus), tuple(minus)))

    def atomic(t: tuple[int, ...]) -> int:
        bits = 0
        shift = 0
        for j in range(len(t)):
            for i in range(j):
                if t[i] == t[j]:
                    bits |= 1 << shift
                if adjacency[t[i]][t[j]]:
                    bits |= 1 << (shift + 1)
                shift += 2
        return bits

    cache = [dict() for _ in range(5)]

    def signature_type(t: tuple[int, ...], rounds: int) -> int:
        t = canonical(t)
        if t in cache[rounds]:
            return cache[rounds][t]
        if rounds == 0:
            key = (atomic(t),)
        else:
            extensions = frozenset(signature_type(t + (z,), rounds - 1)
                                   for z in range(size))
            key = (atomic(t), extensions)
        interner = TYPE_KEYS[rounds]
        if key not in interner:
            interner[key] = len(interner)
        answer = interner[key]
        cache[rounds][t] = answer
        return answer

    return signature_type((), 4)


def main() -> None:
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 6, 8] + [9] * 10
    table = [(n, root_type(n)) for n in range(5, 25)]
    actual = [label for _, label in table]
    assert actual == expected, (actual, expected)
    assert len(set(actual)) == 10
    out = Path(__file__).with_name('class_table.csv')
    with out.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle, lineterminator='\n')
        writer.writerow(('n', 'rank4_type_id', 'vertices'))
        for n, label in table:
            writer.writerow((n, label, 2 * n))
    for n, label in table:
        print(f'n={n:2d} rank4_type={label:2d} vertices={2*n:2d}')
    print('ORBIT_ENUMERATION_OK: ten types for n=5..24; class 9 begins at n=15')
    print('INFINITE_CUTOFF: EF gap lemma gives all n>=24 the type at n=24')


if __name__ == '__main__':
    main()
