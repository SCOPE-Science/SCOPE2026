#!/usr/bin/env python3
"""Independent finite checks for cograph subsets of path powers.

Uses direct four-vertex adjacency testing and a separate finite-state
recurrence.  No finite check is used as the proof for arbitrary n and k.
"""
from itertools import combinations


def expected(n, k):
    q, r = divmod(n, 2*k + 2)
    return q*(k+2) + min(r, k+2)


def unique_expected(n, k):
    return n <= k+2 or n % (2*k+2) == k+2


def is_p4(indices, k):
    deg = [0] * 4
    edge_count = 0
    for i in range(4):
        for j in range(i+1, 4):
            if abs(indices[i] - indices[j]) <= k:
                deg[i] += 1
                deg[j] += 1
                edge_count += 1
    return edge_count == 3 and sorted(deg) == [1, 1, 2, 2]


def brute(n, k):
    forbidden = []
    for verts in combinations(range(n), 4):
        if is_p4(verts, k):
            forbidden.append(sum(1 << v for v in verts))
    best, count = -1, 0
    for mask in range(1 << n):
        ones = mask.bit_count()
        if ones < best:
            continue
        if any(mask & fm == fm for fm in forbidden):
            continue
        if ones > best:
            best, count = ones, 1
        else:
            count += 1
    return best, count


def window_dp(n, k):
    """Checks all subsets using an independent recent-bit recurrence."""
    w = 3*k
    bad = []
    for offsets in combinations(range(1, w+1), 3):
        if is_p4([0, *offsets], k):
            bad.append(sum(1 << (j-1) for j in offsets))
    states = {0: (0, 1)}
    mod = (1 << w) - 1
    for _ in range(n):
        nxt = {}
        for s, (score, ways) in states.items():
            for b in (0, 1):
                if b and any(s & f == f for f in bad):
                    continue
                t = ((s << 1) | b) & mod
                old = nxt.get(t)
                newscore = score + b
                if old is None or newscore > old[0]:
                    nxt[t] = (newscore, ways)
                elif newscore == old[0]:
                    nxt[t] = (newscore, old[1] + ways)
        states = nxt
    top = max(x for x, _ in states.values())
    return top, sum(c for x,c in states.values() if x == top)


def explicit_witness(n, k):
    p, b = 2*k+2, k+2
    selected = {i for i in range(n) if (i % p) < b}
    assert len(selected) == expected(n, k)
    for verts in combinations(sorted(selected), 4):
        assert not is_p4(verts, k), (n, k, verts)


def main():
    direct_cases = dp_cases = witnesses = 0
    for k in range(1, 8):
        for n in range(1, 14):
            got, count = brute(n, k)
            assert got == expected(n, k), (n,k,got)
            assert (count == 1) == unique_expected(n,k), (n,k,count)
            direct_cases += 1
    for k in range(1, 5):
        for n in range(1, 55):
            got, count = window_dp(n, k)
            assert got == expected(n, k), (n,k,got)
            assert (count == 1) == unique_expected(n,k), (n,k,count)
            dp_cases += 1
    for k in range(1, 13):
        for n in range(1, 39):
            explicit_witness(n,k)
            witnesses += 1
    print(f'VERIFY_OK direct={direct_cases} finite_state={dp_cases} witness={witnesses}')

if __name__ == '__main__':
    main()
