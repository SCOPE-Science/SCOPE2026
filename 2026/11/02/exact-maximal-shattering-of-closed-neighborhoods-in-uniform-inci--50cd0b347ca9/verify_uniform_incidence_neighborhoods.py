"""Exact finite checks for closed-neighborhood shattering in uniform-incidence graphs.

Run with Python >= 3.9; the standard library is the only dependency.
All finite checks are supplementary to the accompanying all-parameter proof.
"""
from functools import lru_cache
from itertools import combinations
from math import comb


def graph(n, k):
    blocks = tuple(combinations(range(n), k))
    masks = []
    for p in range(n):
        mask = 1 << p
        for j, block in enumerate(blocks):
            if p in block:
                mask |= 1 << (n + j)
        masks.append(mask)
    for j, block in enumerate(blocks):
        mask = 1 << (n + j)
        for p in block:
            mask |= 1 << p
        masks.append(mask)
    return blocks, tuple(masks)


def shattered(support, masks):
    observed = set()
    goal = 1 << len(support)
    for hypothesis in masks:
        pattern = sum((1 << t) for t, x in enumerate(support) if hypothesis & (1 << x))
        observed.add(pattern)
        if len(observed) == goal:
            return True
    return False


def predicted_vc(n, k):
    return min(k, n - k + 2)


def predicted_max_count(n, k):
    d = predicted_vc(n, k)
    if d == 2:
        return 3 * comb(n, 2) + n * comb(n - 1, 2)
    if d == 3 and k == 3:
        return 4 * comb(n, 3) + 2 * comb(n, 2) * comb(n - 2, 2) + 4 * comb(n, 4)
    if d == 3 and k == n - 1:
        return 8 * comb(n, 3)
    return comb(n, d)


def triple_criterion(n, k, support, blocks):
    points = [x for x in support if x < n]
    selected = [blocks[x - n] for x in support if x >= n]
    a = len(points)
    if k == 2:
        return False
    if a == 3:
        return True
    if a == 2:
        return set(points) <= set(selected[0])
    if a == 1:
        common = set(selected[0]) & set(selected[1])
        return points[0] in common and len(common) >= 2
    U, V, W = map(set, selected)
    return bool(U & V & W and (U & V) - W and (U & W) - V and (V & W) - U)


def online_dimension(masks):
    size = len(masks)
    all_hypotheses = (1 << size) - 1
    @lru_cache(None)
    def depth(version_space):
        count = version_space.bit_count()
        if count < 2:
            return 0
        choices = []
        for query_mask in masks:
            yes = version_space & query_mask
            no = version_space & ~query_mask
            if yes and no:
                choices.append((min(yes.bit_count(), no.bit_count()), yes, no))
        choices.sort(reverse=True)
        best = 0
        for small, yes, no in choices:
            if small.bit_length() <= best:
                continue
            best = max(best, 1 + min(depth(yes), depth(no)))
            if (1 << (best + 1)) > count:
                break
        return best
    return depth(all_hypotheses)


def main():
    total_checked = 0
    triple_checked = 0
    for n in range(3, 8):
        for k in range(2, n):
            blocks, masks = graph(n, k)
            N, d = len(masks), predicted_vc(n, k)
            got = 0
            for support in combinations(range(N), d):
                if shattered(support, masks):
                    got += 1
            assert got == predicted_max_count(n, k), (n, k, got)
            total_checked += comb(N, d)
            if n <= 6:
                assert not any(shattered(S, masks) for S in combinations(range(N), d + 1))
            for support in combinations(range(N), 3):
                actual = shattered(support, masks)
                predicted = triple_criterion(n, k, support, blocks)
                assert actual == predicted, (n, k, support, actual, predicted)
                triple_checked += 1
            if k == 2:
                expected = 2 if n == 3 else 3
                assert online_dimension(masks) == expected
            print(f'RANK_CHECK_PASS n={n} k={k} vc={d} maximum_supports={got}')
    for n, k in ((8, 3), (8, 6), (9, 2), (9, 8)):
        _, masks = graph(n, k)
        d = predicted_vc(n, k)
        got = sum(shattered(S, masks) for S in combinations(range(len(masks)), d))
        assert got == predicted_max_count(n, k), (n, k, got)
        total_checked += comb(len(masks), d)
        print(f'EXTRA_BOUNDARY_PASS n={n} k={k} maximum_supports={got}')
    for n in (3, 4, 5, 6, 7, 8):
        _, masks = graph(n, 2)
        expected = 2 if n == 3 else 3
        assert online_dimension(masks) == expected
    print(f'EXACT_SUPPORT_AND_TRIPLE_CENSUS_PASS supports={total_checked} triple_tests={triple_checked}')
    print('RANK_TWO_ONLINE_RECURRENCE_PASS n=3..8')
    print('ALL_UNIFORM_INCIDENCE_NEIGHBORHOOD_CHECKS_PASS')


if __name__ == '__main__':
    main()
