"""Exact finite checks for the fixed-size Smith-set asymptotic constant.

Uses only the Python standard library. No infinite-limit claim is inferred
from the finite checks: the analytic argument is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import factorial


def winning(i, j, rankings):
    return sum(p.index(i) < p.index(j) for p in rankings) > len(rankings)//2


def strongly_connected(S, rankings):
    if len(S) == 1:
        return True
    for start in S:
        seen = {start}
        for _ in range(len(S)):
            seen |= {v for u in tuple(seen) for v in S if v != u and winning(u,v,rankings)}
        if seen != set(S):
            return False
    return True


def dominates(S, universe, rankings):
    return all(winning(i, j, rankings) for i in S for j in universe if j not in S)


def smith_set(universe, rankings):
    for sz in range(1, len(universe)+1):
        good = [q for q in combinations(universe, sz) if dominates(q, universe, rankings)]
        if good:
            assert len(good) == 1
            return frozenset(good[0])
    raise AssertionError('Impossible')


def rectangle_union(coords, J):
    """Exact union volume of anchored rectangles for fixed voter coordinates J."""
    ss = len(coords)
    v = F(0)
    for k in range(1, ss+1):
        for I in combinations(range(ss), k):
            prod = F(1)
            for j in J:
                prod *= min(coords[i][j] for i in I)
            v += prod if k % 2 else -prod
    return v


def forbidden_volume(coords, ell):
    """Exact union volume in m dimensions of ALL i,J cylinder events."""
    m = len(coords[0])
    cylinders = [(i, J) for i in range(len(coords)) for J in combinations(range(m), ell)]
    v = F(0)
    for mask in range(1, 1<<len(cylinders)):
        height = [F(1)]*m
        k = 0
        for a, (i,J) in enumerate(cylinders):
            if mask & (1<<a):
                k += 1
                for j in J:
                    height[j] = min(height[j], coords[i][j])
        prod = F(1)
        for h in height:
            prod *= h
        v += prod if k%2 else -prod
    return v


def phi(coords, ell):
    return sum((rectangle_union(coords, J) for J in combinations(range(len(coords[0])), ell)), F(0))


def check_enumeration(n):
    all_ranks = list(permutations(range(n)))
    counts = {}
    checks = 0
    for ranks in product(all_ranks, repeat=3):
        S = smith_set(range(n), ranks)
        counts[len(S)] = counts.get(len(S), 0) + 1
        # For every nonempty candidate subset, its defining event matches
        # 'the candidate subset is precisely the Smith set'.
        for k in range(1,n+1):
            for T in combinations(range(n),k):
                expected = set(T) == S
                assert (dominates(T, range(n),ranks) and strongly_connected(T,ranks)) == expected
                checks += 1
    assert sum(counts.values()) == factorial(n)**3
    return counts, checks


def main():
    for n in [3,4]:
        counts, checks = check_enumeration(n)
        assert counts.get(2, 0) == 0
        assert counts.get(3, 0) > 0
        if n==3:
            assert counts[3] == 12  # 12/216=1/18.
        if n==4:
            assert counts[4] > 0
        print('n',n,'majority profile counts',counts,'strong/dominating checks',checks)

    # Exact scaled-overlap identity for three voters and a three-point core:
    coords = [[F(1,3),F(3,4),F(1,2)],
              [F(2,3),F(1,4),F(3,5)],
              [F(3,5),F(1,2),F(4,5)]]
    ph = phi(coords, 2)
    assert ph > 0
    for k in [2,3,4,5,7,11,17]:
        t = F(1,k)
        small = [[z*t for z in row] for row in coords]
        forbidden = forbidden_volume(small, 2)
        assert forbidden >= 0 and forbidden <= 1
        # In m=3, all cross-J intersections use three coordinates.
        correction = (ph*t*t-forbidden)/(t*t*t)
        assert correction >= 0
        if k == 2:
            reference = correction
        else:
            assert correction == reference
        assert forbidden <= t*t*ph
    print('exact 3-voter anchored-box expansion: phi =',ph,
          ', cubic overlap coefficient =',reference)

    # The core is a majority cycle in an explicit open voting-order cell.
    triple = ((0,1,2), (1,2,0), (2,0,1))
    assert strongly_connected(range(3),triple)
    # The integral's positivity is supported by this fixed open cell.
    print('verified an open 3-voter cyclic order cell and exact rational expansion')

if __name__ == '__main__':
    main()
