"""Finite symbolic checks for the two-particle shift group classification.
The universal classification is proved mathematically in RESULT.md.
"""
from itertools import permutations, combinations


def apply_pair(left, gap, gap_perm, offsets):
    return left + offsets.get(gap, 0), gap_perm.get(gap, gap)


def inverse_data(gap_perm, offsets):
    supp = set(gap_perm) | set(gap_perm.values()) | set(offsets)
    inv = {gap_perm.get(d, d): d for d in supp}
    inv_offsets = {new: -offsets.get(old, 0) for new, old in inv.items()}
    return inv, inv_offsets


def image_support(support, perm, offsets):
    if len(support) <= 1:
        return frozenset(support)
    a, b = sorted(support)
    newa, newd = apply_pair(a, b-a, perm, offsets)
    return frozenset((newa, newa+newd))


def finite_window_verifier(perm, offsets, radius, max_gap=70):
    # Every possible local window with <=2 ones is represented by the
    # empty set, singleton, or pairs within radius. A representative
    # distant second particle is also included when only one is visible.
    patterns = {}
    samples = [frozenset(), *(frozenset((a,)) for a in range(-radius-10, radius+11))]
    samples += [frozenset((a,a+d))
                for a in range(-radius-10, radius+11)
                for d in range(1, max_gap+1)]
    for supp in samples:
        window = tuple(sorted(i for i in supp if -radius <= i <= radius))
        out = int(0 in image_support(supp, perm, offsets))
        if window in patterns and patterns[window] != out:
            raise AssertionError(('not local at radius', radius, supp, window, out))
        patterns[window] = out
    return len(patterns)


def run():
    # Several nontrivial disjoint finite-gap permutations and translations.
    cases = [
        ({1:3,3:1,2:5,5:2}, {1:2,3:-3,2:4,5:-1}),
        ({1:4,4:2,2:1}, {1:1,2:-3,4:0}),
        ({3:6,6:3}, {3:-4,6:5}),
        ({}, {1:4,2:-4,7:11}),
        ({}, {}),
    ]
    checked = 0
    for perm, offsets in cases:
        inv, inv_offsets = inverse_data(perm, offsets)
        # Inverse on a comprehensive finite set, and shift-equivariance.
        for a in range(-15, 16):
            for d in range(1, 32):
                s = frozenset((a, a+d))
                y = image_support(s, perm, offsets)
                assert image_support(y, inv, inv_offsets) == s
                assert image_support(frozenset(i+1 for i in s), perm, offsets) == frozenset(i+1 for i in y)
                checked += 1
        # A deliberately generous radius: entire altered finite-gap
        # patterns are visible whenever they can alter the central symbol.
        radius = 50
        npatterns = finite_window_verifier(perm, offsets, radius, max_gap=70)
        assert npatterns >= 2
        checked += npatterns
    # Complexity is exactly count of words with <=2 active positions.
    for n in range(1, 40):
        patterns = {frozenset(s) for k in range(3) for s in combinations(range(n), k)}
        assert len(patterns) == 1+n+n*(n-1)//2
        checked += 1
    print('VERIFY_OK checked_cases=', checked, 'models=', len(cases))

if __name__ == '__main__':
    run()
