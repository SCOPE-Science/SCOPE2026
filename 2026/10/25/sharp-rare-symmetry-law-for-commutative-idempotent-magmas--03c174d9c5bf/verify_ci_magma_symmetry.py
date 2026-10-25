"""Reproducible small-order checks for commutative idempotent magma symmetry.

Requires only the Python standard library. Run: python verify_ci_magma_symmetry.py
The asymptotic statements are established by a separate mathematical proof.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, exp, log


def perm_power_value(permutation, value, exponent):
    for _ in range(exponent):
        value = permutation[value]
    return value


def fixed_fraction_by_pair_orbits(permutation):
    n = len(permutation)
    pair_set = tuple(combinations(range(n), 2))
    unseen = set(pair_set)
    ways = 1
    orbits = 0
    while unseen:
        pair = min(unseen)
        length = 0
        while pair in unseen:
            unseen.remove(pair)
            length += 1
            pair = tuple(sorted((permutation[pair[0]], permutation[pair[1]])))
        fixed_output_count = sum(
            perm_power_value(permutation, value, length) == value
            for value in range(n)
        )
        ways *= fixed_output_count
        orbits += 1
    return Fraction(ways, n ** len(pair_set)), orbits


def is_automorphism(permutation, pair_index, operation_values):
    for pair, value in zip(pair_index, operation_values):
        image_pair = tuple(sorted((permutation[pair[0]], permutation[pair[1]])))
        if operation_values[pair_index[image_pair]] != permutation[value]:
            return False
    return True


def exhaustive_small_order(n):
    pairs = tuple(combinations(range(n), 2))
    lookup = {pair: pos for pos, pair in enumerate(pairs)}
    permutations_n = tuple(permutations(range(n)))
    count_fixed = {p: 0 for p in permutations_n}
    nontrivial = 0
    aut_exactly_one_transposition = 0
    isomorphism_classes = set()
    symmetric_isomorphism_classes = set()
    for table in product(range(n), repeat=len(pairs)):
        symmetries = []
        for p in permutations_n:
            if is_automorphism(p, lookup, table):
                symmetries.append(p)
                count_fixed[p] += 1
        relabelings = []
        for p in permutations_n:
            new_table = [0]*len(pairs)
            for pair, value in zip(pairs, table):
                image = tuple(sorted((p[pair[0]], p[pair[1]])))
                new_table[lookup[image]] = p[value]
            relabelings.append(tuple(new_table))
        canonical = min(relabelings)
        isomorphism_classes.add(canonical)
        if len(symmetries) > 1:
            nontrivial += 1
            symmetric_isomorphism_classes.add(canonical)
        if len(symmetries) == 2 and sum(
            symmetries[1][i] != i for i in range(n)
        ) == 2:
            aut_exactly_one_transposition += 1
    total = n ** len(pairs)
    for p in permutations_n:
        probability, _ = fixed_fraction_by_pair_orbits(p)
        assert Fraction(count_fixed[p], total) == probability
    print('EXHAUSTIVE', 'n', n, 'tables', total,
          'nontrivial_automorphisms', nontrivial,
          'automorphism_group_generated_by_one_transposition',
          aut_exactly_one_transposition,
          'unlabeled_classes', len(isomorphism_classes),
          'unlabeled_symmetric_classes', len(symmetric_isomorphism_classes))
    assert (n, len(isomorphism_classes), len(symmetric_isomorphism_classes)) in ((3, 7, 4), (4, 192, 38))


def check_orbit_support_and_tail(n):
    identity = tuple(range(n))
    permutation_count = {k: 0 for k in range(2, n+1)}
    mass = {k: Fraction(0) for k in range(2, n+1)}
    for p in permutations(range(n)):
        if p == identity:
            continue
        support = sum(p[i] != i for i in range(n))
        probability, pair_orbits = fixed_fraction_by_pair_orbits(p)
        deficit = comb(n, 2) - pair_orbits
        assert 4*deficit >= support*(2*n-support-2)
        permutation_count[support] += 1
        mass[support] += probability
    transposition = (1, 0) + tuple(range(2, n))
    probability, _ = fixed_fraction_by_pair_orbits(transposition)
    m = comb(n-2, 2)+1
    formula = Fraction((n-2)**m, n**(m+n-2))
    assert probability == formula
    assert mass[2] == comb(n, 2)*formula
    rest = sum((mass[k] for k in range(3, n+1)), Fraction(0))
    print('CYCLE_ORBITS', 'n', n, 'nonidentity_permutations',
          sum(permutation_count.values()),
          'single_transposition_probability', probability,
          'tail_to_transposition_ratio', float(rest / mass[2]))


def check_leading_constant():
    for n in (20, 50, 100, 250):
        m = comb(n-2, 2)+1
        log_exact = log(comb(n, 2)) - (n-2)*log(n) + m*log(1-2/n)
        log_leading = 4-log(2)-n+(4-n)*log(n)
        print('ASYMPTOTIC_SCALE', 'n', n,
              'exact_first_moment_over_leading_expression',
              round(exp(log_exact-log_leading), 9))


if __name__ == '__main__':
    for n in (3, 4):
        exhaustive_small_order(n)
    for n in range(3, 8):
        check_orbit_support_and_tail(n)
    check_leading_constant()
    print('ALL_CI_MAGMA_SYMMETRY_CHECKS_PASSED')
