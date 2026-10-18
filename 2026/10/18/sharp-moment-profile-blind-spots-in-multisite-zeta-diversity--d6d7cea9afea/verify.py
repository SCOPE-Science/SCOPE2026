"""Exact finite checks for an incidence-sampling moment inversion theorem.

Run with Python 3.10 or later; standard library only.
"""
import itertools
import json
from collections import defaultdict
from fractions import Fraction
from math import comb


def sites_of_species(sites, species):
    n = len(sites)
    return tuple(sum(1 << j for j, mask in enumerate(sites) if mask & (1 << i))
                 for i in range(species))


def sample_shared_counts(sites, species, k):
    all_sites = range(len(sites))
    return tuple(sum(all(sites[j] & (1 << i) for j in chosen)
                     for i in range(species))
                 for chosen in itertools.combinations(all_sites, k))


def spectrum(sites, species, r):
    n = len(sites)
    occ = sites_of_species(sites, species)
    h = [0] * (n + 1)
    for choice in itertools.combinations(occ, r):
        common = (1 << n) - 1
        for mask in choice:
            common &= mask
        h[common.bit_count()] += 1
    return tuple(h)


def inferred_spectrum(sites, species, r):
    n = len(sites)
    f = []
    for k in range(n + 1):
        samples = sample_shared_counts(sites, species, k)
        f.append(sum(comb(z, r) if z >= r else 0 for z in samples))
    # f[k] = binom(n,k) * E[binom(Z_k,r)].
    h = [sum((-1) ** (k - t) * comb(k, t) * f[k]
             for k in range(t, n + 1)) for t in range(n + 1)]
    return tuple(h)


def profile(sites, species):
    n = len(sites)
    return tuple((sum(zs), sum(z*z for z in zs))
                 for k in range(1, n + 1)
                 for zs in [sample_shared_counts(sites, species, k)])


def laws(sites, species):
    return tuple(tuple(sorted(sample_shared_counts(sites, species, k)))
                 for k in range(1, len(sites) + 1))


def witness_report(sites, species):
    n = len(sites)
    return {
        'site_bitmasks': list(sites),
        'zeta_sample_values': [list(sample_shared_counts(sites, species, k))
                               for k in range(1, n + 1)],
        'mean': [str(Fraction(sum(sample_shared_counts(sites, species, k)), comb(n,k)))
                 for k in range(1, n+1)],
        'second_moment': [str(Fraction(sum(z*z for z in sample_shared_counts(sites, species, k)), comb(n,k)))
                          for k in range(1,n+1)],
        'third_factorial_moment_at_one_site': str(Fraction(sum(comb(z,3) if z>=3 else 0 for z in sample_shared_counts(sites,species,1)), n)),
    }


def main():
    checked_inversions = 0
    for species in range(1, 6):
        n = 3
        for sites in itertools.product(range(1 << species), repeat=n):
            if (sites[0] | sites[1] | sites[2]) != (1 << species) - 1:
                continue
            for r in range(1, species + 1):
                assert inferred_spectrum(sites, species, r) == spectrum(sites, species, r)
                checked_inversions += 1

    checked_small = 0
    classes = 0
    for species in range(1, 5):
        by_signature = {}
        for sites in itertools.product(range(1 << species), repeat=3):
            if (sites[0] | sites[1] | sites[2]) != (1 << species) - 1:
                continue
            key = profile(sites, species)
            value = laws(sites, species)
            if key in by_signature:
                assert by_signature[key] == value, (species, sites, key)
            else:
                by_signature[key] = value
            checked_small += 1
        classes += len(by_signature)

    # Smallest-site witness (three sites and five species).
    u = (0, 7, 25)
    v = (1, 1, 30)
    assert profile(u, 5) == profile(v, 5)
    assert laws(u, 5) != laws(v, 5)
    assert spectrum(u, 5, 1) == spectrum(v, 5, 1)
    assert spectrum(u, 5, 2) == spectrum(v, 5, 2)
    assert spectrum(u, 5, 3) != spectrum(v, 5, 3)
    # Fewest-species witness (four sites and three species).
    a = (7, 1, 2, 4)
    b = (5, 3, 6, 0)
    assert profile(a, 3) == profile(b, 3)
    assert laws(a, 3) != laws(b, 3)
    assert spectrum(a, 3, 1) == spectrum(b, 3, 1)
    assert spectrum(a, 3, 2) == spectrum(b, 3, 2)
    assert spectrum(a, 3, 3) != spectrum(b, 3, 3)

    # Exact combinatorial certificate for three unordered values in [0,4].
    coll = defaultdict(list)
    for tr in itertools.combinations_with_replacement(range(5), 3):
        coll[(sum(tr), sum(z*z for z in tr))].append(tr)
    collisions = [v for v in coll.values() if len(v) > 1]
    assert collisions == [[(0,3,3),(1,1,4)]]

    result = {
        'algorithm': 'exact integer exhaustive incidence enumeration; rational moments',
        'max_incidence_sites': 3,
        'max_incidence_species_for_inversion': 5,
        'inversion_instances': checked_inversions,
        'small_species_cases': checked_small,
        'small_species_distinct_moment_profiles': classes,
        'integer_triple_profiles_tested': 35,
        'integer_triple_collisions': [[[0,3,3],[1,1,4]]],
        'three_site_five_species_witness': [witness_report(u,5), witness_report(v,5)],
        'four_site_three_species_witness': [witness_report(a,3), witness_report(b,3)],
        'status': 'PASS',
    }
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
