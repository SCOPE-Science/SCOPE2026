#!/usr/bin/env python3
"""Finite cross-checks for connected EF1 with common additive star valuations.

No third-party dependencies. The general theorem is proved analytically in RESULT.md;
these exhaustive and direct checks are supplementary.
"""
from itertools import combinations, combinations_with_replacement


def exact_criterion(center, leaves, agents):
    """Closed-form theorem for a star with len(leaves) leaves."""
    m = len(leaves)
    assert 1 <= agents <= m + 1
    r = m - agents + 1
    if agents == 1 or r <= 1:
        return True
    ordered = sorted(leaves)
    return ordered[r] >= center + sum(ordered[:r - 1])


def direct_search(center, leaves, agents):
    """Search all star-connected partitions; evaluate pairwise EF1 directly.

    The central bundle is forced, every other bundle is a singleton leaf.
    Thus choices of its r leaves enumerate all connected partitions up to
    renaming agents. The test below uses no closed-form inequality.
    """
    m = len(leaves)
    assert 1 <= agents <= m + 1
    if agents == 1:
        return True

    def worth(bundle):
        return sum(center if v == m else leaves[v] for v in bundle)

    def is_connected(bundle):
        return len(bundle) <= 1 or m in bundle

    for central_leaves in combinations(range(m), m - agents + 1):
        central = frozenset((m, *central_leaves))
        others = [frozenset((j,)) for j in range(m) if j not in central]
        bundles = [central] + others
        assert len(bundles) == agents
        valid = True
        for recipient in bundles:
            for envied in bundles:
                if recipient == envied:
                    continue
                if worth(recipient) >= worth(envied):
                    continue
                if not any(
                    is_connected(envied - {v})
                    and worth(recipient) >= worth(envied - {v})
                    for v in envied
                ):
                    valid = False
                    break
            if not valid:
                break
        if valid:
            return True
    return False


def realize(bits):
    """Construct pairwise-distinct positive integer weights for bits r=2,...,m-1.

    bits[r-2] is True exactly when an allocation with r leaves in the hub
    bundle should exist. Strict feasibility or infeasibility margin is 1.
    """
    center = 6
    leaves = [4, 5]
    for bit in bits:
        r = len(leaves)
        threshold = center + sum(leaves[:r-1])
        leaves.append(threshold + (1 if bit else -1))
    assert leaves == sorted(set(leaves))
    assert len(set(leaves + [center])) == len(leaves) + 1
    for r, bit in enumerate(bits, start=2):
        margin = leaves[r] - center - sum(leaves[:r-1])
        assert margin == (1 if bit else -1)
    return center, leaves


def main():
    checked = 0
    for m in range(3, 9):
        for center in range(5):
            for leaves in combinations_with_replacement(range(5), m):
                for agents in range(1, m + 2):
                    assert direct_search(center, leaves, agents) == exact_criterion(center, leaves, agents), (center, leaves, agents)
                    checked += 1
    print('Direct-search versus criterion finite tests:', checked)

    patterns = 0
    for m in range(3, 12):
        for mask in range(1 << (m - 2)):
            bits = tuple(bool(mask & (1 << i)) for i in range(m - 2))
            center, leaves = realize(bits)
            for r, expected in enumerate(bits, start=2):
                agents = m - r + 1
                assert exact_criterion(center, leaves, agents) == expected
                if m <= 7:
                    assert direct_search(center, leaves, agents) == expected
            assert all(exact_criterion(center, leaves, a) for a in (1, m, m + 1))
            patterns += 1
    print('Distinct realization patterns checked:', patterns)

    center, leaves = 6, [4, 5, 9, 16, 23]
    assert [direct_search(center, leaves, k) for k in range(1, 7)] == [True, False, True, False, True, True]
    print('Six-vertex witness: center=6, leaf weights=[4,5,9,16,23]')
    print('Feasibility for 1,...,6 agents: yes,no,yes,no,yes,yes')
    print('All finite checks passed.')


if __name__ == '__main__':
    main()
