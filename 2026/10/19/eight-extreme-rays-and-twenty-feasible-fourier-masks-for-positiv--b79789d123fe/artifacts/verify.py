"""Exact incidence certificate for two-sided nonnegative Walsh functions on eight points.
Python 3 standard library only. Coordinates use binary integers 0,...,7."""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter

N = 8
H = [[1 if (x & y).bit_count() % 2 == 0 else -1 for y in range(8)] for x in range(8)]
S = (0, 3, 4, 5, 6, 7)


def solve(A, b):
    a = [[Q(v) for v in row] + [Q(vb)] for row, vb in zip(A, b)]
    for j in range(N):
        pivot = next((i for i in range(j, N) if a[i][j]), None)
        if pivot is None:
            return None
        a[j], a[pivot] = a[pivot], a[j]
        div = a[j][j]
        a[j] = [v / div for v in a[j]]
        for i in range(N):
            if i != j and a[i][j]:
                m = a[i][j]
                a[i] = [a[i][t] - m * a[j][t] for t in range(N+1)]
    return tuple(row[-1] for row in a)


def transform(v):
    return tuple(sum(Q(H[x][j]) * v[j] for j in range(8)) for x in range(8))


def spectrum(mask):
    return [i for i in range(8) if (mask >> i) & 1]


def compute():
    unit = [[int(i == j) for j in range(8)] for i in range(8)]
    equalities = [[1]*8, H[1], H[2]]
    inequalities = unit + [H[x] for x in S]
    vertices = set()
    considered = 0
    for idx in combinations(range(14), 5):
        considered += 1
        a = equalities + [inequalities[j] for j in idx]
        v = solve(a, (1, 0, 0, 0, 0, 0, 0, 0))
        if v is None:
            continue
        w = transform(v)
        if all(t >= 0 for t in v) and all(w[x] >= 0 for x in S):
            vertices.add(v)
    assert considered == 2002
    assert len(vertices) == 8
    vertex_masks = sorted(sum((1 << i) for i, t in enumerate(v) if t > 0) for v in vertices)
    assert vertex_masks == [0x09, 0x0f, 0x69, 0x81, 0x99, 0xa5, 0xc3, 0xff]

    allowed = {}
    for mask in range(1, 256):
        compatible = [v for v in vertices if all(v[i] == 0 for i in range(8) if not (mask >> i & 1))]
        if not compatible:
            continue
        # Coordinate and strict time inequalities are linear: their simultaneous
        # strict satisfaction is equivalent to positivity somewhere separately,
        # by averaging all compatible vertices.
        if any(not any(v[i] > 0 for v in compatible) for i in spectrum(mask)):
            continue
        if any(not any(transform(v)[x] > 0 for v in compatible) for x in S):
            continue
        allowed[mask] = len(spectrum(mask))
        v = tuple(sum(pt[i] for pt in compatible) / len(compatible) for i in range(8))
        w = transform(v)
        assert all(v[i] > 0 for i in spectrum(mask))
        assert all(v[i] == 0 for i in range(8) if not mask >> i & 1)
        assert w[1] == w[2] == 0
        assert all(w[x] > 0 for x in S)
    expected = {3:[0x89],4:[0x99],5:[0x8f,0xad,0xcb,0xe9],
                6:[0x9f,0xaf,0xbd,0xcf,0xdb,0xeb,0xed,0xf9],
                7:[0xbf,0xdf,0xef,0xfb,0xfd],8:[0xff]}
    grouped = {k: sorted(m for m,v in allowed.items() if v == k) for k in expected}
    assert grouped == expected, (grouped, expected)
    assert len(allowed) == 20
    return grouped

if __name__ == '__main__':
    groups=compute()
    print('Feasible Fourier-support sizes and masks:')
    for k,masks in groups.items():
        print(k, ' '.join(f'{m:02x}' for m in masks))
    print('VERIFY_OK')
