#!/usr/bin/env python3
"""Exact finite shelling certificate for the n=4 complex in arXiv:2109.09002.

The vertices are the variables w_{i,j}, 1<=i<=5, 1<=j<=4. The minimal
nonfaces are the supports of x_2,...,x_5, y_2,...,y_5, z_3,...,z_5 in
Proposition 7.3. This script exhaustively enumerates every subset of the 20
vertices, identifies all minimal vertex covers of those 11 supports, forms
their complements (the facets), and verifies a shelling order by the pure
shelling criterion. No third-party packages are required.
"""

N_ROWS, N_COLS, N = 5, 4, 20
VERTICES = [(i, j) for i in range(1, N_ROWS + 1) for j in range(1, N_COLS + 1)]
VID = {v: i for i, v in enumerate(VERTICES)}
FULL = (1 << N) - 1


def mask_of(coords):
    m = 0
    for v in coords:
        if v not in VID:
            raise AssertionError(f"invalid variable index: {v}")
        m |= 1 << VID[v]
    return m


def generators():
    E = []
    # x_h = prod_{i=2}^{h-1} w_{i,n+2-i} prod_{i=h+1}^{n+1} w_{i,n+3-i}
    for h in range(2, N_ROWS + 1):
        E.append(mask_of(
            [(i, 6 - i) for i in range(2, h)] +
            [(i, 7 - i) for i in range(h + 1, N_ROWS + 1)]))
    # y_h = prod_{i=1}^{h-1} w_{i,n+1-i} prod_{i=h+1}^{n+1} w_{i,n+2-i}
    for h in range(2, N_ROWS + 1):
        E.append(mask_of(
            [(i, 5 - i) for i in range(1, h)] +
            [(i, 6 - i) for i in range(h + 1, N_ROWS + 1)]))
    # z_h = prod_{i=3}^{h-1} w_{i,n+3-i} prod_{i=h}^{n+1} w_{i,n+2-i}
    #       prod_{i=h+1}^{n+1} w_{i,n+4-i}
    for h in range(3, N_ROWS + 1):
        E.append(mask_of(
            [(i, 7 - i) for i in range(3, h)] +
            [(i, 6 - i) for i in range(h, N_ROWS + 1)] +
            [(i, 8 - i) for i in range(h + 1, N_ROWS + 1)]))
    return E


def bits(mask):
    return [i for i in range(N) if (mask >> i) & 1]


def coord_tuple(mask):
    return tuple(VERTICES[i] for i in bits(mask))


def shelling_condition(facet, earlier):
    """Check: for every earlier G, some earlier H has |F\\H|=1 and F∩G⊆F∩H."""
    for G in earlier:
        FG = facet & G
        found = False
        for H in earlier:
            if (facet & ~H).bit_count() == 1 and (FG & ~(facet & H)) == 0:
                found = True
                break
        if not found:
            return False
    return True


def main():
    E = generators()
    assert len(E) == 11
    assert all(e and (e & ~FULL) == 0 for e in E)
    assert len(set(E)) == len(E)
    assert not any(a != b and (a & b) == a for a in E for b in E)

    # Complete enumeration of all 2^20 subsets; is_cover[C] means C hits every
    # support of a generator of the square-free monomial ideal.
    is_cover = bytearray(1 << N)
    for C in range(1 << N):
        is_cover[C] = int(all(C & e for e in E))
    covers = []
    for C in range(1 << N):
        if not is_cover[C]:
            continue
        if all(not is_cover[C ^ (1 << i)] for i in bits(C)):
            covers.append(C)

    assert len(covers) == 50, f"expected 50 minimal covers, got {len(covers)}"
    assert {C.bit_count() for C in covers} == {4}, "minimal covers are not all size 4"
    facets = sorted((FULL ^ C for C in covers), key=lambda m: tuple(bits(m)))
    assert len(facets) == 50 and {F.bit_count() for F in facets} == {16}

    # Deterministic greedy construction of a shelling order.
    remaining = set(facets)
    order = []
    while remaining:
        candidates = [F for F in remaining if shelling_condition(F, order)]
        if not candidates:
            raise AssertionError(f"greedy shelling got stuck after {len(order)} facets")
        F = min(candidates, key=lambda m: tuple(bits(m)))
        assert shelling_condition(F, order)
        order.append(F)
        remaining.remove(F)

    assert len(order) == 50
    for j, F in enumerate(order):
        assert shelling_condition(F, order[:j]), f"shelling check failed at facet {j + 1}"

    print("vertices=20")
    print("minimal_nonfaces=11")
    print("minimal_vertex_covers=50; cover_size=4")
    print("facets=50; facet_size=16; dimension=15")
    print("shelling_order (each row lists the 4 vertices omitted from that facet):")
    for idx, F in enumerate(order, 1):
        C = FULL ^ F
        coords = " ".join(f"({i},{j})" for i, j in coord_tuple(C))
        print(f"{idx:02d}: {coords}")
    print("verification=PASS: every earlier/current facet pair satisfies the pure shelling criterion")
    print("consequence=the Stanley-Reisner ring is Cohen-Macaulay over every field")


if __name__ == "__main__":
    main()
