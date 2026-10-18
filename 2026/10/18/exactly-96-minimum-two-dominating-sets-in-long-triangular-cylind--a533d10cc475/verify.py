"""Independent checks for the exact minimum two-domination profiles of C_3 square P_n.

Run with Python 3.9+ as ``python verify.py``.  All computations use integers.
"""
from itertools import combinations, permutations, product

COLORS = (0, 1, 2)
FULL = 7


def bitcount(mask):
    return mask.bit_count()


def local_valid(left, center, right):
    """Verify two-domination in the central K_3 column."""
    for color in COLORS:
        bit = 1 << color
        if center & bit:
            continue
        vertical_neighbors = bitcount(center)
        horizontal_neighbors = bool(left & bit) + bool(right & bit)
        if vertical_neighbors + horizontal_neighbors < 2:
            return False
    return True


def valid(layers):
    return all(local_valid(layers[j - 1] if j else 0,
                           layers[j],
                           layers[j + 1] if j + 1 < len(layers) else 0)
               for j in range(len(layers)))


def dp_optimum(n):
    """Two-column min-plus/counting dynamic program over all 8 K_3 masks."""
    states = {(0, b): (bitcount(b), 1) for b in range(8)}
    for _ in range(1, n):
        new_states = {}
        for (a, b), (cost, ways) in states.items():
            for c in range(8):
                if not local_valid(a, b, c):
                    continue
                k = (b, c)
                nc = cost + bitcount(c)
                if k not in new_states or nc < new_states[k][0]:
                    new_states[k] = (nc, ways)
                elif nc == new_states[k][0]:
                    new_states[k] = (nc, new_states[k][1] + ways)
        states = new_states
    feasible = [(cost, ways) for (a, b), (cost, ways) in states.items()
                if local_valid(a, b, 0)]
    optimum = min(cost for cost, ways in feasible)
    return optimum, sum(ways for cost, ways in feasible if cost == optimum)


def minimum_structures(n):
    """Generate only the four proved boundary profiles (n >= 7)."""
    assert n >= 7
    for a, b in product((0, 1), (n - 2, n - 1)):
        # indices a,b are the only two double columns
        mid_positions = list(range(a + 1, b))
        L = len(mid_positions)
        assert L >= 3
        for rainbow in permutations(COLORS):
            singles = [rainbow[j % 3] for j in range(L)]
            for lo_side, hi_side in product((0, 1), repeat=2):
                layers = [None] * n
                for j, col in zip(mid_positions, singles):
                    layers[j] = 1 << col
                # For the first core vertex, its second core neighbor
                # covers one missing color; the left double must cover the third.
                third_left = next(x for x in COLORS if x not in singles[:2])
                opt_left = (singles[0], singles[1])
                layers[a] = (1 << third_left) | (1 << opt_left[lo_side])
                if a == 1:
                    layers[0] = FULL ^ layers[1]
                third_right = next(x for x in COLORS if x not in singles[-2:])
                opt_right = (singles[-2], singles[-1])
                layers[b] = (1 << third_right) | (1 << opt_right[hi_side])
                if b == n - 2:
                    layers[n - 1] = FULL ^ layers[n - 2]
                assert all(mask is not None for mask in layers)
                yield (a, b), tuple(layers)


def direct_mask_valid(mask, n):
    for j in range(n):
        for i in COLORS:
            v = j * 3 + i
            if mask >> v & 1:
                continue
            count = sum(bool(mask >> (3*j + q) & 1) for q in COLORS if q != i)
            if j > 0:
                count += bool(mask >> (3 * (j - 1) + i) & 1)
            if j + 1 < n:
                count += bool(mask >> (3 * (j + 1) + i) & 1)
            if count < 2:
                return False
    return True


def brute_optimum(n):
    """Independent direct graph-neighborhood enumeration, small n only."""
    universe = range(3*n)
    for k in range(3*n + 1):
        count = 0
        for vertices in combinations(universe, k):
            bitset = sum(1 << v for v in vertices)
            count += direct_mask_valid(bitset, n)
        if count:
            return (k, count)
    raise AssertionError('no two-dominating set')


def main():
    for n in range(1, 8):
        expected = ((2, 3), (3, 6), (4, 3),
                    (6, 78), (7, 99), (8, 99), (9, 96))[n - 1]
        assert dp_optimum(n) == expected, (n, dp_optimum(n), expected)
    for n in range(2, 8):
        assert brute_optimum(n) == dp_optimum(n), n
    for n in range(7, 201):
        optimum, count = dp_optimum(n)
        assert (optimum, count) == (n+2, 96), (n, optimum, count)
        if n <= 40 or n in (100, 150, 200):
            structures = list(minimum_structures(n))
            assert len(structures) == 96
            assert len({layers for p, layers in structures}) == 96
            for p, layers in structures:
                assert sum(bitcount(mask) for mask in layers) == n + 2
                assert valid(layers)
                assert tuple(j for j, mask in enumerate(layers) if bitcount(mask) == 2) == p
    print('VERIFIED: direct exhaustive n=2..7, exact mask DP n=1..200,')
    print('          boundary constructions n=7..40,100,150,200; 96 per n>=7.')


if __name__ == '__main__':
    main()
