"""Exact finite profile checker for a committee proportionality boundary.
Public, stand-alone: Python 3.9+, no third-party packages.
"""
from collections import Counter
from itertools import combinations_with_replacement, permutations
from math import lcm


def satisfies_weak(n, k, winners, challenger):
    """Every coalition of supporters of the unelected candidate."""
    utilities = [sum((d >> i) & 1 for d in winners) for i in range(n)]
    for s in range(1, 1 << n):
        if s & ~challenger:
            continue
        t = s.bit_count()
        if not any(n * (utilities[i] + 1) > k * t
                   for i in range(n) if (s >> i) & 1):
            return False
    return True


def satisfies_strong(n, k, winners, challenger):
    """Exact rational form of the payment-based strong EJR+ condition."""
    scale = lcm(*range(1, n + 1))
    for s in range(1, 1 << n):
        supporters = s & challenger
        t = supporters.bit_count()
        if not t:
            continue
        scores = [0] * n
        for i in range(n):
            if not ((s >> i) & 1):
                continue
            if (challenger >> i) & 1:
                scores[i] += scale // t
            for d in winners:
                if (d >> i) & 1:
                    scores[i] += scale // max(t, (s & d).bit_count())
        if all(n * scores[i] <= k * scale
               for i in range(n) if (s >> i) & 1):
            return False
    return True


def pareto_optimal(winners, challenger):
    """For a full k-of-(k+1) committee, no candidate can replace a winner to Pareto-improve."""
    return all((d & ~challenger) != 0 or d == challenger for d in winners)


def permute(mask, p):
    return sum(1 << p[i] for i in range(len(p)) if (mask >> i) & 1)


def signature(winners, challenger, p):
    return tuple(sorted(permute(x, p) for x in winners)), permute(challenger, p)


def enumerate_boundary(n, k):
    types = range(1, 1 << n)
    differences = set()
    all_cases = 0
    for winners in combinations_with_replacement(types, k):
        for challenger in types:
            all_cases += 1
            if satisfies_weak(n, k, winners, challenger) and not satisfies_strong(n, k, winners, challenger):
                differences.add((winners, challenger))
    remaining = set(differences)
    orbits = []
    while remaining:
        w, c = min(remaining)
        orbit = {signature(w, c, p) for p in permutations(range(n))}
        assert orbit <= differences
        remaining.difference_update(orbit)
        orbits.append((min(orbit), len(orbit), pareto_optimal(w, c)))
    return all_cases, len(differences), sorted(orbits)


def main():
    examined = 0
    for n, ks in [(1, range(1, 5)), (2, range(1, 7)),
                  (3, range(1, 4)), (4, range(1, 3)),
                  (5, range(1, 3))]:
        for k in ks:
            cases, gap, _ = enumerate_boundary(n, k)
            examined += cases
            assert gap == 0, (n, k, gap)
    print('SMALL_REGIME_OK cases=', examined)
    results = {}
    for n, k in [(3, 4), (4, 3)]:
        cases, gap, orbits = enumerate_boundary(n, k)
        print('BOUNDARY', n, k, 'cases', cases, 'gap_profiles', gap,
              'voter_relabeling_orbits', len(orbits),
              'pareto_efficient_orbits', sum(x[2] for x in orbits))
        for v in orbits:
            print('ORBIT', n, k, v)
        results[(n, k)] = (cases, gap, len(orbits), sum(x[2] for x in orbits))
    assert results[(3, 4)] == (1470, 18, 4, 1)
    assert results[(4, 3)] == (10200, 6, 1, 1)
    for n, k, w, c in [(3, 4, (1, 1, 6, 7), 6),
                        (4, 3, (1, 2, 15), 12)]:
        assert satisfies_weak(n, k, w, c)
        assert not satisfies_strong(n, k, w, c)
        assert pareto_optimal(w, c)
    print('VERIFY_OK sharp_boundary=8 pareto_witnesses=2')


if __name__ == '__main__':
    main()
