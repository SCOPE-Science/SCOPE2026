"""Exact finite checks for the first nonconcave approval-coverage layer.

Standard-library only; every committee is explicitly enumerated.
The infinite-size conclusions require the accompanying analytic proof.
"""
from itertools import combinations, combinations_with_replacement, permutations
from math import comb


def profile(sets):
    """Exact maximum-coverage value at each committee cardinality."""
    return [max((sum(0 for _ in []) if not indices else
                 __import__('functools').reduce(int.__or__, (sets[i] for i in indices), 0)).bit_count()
                for indices in combinations(range(len(sets)), k))
            for k in range(len(sets) + 1)]


def canonical_bad(sets):
    """A bad set family is three disjoint two-sets and a transversal three-set."""
    sizes = [s.bit_count() for s in sets]
    if sorted(sizes) != [2, 2, 2, 3]:
        return False
    d = sets[sizes.index(3)]
    pairs = [s for s in sets if s.bit_count() == 2]
    return (pairs[0] & pairs[1] == pairs[0] & pairs[2] == pairs[1] & pairs[2] == 0
            and (pairs[0] | pairs[1] | pairs[2]).bit_count() == 6
            and all((p & d).bit_count() == 1 for p in pairs))


def voter_interval(sets, n):
    for order in permutations(range(n)):
        loc = {v: j for j, v in enumerate(order)}
        if all((not pts or max(pts) - min(pts) + 1 == len(pts))
               for s in sets
               for pts in [[loc[v] for v in range(n) if s >> v & 1]]):
            return True
    return False


def main():
    checks = 0
    bad_n6 = 0
    # Multisets include empty and repeated supporter sets, so this is all
    # labeled-voter, unordered-candidate profiles with four candidates.
    for n in range(1, 7):
        seen_bad = 0
        for sets in combinations_with_replacement(range(1 << n), 4):
            m = profile(sets)
            violations = [k for k in range(1, 4)
                          if 2 * m[k] < m[k-1] + m[k+1]]
            if n < 6:
                assert not violations, (n, sets, m)
            else:
                assert bool(violations) == canonical_bad(sets), (sets, m, violations)
                if violations:
                    assert violations == [2] and m == [0, 3, 4, 6, 6]
                    seen_bad += 1
            checks += 1
        assert seen_bad == (120 if n == 6 else 0), (n, seen_bad)
        if n == 6:
            bad_n6 = seen_bad
    sets = [0b000011, 0b001100, 0b110000, 0b010101]
    assert profile(sets) == [0, 3, 4, 6, 6]
    assert not voter_interval(sets, 6)
    for v in range(6):
        remapped = [sum(1 << (i - (i > v)) for i in range(6)
                        if i != v and (s >> i & 1)) for s in sets]
        assert voter_interval(remapped, 5), (v, remapped)
    print('PASS; total exhaustive 4-candidate multiset profiles:', checks)
    print('PASS; nonconcave n=6, m=4 voter-labeled candidate-unlabeled:', bad_n6)
    print('PASS; candidate-labeled minimal profiles:', bad_n6 * 24)
    print('PASS; the witness is voter-deletion-critical for voter intervals')


if __name__ == '__main__':
    main()
