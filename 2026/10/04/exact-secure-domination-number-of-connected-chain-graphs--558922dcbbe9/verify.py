#!/usr/bin/env python3
"""Exhaustive finite checks for the secure-domination formula on chain graphs."""
from itertools import combinations


def compositions(n, k):
    if k == 1:
        yield (n,)
        return
    for cuts in combinations(range(1, n), k - 1):
        points = (0,) + cuts + (n,)
        yield tuple(points[i + 1] - points[i] for i in range(k))


def build_chain(a_blocks, b_blocks):
    p = len(a_blocks)
    assert p == len(b_blocks) and p >= 1
    a_ranges = []
    b_ranges = []
    s = 0
    for z in a_blocks:
        a_ranges.append((s, s + z))
        s += z
    a_order = s
    for z in b_blocks:
        b_ranges.append((s, s + z))
        s += z
    n = s
    adj = [0] * n
    for i, (lo, hi) in enumerate(a_ranges):
        for u in range(lo, hi):
            for j in range(i + 1):
                blo, bhi = b_ranges[j]
                for v in range(blo, bhi):
                    adj[u] |= 1 << v
                    adj[v] |= 1 << u
    return adj, a_order, n - a_order


def is_dominating(adj, chosen):
    covered = chosen
    work = chosen
    while work:
        bit = work & -work
        u = bit.bit_length() - 1
        covered |= adj[u]
        work -= bit
    return covered == (1 << len(adj)) - 1


def is_secure(adj, chosen):
    global SUBSET_SECURITY_CHECKS, SWAP_CHECKS
    SUBSET_SECURITY_CHECKS += 1
    if not is_dominating(adj, chosen):
        return False
    outside = ((1 << len(adj)) - 1) ^ chosen
    while outside:
        bit = outside & -outside
        u = bit.bit_length() - 1
        outside -= bit
        defenders = adj[u] & chosen
        defended = False
        while defenders:
            dbit = defenders & -defenders
            defenders -= dbit
            SWAP_CHECKS += 1
            if is_dominating(adj, (chosen ^ dbit) | bit):
                defended = True
                break
        if not defended:
            return False
    return True


def brute_gamma(adj):
    n = len(adj)
    for k in range(1, n + 1):
        for comb in combinations(range(n), k):
            chosen = 0
            for u in comb:
                chosen |= 1 << u
            if is_secure(adj, chosen):
                return k
    raise AssertionError("no secure dominating set found")


def leaf_excess(a_blocks, b_blocks):
    # In the canonical chain blocks, A_1 is a leaf class exactly when |B_1|=1,
    # and B_p is a leaf class exactly when |A_p|=1.
    e_a = max(a_blocks[0] - 1, 0) if b_blocks[0] == 1 else 0
    e_b = max(b_blocks[-1] - 1, 0) if a_blocks[-1] == 1 else 0
    return e_a, e_b


def predicted_gamma(a_blocks, b_blocks):
    a = sum(a_blocks)
    b = sum(b_blocks)
    e_a, e_b = leaf_excess(a_blocks, b_blocks)
    return e_a + e_b + min(4, a - e_a, b - e_b)


def trim_profile(a_blocks, b_blocks):
    aa = list(a_blocks)
    bb = list(b_blocks)
    e_a, e_b = leaf_excess(a_blocks, b_blocks)
    if e_a:
        aa[0] = 1
    if e_b:
        bb[-1] = 1
    return tuple(aa), tuple(bb), e_a + e_b


SUBSET_SECURITY_CHECKS = 0
SWAP_CHECKS = 0
profiles = 0
twin_reduction_checks = 0
h3_check = False

for order in range(2, 11):
    for a_size in range(1, order):
        b_size = order - a_size
        for p in range(1, min(a_size, b_size) + 1):
            for a_blocks in compositions(a_size, p):
                for b_blocks in compositions(b_size, p):
                    adj, a, b = build_chain(a_blocks, b_blocks)
                    actual = brute_gamma(adj)
                    expected = predicted_gamma(a_blocks, b_blocks)
                    assert actual == expected, (a_blocks, b_blocks, actual, expected)

                    ta, tb, excess = trim_profile(a_blocks, b_blocks)
                    tadj, _, _ = build_chain(ta, tb)
                    trimmed = brute_gamma(tadj)
                    assert actual == excess + trimmed, (a_blocks, b_blocks, actual, excess, trimmed)
                    twin_reduction_checks += 1
                    profiles += 1

                    if a_blocks == (1, 1, 1) and b_blocks == (1, 1, 1):
                        assert actual == 3
                        # The whole A side is an explicit size-three secure dominating set.
                        whole_a = (1 << 3) - 1
                        assert is_secure(adj, whole_a)
                        h3_check = True

assert profiles == 511
assert h3_check
print(
    "VERIFY_OK "
    f"profiles={profiles} "
    f"twin_reduction_checks={twin_reduction_checks} "
    f"secure_subset_checks={SUBSET_SECURITY_CHECKS} "
    f"swap_checks={SWAP_CHECKS} "
    "max_order=10 h3_gamma=3"
)
