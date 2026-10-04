#!/usr/bin/env python3
from collections import defaultdict


def elems(k, deleted):
    full = (1 << k) - 1
    return [x for x in range(1, full) if x != deleted]


def leq(x, y):
    return (x & y) == x


def strict_upper(x, E):
    return [y for y in E if x != y and leq(x, y)]


def strict_lower(x, E):
    return [y for y in E if x != y and leq(y, x)]


def has_minimum(S):
    return any(all(leq(x, y) for y in S) for x in S)


def has_maximum(S):
    return any(all(leq(y, x) for y in S) for x in S)


def beat_points(E):
    up = []
    down = []
    for x in E:
        U = strict_upper(x, E)
        L = strict_lower(x, E)
        if U and has_minimum(U):
            up.append(x)
        if L and has_maximum(L):
            down.append(x)
    return up, down


def monotone(E, f):
    for x in E:
        for y in E:
            if leq(x, y) and not leq(f[x], f[y]):
                return False
    return True


def chain_stats(E):
    E = sorted(E, key=lambda x: (x.bit_count(), x))
    dp = {}
    totals = defaultdict(int)
    for x in E:
        d = defaultdict(int)
        d[1] = 1
        for y in E:
            if y == x:
                continue
            if y.bit_count() >= x.bit_count():
                break
            if leq(y, x):
                for ell, c in dp[y].items():
                    d[ell + 1] += c
        dp[x] = d
        for ell, c in d.items():
            totals[ell] += c
    euler = sum((1 if ell % 2 else -1) * c for ell, c in totals.items())
    max_len = max(totals)
    return euler, max_len


def check_extreme(k, A, E, rank):
    full = (1 << k) - 1
    if rank == 1:
        a = A
        f = {x: (x & ~a) if (x & a) else x for x in E}
        assert all(v in E for v in f.values())
        assert monotone(E, f)
        assert all(f[f[x]] == f[x] for x in E)
        assert all(leq(f[x], x) for x in E)
        image = set(f.values())
        maximum = full & ~a
        assert maximum in image and all(leq(x, maximum) for x in image)
        assert all(f[x] == x for x in image)
    elif rank == k - 1:
        a = full ^ A
        f = {x: (x | a) if not (x & a) else x for x in E}
        assert all(v in E for v in f.values())
        assert monotone(E, f)
        assert all(f[f[x]] == f[x] for x in E)
        assert all(leq(x, f[x]) for x in E)
        image = set(f.values())
        minimum = a
        assert minimum in image and all(leq(minimum, x) for x in image)
        assert all(f[x] == x for x in image)


def main():
    summaries = []
    for k in range(4, 9):
        for rank in range(1, k):
            A = (1 << rank) - 1
            E = elems(k, A)
            assert len(E) == (1 << k) - 3
            up, down = beat_points(E)
            if rank in (1, k - 1):
                check_extreme(k, A, E, rank)
            else:
                assert up == [] and down == []
            euler, max_len = chain_stats(E)
            assert euler == 1
            assert max_len == k - 1
            summaries.append((k, rank, len(E), len(up), len(down), euler, max_len))
    print('VERIFY_OK cases=%d range=k4..8 point_formula=2^k-3 internal_no_beats=yes extreme_retractions=yes euler=1 max_chain=k-1' % len(summaries))


if __name__ == '__main__':
    main()
