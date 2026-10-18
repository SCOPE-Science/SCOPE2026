"""Independently enumerate directed Hom cells and calculate mod-prime cellular homology."""
from collections import defaultdict


def verify(n, prime=1000003):
    m = (n - 1) // 2
    vertices = range(n)
    out = [sum(1 << ((a + j) % n) for j in range(1, m + 1)) for a in vertices]
    inn = [sum(1 << ((a - j) % n) for j in range(1, m + 1)) for a in vertices]
    all_mask = (1 << n) - 1
    out_inter = [all_mask] * (1 << n)
    in_inter = [all_mask] * (1 << n)
    for mask in range(1, 1 << n):
        bit = mask & -mask
        a = bit.bit_length() - 1
        out_inter[mask] = out_inter[mask ^ bit] & out[a]
        in_inter[mask] = in_inter[mask ^ bit] & inn[a]
    cells = defaultdict(list)
    for A in range(1, 1 << n):
        B = out_inter[A]
        while B:
            C = out_inter[B] & in_inter[A]
            while C:
                d = A.bit_count() + B.bit_count() + C.bit_count() - 3
                cells[d].append((A, B, C))
                C = (C - 1) & (out_inter[B] & in_inter[A])
            B = (B - 1) & out_inter[A]
    rank = {}
    for d in sorted(cells):
        if d == 0:
            continue
        lower_index = {cell: j for j, cell in enumerate(cells[d - 1])}
        pivots = {}
        for cell in cells[d]:
            vector = {}
            offset = 0
            for coordinate, subset in enumerate(cell):
                if subset.bit_count() >= 2:
                    loc = 0
                    for a in vertices:
                        if (subset >> a) & 1:
                            face = list(cell)
                            face[coordinate] ^= 1 << a
                            j = lower_index[tuple(face)]
                            sign = 1 if ((loc + offset) % 2 == 0) else prime - 1
                            vector[j] = sign
                            loc += 1
                offset += subset.bit_count() - 1
            while vector:
                j = min(vector)
                if j not in pivots:
                    inverse = pow(vector[j], -1, prime)
                    pivots[j] = {k: (v * inverse) % prime for k, v in vector.items()}
                    break
                scalar = vector[j]
                for k, v in pivots[j].items():
                    new_value = (vector.get(k, 0) - scalar * v) % prime
                    if new_value:
                        vector[k] = new_value
                    else:
                        vector.pop(k, None)
        rank[d] = len(pivots)
    betti = {d: len(cells[d]) - rank.get(d, 0) - rank.get(d + 1, 0)
             for d in sorted(cells)}
    expected = {d: int(d in (0, 1)) for d in cells}
    assert betti == expected, (n, betti, expected)
    print(f'n={n} cells_by_dimension={tuple(len(cells[d]) for d in sorted(cells))} '
          f'Betti_Fp={betti}')


if __name__ == '__main__':
    for n in (5, 7, 9, 11, 13):
        verify(n)
    print('HOM_CELLULAR_CHAIN_CHECK_OK')
