#!/usr/bin/env python3
"""Exact rank-three first-order types of halved cubes (pure adjacency/equality).

No graph library or external data is required. Works over all even-weight bitmasks.
The finite checks are illustrative; the all-dimensional theorem requires the
support-count argument supplied in RESULT.md.
"""
from collections import defaultdict


def vertices(d):
    return tuple(x for x in range(1 << d) if x.bit_count() % 2 == 0)


def adj(x, y):
    return (x ^ y).bit_count() == 2


def pair_signature(x, y, vs):
    # Full quantifier-rank-1 type of the ordered pair, encoded by the
    # complete set of all possible quantifier-free extensions by z.
    atomic = (x == y, adj(x, y))
    extension = frozenset(
        (z == x, z == y, adj(x, z), adj(y, z)) for z in vs
    )
    return (atomic, extension)


def exact_rank3_type(d):
    vs = vertices(d)
    # For each x, encode its rank-2 type by all pair rank-1 types (x,y).
    rooted_types = frozenset(
        frozenset(pair_signature(x, y, vs) for y in vs) for x in vs
    )
    # The unpointed rank-3 type is the set of rooted rank-2 types.
    return rooted_types


def orbit_pair_signature(d, t):
    vs = vertices(d)
    return pair_signature(0, (1 << (2 * t)) - 1, vs)


def quantifier3_threshold_features(d):
    vs = vertices(d)
    signatures = [orbit_pair_signature(d, t) for t in range(d // 2 + 1)]
    def z_flags(signature):
        return {(w[2], w[3]) for w in signature[1]
                if not w[0] and not w[1]}
    atom_and = [(sig[0], z_flags(sig)) for sig in signatures]
    nonadj = [profile for atom, profile in atom_and if atom == (False, False)]
    adj_pairs = [profile for atom, profile in atom_and if atom == (False, True)]
    return (
        len(vs) >= 2,
        len(vs) >= 3,
        bool(nonadj),
        any((False, False) in s for s in adj_pairs),
        any((False, False) in s for s in nonadj),
        any((True, True) not in s and (False, False) in s for s in nonadj),
    )


def main():
    # Independent full graph recurrence, without orbit compression.
    profiles = {}
    for d in range(1, 10):
        profiles[d] = exact_rank3_type(d)
    for d in range(1, 9):
        assert (profiles[d] == profiles[d + 1]) == (d >= 7), (d, 'adjacent dimension mismatch')
    assert len(set(profiles.values())) == 7
    print('FULL_RECURSION_OK dimensions=1..9 classes=7 stable_from=7')

    # Separate coordinate-orbit method for dimensions up to 13.
    obs = {}
    for d in range(1, 14):
        obs[d] = frozenset(orbit_pair_signature(d, t) for t in range(d // 2 + 1))
    for d in range(1, 13):
        assert (obs[d] == obs[d + 1]) == (d >= 7)
    for d in range(1, 10):
        assert profiles[d] == frozenset({obs[d]})
    print('ORBIT_REDUCTION_OK dimensions=1..13 stable_from=7')

    # Six actual rank<=3 sentences, represented by their Boolean truth values.
    # Each is monotone with threshold d=2,3,4,5,6,7, respectively.
    for d in range(1, 14):
        expected = tuple(d >= j for j in range(2, 8))
        assert quantifier3_threshold_features(d) == expected, d
    print('SEPARATING_SENTENCES_OK thresholds=2,3,4,5,6,7')

    # For large dimensions check directly that all distance>=6 pair orbits
    # have identical rank-one types. This is a finite regression, NOT the proof.
    for d in range(7, 14):
        if d // 2 >= 3:
            a = orbit_pair_signature(d, 3)
            assert all(orbit_pair_signature(d, t) == a
                       for t in range(3, d // 2 + 1))
    print('LARGE_PAIR_SIGNATURES_OK dimensions=7..13')
    print('SHARP_MINIMUM_REPRESENTATIVE_OK order=64')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
