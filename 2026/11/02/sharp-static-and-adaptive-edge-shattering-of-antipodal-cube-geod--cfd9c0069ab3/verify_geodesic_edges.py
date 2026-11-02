#!/usr/bin/env python3
"""Recompute edge-incidence shattering for antipodal Boolean-cube geodesics.

Uses independently built permutation and subset-state recursions. The checks
are finite sanity tests; the arbitrary-dimensional theorem has a proof.
"""
from itertools import permutations


def base_trace(perm):
    used = 0
    mask = 0
    for i, coord in enumerate(perm):
        if used == (1 << i) - 1 and coord == i:
            mask |= 1 << i
        used |= 1 << coord
    return mask


def traces_from_permutations(d):
    return {base_trace(p) for p in permutations(range(d))}


def traces_from_prefix_states(d):
    # Dynamic enumeration of (used coordinate subset, selected canonical edges).
    states = {0: {0}}
    for step in range(d):
        nxt = {}
        for used, traces in states.items():
            for coord in range(d):
                if used & (1 << coord):
                    continue
                new_used = used | (1 << coord)
                add = (1 << step) if used == (1 << step) - 1 and coord == step else 0
                target = nxt.setdefault(new_used, set())
                target.update(t | add for t in traces)
        states = nxt
    return states[(1 << d) - 1]


def pattern_criterion(support, d):
    if d == 1:
        return support == 0
    if (support & 3) == 3 or ((support >> (d - 2)) & 3) == 3:
        return False
    return all(((support >> k) & 7) != 7 for k in range(d - 2))


def check_supports(d, traces):
    by_degree = {}
    for support in range(1 << d):
        observations = {t & support for t in traces}
        shattered = len(observations) == (1 << support.bit_count())
        expected = pattern_criterion(support, d)
        assert shattered == expected, (d, support, shattered, expected)
        if shattered:
            by_degree[support.bit_count()] = by_degree.get(support.bit_count(), 0) + 1
    vc = max(by_degree)
    assert vc == (2 * d) // 3, (d, vc)
    return by_degree


def edge_on_perm(prefix_mask, coord, perm):
    used = 0
    for x in perm:
        if used == prefix_mask and x == coord:
            return True
        used |= 1 << x
    return False


def adaptive_tree(d):
    # At each node two fixed-next-letter subfamilies ensure both children
    # retain the full remaining permutation class; no recursion on a guessed rank.
    leaves = []
    def rec(prefix, remaining, requirements):
        if len(remaining) == 1:
            perm = tuple(prefix + [remaining[0]])
            for mask, c, value in requirements:
                assert edge_on_perm(mask, c, perm) is value
            leaves.append(perm)
            return
        a, b = remaining[:2]
        used = sum(1 << x for x in prefix)
        rec(prefix + [a], [x for x in remaining if x != a],
            requirements + [(used, a, True)])
        rec(prefix + [b], [x for x in remaining if x != b],
            requirements + [(used, a, False)])
    if d == 1:
        leaves.append((0,))
    else:
        rec([], list(range(d)), [])
    assert len(leaves) == (1 << (d - 1))
    assert len(set(leaves)) == len(leaves)
    return len(leaves)


def main():
    for d in range(1, 10):
        direct = traces_from_permutations(d)
        dp = traces_from_prefix_states(d)
        assert direct == dp, d
        stats = check_supports(d, direct)
        print(f'DIRECT_AND_DP_TRACES_PASS d={d} trace_patterns={len(dp)} VC={max(stats)} spectrum={stats}')
    for d in range(10, 13):
        dp = traces_from_prefix_states(d)
        stats = check_supports(d, dp)
        print(f'INDEPENDENT_DP_AND_CRITERION_PASS d={d} trace_patterns={len(dp)} VC={max(stats)}')
    for d in range(1, 12):
        leaves = adaptive_tree(d)
        print(f'CONSTRUCTIVE_ADAPTIVE_TREE_PASS d={d} depth={d - 1} leaves={leaves}')
    print('ALL_ANTIPODAL_GEODESIC_EDGE_SHATTERING_CHECKS_PASS')


if __name__ == '__main__':
    main()
