"""Independent finite tests of the modal-Kleene cube normal form.

No external dependencies. Run: python checker.py
Exhaustively enumerates all scalar truth tables for n=1,2; the proof
for arbitrary n is mathematical and is not delegated to this program.
"""
from itertools import product

T = (-1, 0, 1)


def component_le(x, y):
    return all(a <= b for a, b in zip(x, y))


def tables_from_thresholds(n, points):
    negzero = list(product((-1, 0), repeat=n))
    signs = list(product((-1, 1), repeat=n))
    result = set()
    for lower in negzero:
        # The plus-one filter is empty, so the output is at most zero.
        result.add(tuple(0 if component_le(lower, x) else -1
                         for x in points))
        for upper in signs:
            if not component_le(lower, upper):
                continue
            result.add(tuple(1 if component_le(upper, x) else
                             (0 if component_le(lower, x) else -1)
                             for x in points))
    return result


def brute_scalar(n):
    points = list(product(T, repeat=n))
    index = {p: i for i, p in enumerate(points)}
    size = len(points)
    meet = [[index[tuple(min(a, b) for a, b in zip(x, y))]
             for y in points] for x in points]
    join = [[index[tuple(max(a, b) for a, b in zip(x, y))]
             for y in points] for x in points]
    neg = [index[tuple(-a for a in x)] for x in points]
    low = [meet[z][neg[z]] for z in range(size)]
    high = [join[z][neg[z]] for z in range(size)]
    accepted = set()
    for f in product(T, repeat=size):
        if any(f[meet[x][y]] != min(f[x], f[y])
               for x in range(size) for y in range(size)):
            continue
        if any(f[high[z]] < 0 for z in range(size)):
            continue
        if any(f[join[x][low[z]]] > max(f[x], -f[join[x][low[z]]])
               for x in range(size) for z in range(size)):
            continue
        accepted.add(f)
    constructed = tables_from_thresholds(n, points)
    assert accepted == constructed, (n, len(accepted), len(constructed))
    normal = sum(f[index[(1,) * n]] == 1 for f in accepted)
    assert len(accepted) == 3**n + 2**n
    assert normal == 3**n
    print('n=%d scalar=%d normal_scalar=%d full_operators=%d normal_full=%d'
          % (n, len(accepted), normal, len(accepted)**n, normal**n))


if __name__ == '__main__':
    brute_scalar(1)
    brute_scalar(2)
    print('All exhaustive scalar tables agree with the threshold forms.')
