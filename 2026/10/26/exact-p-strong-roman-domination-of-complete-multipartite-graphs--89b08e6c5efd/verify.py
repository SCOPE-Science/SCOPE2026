#!/usr/bin/env python3
"""Independent finite checks of the p-strong Roman formula on multipartite graphs.

Usage: python verify.py
Requires Python 3.10+ standard library only.
"""
from itertools import combinations_with_replacement, combinations, product
from math import ceil


def formula(part_sizes, p):
    n = sum(part_sizes)
    assert len(part_sizes) >= 3 and p >= 2
    one = min(s + ceil((n-s)/p) for s in part_sizes)
    two = min(
        2 + ceil((n-part_sizes[i]-1)/p) + ceil((n-part_sizes[j]-1)/p)
        - int((n-part_sizes[i]-1) % p == 1 and (n-part_sizes[j]-1) % p == 1)
        for i, j in combinations(range(len(part_sizes)), 2)
    )
    return min(one, two)


def zero_profile_oracle(part_sizes, p):
    """Optimize directly over all zero profiles and all subsets of defender parts.

    Uses only the definition; does not assume that two defenders suffice.
    It is a separate exact optimization from the claimed closed formula.
    """
    n = sum(part_sizes)
    best = n
    for zeros in product(*(range(s+1) for s in part_sizes)):
        Z = sum(zeros)
        if Z == 0:
            continue
        possible = [i for i, s in enumerate(part_sizes) if zeros[i] < s]
        if not possible:
            continue
        zero_parts = [i for i, z in enumerate(zeros) if z]
        for mask in range(1, 1 << len(possible)):
            selected = [possible[t] for t in range(len(possible)) if mask & (1 << t)]
            if not all(any(j != i for j in selected) for i in zero_parts):
                continue
            weight = n - Z + sum(ceil((Z-zeros[j])/p) for j in selected)
            best = min(best, weight)
    return best


def label_oracle(part_sizes, p, ceiling):
    """Directly enumerate labelled functions and every zero vertex's witnesses."""
    n = sum(part_sizes)
    side = tuple(i for i, s in enumerate(part_sizes) for _ in range(s))
    neighborhoods = tuple(tuple(j for j in range(n) if side[i] != side[j]) for i in range(n))
    best = n
    for labeling in product(range(ceiling+1), repeat=n):
        weight = sum(labeling)
        if weight >= best:
            continue
        zeros = [i for i, x in enumerate(labeling) if x == 0]
        good = True
        for u in zeros:
            if not any(labeling[v] >= 1 + ceil(sum(labeling[w] == 0 for w in neighborhoods[v]) / p)
                       for v in neighborhoods[u]):
                good = False
                break
        if good:
            best = weight
    return best


def main():
    zero_checks = 0
    direct_checks = 0
    profiles = 0
    for n in range(3, 14):
        for r in range(3, min(5, n)+1):
            for parts in combinations_with_replacement(range(1, 9), r):
                if sum(parts) != n:
                    continue
                profiles += 1
                delta = n - min(parts)
                for p in range(3, min(7, delta-1)+1):
                    expected = formula(parts, p)
                    observed = zero_profile_oracle(parts, p)
                    assert expected == observed, (parts,p,expected,observed)
                    zero_checks += 1
                    if n <= 8:
                        observed_labeled = label_oracle(parts, p, 1+ceil(delta/p))
                        assert expected == observed_labeled, (parts,p,expected,observed_labeled)
                        direct_checks += 1
    examples = [(4,(5,5,5),7),(3,(6,8,8),11),(5,(4,8,8),7),(6,(4,4,4),5)]
    for p,parts,expected in examples:
        assert formula(parts,p) == zero_profile_oracle(parts,p) == expected, (p,parts)
    print(f'ZERO_PROFILE_CHECKS={zero_checks}')
    print(f'DIRECT_LABEL_CHECKS={direct_checks}')
    print(f'GRAPH_PROFILES={profiles}')
    print(f'CONGRUENCE_EXAMPLES={len(examples)}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
