#!/usr/bin/env python3
"""Finite independent checks for equivalence-relation type profiles.

No third-party packages required. Execute with Python 3.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product
from math import factorial

@lru_cache(None)
def integer_partitions(n, upper=None):
    if upper is None:
        upper = n
    if n == 0:
        return ((),)
    return tuple((j,) + rest for j in range(min(upper, n), 0, -1)
                 for rest in integer_partitions(n-j, j))


def class_labels(parts):
    labels = []
    for label, size in enumerate(parts):
        labels.extend([label] * size)
    return tuple(labels)


def injective_signature(labels, tuple_values):
    return tuple(labels[tuple_values[i]] == labels[tuple_values[j]]
                 for i in range(len(tuple_values))
                 for j in range(i+1, len(tuple_values)))


def full_signature(labels, tuple_values):
    k = len(tuple_values)
    return tuple((tuple_values[i] == tuple_values[j],
                  labels[tuple_values[i]] == labels[tuple_values[j]])
                 for i in range(k) for j in range(i+1, k))


def direct_injective_profile(parts, r):
    labels = class_labels(parts)
    n = len(labels)
    if r > n:
        return 0
    return len({injective_signature(labels, vals)
                for vals in permutations(range(n), r)})


def direct_qf_types(parts, k):
    labels = class_labels(parts)
    return len({full_signature(labels, vals)
                for vals in product(range(len(labels)), repeat=k)})


def labelled_partition_count(parts):
    n = sum(parts)
    denom = 1
    for s in parts:
        denom *= factorial(s)
    for count in Counter(parts).values():
        denom *= factorial(count)
    assert factorial(n) % denom == 0
    return factorial(n) // denom


def fits(capacities, demanded):
    return len(demanded) <= len(capacities) and all(
        a <= b for a, b in zip(demanded, capacities))


def formula_injective_profile(parts, r):
    return sum(labelled_partition_count(mu)
               for mu in integer_partitions(r)
               if fits(parts, mu))


def unlabeled_profile(parts, r):
    return sum(1 for mu in integer_partitions(r) if fits(parts, mu))


def stirling_row(k):
    prev = [1]
    for m in range(1, k+1):
        cur = [0]*(m+1)
        for j, value in enumerate(prev):
            cur[j] += j*value
            cur[j+1] += value
        prev = cur
    return prev


def type_count_formula(parts, k):
    n = sum(parts)
    return sum(stirling_row(k)[r] * formula_injective_profile(parts, r)
               for r in range(1, min(n, k)+1)) if k else 1


def run():
    injector_cases = 0
    direct_tuple_assignments = 0
    nprofiles = 0
    for n in range(1, 8):
        for parts in integer_partitions(n):
            nprofiles += 1
            for r in range(1, n+1):
                got = direct_injective_profile(parts, r)
                expected = formula_injective_profile(parts, r)
                assert got == expected, (parts, r, got, expected)
                injector_cases += 1
            for k in range(1, min(5, n+1)+1):
                got = direct_qf_types(parts, k)
                expected = type_count_formula(parts, k)
                assert got == expected, (parts, k, got, expected)
                direct_tuple_assignments += n**k

    for n in range(1, 6):
        labelled_profiles = defaultdict(list)
        unlabeled_profiles = defaultdict(list)
        for parts in integer_partitions(n):
            lb = tuple(formula_injective_profile(parts, r) for r in range(1, n+1))
            ub = tuple(unlabeled_profile(parts, r) for r in range(1, n+1))
            labelled_profiles[lb].append(parts)
            unlabeled_profiles[ub].append(parts)
        def nontrivial_collision(groups):
            return [set(v) for v in groups.values()
                    if len([p for p in v if p not in ((n,), (1,)*n)]) >= 2]
        nc = nontrivial_collision(labelled_profiles)
        if n < 5:
            assert not nc, (n, nc)
        else:
            assert nc == [{(3,2), (2,1,1,1)}], (n, nc)
        if n == 4:
            assert {(3,1), (2,1,1)} in nontrivial_collision(unlabeled_profiles)

    A = (3, 2)
    B = (2, 1, 1, 1)
    expected = (1, 2, 4, 7, 10)
    assert tuple(formula_injective_profile(A, r) for r in range(1, 6)) == expected
    assert tuple(formula_injective_profile(B, r) for r in range(1, 6)) == expected
    assert tuple(type_count_formula(A, k) for k in range(1, 6)) == (1,3,11,46,211)
    for k in range(1, 8):
        assert direct_qf_types(A, k) == direct_qf_types(B, k) == type_count_formula(A, k)
        direct_tuple_assignments += 2*(5**k)
    assert unlabeled_profile(A, 3) == unlabeled_profile(B, 3) == 2
    assert unlabeled_profile(A, 4) == unlabeled_profile(B, 4) == 2
    print('VERIFY_OK partitions_tested=%d injective_profile_checks=%d '
          'direct_tuple_assignments=%d first_nondegenerate_labeled_collision=n5 '
          'first_nondegenerate_unlabeled_collision=n4 n5_injective_profile=%s'
          % (nprofiles, injector_cases, direct_tuple_assignments, expected))

if __name__ == '__main__':
    run()
