"""Exact finite first-order rank-four types for ordinary and twisted circular ladders.

Only the Python standard library is required. The recurrence models all quantifier
prefixes (not only existential sentences) and retains equality/repeated choices.
"""
from functools import lru_cache


def ladder(n, twist):
    assert n >= 3
    size = 2 * n
    neighbours = [0] * size

    def edge(i, j):
        neighbours[i] |= 1 << j
        neighbours[j] |= 1 << i

    for i in range(n):
        edge(2*i, 2*i+1)
        for layer in (0, 1):
            if i+1 < n:
                edge(2*i+layer, 2*(i+1)+layer)
            else:
                edge(2*i+layer, 1-layer if twist else layer)
    assert all(x.bit_count() == 3 for x in neighbours)
    return tuple(neighbours)


def rank_four_type(neighbours):
    """Full rank-4 theory via T_0=atomic and T_{j+1}=atomic+extension types.

    Vertices in three-variable tuples may coincide; the extra vertex may also
    repeat one of them. Therefore no injectivity assumption enters the logic.
    """
    size = len(neighbours)
    universe = (1 << size) - 1

    @lru_cache(None)
    def triple_rank_one(a, b, c):
        selected = (a, b, c)
        ns = (neighbours[a], neighbours[b], neighbours[c])
        atomic = (int(a == b) | (int(a == c) << 1)
                  | (int(b == c) << 2)
                  | (int(bool(ns[0] & (1 << b))) << 3)
                  | (int(bool(ns[0] & (1 << c))) << 4)
                  | (int(bool(ns[1] & (1 << c))) << 5))
        used = (1 << a) | (1 << b) | (1 << c)
        extensions = 0
        # New fourth vertex: its 3-bit adjacency pattern to a,b,c.
        for pattern in range(8):
            candidates = universe & ~used
            for pos, mask in enumerate(ns):
                candidates &= mask if (pattern >> pos) & 1 else universe ^ mask
            if candidates:
                extensions |= 1 << pattern
        # Old fourth vertex: explicitly retain equality with each marked place.
        for x in set(selected):
            equality = sum(1 << i for i,v in enumerate(selected) if v == x)
            adjacency = sum(1 << i for i,v in enumerate(selected)
                            if (neighbours[x] >> v) & 1)
            extensions |= 1 << ((equality << 3) | adjacency)
        return atomic, extensions

    @lru_cache(None)
    def pair_rank_two(a, b):
        return (int(a == b), int(bool(neighbours[a] & (1 << b))),
                frozenset(triple_rank_one(a,b,c) for c in range(size)))

    def singleton_rank_three(a):
        return frozenset(pair_rank_two(a,b) for b in range(size))

    return frozenset(singleton_rank_three(a) for a in range(size))


def main():
    seen = {}
    small = {}
    for n in range(3, 17):
        for twist in (False, True):
            family = 'twisted' if twist else 'ordinary'
            structure = rank_four_type(ladder(n, twist))
            seen[(family,n)] = structure
            if n <= 8:
                small[(family,n)] = structure
    stable = seen['ordinary',9]
    assert seen['twisted',9] == stable
    assert len(set(small.values())) == 12
    assert all(t != stable for t in small.values())
    assert len(set(seen.values())) == 13
    for key, t in seen.items():
        if key[1] >= 9:
            assert t == stable, key
    print('EXACT_SMALL_CENSUS_OK initial_graphs=28 classes=13 isolated_small_classes=12')
    print('SHARP_THRESHOLD_OK first_stable_rungs=9 least_largest_representative=18')
    # Additional observations at lengths beyond the finite base interval.
    for n in (17,18,19,20,21,22,23,24):
        for twist in (False,True):
            assert rank_four_type(ladder(n,twist)) == stable, (n,twist)
    print('SUPPLEMENTAL_STABILITY_OK rung_counts=17..24 both_twists')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
