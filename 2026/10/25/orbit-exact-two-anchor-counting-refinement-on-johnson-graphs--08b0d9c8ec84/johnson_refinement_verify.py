"""Reproducibility checks for two individually coloured vertices of Johnson graphs.

No third-party packages are used. Run: python johnson_refinement_verify.py
"""
from collections import Counter
from itertools import combinations
from math import comb


def coefficient(sizes, weight):
    coeffs = [1] + [0] * weight
    for size in sizes:
        nxt = [0] * (weight + 1)
        for j, v in enumerate(coeffs):
            if v:
                for z in range(min(size, weight - j) + 1):
                    nxt[j + z] += v
        coeffs = nxt
    return coeffs[weight]


def one_case(n, k, r):
    points = list(combinations(range(n), k))
    where = {p: i for i, p in enumerate(points)}
    A = set(range(k))
    B = set(range(k - r)) | set(range(k, k + r))
    C, P, Q, D = A & B, A - B, B - A, set(range(n)) - (A | B)
    csize = len(C)
    dsize = len(D)

    neighbors = []
    for vertex in points:
        s = set(vertex)
        row = [where[tuple(sorted((s - {i}) | {j}))]
               for i in vertex for j in range(n) if j not in s]
        assert len(row) == k * (n - k) and len(set(row)) == len(row)
        neighbors.append(row)

    signatures = []
    for vertex in points:
        v = set(vertex)
        a, b, c, d = (len(v & part) for part in (C, P, Q, D))
        s = (a, b, c, d)
        if n == 2 * k:
            flip = (csize - d, r - c, r - b, csize - a)
            s = min(s, flip)
        signatures.append(s)

    init = [2] * len(points)
    init[where[tuple(sorted(A))]] = 0
    init[where[tuple(sorted(B))]] = 1
    colors = init
    rounds = 0
    while True:
        # Canonical renaming is immaterial: old colours are kept in every signature.
        names = {}
        updated = []
        for i, row in enumerate(neighbors):
            description = (colors[i], tuple(sorted(Counter(colors[v] for v in row).items())))
            if description not in names:
                names[description] = len(names)
            updated.append(names[description])
        if len(set(updated)) == len(set(colors)):
            break
        colors = updated
        rounds += 1
        assert rounds <= k + 1, ('round bound', n, k, r)

    color_to_profile, profile_to_color = {}, {}
    for color, profile in zip(colors, signatures):
        assert color_to_profile.setdefault(color, profile) == profile
        assert profile_to_color.setdefault(profile, color) == color

    block_profiles = coefficient([csize, r, r, dsize], k)
    predicted = block_profiles if n != 2 * k else (block_profiles + (csize + 1) * (r + 1)) // 2
    assert len(color_to_profile) == predicted, ('orbit count', n, k, r)

    # Directly check the two distinguishing neighbour counts and their difference.
    for i, vertex in enumerate(points):
        v = set(vertex)
        x, y = len(v & A), len(v & B)
        a, d = len(v & C), len(v & D)
        plus = sum(len(set(points[j]) & A) == x + 1 and
                   len(set(points[j]) & B) == y + 1 for j in neighbors[i])
        minus = sum(len(set(points[j]) & A) == x - 1 and
                    len(set(points[j]) & B) == y - 1 for j in neighbors[i])
        assert plus == d * (csize - a)
        assert minus == a * (dsize - d)
        assert plus - minus == (k - x - y) * csize + (2 * k - n) * a
    return len(points), len(color_to_profile), rounds


def main():
    cases, vertices = 0, 0
    max_rounds = 0
    for n in range(2, 13):
        for k in range(1, n // 2 + 1):
            for r in range(1, k + 1):
                count, orbits, steps = one_case(n, k, r)
                cases += 1
                vertices += count
                max_rounds = max(max_rounds, steps)
    print('FULL_CHECKS_PASS')
    print('parameter_cases:', cases)
    print('total_vertex_instances:', vertices)
    print('maximum_proper_refinement_rounds:', max_rounds)
    for n,k,r in ((4,2,1),(6,3,1),(7,3,1),(8,4,2),(9,4,2),(10,5,3),(12,6,3)):
        count, orbits, steps = one_case(n,k,r)
        print('sample', n,k,r,'vertices',count,'orbits',orbits,'rounds',steps)

if __name__ == '__main__':
    main()
