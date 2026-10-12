#!/usr/bin/env python3
"""Finite checks of the sharp separating-size theorem for (Box Diamond)^m top.

Run with Python 3 standard library: python3 verify_rank.py
Finite testing supplements, and does not replace, the all-size proof.
"""
import random


def stages(rows):
    """B[k] = failure set of alpha_k, computed from adjacency bit masks."""
    n = len(rows)
    result = [0]
    while True:
        old = result[-1]
        new = 0
        for x in range(n):
            for y in range(n):
                if rows[x] >> y & 1 and rows[y] & ~old == 0:
                    new |= 1 << x
                    break
        if new == old:
            return result
        assert old & ~new == 0
        result.append(new)
        assert len(result) <= n + 1


def direct_truth_masks(rows, length):
    """Direct Kripke evaluation of nested box/diamond, unlike the F recurrence."""
    n = len(rows)
    mask = (1 << n) - 1
    values = [mask]
    for _ in range(length):
        old = values[-1]
        diamonds = 0
        for y in range(n):
            if rows[y] & old:
                diamonds |= 1 << y
        box_diamond = 0
        for x in range(n):
            if rows[x] & ~diamonds == 0:
                box_diamond |= 1 << x
        values.append(box_diamond)
    return values


def check(rows):
    n = len(rows)
    B = stages(rows)
    U = B[-1]
    truth = direct_truth_masks(rows, len(B)-1)
    assert all((~truth[i] & ((1 << n) - 1)) == B[i] for i in range(len(B)))
    # Rank-core lemma: a finite-rank point always has a successor of infinite rank.
    for x in range(n):
        if U >> x & 1:
            assert rows[x] & ~U, (n, rows, x, B)
    # Every exact j-th failure has j distinct finite-rank worlds and j
    # pairwise distinct infinite-rank witnesses, hence at least 2j worlds.
    for j in range(1, len(B)):
        if not (B[j] & ~B[j-1]):
            continue
        assert 2*j <= n, (n, rows, j, B)
        x = next(x for x in range(n) if (B[j] & ~B[j-1]) >> x & 1)
        seen_x = []
        seen_y = []
        for k in range(j, 0, -1):
            assert (B[k] & ~B[k-1]) >> x & 1
            seen_x.append(x)
            y = next(y for y in range(n) if rows[x] >> y & 1 and rows[y] & ~B[k-1] == 0)
            assert (U >> y) & 1 == 0
            seen_y.append(y)
            if k == 1:
                assert rows[y] == 0
            else:
                assert rows[y] & ~B[k-2]
                x = next(z for z in range(n) if rows[y] >> z & 1 and (B[k-1] & ~B[k-2]) >> z & 1)
        assert len(set(seen_x + seen_y)) == 2*j


def path(n):
    return [(1 << (x+1)) if x+1 < n else 0 for x in range(n)]


def test():
    exhaustive = 0
    for n in range(1,5):
        mask = (1 << n) - 1
        for bits in range(1 << (n*n)):
            rows = [(bits >> (i*n)) & mask for i in range(n)]
            check(rows)
            exhaustive += 1
    rng = random.Random(260615437)
    sampled = 0
    for n in range(5, 11):
        for _ in range(1500):
            p = rng.choice((0.02, .08, .2, .5, .8))
            rows = [sum((1 << j) for j in range(n) if rng.random() < p)
                    for _ in range(n)]
            check(rows)
            sampled += 1
    path_checked = 0
    for m in range(0, 51):
        rows = path(2*m+2)
        B = stages(rows)
        assert (B[m+1] & ~B[m]) & 1
        if m > 0:
            assert ((B[m+1] & ~B[m]) >> 0) & 1
        check(rows)
        path_checked += 1
    print('VERIFY_OK: exhaustive_frames=%d random_frames=%d path_sizes=%d' %
          (exhaustive, sampled, path_checked))
    print('exhaustive_by_size=2,16,512,65536; all inequalities and explicit witness chains checked')
    for m in range(1, 7):
        print('m=%d first_separating_size=%d' % (m, 2*m+2))

if __name__ == '__main__':
    test()
