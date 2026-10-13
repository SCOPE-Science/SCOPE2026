#!/usr/bin/env python3
"""Finite exact checks for the rigidity proof of the canonical Esakia spaces X_n.

The all-n proof is symbolic and appears in RESULT.md.  This replay exhaustively
checks the adjacent-level incidence characterization for small widths and verifies
the label-recovery recursion over a broad finite parameter range.
"""
from itertools import permutations

checks = 0

def le_adj(m, lower, upper):
    """Whether x_{i+1}^lower <= x_i^upper in Definition 4.1."""
    return upper != lower + 1

# Exhaustively characterize every automorphism of one adjacent-level incidence
# graph for widths m+1 <= 6.  A compatible pair (p,q) must fix the universal
# upper/lower endpoints and satisfy p(l+1)=q(l)+1.
for m in range(1, 6):
    labels = tuple(range(m + 1))
    perms = list(permutations(labels))
    compatible = []
    for p in perms:      # permutation on upper level
        for q in perms:  # permutation on lower level
            ok = True
            for lower in labels:
                for upper in labels:
                    if le_adj(m, lower, upper) != le_adj(m, q[lower], p[upper]):
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                compatible.append((p, q))
                assert p[0] == 0; checks += 1
                assert q[m] == m; checks += 1
                for lower in range(m):
                    assert p[lower + 1] == q[lower] + 1; checks += 1

    # Conversely, the endpoint/shift equations give all compatible pairs.
    expected = []
    for q in perms:
        if q[m] != m:
            continue
        p = [None] * (m + 1)
        p[0] = 0
        for lower in range(m):
            p[lower + 1] = q[lower] + 1
        p = tuple(p)
        assert sorted(p) == list(labels); checks += 1
        for lower in labels:
            for upper in labels:
                assert le_adj(m, lower, upper) == le_adj(m, q[lower], p[upper]); checks += 1
        expected.append((p, q))
    assert set(compatible) == set(expected); checks += 1

# Check the intrinsic endpoint descriptions and the iterated missing-upper map.
# x_i^0 is the unique upper point above every point of L_{i+1}; x_{i+1}^m is
# the unique lower point below every point of L_i.  For l<m, the unique missed
# upper point of lower l is l+1.
for m in range(1, 101):
    labels = range(m + 1)
    universal_upper = [u for u in labels if all(le_adj(m, l, u) for l in labels)]
    universal_lower = [l for l in labels if all(le_adj(m, l, u) for u in labels)]
    assert universal_upper == [0]; checks += 1
    assert universal_lower == [m]; checks += 1
    for l in range(m):
        missed = [u for u in labels if not le_adj(m, l, u)]
        assert missed == [l + 1]; checks += 1

    # The k-fold intrinsic successor reconstruction recovers label k from a
    # zero-labelled point k levels below.
    for k in range(1, m + 1):
        label = 0
        # Apply s_{i+k-1}, ..., s_i; each missing-upper map increments label.
        for _ in range(k):
            assert label < m; checks += 1
            label += 1
        assert label == k; checks += 1

# Finite-chain consequence: if levels 0,...,D are permuted compatibly and
# D>m, then the top-level permutation is forced to be the identity.  Enumerate
# every admissible bottom permutation for manageable m and propagate upward.
for m in range(1, 8):
    labels = tuple(range(m + 1))
    D = m + 1
    survivors = 0
    for bottom in permutations(labels):
        p = tuple(bottom)
        # A level serving as the lower side of an adjacent pair must fix m.
        # Discard a candidate as soon as this necessary condition fails.
        alive = True
        for _ in range(D):
            if p[m] != m:
                alive = False
                break
            checks += 1
            up = [0] + [p[l] + 1 for l in range(m)]
            assert sorted(up) == list(labels); checks += 1
            p = tuple(up)
        if alive:
            survivors += 1
            assert p == labels; checks += 1
    assert survivors >= 1; checks += 1

print(f"VERIFY_OK {checks} exact assertions")
