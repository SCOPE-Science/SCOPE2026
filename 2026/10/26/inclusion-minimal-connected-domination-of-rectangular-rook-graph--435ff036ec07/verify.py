#!/usr/bin/env python3
"""Check the minimal connected-domination census for small rook graphs.

The graph-theoretic enumeration is independent of the Stirling polynomial.
Run with: python3 verify.py
"""
from collections import Counter
from math import comb, factorial


def stirling(n, k):
    if not 0 <= k <= n:
        return 0
    row = [1]
    for size in range(1, n + 1):
        nxt = [0] * (size + 1)
        for blocks in range(1, size + 1):
            nxt[blocks] = blocks * (row[blocks] if blocks < len(row) else 0) + row[blocks - 1]
        row = nxt
    return row[k]


def prediction(p, q):
    result = Counter()
    bound = min(p - 1, q - 1)
    for c in range(1, bound + 1):
        result[p + c - 1] += comb(q, c) * p ** (c - 1) * factorial(c) * stirling(p - 1, c)
    for r in range(1, bound + 1):
        result[q + r - 1] += comb(p, r) * q ** (r - 1) * factorial(r) * stirling(q - 1, r)
    return result


def actual(p, q):
    n = p * q
    cells = [(i, j) for i in range(p) for j in range(q)]
    adj = [0] * n
    for a, (row, col) in enumerate(cells):
        adj[a] = sum(1 << b for b, (r, c) in enumerate(cells) if b != a and (r == row or c == col))
    closed = [adj[a] | (1 << a) for a in range(n)]
    full = (1 << n) - 1

    def connected(mask):
        if not mask:
            return False
        start = mask & -mask
        reached = start
        fringe = start
        while fringe:
            bit = fringe & -fringe
            fringe -= bit
            vertex = bit.bit_length() - 1
            expansion = adj[vertex] & mask & ~reached
            reached |= expansion
            fringe |= expansion
        return reached == mask

    def cd(mask):
        if not connected(mask):
            return False
        dominated = 0
        selection = mask
        while selection:
            bit = selection & -selection
            selection -= bit
            dominated |= closed[bit.bit_length() - 1]
        return dominated == full

    def structural(mask):
        # Count occupied rows, columns, and degrees of every incidence vertex.
        occupied_rows, occupied_cols = set(), set()
        row_degrees = [0] * p
        col_degrees = [0] * q
        for index, (row, col) in enumerate(cells):
            if mask & (1 << index):
                occupied_rows.add(row)
                occupied_cols.add(col)
                row_degrees[row] += 1
                col_degrees[col] += 1
        size = mask.bit_count()
        row_type = (len(occupied_rows) == p and len(occupied_cols) < q
                    and size == p + len(occupied_cols) - 1
                    and all(col_degrees[col] >= 2 for col in occupied_cols))
        col_type = (len(occupied_cols) == q and len(occupied_rows) < p
                    and size == q + len(occupied_rows) - 1
                    and all(row_degrees[row] >= 2 for row in occupied_rows))
        # Connected is separately certified in cd(mask).
        return row_type != col_type

    counts = Counter()
    n_checked = 0
    for mask in range(1, 1 << n):
        if not cd(mask):
            continue
        deleting = mask
        is_minimal = True
        while deleting:
            bit = deleting & -deleting
            deleting -= bit
            if cd(mask ^ bit):
                is_minimal = False
                break
        if is_minimal:
            n_checked += 1
            assert structural(mask), (p, q, mask, "characterization mismatch")
            counts[mask.bit_count()] += 1
    return counts, n_checked


def main():
    boards = ((2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4))
    total = 0
    for p, q in boards:
        obtained, count = actual(p, q)
        expected = prediction(p, q)
        assert obtained == expected, (p, q, obtained, expected)
        assert count == sum(expected.values())
        total += count
        print(f"R({p},{q}): {dict(sorted(obtained.items()))} PASS")
    print(f"PASS: {len(boards)} complete labeled graphs; {total} minimal sets checked")


if __name__ == "__main__":
    main()
