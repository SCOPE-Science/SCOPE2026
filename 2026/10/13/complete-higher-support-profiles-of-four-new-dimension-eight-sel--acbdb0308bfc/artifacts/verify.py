#!/usr/bin/env python3
from itertools import combinations
from math import prod

CODES = {
    91: [
        '9178c93aad6db724a17528e',
        '524e3aa98bd1d2a3d2e97c8',
        '302ae870277bdc487aa05b4',
        '0b12221ce1c887cef9dbcee',
        '070e41fc1ff701c1f1073f0',
        '00fe7803ff87ffc03e1f02c',
        '0001f800007fffffc01ffcc',
        '000007ffffffffffffe0006',
    ],
    98: [
        '80c090d0a8f8e4ecdcbcdafb8',
        '40604868547c72766e5e6d7d0',
        '203024342a3e393b372fb6bf8',
        '1018121a151f9c9d9b975b5f0',
        '080c090d8a8f4ececdcbadae4',
        '0406848645c72767e6e5d6d70',
        '02034243a2e393b373f26bea4',
        '018121a151f1c9d9b979b5f50',
    ],
    114: [
        '80e090b0a898f8a4d4f4ecdcbcff8',
        '40704858544c7c526a7a766e5e7f0',
        '2038242c2a263e29353d3b372fbe4',
        '101c121615131f949a9e9d9b97df0',
        '080e090b8a898f4a4d4fcecdcbee4',
        '0407848545c4c725a6a767e6e5f70',
        '028342c2a262e39253d3b373f2fa4',
        '01c121615131f149a9e9d9b979fd0',
    ],
    191: [
        '80b651765a7a08cb754997e9700e853acce5f301d7b8d1f0',
        '412edb24a676e85bece929278b70dcfcce124854b11e71bc',
        '210b43ef6f85d10d00d633f55764b8bb8959f8a1faee0188',
        '1036f4a81c1885b45aafcb87cfc8f1e8db0d3f83e1f048c6',
        '099cc9b65fffbfb4aadb2a19329df8981180900c47bb2ae4',
        '05215e997ff8240c8ef265c31041575498e35bba0776d7ec',
        '028caea7f532f75d2d15c371119b4272a337bf84ed22c538',
        '006106140007bffe9bd3bdef901800896a5abedbffdfd4e0',
    ],
}

EXPECTED = {
    91: ((42,64,75,81,84,87,89,91), (54,982,872,334,5,12,1,1)),
    98: ((46,70,82,88,91,94,96,98), (74,2337,6468,1481,19,12,1,1)),
    114: ((54,82,96,103,107,110,112,114), (70,2016,4715,805,66,23,2,1)),
    191: ((94,142,166,178,184,187,189,191), (94,4340,24800,25420,4774,125,2,1)),
}

GAUSSIAN_8 = (1,255,10795,97155,200787,97155,10795,255,1)


def parse_row(h, n):
    bits = ''.join(f'{int(c, 16):04b}' for c in h.strip())
    if len(bits) < n:
        raise AssertionError((h, n, len(bits)))
    if any(b != '0' for b in bits[n:]):
        raise AssertionError(f'nonzero source padding for n={n}: {h}')
    x = 0
    for j, b in enumerate(bits[:n]):
        if b == '1':
            x |= 1 << j
    return x


def gf2_rank(rows):
    a = list(rows)
    rank = 0
    col = 0
    maxcol = max((x.bit_length() for x in a), default=0)
    while col < maxcol and rank < len(a):
        pivot = next((i for i in range(rank, len(a)) if (a[i] >> col) & 1), None)
        if pivot is None:
            col += 1
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for i in range(len(a)):
            if i != rank and ((a[i] >> col) & 1):
                a[i] ^= a[rank]
        rank += 1
        col += 1
    return rank


def rref_bases(k, r):
    if r == 0:
        yield ()
        return
    for piv in combinations(range(k), r):
        nonpiv = [j for j in range(k) if j not in piv]
        rows = [1 << p for p in piv]

        def rec(t):
            if t == len(nonpiv):
                yield tuple(rows)
                return
            j = nonpiv[t]
            active = 0
            while active < r and piv[active] < j:
                active += 1
            for mask in range(1 << active):
                changed = []
                for i in range(active):
                    if (mask >> i) & 1:
                        rows[i] ^= 1 << j
                        changed.append(i)
                yield from rec(t + 1)
                for i in changed:
                    rows[i] ^= 1 << j

        yield from rec(0)


def span_vectors(basis):
    vals = [0]
    for b in basis:
        vals += [x ^ b for x in vals]
    return vals


def encode_message(m, rows):
    x = 0
    i = 0
    while m:
        if m & 1:
            x ^= rows[i]
        i += 1
        m >>= 1
    return x


def column_multiplicities(rows, n):
    counts = [0] * 256
    for j in range(n):
        v = 0
        for i, row in enumerate(rows):
            v |= ((row >> j) & 1) << i
        counts[v] += 1
    return counts


def check_code(n, hexrows):
    rows = [parse_row(h, n) for h in hexrows]
    assert len(rows) == 8 and gf2_rank(rows) == 8
    for a in rows:
        for b in rows:
            assert ((a & b).bit_count() & 1) == 0

    encoded = [encode_message(m, rows) for m in range(256)]
    assert min(x.bit_count() for x in encoded[1:]) == EXPECTED[n][0][0]
    colcounts = column_multiplicities(rows, n)
    assert colcounts[0] == 0

    direct_min = [None] * 9
    direct_count = [0] * 9
    dual_max = [None] * 9
    dual_count = [0] * 9
    subspace_counts = [0] * 9

    for r in range(9):
        for basis in rref_bases(8, r):
            subspace_counts[r] += 1

            # Direct support route: a coordinate is active in the subcode
            # iff at least one encoded basis vector is nonzero there.
            support = 0
            for b in basis:
                support |= encoded[b]
            sw = support.bit_count()
            if direct_min[r] is None or sw < direct_min[r]:
                direct_min[r], direct_count[r] = sw, 1
            elif sw == direct_min[r]:
                direct_count[r] += 1

            # Orthogonal-section route: for any message-space W, sum the
            # multiplicities of generator columns lying in W.
            mass = sum(colcounts[v] for v in span_vectors(basis))
            if dual_max[r] is None or mass > dual_max[r]:
                dual_max[r], dual_count[r] = mass, 1
            elif mass == dual_max[r]:
                dual_count[r] += 1

    assert tuple(subspace_counts) == GAUSSIAN_8
    direct_d = tuple(direct_min[1:])
    direct_c = tuple(direct_count[1:])
    expected_d, expected_c = EXPECTED[n]
    assert direct_d == expected_d, (n, direct_d, expected_d)
    assert direct_c == expected_c, (n, direct_c, expected_c)

    dual_d = tuple(n - dual_max[8-r] for r in range(1, 9))
    dual_c = tuple(dual_count[8-r] for r in range(1, 9))
    assert dual_d == expected_d, (n, dual_d, expected_d)
    assert dual_c == expected_c, (n, dual_c, expected_c)
    assert direct_d == dual_d and direct_c == dual_c

    return {
        'n': n,
        'd': direct_d,
        'minimizers': direct_c,
        'dual_maxima_by_dimension_0_to_7': tuple(dual_max[:8]),
        'dual_maximizer_counts_by_dimension_0_to_7': tuple(dual_count[:8]),
    }


def main():
    results = [check_code(n, CODES[n]) for n in (91,98,114,191)]
    for r in results:
        print(r)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
