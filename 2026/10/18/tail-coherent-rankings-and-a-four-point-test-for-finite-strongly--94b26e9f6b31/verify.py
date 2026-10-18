"""Reproduce the exact finite census of coherent centered selection rankings.

Uses only the Python standard library. Run: python verify.py
"""
from itertools import permutations, product
from math import factorial


def rank_orders(n):
    return [[(w,) + p for p in permutations(i for i in range(n) if i != w)]
            for w in range(n)]


def four_point(profile):
    n = len(profile)
    positions = [{v: k for k, v in enumerate(row)} for row in profile]
    for w, row in enumerate(profile):
        for j in range(1, n - 2):
            u = row[j]
            pu = positions[u]
            for i in range(j + 1, n):
                for k in range(i + 1, n):
                    if pu[row[i]] > pu[row[k]]:
                        return False
    return True


def select(profile, w, A):
    return next(v for v in profile[w] if A & (1 << v))


def dense_from_definition(profile):
    n = len(profile)
    for w in range(n):
        for A in range(1, 1 << n):
            u = select(profile, w, A)
            C = A
            while C:
                if select(profile, w, C) != select(profile, u, C):
                    return False
                C = (C - 1) & A
    return True


def relabel(profile, permutation):
    n = len(profile)
    result = [None] * n
    for w, row in enumerate(profile):
        result[permutation[w]] = tuple(permutation[x] for x in row)
    return tuple(result)


def enumerate_valid(n):
    rows = rank_orders(n)
    fixed = rows[0][0]
    assert fixed == tuple(range(n))
    canonical = []
    for remainder in product(*rows[1:]):
        profile = (fixed,) + remainder
        if four_point(profile):
            canonical.append(profile)
            assert dense_from_definition(profile)
    # Every initial row is obtained exactly once by permuting the n-1
    # labels other than 0; relabeling expands canonical representatives.
    perms_fix0 = [(0,) + p for p in permutations(range(1, n))]
    valid = {relabel(profile, perm)
             for profile in canonical for perm in perms_fix0}
    assert len(valid) == len(canonical) * factorial(n - 1)
    return valid


def orbit_sizes(valid, n):
    unvisited = set(valid)
    group = list(permutations(range(n)))
    sizes = []
    while unvisited:
        profile = unvisited.pop()
        orbit = {relabel(profile, p) for p in group}
        assert orbit <= valid
        unvisited.difference_update(orbit)
        sizes.append(len(orbit))
    return sorted(sizes)


def main():
    expected = {1: (1, 1), 2: (1, 1), 3: (8, 2),
                4: (138, 7), 5: (3984, 34)}
    for n, (count, orbit_count) in expected.items():
        valid = enumerate_valid(n)
        sizes = orbit_sizes(valid, n)
        assert len(valid) == count, (n, len(valid), count)
        assert len(sizes) == orbit_count, (n, len(sizes), orbit_count)
        print(f"worlds={n}, labelled={len(valid)}, isomorphism_classes={len(sizes)}")
    # Exhaustive check of equivalence of the local test with the original
    # subset-based density axiom, independently for all ranking profiles.
    for n in (1, 2, 3, 4):
        rows = rank_orders(n)
        for profile in product(*rows):
            assert four_point(profile) == dense_from_definition(profile)
    print("VERIFY_OK")


if __name__ == '__main__':
    main()
