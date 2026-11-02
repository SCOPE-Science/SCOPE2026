#!/usr/bin/env python3
"""Independent finite checks for carousel-tournament logical cutoffs.

Run: python3 verify.py
Only Python standard library is required. Finite checks corroborate,
not replace, the arbitrary-rank mathematical proof.
"""
from functools import lru_cache
from itertools import product


def arc(n, x, y):
    return x != y and 1 <= ((y - x) % n) <= n // 2


@lru_cache(maxsize=None)
def formula(n, kind, rank, target, x, y):
    """Truth of recursively defined three-variable threshold formula."""
    if not arc(n, x, y):
        return False
    if rank == 0:
        assert target == 0
        return True
    lower = (1 << (rank - 1)) - 1
    if target <= lower:
        return formula(n, kind, rank - 1, target, x, y)
    left = min(lower, target - 1)
    right = target - 1 - left
    assert 0 <= right <= lower
    for z in range(n):
        if kind == 'A':
            if (arc(n, x, z) and arc(n, z, y) and
                formula(n, 'A', rank - 1, left, x, z) and
                formula(n, 'A', rank - 1, right, z, y)):
                return True
        else:
            if (arc(n, x, z) and arc(n, y, z) and
                formula(n, 'A', rank - 1, left, y, z) and
                formula(n, 'B', rank - 1, right, x, z)):
                return True
    return False


def verify_formulas():
    checks = 0
    for n in range(3, 50, 2):
        m = n // 2
        for d in range(1, m + 1):
            for rank in range(5):
                for target in range(1 << rank):
                    assert formula(n, 'A', rank, target, 0, d) == (d - 1 >= target)
                    assert formula(n, 'B', rank, target, 0, d) == (m - d >= target)
                    checks += 2
    return checks


def verify_logical_types():
    """Independent exact FO^3 rank-type refinement, not using the proof."""
    orders = list(range(3, 40, 2))
    atom = {}
    structures = {}
    for n in orders:
        states = list(product(range(-1, n), repeat=3))
        index = {p: i for i, p in enumerate(states)}
        color = []
        for p in states:
            a = []
            for i, j in ((0, 1), (0, 2), (1, 2)):
                x, y = p[i], p[j]
                if x < 0 or y < 0:
                    a.append(0)
                elif x == y:
                    a.append(1)
                elif arc(n, x, y):
                    a.append(2)
                else:
                    a.append(3)
            key = tuple(x >= 0 for x in p) + tuple(a)
            color.append(atom.setdefault(key, len(atom)))
        substitutions = [
            [[index[p[:j] + (v,) + p[j + 1:]] for v in range(n)]
             for j in range(3)] for p in states
        ]
        structures[n] = [color, substitutions, index[(-1, -1, -1)]]
    outputs = []
    for rank in range(6):
        groups = {}
        for n, (colors, _, empty) in structures.items():
            groups.setdefault(colors[empty], []).append(n)
        observed = list(groups.values())
        threshold = max(3, (1 << rank) - 1)
        expected = [[n] for n in orders if n < threshold]
        expected.append([n for n in orders if n >= threshold])
        assert observed == expected, (rank, observed, expected)
        outputs.append((rank, threshold, len(observed)))
        if rank == 5:
            break
        next_colors = {}
        for n, (colors, repl, empty) in structures.items():
            revised = []
            for i, moves in enumerate(repl):
                key = ((colors[i],) +
                       tuple(frozenset(colors[j] for j in choices)
                             for choices in moves))
                revised.append(next_colors.setdefault(key, len(next_colors)))
            structures[n][0] = revised
    return outputs


def main():
    count = verify_formulas()
    print('FORMULA_THRESHOLD_CHECKS', count, 'PASS')
    rows = verify_logical_types()
    print('INDEPENDENT_FO3_REFINEMENT', 'PASS')
    for rank, threshold, group_count in rows:
        print('rank', rank, 'stabilization', threshold, 'classes_sample', group_count)
    print('SAMPLE_ORDERS', 'odd integers 3 through 39')
    print('NO_INFINITE_CLAIM_FROM_FINITE_ENUMERATION')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
