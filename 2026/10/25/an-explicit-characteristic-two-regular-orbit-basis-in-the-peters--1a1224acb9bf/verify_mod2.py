"""Exact, standalone forest-complex character calculation for KG(5,2).

Usage: python3 verify.py
Requires only the Python standard library.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations

LABELS = tuple(range(5))
VERTICES = tuple(combinations(LABELS, 2))
VINDEX = {u: i for i, u in enumerate(VERTICES)}
EDGES = tuple((u, v) for u in range(10) for v in range(u + 1, 10)
              if not set(VERTICES[u]).intersection(VERTICES[v]))
EINDEX = {e: i for i, e in enumerate(EDGES)}
assert (len(VERTICES), len(EDGES)) == (10, 15)


def is_forest(mask):
    parent = list(range(10))

    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i

    for j, (u, v) in enumerate(EDGES):
        if mask & (1 << j):
            ru, rv = root(u), root(v)
            if ru == rv:
                return False
            parent[ru] = rv
    return True


FOREST = bytearray(is_forest(i) for i in range(1 << 15))
EXPECTED_F = (1, 15, 105, 455, 1365, 2991, 4875, 5805, 4680, 2000)
f = tuple(sum(bool(FOREST[m]) for m in range(1 << 15) if m.bit_count() == k)
          for k in range(10))
assert f == EXPECTED_F
assert -sum(((-1) ** k) * n for k, n in enumerate(f)) == 240


def cycle_type(p):
    visited = set()
    lengths = []
    for i in range(5):
        if i not in visited:
            t = i
            length = 0
            while t not in visited:
                visited.add(t)
                length += 1
                t = p[t]
            lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def edge_action(p):
    vertex_action = tuple(VINDEX[tuple(sorted((p[a], p[b])))]
                          for a, b in VERTICES)
    action = tuple(EINDEX[tuple(sorted((vertex_action[u], vertex_action[v])))]
                   for u, v in EDGES)
    assert sorted(action) == list(range(15))
    return action


def edge_orbits(action):
    visited = set()
    orbits = []
    for j in range(15):
        if j not in visited:
            orbit = []
            t = j
            while t not in visited:
                visited.add(t)
                orbit.append(t)
                t = action[t]
            orbits.append(tuple(orbit))
    return orbits


def orbit_polynomial(action):
    orbits = edge_orbits(action)
    orbit_mask = tuple(sum(1 << e for e in orbit) for orbit in orbits)
    counts = [0] * (len(orbits) + 1)
    for chosen in range(1 << len(orbits)):
        m = 0
        for j, mask in enumerate(orbit_mask):
            if chosen & (1 << j):
                m |= mask
        if FOREST[m]:
            counts[chosen.bit_count()] += 1
    return tuple(counts)



# Each hexadecimal integer is the coefficient bit-vector of a top cycle.
# Bit j is the lexicographically j-th nine-edge spanning forest.
SEED_HEX = (
    "dbb9ea001adaf5b6d603d46db660b5bd3457b67bcba4bd9c197bd61deb3634ddb8586000cd582d4d5686eab867b61d67b21b375a0e86c0b80d4076d0ed6050f906c1751191b3bc8d6cb85b1216dc36724b85704775a36ccca19776c330337a8af667c6b72a30f0022d9d5c75cbb451d0589da18acaead5a31b77789d6d0036a3c91d9f0b40e26f28c2e86f96db718aa6db7b6ce6b65168cd80c56181b379f60dc5fa28c2d6385b75644504a35406e40c500290becd452da8b8db40c0078f2e5bb0709ad07b2954e903e6610c42b06bb3310ce8c30a3988568db966c7b4cd8cbbc87e37ab1ac4c919ec0c05d2b1a31735967585d5c96977cc973",
    "770d9b0c3ae21b367e16d16e7b6747ef199d03c00a760167d9eafea28f35a1bb9c230d44e204d08cdf4ab9a21ba1b1081e47087cb62fa22aed0cf0c0c22140badb8b703c8817cceba9dba7d1278abfd6ef180b961a80fc77db3561bd546cf16d113b9b5165fec3095cdabbee868d83f608132508a30df3c579cd7482bff4ce8b8fb68fc3656ed1a842643daa7b662201a1a9c7c1b229c3519d16d16b0dbcf5b5003d0dbd150144099b6e4c7824aa46de5ee7339078a03f412320b94dcdc59c4ec7d3cf9a876ef0c96105e60a2599f19f66d8c3586d7a2f963786d3c1ea039e314eeb8b3f64c379079984c0ada8c33a0635ca043f7367bd3cbd13",
)


def rank_mod_two(rows):
    pivots = {}
    for row in rows:
        while row:
            j = row.bit_length() - 1
            if j not in pivots:
                pivots[j] = row
                break
            row ^= pivots[j]
    return len(pivots)


def main():
    top = [m for m, ok in enumerate(FOREST) if ok and m.bit_count() == 9]
    low = {m: 0 for m, ok in enumerate(FOREST) if ok and m.bit_count() == 8}
    assert (len(top), len(low)) == (2000, 4680)
    ti = {m: i for i, m in enumerate(top)}
    for col, mask in enumerate(top):
        for j in range(15):
            if mask & (1 << j):
                low[mask ^ (1 << j)] ^= 1 << col
    b2rank = rank_mod_two(low.values())
    assert b2rank == 1760
    nullity = len(top) - b2rank
    assert nullity == 240

    seeds = [int(h, 16) for h in SEED_HEX]
    for seed in seeds:
        assert seed.bit_length() <= len(top)
        assert all((row & seed).bit_count() % 2 == 0 for row in low.values())
    orbit_columns = []
    for seed in seeds:
        active = [i for i in range(len(top)) if (seed >> i) & 1]
        for p in permutations(LABELS):
            edge_perm = edge_action(p)
            permuted_mask = lambda m: sum(1 << edge_perm[j] for j in range(15) if m & (1 << j))
            action_column = sum(1 << ti[permuted_mask(top[j])] for j in active)
            assert all((row & action_column).bit_count() % 2 == 0 for row in low.values())
            orbit_columns.append(action_column)
    assert len(orbit_columns) == 240
    orb_rank = rank_mod_two(orbit_columns)
    assert orb_rank == 240
    print('GRAPH_VERTICES_EDGES', len(VERTICES), len(EDGES))
    print('TOP_FACES_LOWER_FACES', len(top), len(low))
    print('TOP_BOUNDARY_RANK_MOD2', b2rank, 'H8_DIM_MOD2', nullity)
    print('EXPLICIT_SEED_SUPPORT_SIZES', *(s.bit_count() for s in seeds))
    print('TWO_120_ELEMENT_SYMMETRY_ORBITS_RANK_MOD2', orb_rank)
    print('H8_MOD2_TWO_FREE_REGULAR_F2_S5_MODULES')
    print('VERIFY_OK_PETERSEN_FOREST_COMPLEX_MOD2_REGULAR_ORBIT_BASIS')

if __name__ == '__main__':
    main()
