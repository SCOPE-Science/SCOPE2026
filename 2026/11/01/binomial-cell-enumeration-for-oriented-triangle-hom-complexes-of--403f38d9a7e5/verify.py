"""Exact finite checks for cyclic-tournament directed Hom cell enumeration.

The theorem is proved for every order in RESULT.md; finite checks are not
used to infer its universal quantifier. Python 3, standard library only.
"""
from collections import Counter
from itertools import product
from math import comb


def bit_indices(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask -= bit


def nonempty_submasks(mask):
    sub = mask
    while sub:
        yield sub
        sub = (sub - 1) & mask


def direct_cells(n):
    """Enumerate the definition directly, without the proposed cell formula."""
    m = (n - 1) // 2
    allmask = (1 << n) - 1
    out = [sum(1 << ((a + j) % n) for j in range(1, m + 1))
           for a in range(n)]
    inn = [sum(1 << ((a - j) % n) for j in range(1, m + 1))
           for a in range(n)]
    for a in range(1, 1 << n):
        allowed_b = allmask
        allowed_c = allmask
        for x in bit_indices(a):
            allowed_b &= out[x]
            allowed_c &= inn[x]
        if not allowed_b or not allowed_c:
            continue
        for b in nonempty_submasks(allowed_b):
            c_choices = allowed_c
            for y in bit_indices(b):
                c_choices &= out[y]
            for c in nonempty_submasks(c_choices):
                yield a, b, c


def six_parameter_counts(m):
    """Independent stars-and-bars count using six nonnegative integers."""
    out = Counter()
    n = 2 * m + 1
    def block(u):
        if u == 0:
            return {1: 1}
        return {2 + k: comb(u - 1, k) for k in range(u)}
    for u in range(m):
        for v in range(m - u):
            for w in range(m - u - v):
                rest = m - 1 - u - v - w
                ba, bb, bc = block(u), block(v), block(w)
                ways_gaps = comb(rest + 2, 2)
                for na, ca in ba.items():
                    for nb, cb in bb.items():
                        for nc, cc in bc.items():
                            out[na + nb + nc - 3] += n * ways_gaps * ca * cb * cc
    return out


def canonical_anchor(cell, n):
    """Find first A after C and reconstruct six-gap coordinates."""
    a, b, c = cell
    sets = tuple(set(bit_indices(x)) for x in cell)
    anchors = []
    for start in sets[0]:
        colored = [((start + t) % n, j) for t in range(n)
                   for j, group in enumerate(sets)
                   if (start + t) % n in group]
        kinds = [j for _, j in colored]
        if kinds and kinds[0] == 0 and kinds == sorted(kinds):
            anchors.append(start)
    if len(anchors) != 1:
        raise AssertionError((n, cell, 'anchors', anchors))
    start = anchors[0]
    blocks = [[(v - start) % n for v in sorted(group)] for group in sets]
    blocks = [sorted(block) for block in blocks]
    u, v, w = (max(block) - min(block) for block in blocks)
    p = min(blocks[1]) - max(blocks[0])
    q = min(blocks[2]) - max(blocks[1])
    r = n - max(blocks[2])
    m = (n - 1) // 2
    i = m - u - v - p
    j = m - v - w - q
    k = m - w - u - r
    assert min(p, q, r) >= 1
    assert min(u, v, w, i, j, k) >= 0
    assert u + v + w + i + j + k == m - 1
    return start, (u, v, w, i, j, k)


def rotate(mask, k, n):
    return sum(1 << ((j + k) % n) for j in bit_indices(mask))


def verify():
    for n in range(3, 20, 2):
        m = (n - 1) // 2
        count = Counter()
        cell_total = 0
        anchors_checked = 0
        rotations_checked = 0
        for cell in direct_cells(n):
            d = sum(x.bit_count() for x in cell) - 3
            count[d] += 1
            cell_total += 1
            if n <= 15:
                canonical_anchor(cell, n)
                anchors_checked += 1
                for k in range(1, n):
                    if tuple(rotate(s, k, n) for s in cell) == cell:
                        raise AssertionError(('rotation stabilizer', n, cell, k))
                    rotations_checked += 1
        expected = [n * comb(m + 1, 2) * comb(m - 1, d)
                    for d in range(m)]
        assert [count[d] for d in range(m)] == expected
        assert count == six_parameter_counts(m)
        assert cell_total == n * comb(m + 1, 2) * 2 ** (m - 1)
        chi = sum((-1) ** d * count[d] for d in count)
        assert chi == (3 if n == 3 else 0)
        print(f'n={n} f={expected} chi={chi} '
              f'cells={cell_total} anchors={anchors_checked} '
              f'nonidentity_rotation_tests={rotations_checked}')
    print('CYCLIC_TOURNAMENT_HOM_CELL_POLYNOMIAL_VERIFIED')


if __name__ == '__main__':
    verify()
