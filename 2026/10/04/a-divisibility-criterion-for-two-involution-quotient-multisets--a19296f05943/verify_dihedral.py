#!/usr/bin/env python3
"""Finite stress-test for the two-involution quotient-realizability theorem.

This is not the general proof.  It exhaustively checks the base dihedral case
for n=3,...,10 by enumerating every {s,t}-labeling of the 2n vertices and
checking whether x -> label(x)x is a permutation.  It also checks the block
arithmetic used for ambient index m.
"""
from collections import Counter


def mul(n, a, b):
    """Multiply r^i f^e * r^j f^d in D_{2n}, with f r f = r^{-1}."""
    i, e = a
    j, d = b
    return ((i + (j if e == 0 else -j)) % n, (e + d) & 1)


def idx(n, a):
    i, e = a
    return e * n + i


def elt(n, k):
    return (k % n, k // n)


def base_census(n):
    N = 2 * n
    s = (0, 1)
    t = ((n - 1) % n, 1)  # then s*t = r
    one = (0, 0)
    assert mul(n, s, s) == one
    assert mul(n, t, t) == one

    st = mul(n, s, t)
    x = one
    order = None
    for k in range(1, n + 1):
        x = mul(n, x, st)
        if x == one:
            order = k
            break
    assert order == n

    im_s = []
    im_t = []
    for k in range(N):
        x = elt(n, k)
        im_s.append(idx(n, mul(n, s, x)))
        im_t.append(idx(n, mul(n, t, x)))

    counts = Counter()
    for mask in range(1 << N):
        seen = 0
        ok = True
        q = mask.bit_count()  # bit 1 means label s, bit 0 means label t
        for k in range(N):
            y = im_s[k] if ((mask >> k) & 1) else im_t[k]
            bit = 1 << y
            if seen & bit:
                ok = False
                break
            seen |= bit
        if ok:
            assert seen == (1 << N) - 1
            counts[q] += 1
    return counts


def ambient_arithmetic_check(n, m):
    # A block contributes 0, n, or 2n copies of s.  Check that all and only
    # multiples of n between 0 and 2nm are obtainable from m blocks.
    reachable = {0}
    for _ in range(m):
        reachable = {a + b for a in reachable for b in (0, n, 2 * n)}
    expected = set(range(0, 2 * n * m + 1, n))
    assert reachable == expected


for n in range(3, 11):
    counts = base_census(n)
    qs = sorted(counts)
    assert qs == [0, n, 2 * n], (n, counts)
    print(f"n={n}: q-values={qs}, realizing_labelings={dict(sorted(counts.items()))}")
    for m in range(1, 7):
        ambient_arithmetic_check(n, m)

print("VERIFY_OK")
