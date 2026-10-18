"""Independent finite checks for strong-majority colorings of Boolean cubes.

Run: python3 verify_cube_majority.py
No third-party packages are required. The infinite-dimensional results
are proved mathematically; these checks test explicit constructions and
small finite certificates.
"""
from itertools import combinations


def parity(x):
    return x.bit_count() % 2


def synd2(x, columns):
    s = 0
    for j, a in enumerate(columns):
        if x & (1 << j):
            s ^= a
    return s


def coloring(d):
    if d % 2 == 0:
        return [parity(v & ((1 << (d // 2)) - 1)) for v in range(1 << d)], 2
    if d == 3:
        col = (1, 2, 3)
        return [synd2(v, col) for v in range(1 << d)], 4
    if d == 5:
        col = (1, 1, 2, 2, 3)
        return [synd2(v, col) for v in range(1 << d)], 4
    if d >= 7 and d % 2:
        columns = tuple(range(1, 8))
        shift = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2}
        if d == 7:
            return [shift[synd2(v, columns)] for v in range(128)], 3
        prev, _ = coloring(d - 2)
        mask = (1 << (d - 2)) - 1
        return [(prev[v & mask] + ((v >> (d - 1)) & 1)) % 3 for v in range(1 << d)], 3
    raise ValueError('Only dimensions d >= 2 are supported')


def validate(d):
    colors, count = coloring(d)
    assert len(colors) == 1 << d
    assert set(colors) == set(range(count))
    for x in range(1 << d):
        neighbor_counts = [0] * count
        for j in range(d):
            neighbor_counts[colors[x ^ (1 << j)]] += 1
        assert max(neighbor_counts) <= d // 2, (d, x, neighbor_counts)
    return (d, count, 1 << d)


def check_five_cube_obstruction():
    odd = [x for x in range(32) if parity(x)]
    max_far = -1
    witness = None
    n = 0
    for six in combinations(odd, 6):
        far_pairs = sum((u ^ v).bit_count() == 4 for u, v in combinations(six, 2))
        n += 1
        if far_pairs > max_far:
            max_far, witness = far_pairs, six
    assert n == 8008
    assert max_far == 7, (max_far, witness)
    for u, v in combinations(odd, 2):
        common = sum(((u ^ z).bit_count() == 4 and (v ^ z).bit_count() == 4) for z in odd)
        assert common <= 2
    assert all(not ((u ^ v).bit_count() == 4 and (v ^ w).bit_count() == 4 and (w ^ u).bit_count() == 4)
               for u, v, w in combinations(odd, 3))
    return (n, max_far)


if __name__ == '__main__':
    assert check_five_cube_obstruction() == (8008, 7)
    results = [validate(d) for d in range(2, 15)]
    print('CERTIFICATE_OK', 'six_subsets=8008', 'max_distance4_edges=7',
          'dimensions=' + ','.join(str(d) for d, _, _ in results))
    print('COLORS', ', '.join(f'{d}:{c}' for d, c, _ in results))
