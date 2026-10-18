"""Finite independent checks for the sparse four-cycle concept identity.

No finite enumeration here constitutes a proof of the probabilistic limit.
Python 3.9+; standard library only.
"""
from itertools import combinations


def inspect_graph(n, mask):
    """n by n incidence graph represented by an integer bit mask."""
    row = [0] * n
    col = [0] * n
    for i in range(n):
        for j in range(n):
            if (mask >> (i * n + j)) & 1:
                row[i] |= 1 << j
                col[j] |= 1 << i
    full = (1 << n) - 1

    # Independently reconstruct all formal concepts from closure pairs.
    formal_concepts = set()
    for a in range(1 << n):
        b = full
        for i in range(n):
            if (a >> i) & 1:
                b &= row[i]
        aa = full
        for j in range(n):
            if (b >> j) & 1:
                aa &= col[j]
        if aa == a:
            formal_concepts.add((a, b))

    dl = [x.bit_count() for x in row]
    dr = [x.bit_count() for x in col]
    heavy = sum(d >= 2 for d in dl + dr)
    isolated_edges = sum(
        dl[i] == 1 and dr[j] == 1
        for i in range(n)
        for j in range(n)
        if (row[i] >> j) & 1
    )
    squares = []
    for i, k in combinations(range(n), 2):
        for j, l in combinations(range(n), 2):
            if all((row[u] >> v) & 1 for u in (i, k) for v in (j, l)):
                squares.append((i, k, j, l))

    good = dl.count(0) > 0 and dr.count(0) > 0
    if any((row[i] & row[k]).bit_count() >= 3
           for i, k in combinations(range(n), 2)):
        good = False
    if any((col[j] & col[l]).bit_count() >= 3
           for j, l in combinations(range(n), 2)):
        good = False
    if any(set(s[:2]) & set(t[:2]) or set(s[2:]) & set(t[2:])
           for s, t in combinations(squares, 2)):
        good = False

    correction = sum(
        1 - sum(d == 2 for d in (dl[i], dl[k], dr[j], dr[l]))
        for i, k, j, l in squares
    )
    predicted = 2 + heavy + isolated_edges + correction
    return len(formal_concepts), predicted, good, correction, len(squares)


def run_checks():
    counts = []
    for n in range(1, 5):
        good_count = 0
        for mask in range(1 << (n * n)):
            actual, predicted, good, _, _ = inspect_graph(n, mask)
            if good:
                good_count += 1
                assert actual == predicted, (n, mask, actual, predicted)
        counts.append(good_count)

    # A single four-cycle, from all four possible vertices with external leaves.
    # Each type has a separate isolated vertex on each shore.
    for z in range(5):
        n = 5
        mask = 0
        for i in (0, 1):
            for j in (0, 1):
                mask |= 1 << (i * n + j)
        # Add one exclusive external neighbor to precisely 4-z cycle vertices.
        for t in range(4 - z):
            if t < 2:  # cycle vertices on the object shore
                mask |= 1 << (t * n + (2 + t))
            else:  # cycle vertices on the attribute shore
                j = t - 2
                mask |= 1 << ((2 + j) * n + j)
        actual, predicted, good, correction, num = inspect_graph(n, mask)
        assert good and num == 1 and correction == 1 - z and actual == predicted

    assert counts == [1, 5, 91, 5005], counts
    print('VERIFY_OK: exhaustive n=1..4; qualifying context counts', counts)
    print('VERIFY_OK: five isolated four-cycle mark cases z=0..4')


if __name__ == '__main__':
    run_checks()
