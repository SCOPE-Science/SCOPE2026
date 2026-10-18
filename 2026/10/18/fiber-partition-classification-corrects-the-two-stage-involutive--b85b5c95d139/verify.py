"""Independent finite checks of the two-fiber Boolean Płonka classification.

Run with: python3 verify.py
Only the Python standard library is required.
"""
from collections import Counter
from itertools import permutations, product
from math import factorial


def signature(f, a):
    counts = Counter(f)
    return tuple(sorted(counts.values(), reverse=True))


def partitions_of_b(b, maximum_length):
    def rec(remaining, ceiling, prefix):
        if remaining == 0:
            if len(prefix) <= maximum_length:
                yield tuple(prefix)
            return
        if len(prefix) >= maximum_length:
            return
        for k in range(min(remaining, ceiling), 0, -1):
            yield from rec(remaining - k, k, prefix + [k])
    return set(rec(b, b, []))


def automorphism_count(a, lam):
    r = len(lam)
    mult = Counter(lam)
    ans = factorial(a - r)
    for size, frequency in mult.items():
        ans *= (factorial(size) ** frequency) * factorial(frequency)
    return ans


def orbit_of(f, a, b):
    # Every isomorphism of two-stage systems is a pair of atomic permutations.
    s = set()
    for alpha in permutations(range(a)):
        for beta in permutations(range(b)):
            transformed = [0] * b
            for j in range(b):
                transformed[beta[j]] = alpha[f[j]]
            s.add(tuple(transformed))
    return s


def inverse_image(mask, f, b):
    return sum((1 << j) for j in range(b) if mask & (1 << f[j]))


def plonka_ops(a, b, f):
    # Elements are (level, subset-mask); constants live at level zero.
    universe = tuple([(0, x) for x in range(1 << a)] +
                     [(1, x) for x in range(1 << b)])
    def lift(v):
        return inverse_image(v[1], f, b) if v[0] == 0 else v[1]
    def join(x, y):
        if x[0] == y[0] == 0:
            return (0, x[1] | y[1])
        return (1, lift(x) | lift(y))
    def negate(x):
        return (x[0], x[1] ^ ((1 << (a if x[0] == 0 else b)) - 1))
    def meet(x, y):
        return negate(join(negate(x), negate(y)))
    return universe, join, meet, negate, (0, 0), (0, (1 << a) - 1)


def check_identities(a, b, f):
    elements, join, meet, neg, zero, one = plonka_ops(a, b, f)
    for x in elements:
        assert join(x, x) == x
        assert neg(neg(x)) == x
        assert join(zero, x) == x
        assert one == neg(zero)
        for y in elements:
            assert join(x, y) == join(y, x)
            assert meet(x, y) == neg(join(neg(x), neg(y)))
            assert meet(x, join(neg(x), y)) == meet(x, y)
            for z in elements:
                assert join(x, join(y, z)) == join(join(x, y), z)
    return len(elements)


def main():
    total_maps = 0
    total_orbits = 0
    cases = 0
    for a in range(1, 5):
        for b in range(1, 6):
            maps = [tuple(f) for f in product(range(a), repeat=b)]
            signatures = {signature(f, a) for f in maps}
            expected = partitions_of_b(b, a)
            assert signatures == expected, (a, b, signatures, expected)
            assert sum(factorial(a) * factorial(b) // automorphism_count(a, lam)
                       for lam in signatures) == a ** b
            # Exhaustively compute the actual left-right permutation action.
            covered = set()
            for lam in signatures:
                representative = next(f for f in maps if signature(f, a) == lam)
                orbit = orbit_of(representative, a, b)
                assert len(orbit) == factorial(a) * factorial(b) // automorphism_count(a, lam)
                assert {signature(g, a) for g in orbit} == {lam}
                assert not (orbit & covered)
                covered |= orbit
            assert covered == set(maps), (a, b)
            total_maps += len(maps)
            total_orbits += len(signatures)
            cases += 1

    a, b = 2, 4
    f = (0, 0, 0, 1)
    g = (0, 0, 1, 1)
    assert signature(f, a) == (3, 1) and signature(g, a) == (2, 2)
    assert len(set(f)) == len(set(g)) == 2
    assert not orbit_of(f, a, b).intersection(orbit_of(g, a, b))
    assert len(partitions_of_b(4, 2)) == 3
    assert check_identities(a, b, f) == 20
    assert check_identities(a, b, g) == 20
    # Sharp earliest fixed-shape failure: for a,b with 2^a+2^b<20,
    # the fiber-count invariant is sufficient; compare signatures at each rank.
    checked_smaller = 0
    for aa in range(1, 5):
        for bb in range(1, 5):
            if (1 << aa) + (1 << bb) >= 20:
                continue
            rank_parts = Counter(map(len, partitions_of_b(bb, aa)))
            assert all(v == 1 for v in rank_parts.values()), (aa, bb, rank_parts)
            checked_smaller += 1
    print('VERIFY_OK', 'parameter_pairs', cases, 'maps', total_maps,
          'orbits', total_orbits, 'strictly_smaller_shapes', checked_smaller,
          'counterexample_shape', (4, 16), 'rank', 2,
          'distinguished_fibers', ((3, 1), (2, 2)),
          'corrected_types', 3, 'rank_only_types', 2,
          'axioms_checked', 8)


if __name__ == '__main__':
    main()
