"""Explicit four-word construction for a three-row rook graph.

Uses the Cartesian-product occurrence substitution of Broere--Zantema
(arXiv:1808.01800, Section 5) with base word (0,1,...,n-1)^2.
"""
from collections import Counter


def word(n):
    assert n >= 2
    base = list(range(n)) * 2
    pieces = []
    for f in (3, 2, 1):
        occurrence = [0] * n
        block = []
        for x in base:
            occurrence[x] += 1
            if f == 1:
                rows = (1,) if occurrence[x] == 1 else (3, 2, 1)
            elif occurrence[x] == 1:
                rows = (f,)
            else:
                rows = tuple(range(f - 1, 0, -1)) + tuple(range(3, f - 1, -1))
            block.extend((r, x) for r in rows)
        pieces.extend(block)
    return pieces


def check(n):
    w = word(n)
    assert len(w) == 12 * n
    counts = Counter(w)
    assert len(counts) == 3 * n
    assert set(counts.values()) == {4}
    vertices = sorted(counts)
    for i, u in enumerate(vertices):
        for v in vertices[i + 1:]:
            trace = [z for z in w if z == u or z == v]
            alternates = all(trace[t] != trace[t + 1]
                             for t in range(len(trace) - 1))
            edge = (u[0] == v[0]) or (u[1] == v[1])
            assert alternates == edge, (n, u, v, trace)
    return len(w)


if __name__ == '__main__':
    for n in range(2, 11):
        length = check(n)
        print(f'n={n}: vertices={3*n}, word_length={length}, PASS')
