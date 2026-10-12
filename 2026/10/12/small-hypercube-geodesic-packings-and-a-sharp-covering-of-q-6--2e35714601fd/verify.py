#!/usr/bin/env python3
"""Exact small-cube geodesic packing and covering checks; Python standard library only."""
from itertools import permutations, combinations

PACK4 = ((0, 1, 3, 7, 15), (13, 5, 4, 6, 2))
PACK5 = (
    (1, 0, 4, 6, 22, 30),
    (2, 18, 16, 24, 28, 29),
    (5, 13, 15, 31, 27, 26),
    (11, 3, 7, 23, 21, 20),
    (14, 12, 8, 9, 25, 17),
)
PACK6 = (
    (0, 1, 3, 7, 15, 31, 63),
    (4, 6, 2, 34, 42, 43, 59),
    (17, 16, 20, 52, 60, 62, 46),
    (5, 13, 9, 8, 24, 56, 58),
    (23, 21, 29, 61, 45, 44, 40),
    (25, 57, 41, 33, 32, 36, 38),
    (12, 14, 10, 11, 27, 19, 51),
    (28, 30, 22, 54, 55, 39, 35),
    (26, 18, 50, 48, 49, 53, 37),
)

def power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0

def check_path(path, d):
    assert len(path) == d + 1
    assert len(set(path)) == d + 1
    assert all(0 <= v < (1 << d) for v in path)
    assert path[0] ^ path[-1] == (1 << d) - 1
    flips = [path[i] ^ path[i + 1] for i in range(d)]
    assert all(power_of_two(x) for x in flips)
    assert len(set(flips)) == d

def check_pack(paths, d):
    all_vertices = []
    for path in paths:
        check_path(path, d)
        all_vertices.extend(path)
    assert len(all_vertices) == len(set(all_vertices))
    return sorted(set(range(1 << d)) - set(all_vertices))

def path_mask(path):
    return sum(1 << v for v in path)

def paths_by_permutation(d):
    masks = set()
    for start in range(1 << d):
        for perm in permutations(range(d)):
            v = start
            mask = 1 << v
            for j in perm:
                v ^= 1 << j
                mask |= 1 << v
            masks.add(mask)
    return masks

def paths_by_induced_subsets_4():
    answer = set()
    for subset in combinations(range(16), 5):
        deg = [sum(power_of_two(u ^ v) for v in subset if u != v) for u in subset]
        if sorted(deg) != [1, 1, 2, 2, 2]:
            continue
        ends = [u for u, degree in zip(subset, deg) if degree == 1]
        if ends[0] ^ ends[1] == 15:
            answer.add(path_mask(subset))
    return answer

def main():
    a = paths_by_permutation(4)
    b = paths_by_induced_subsets_4()
    assert a == b
    assert len(a) == 192
    canon = path_mask((0, 1, 3, 7, 15))
    compat = sorted(x for x in a if x & canon == 0)
    assert len(compat) == 31
    assert all(x & y for i, x in enumerate(compat) for y in compat[i+1:])
    pair_count = sum(1 for x, y in combinations(a, 2) if x & y == 0)
    assert pair_count == 2976
    # Stronger direct check beyond symmetry-based argument.
    assert not any(x & y == 0 and x & z == 0 and y & z == 0
                   for i, x in enumerate(sorted(a))
                   for j, y in enumerate(sorted(a)[i + 1:], i + 1)
                   for z in sorted(a)[j + 1:])
    print('Q4 paths=192, compatible-with-canonical=31, pairs=2976, triples=0')
    for d, ps, required in [(4, PACK4, 2), (5, PACK5, 5), (6, PACK6, 9)]:
        assert len(ps) == required
        rem = check_pack(ps, d)
        print(f'Q{d} disjoint geodesics={len(ps)} uncovered={rem}')
    uncovered6 = check_pack(PACK6, 6)
    assert uncovered6 == [47]
    extra = [47]
    for j in range(6):
        extra.append(extra[-1] ^ (1 << j))
    check_path(extra, 6)
    assert len(set(sum((list(p) for p in PACK6), []) + extra)) == 64
    print('Q6 geodesic cover=10, lower bound ceil(64/7)=10')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
