"""Reproduce dual mutual-visibility coloring checks for 3-, 4-, and 5-cubes.

Uses exact shortest paths (all coordinate-change permutations) and an independent
restricted-graph breadth-first search. Requires only Python standard library.
"""
from collections import deque
from itertools import permutations


def geodesic_masks(d):
    """Internal vertex masks for every unordered pair in the d-cube."""
    pairs = []
    for a in range(1 << d):
        for b in range(a + 1, 1 << d):
            differences = [i for i in range(d) if (a ^ b) & (1 << i)]
            paths = set()
            for perm in permutations(differences):
                v, interior = a, 0
                for bit in perm[:-1]:
                    v ^= 1 << bit
                    interior |= 1 << v
                paths.add(interior)
            pairs.append((a, b, tuple(paths)))
    return pairs


def is_dual_from_geodesics(mask, pairs):
    for x, y, geodesics in pairs:
        if ((mask >> x) & 1) == ((mask >> y) & 1):
            if not any(interior & mask == 0 for interior in geodesics):
                return False
    return True


def is_dual_bfs(d, mask):
    """Independent shortest-path test; no geodesic enumeration."""
    vertices = 1 << d
    for a in range(vertices):
        for b in range(a + 1, vertices):
            if ((mask >> a) & 1) != ((mask >> b) & 1):
                continue
            dist = (a ^ b).bit_count()
            queue = deque([(a, 0)])
            seen = {a}
            success = False
            while queue:
                v, h = queue.popleft()
                if h >= dist:
                    if v == b:
                        success = True
                    continue
                for bit in range(d):
                    w = v ^ (1 << bit)
                    if w not in seen and (w == b or not (mask >> w) & 1):
                        seen.add(w)
                        queue.append((w, h + 1))
            if not success:
                return False
    return True


def main():
    n4 = 1 << 4
    full4 = (1 << n4) - 1
    pairs4 = geodesic_masks(4)
    solutions = []
    for mask in range(1 << n4):
        if is_dual_from_geodesics(mask, pairs4) and is_dual_from_geodesics(full4 ^ mask, pairs4):
            solutions.append(mask)
    assert len(solutions) == 24, len(solutions)
    assert 35793 in solutions
    assert all(mask.bit_count() == 8 for mask in solutions)
    for mask in solutions:
        for vertex in range(n4):
            assert ((mask >> vertex) & 1) == ((mask >> (vertex ^ 15)) & 1)
        assert is_dual_bfs(4, mask) and is_dual_bfs(4, full4 ^ mask)

    # All 24 solutions form one orbit under coordinate permutations and bit flips.
    orbit = set()
    for perm in permutations(range(4)):
        for shift in range(16):
            transformed = 0
            for v in range(16):
                if (35793 >> v) & 1:
                    w = shift
                    for src in range(4):
                        if v & (1 << src):
                            w ^= 1 << perm[src]
                    transformed |= 1 << w
            orbit.add(transformed)
    assert orbit == set(solutions)

    # Exact two-color witnesses for cubes of dimension two and three.
    for d, sample in ((2, 3), (3, 23), (4, 35793)):
        full = (1 << (1 << d)) - 1
        assert is_dual_bfs(d, sample) and is_dual_bfs(d, full ^ sample)

    # On Q5, use separate colors on the two four-dimensional faces.
    M = 35793
    full5 = (1 << 32) - 1
    four_sets = (M, full4 ^ M, M << 16, (full4 ^ M) << 16)
    assert sum(set_.bit_count() for set_ in four_sets) == 32
    assert not any(four_sets[i] & four_sets[j] for i in range(4) for j in range(i + 1, 4))
    assert sum(four_sets) == full5
    for set_ in four_sets:
        assert is_dual_bfs(5, set_)

    # A three-coloring of Q5 is impossible by the published Theorem 3.14:
    # every dual mutual-visibility set has at most 10 vertices, while 3*10 < 32.
    # The external bound is not reproduced by this finite verifier.
    print('Q4_EXHAUSTIVE_MASKS=65536')
    print('Q4_DUAL_TWO_COLORINGS_LABELED=24')
    print('Q4_UNORDERED_BIPARTITIONS=12')
    print('Q4_EACH_COLOR_SIZE=8')
    print('Q4_ANTIPODAL_AND_SINGLE_AUTOMORPHISM_ORBIT=PASS')
    print('Q2_Q3_Q4_TWO_COLOR_WITNESSES=PASS')
    print('Q5_EXPLICIT_FOUR_COLORING_INDEPENDENT_BFS=PASS')
    print('Q5_THREE_COLOR_LOWER_BOUND_USES_KORZE_VESEL_THEOREM_3_14')
    print('ALL_STANDALONE_CHECKS_PASSED')


if __name__ == '__main__':
    main()
