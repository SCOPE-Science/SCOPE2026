#!/usr/bin/env python3
"""Exhaustive small-incidence verification for sample-based richness variance reversal.

Rows are distinct species identities, represented by possibly repeated nonzero
site-set masks. Each site occurs in at least one row. All arithmetic is exact.
"""
from collections import defaultdict
from fractions import Fraction
from functools import reduce
from itertools import combinations, combinations_with_replacement, permutations
from math import comb


def types_of_communities(sites, species):
    labels = tuple(range(sites))
    site_permutations = tuple(permutations(labels))
    def canonical(rows):
        return min(
            tuple(sorted(sum((1 << p[j]) for j in labels if row & (1 << j))
                         for row in rows))
            for p in site_permutations
        )
    canonical_types = set()
    labeled_site_models = 0
    for rows in combinations_with_replacement(range(1, 1 << sites), species):
        if reduce(lambda a, b: a | b, rows, 0) != (1 << sites) - 1:
            continue
        labeled_site_models += 1
        canonical_types.add(canonical(rows))
    return sorted(canonical_types), labeled_site_models


def direct_moments(sites, rows, effort):
    richness = [sum(any(mask & (1 << site) for site in subset)
                    for mask in rows)
                for subset in combinations(range(sites), effort)]
    mu = Fraction(sum(richness), len(richness))
    var = sum(((v - mu) ** 2 for v in richness), Fraction()) / len(richness)
    return mu, var


def covariance_moments(sites, rows, effort):
    sample_count = comb(sites, effort)
    q = [Fraction(comb(sites - mask.bit_count(), effort), sample_count)
         for mask in rows]
    mu = sum((1 - x for x in q), Fraction())
    var = sum((x * (1-x) for x in q), Fraction())
    for i, j in combinations(range(len(rows)), 2):
        q_union = Fraction(comb(sites - (rows[i] | rows[j]).bit_count(),
                                effort), sample_count)
        var += 2 * (q_union - q[i]*q[j])
    return mu, var


def cross(var_a, var_b):
    differences = [a-b for a,b in zip(var_a, var_b)]
    return min(differences) < 0 < max(differences)


def pair_orbits(sites, species):
    classes, raw_count = types_of_communities(sites, species)
    by_profile = defaultdict(list)
    for rows in classes:
        moments = tuple(direct_moments(sites, rows, effort)
                        for effort in range(1, sites+1))
        for effort, actual in enumerate(moments, 1):
            assert actual == covariance_moments(sites, rows, effort)
        signature = tuple(v for mu,v in moments[:-1])
        profile = tuple(sorted(row.bit_count() for row in rows))
        by_profile[profile].append((rows, signature, moments))
    pairs = []
    for profile, models in by_profile.items():
        for (a, av, am), (b, bv, bm) in combinations(models, 2):
            if cross(av,bv):
                assert tuple(x for x,_ in am) == tuple(x for x,_ in bm)
                pairs.append((profile, a, b))
    return sorted(pairs), len(classes), raw_count


def main():
    # No smaller total of sites plus species can exhibit a reversal.
    tested = 0
    for sites in range(1, 6):
        for species in range(1, 7-sites):
            pairs, _, _ = pair_orbits(sites, species)
            assert not pairs, (sites, species, pairs)
            tested += 1

    p34, classes34, raw34 = pair_orbits(3,4)
    p43, classes43, raw43 = pair_orbits(4,3)
    expected34 = [
        ((1,1,2,2), (1,1,6,6), (1,2,3,5)),
        ((1,1,2,2), (1,1,6,6), (1,2,5,5)),
        ((1,1,2,3), (1,1,6,7), (1,2,3,7)),
    ]
    expected43 = [
        ((2,2,2), (3,3,12), (3,5,9)),
    ]
    assert p34 == expected34, (p34, expected34)
    assert p43 == expected43, (p43, expected43)
    assert (classes34, raw34, classes43, raw43) == (42, 168, 42, 400)
    # Directly check the displayed variance values of one representative per shape.
    a, b = (1,1,6,6), (1,2,3,5)
    assert [direct_moments(3,x,k) for k in (1,2) for x in (a,b)] == [
        (Fraction(2), Fraction(0)),
        (Fraction(2), Fraction(2,3)),
        (Fraction(10,3), Fraction(8,9)),
        (Fraction(10,3), Fraction(2,9))]
    a, b = (3,3,12), (3,5,9)
    assert [direct_moments(4,x,k) for k in (1,2,3) for x in (a,b)] == [
        (Fraction(3,2), Fraction(1,4)),
        (Fraction(3,2), Fraction(3,4)),
        (Fraction(5,2), Fraction(7,12)),
        (Fraction(5,2), Fraction(1,4)),
        (Fraction(3), Fraction(0)),
        (Fraction(3), Fraction(0))]
    print('VERIFY_OK smaller_shape_pairs_tested=%d small_communities_34=%d'
          ' small_communities_43=%d minimal_pair_orbits=%d' %
          (tested, classes34, classes43, len(p34)+len(p43)))


if __name__ == '__main__':
    main()
