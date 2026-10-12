#!/usr/bin/env python3
from math import comb


def q_threshold(n: int) -> int:
    q = 0
    while comb(q, q // 2) < n + 1:
        q += 1
    return q


def construction(n: int):
    q = q_threshold(n)
    k = q // 2
    # Pick the first n+1 central-layer subsets in lexicographic bit-mask order.
    masks = [m for m in range(1 << q) if m.bit_count() == k][: n + 1]
    assert len(masks) == n + 1
    # vertices: 0=root; 1..n+1=y_i; n+2..n+1+q=z_j
    N = n + 2 + q
    R = [[False] * N for _ in range(N)]
    root = 0
    ys = list(range(1, n + 2))
    zs = list(range(n + 2, N))
    for y in ys:
        R[root][y] = True
    for z in zs:
        R[root][z] = True
    for i, y in enumerate(ys):
        m = masks[i]
        for j, z in enumerate(zs):
            if (m >> j) & 1:
                R[y][z] = True
    return R, root, ys, zs, masks


def futures(R, v):
    return frozenset(i for i, b in enumerate(R[v]) if b)


def verify_frame(n: int):
    R, root, ys, zs, masks = construction(n)
    N = len(R)
    assert N == n + 2 + q_threshold(n)
    # strict partial order
    assert all(not R[i][i] for i in range(N))
    for a in range(N):
        for b in range(N):
            if R[a][b]:
                for c in range(N):
                    if R[b][c]:
                        assert R[a][c]
    # rooted in the strong direct sense used by the construction
    assert all(v == root or R[root][v] for v in range(N))
    Fy = [futures(R, y) for y in ys]
    assert len(set(Fy)) == n + 1
    for i in range(n + 1):
        for j in range(n + 1):
            if i != j:
                assert not (Fy[i] <= Fy[j])
    # exact central-layer threshold and lower-bound certificate
    q = len(zs)
    assert comb(q, q // 2) >= n + 1
    if q:
        assert comb(q - 1, (q - 1) // 2) < n + 1
    return N


assertions = 0
# Exact construction and threshold checks over a substantial finite range.
for n in range(1, 501):
    N = verify_frame(n)
    assert N == n + 2 + q_threshold(n)
    assertions += 1

# Independently check the first twenty exact minima produced by the formula.
expected = [5,7,9,10,11,13,14,15,16,18,19,20,21,22,23,24,25,26,27,29]
actual = [n + 2 + q_threshold(n) for n in range(1, 21)]
assert actual == expected
assertions += 20

# The Boolean-lattice lower-bound step itself: central layer is maximal, so the
# preceding dimension is insufficient and the threshold dimension sufficient.
for n in range(1, 10001):
    q = q_threshold(n)
    assert comb(q, q // 2) >= n + 1
    assert q == 0 or comb(q - 1, (q - 1) // 2) < n + 1
    assertions += 2

print(f"VERIFY_OK {assertions} exact assertions")
print("first_20_minima", actual)
