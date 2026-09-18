#!/usr/bin/env python3
"""Finite checks for the identical-leakage stabilizer theorem over GF(8)/GF(2)."""

MOD = 0b1011  # x^3 + x + 1


def mul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & 0b1000:
            a ^= MOD
    return r & 7


def sq(a):
    return mul(a, a)


def power(a, e):
    r = 1
    while e:
        if e & 1:
            r = mul(r, a)
        a = mul(a, a)
        e >>= 1
    return r


def trace(a):
    # Tr_{GF(8)/GF(2)}(a) = a + a^2 + a^4.
    t = a ^ sq(a) ^ power(a, 4)
    assert t in (0, 1)
    return t


def binary_rank(rows):
    rows = [sum((bit & 1) << j for j, bit in enumerate(row)) for row in rows]
    rank = 0
    if not rows:
        return 0
    ncols = max((x.bit_length() for x in rows), default=0)
    for col in range(ncols - 1, -1, -1):
        pivot = next((i for i in range(rank, len(rows)) if (rows[i] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i] >> col) & 1):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def expand_matrix(X):
    """Column-wise GF(2)-coordinate expansion used in the cited rank criterion."""
    u = len(X)
    v = len(X[0]) if u else 0
    out = []
    for i in range(u):
        for bit in range(3):
            out.append([(X[i][j] >> bit) & 1 for j in range(v)])
    return out


def kron_gf8(G, X):
    out = []
    for grow in G:
        for xrow in X:
            row = []
            for g in grow:
                row.extend([x if g else 0 for x in xrow])
            out.append(row)
    return out


def main():
    kernel = [x for x in range(8) if trace(x) == 0]
    stabilizer = [a for a in range(8) if all(trace(mul(a, x)) == 0 for x in kernel)]
    assert stabilizer == [0, 1]

    # A coefficient outside GF(2) can create genuinely new trace information.
    alpha = 2
    pairs = {(trace(x), trace(mul(alpha, x))) for x in range(8)}
    assert pairs == {(0, 0), (0, 1), (1, 0), (1, 1)}

    # Representative checks of rank_B(G tensor X) = rank_B(G) rank_B(X)
    # for computation matrices G defined over the base field GF(2).
    X = [[1, 2, 4, 7], [3, 5, 6, 1]]
    tests = [
        [[1, 0, 1], [0, 1, 1]],
        [[1, 0, 1, 1], [0, 1, 1, 0]],
        [[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]],
    ]
    rx = binary_rank(expand_matrix(X))
    for G in tests:
        rg = binary_rank(G)
        lhs = binary_rank(expand_matrix(kron_gf8(G, X)))
        rhs = rg * rx
        assert lhs == rhs, (G, lhs, rhs)

    print("GF(8)/GF(2) trace kernel:", kernel)
    print("trace-leakage stabilizer:", stabilizer)
    print("outside-base coefficient alpha=2 yields pairs:", sorted(pairs))
    print("rank factorization tests: PASS")
    print("all checks: PASS")


if __name__ == "__main__":
    main()
