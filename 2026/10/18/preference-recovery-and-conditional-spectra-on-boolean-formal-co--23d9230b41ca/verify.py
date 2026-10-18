"""Independent exhaustive finite checks of preferential contranominal contexts.

Standard library only. No theorem is inferred from finite exhaustiveness.
"""
from itertools import product, combinations
from math import comb


def bits(mask, n):
    return [i for i in range(n) if (mask >> i) & 1]


def all_partial_orders(n):
    """Encode a strict poset by predecessor masks; transitivity is checked."""
    pairs = list(combinations(range(n), 2))
    for directions in product((0, 1, 2), repeat=len(pairs)):
        below = [0] * n
        for (i, j), direction in zip(pairs, directions):
            if direction == 1: below[j] |= 1 << i
            if direction == 2: below[i] |= 1 << j
        if all(not ((below[y] & (1 << x)) and (below[x] & ~below[y]))
               for y in range(n) for x in bits(below[y], n)):
            yield tuple(below)


def minima(X, below, n):
    return sum(1 << x for x in bits(X, n) if not (X & below[x]))


def direct_extent(A, n):
    # Derivation in incidence (object, attribute) iff object != attribute.
    return sum(1 << g for g in range(n)
               if all(g != a for a in bits(A, n)))


def direct_attributes(Y, n):
    return sum(1 << a for a in range(n)
               if all(g != a for g in bits(Y, n)))


def direct_min_extent(X, below, n):
    return sum(1 << g for g in bits(X, n)
               if not any((h != g) and (X & (1 << h)) and (below[g] & (1 << h))
                          for h in range(n)))


def poly_expected(below, n):
    coeffs = [0] * (n + 1)
    for dmask in below:
        d = dmask.bit_count()
        for t in range(1, n + 1):
            coeffs[t] += comb(n-1, t-1) - (comb(n-1-d, t-1) if t-1 <= n-1-d else 0)
    return coeffs


def check_one(below, n):
    full = (1 << n)-1
    actual_poly = [0] * (n+1)
    typical_extents = set()
    for A in range(1 << n):
        X = direct_extent(A,n)
        assert X == full ^ A
        Y = direct_min_extent(X,below,n)
        # Compute every singleton nonmonotonic consequence directly from the incidence table.
        inferred = direct_attributes(Y,n)
        assert inferred & A == A
        novel = inferred & ~A & full
        assert novel == (X & ~minima(X,below,n))
        actual_poly[X.bit_count()] += novel.bit_count()
        typical_extents.add(direct_extent(direct_attributes(Y,n),n))
        assert direct_extent(direct_attributes(Y,n),n) == Y  # valid order
        for x in bits(novel,n): assert x not in bits(A,n)
    antichains = {X for X in range(1 << n) if all(not (X & below[x]) for x in bits(X,n))}
    assert typical_extents == antichains
    assert actual_poly == poly_expected(below,n)
    # The two-object residual tests recover each individual strict comparison.
    for x in range(n):
        for y in range(n):
            if x == y: continue
            X = (1 << x) | (1 << y)
            A = full ^ X
            Y = direct_min_extent(direct_extent(A,n),below,n)
            inferred = direct_attributes(Y,n)
            assert bool(inferred & (1 << y)) == bool(below[y] & (1 << x))
    return len(typical_extents)


def test_sharp(n):
    # The orders differ by x<y and every other point z<y.
    x, y = 0, 1
    Z = tuple(range(2,n))
    base = [0]*n
    base[y] = sum(1<<z for z in Z)
    longer = base.copy()
    longer[y] |= 1<<x
    full=(1<<n)-1
    for X in range(1<<n):
        if X.bit_count()>=3:
            assert direct_attributes(direct_min_extent(X,base,n),n) == direct_attributes(direct_min_extent(X,longer,n),n)
    pair=(1<<x)|(1<<y)
    assert direct_attributes(direct_min_extent(pair,base,n),n) != direct_attributes(direct_min_extent(pair,longer,n),n)
    check_one(tuple(base),n); check_one(tuple(longer),n)


def test_orientation():
    # Distinct labeled posets with identical comparability graph.
    below_V = (0,0,0b011)
    below_D = (0b100,0b100,0)
    def typical(below):
        return {X for X in range(8) if all(not (X & below[x]) for x in bits(X,3))}
    assert typical(below_V) == typical(below_D)
    assert poly_expected(below_V,3) == [0,0,2,1]
    assert poly_expected(below_D,3) == [0,0,2,2]
    assert sum(poly_expected(below_V,3)) == 3
    assert sum(poly_expected(below_D,3)) == 4




def test_same_typical_and_spectrum():
    # Two nonisomorphic five-point preference posets with the same comparisons
    # after orientations are forgotten, and the same predecessor-degree multiset.
    P = (0, 0b01100, 0, 0b00100, 0b01101)
    Q = (0b10000, 0, 0b10010, 0b10110, 0)
    n=5
    for x in range(n):
        for y in range(x+1,n):
            assert bool(P[x]&(1<<y) or P[y]&(1<<x)) == bool(Q[x]&(1<<y) or Q[y]&(1<<x))
    assert sorted(x.bit_count() for x in P) == sorted(x.bit_count() for x in Q)
    assert poly_expected(P,n) == poly_expected(Q,n) == [0,0,6,14,11,3]
    tP = {A for A in range(1<<n) if all(not (A & P[x]) for x in bits(A,n))}
    tQ = {A for A in range(1<<n) if all(not (A & Q[x]) for x in bits(A,n))}
    assert tP == tQ
    check_one(P,n); check_one(Q,n)
    # The unique degree-three Hasse vertex has one predecessor in P
    # and two predecessors in Q, so there is no poset isomorphism.
    def covers(b):
        return {(x,y) for y in range(n) for x in bits(b[y],n)
                if not any((b[z]&(1<<x)) for z in bits(b[y],n) if z!=x)}
    def branch_in(b):
        c=covers(b)
        for v in range(n):
            inc=sum(x==v or y==v for x,y in c)
            if inc==3:return sum(y==v for x,y in c)
        raise AssertionError('no Hasse branch')
    assert branch_in(P)==1 and branch_in(Q)==2

def main():
    tested=0
    total_premises=0
    counts=[]
    for n in range(1,6):
        c=0
        for below in all_partial_orders(n):
            check_one(below,n)
            c+=1
        counts.append(c)
        tested += c
        total_premises += c*(1<<n)
    assert counts == [1,3,19,219,4231], counts
    test_orientation()
    test_same_typical_and_spectrum()
    for n in range(3,9):test_sharp(n)
    print('VERIFY_OK posets_n_1_to_5=',counts,
          'total_posets=',tested,'direct_incidence_premises=',total_premises,
          'minima_typical_concepts=PASS','singleton_conditionals=PASS',
          'predecessor_polynomials=PASS','binary_reconstruction=PASS',
          'identical_short_premises_n_3_to_8=PASS','orientation_gap=PASS','five_point_nonisomorphic_spectrum_collision=PASS')

if __name__ == '__main__': main()
