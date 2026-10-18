"""Exact integer certificate verifier for divisor-layer tilings."""
import json
from pathlib import Path

DATA = json.loads(Path(__file__).with_name('certificates.json').read_text(encoding='utf-8'))
EXPECTED = {(i, j) for i in (3, 4, 5) for j in (3, 4, 5)} | {(i, 2) for i in (4, 5, 6, 7)}
TILES = {}
for t in DATA['tiles']:
    I, J = t['I'], t['J']
    assert (I, J) in EXPECTED and (I, J) not in TILES
    assert len(t['colors']) == I * J
    sums = [0, 0, 0]
    terms = set()
    for i in range(I):
        for j in range(J):
            pair = t['colors'][i * J + j]
            assert len(pair) == 2
            for e in (0, 1):
                color = pair[e]
                assert type(color) is int and 0 <= color < 3
                weight = (2 ** i) * (3 ** j) * (5 ** e)
                assert weight not in terms
                terms.add(weight)
                sums[color] += weight
    assert sums == [t['each_sum']] * 3, (I, J, sums)
    assert t['each_sum'] == (2 ** I - 1) * (3 ** J - 1)
    TILES[(I, J)] = t
assert set(TILES) == EXPECTED


def lengths(L, minimum):
    if minimum == 3:
        if L < 3:
            raise ValueError(L)
        # All lengths >=3 are sums of 3,4,5.
        q, r = divmod(L, 3)
        if r == 0:
            return [3] * q
        return [3] * (q - 1) + [3 + r]
    if minimum == 4:
        if L < 4:
            raise ValueError(L)
        q, r = divmod(L, 4)
        if r == 0:
            return [4] * q
        return [4] * (q - 1) + [4 + r]
    raise ValueError(minimum)


def partition(a, b):
    if a >= 2 and b >= 2:
        ii, jj = lengths(a + 1, 3), lengths(b + 1, 3)
    elif a >= 3 and b == 1:
        ii, jj = lengths(a + 1, 4), [2]
    else:
        return None
    sums, indices, i0 = [0, 0, 0], set(), 0
    for I in ii:
        j0 = 0
        for J in jj:
            cert = TILES[(I, J)]['colors']
            for i in range(I):
                for j in range(J):
                    for e in range(2):
                        key = (i0 + i, j0 + j, e)
                        assert key not in indices
                        indices.add(key)
                        sums[cert[i * J + j][e]] += 2 ** key[0] * 3 ** key[1] * 5 ** e
            j0 += J
        assert j0 == b + 1
        i0 += I
    assert i0 == a + 1
    assert len(indices) == 2 * (a + 1) * (b + 1)
    return sums

for a in range(0, 16):
    for b in range(0, 16):
        N = 2 ** a * 3 ** b * 5
        sigma = 3 * (2 ** (a + 1) - 1) * (3 ** (b + 1) - 1)
        criterion = (a >= 2 and b >= 2) or (a >= 3 and b == 1)
        assert (sigma >= 3 * N) == criterion, (a, b)
        s = partition(a, b)
        assert (s is not None) == criterion
        if s is not None:
            assert s == [sigma // 3] * 3, (a, b, s)
print('PASS: 13 tile certificates; 256 parameter checks; disjoint exhaustive divisor partitions')
