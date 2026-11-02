#!/usr/bin/env python3
"""Reproduce the rational homology character of a directed Hom complex.

Requires Python 3.10+; only the standard library. No external data files.
"""
from collections import Counter, defaultdict, deque

P = 19
RES = frozenset((k*k) % P for k in range(1, P))
MASK = (1 << P) - 1
OUT = [sum(1 << j for j in range(P) if (j-i) % P in RES) for i in range(P)]
IN = [sum(1 << j for j in range(P) if (i-j) % P in RES) for i in range(P)]


def submasks_nonzero(mask):
    part = mask
    while part:
        yield part
        part = (part - 1) & mask


def cells_by_dim():
    cells = defaultdict(list)
    for A in range(1, 1 << P):
        b_candidates = c_candidates = MASK
        remainder = A
        while remainder:
            bit = remainder & -remainder
            remainder ^= bit
            i = bit.bit_length()-1
            b_candidates &= OUT[i]
            c_candidates &= IN[i]
            if not b_candidates:
                break
        if not b_candidates:
            continue
        for B in submasks_nonzero(b_candidates):
            possible_c = c_candidates
            remainder = B
            while remainder and possible_c:
                bit = remainder & -remainder
                remainder ^= bit
                possible_c &= OUT[bit.bit_length()-1]
            for C in submasks_nonzero(possible_c):
                d = A.bit_count()+B.bit_count()+C.bit_count()-3
                cells[d].append((A, B, C))
    return cells


def boundary(cell):
    """The oriented product-of-simplices cellular boundary."""
    for k, m in enumerate(cell):
        if m.bit_count() <= 1:
            continue
        prefix = sum(cell[j].bit_count()-1 for j in range(k))
        q = 0
        while m:
            bit = m & -m
            m ^= bit
            face = list(cell)
            face[k] ^= bit
            yield tuple(face), -1 if (prefix+q) & 1 else 1
            q += 1


def gf2_rank(vectors):
    pivots = {}
    for vector in vectors:
        while vector:
            b = vector.bit_length()-1
            if b in pivots:
                vector ^= pivots[b]
            else:
                pivots[b] = vector
                break
    return len(pivots)


def signed_cell_trace(cells, a, b, all_masks):
    images = [(a*i+b) % P for i in range(P)]
    fixed_sign = {}
    for mask in all_masks:
        moved = []
        rem = mask
        image = 0
        while rem:
            bit = rem & -rem
            rem ^= bit
            y = images[bit.bit_length()-1]
            moved.append(y)
            image |= 1 << y
        if image != mask:
            fixed_sign[mask] = 0
            continue
        inv = sum(moved[i] > moved[j] for i in range(len(moved))
                  for j in range(i+1,len(moved)))
        fixed_sign[mask] = -1 if inv & 1 else 1
    lefschetz = 0
    for d, level in cells.items():
        factor = -1 if d & 1 else 1
        for A, B, C in level:
            value = fixed_sign[A] * fixed_sign[B] * fixed_sign[C]
            lefschetz += factor * value
    return lefschetz


def main():
    assert RES == {1, 4, 5, 6, 7, 9, 11, 16, 17}
    cells = cells_by_dim()
    f = tuple(len(cells[d]) for d in range(5))
    assert f == (855, 5130, 9234, 4959, 684), f
    ids = [{c:i for i,c in enumerate(cells[d])} for d in range(5)]
    assert all(len(ids[d]) == len(cells[d]) for d in range(5))

    ranks = {}
    for d in range(1, 5):
        lower = ids[d-1]
        columns = []
        rows = [0] * len(cells[d-1])
        for j, cell in enumerate(cells[d]):
            col = 0
            for face, sgn in boundary(cell):
                assert sgn in (-1, 1)
                i = lower[face]
                assert not (col >> i) & 1
                col |= 1 << i
                rows[i] |= 1 << j
            columns.append(col)
        r_col = gf2_rank(columns)
        r_row = gf2_rank(rows)
        assert r_col == r_row, (d, r_col, r_row)
        ranks[d] = r_col
    assert tuple(ranks[d] for d in range(1,5)) == (854, 4276, 4275, 684), ranks
    mod2 = tuple(f[d] - ranks.get(d,0) - ranks.get(d+1,0) for d in range(5))
    assert mod2 == (1, 0, 683, 0, 0), mod2
    # An independent, signed chain-condition check, not inferred from mod-two arithmetic.
    for d in range(2,5):
        for cell in cells[d]:
            summed = Counter()
            for face, coefficient in boundary(cell):
                for codim2, second_coefficient in boundary(face):
                    summed[codim2] += coefficient * second_coefficient
            assert not any(summed.values()), (d,cell)

    # Euler characteristic + field comparison bound the rational Betti numbers:
    # betti_Q(d) <= betti_F2(d), and chi = 684, hence beta_Q=(1,0,683,0,0).
    assert sum((-1)**d*f[d] for d in range(5)) == 684
    masks = set(mask for group in cells.values() for cell in group for mask in cell)
    chars = Counter()
    for a in sorted(RES):
        for b in range(P):
            # Every affine map preserves the Paley orientation.
            assert {(a*r)%P for r in RES} == RES
            trace_h2 = signed_cell_trace(cells,a,b,masks)-1
            if a == 1 and b == 0:
                expected = 683
            elif a == 1:
                expected = -1
            elif a in (7,11):
                expected = 8
            else:
                expected = -1
            assert trace_h2 == expected, (a,b,trace_h2,expected)
            chars[(a,trace_h2)] += 1
    assert sum(chars.values()) == 171
    assert sum(mult * count for (a,mult),count in chars.items()) == 171*5

    # Character of 5 trivial + 6 rational C3-cyclotomic +
    # 3 rational C9-cyclotomic + 36 rational 19-point augmentation modules.
    for a in RES:
        for b in range(P):
            if a == 1 and b == 0:
                values = (1, 2, 6, 18)
            elif a == 1:
                values = (1, 2, 6, -1)
            elif a in (7,11):
                values = (1, 2, -3, 0)
            else:
                values = (1, -1, 0, 0)
            assert sum(x*y for x,y in zip((5,6,3,36),values)) == (
                683 if (a,b)==(1,0) else 8 if a in (7,11) else -1)
    print('PALEY19_HOM_C3_RATIONAL_AFFINE_CHARACTER_VERIFY_OK')
    print('f_vector', f)
    print('mod2_boundary_ranks', tuple(ranks[d] for d in range(1,5)))
    print('rational_betti', (1,0,683,0,0))
    print('affine_elements',sum(chars.values()))
    print('character_distribution',dict(sorted(Counter({683:1,-1:18+6*19,8:2*19}).items())))
    print('affine_invariants',5)


if __name__ == '__main__':
    main()
