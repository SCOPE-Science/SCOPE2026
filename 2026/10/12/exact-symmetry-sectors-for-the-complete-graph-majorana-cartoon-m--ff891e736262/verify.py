#!/usr/bin/env python3
from itertools import combinations

def mul(a, b):
    # (phase mod 4, bit mask) represents i^phase times ordered Clifford monomial.
    pa, ma = a
    pb, mb = b
    inv = 0
    x = ma
    while x:
        lsb = x & -x
        ia = lsb.bit_length() - 1
        inv += (mb & ((1 << ia) - 1)).bit_count()
        x ^= lsb
    return ((pa + pb + 2 * (inv & 1)) % 4, ma ^ mb)

def edges_of_complete_graph(n):
    return [(u, v) for u in range(n) for v in range(u + 1, n)]

def star_masks(n):
    edges = edges_of_complete_graph(n)
    masks = []
    for v in range(n):
        m = 0
        for j, (a, b) in enumerate(edges):
            if a == v or b == v:
                m |= 1 << j
        masks.append(m)
    return edges, masks

def cut_mask(n, edges, subset_mask):
    m = 0
    for j, (a, b) in enumerate(edges):
        if ((subset_mask >> a) & 1) ^ ((subset_mask >> b) & 1):
            m |= 1 << j
    return m

def check_n(n):
    assert n % 4 == 0
    edges, sm = star_masks(n)
    k = n - 1
    parity = (k * (k - 1) // 2) & 1
    assert parity == 1  # raw star is anti-Hermitian and squares to -I

    corrected = [(1, m) for m in sm]  # i times the raw star product
    for s in corrected:
        assert mul(s, s) == (0, 0)
    for i in range(n):
        for j in range(n):
            assert mul(corrected[i], corrected[j]) == mul(corrected[j], corrected[i])

    # The first n-1 corrected stars are independent as involutions: every
    # nonempty subset has a nonempty cut monomial. Exhaustively verify modest n.
    seen_masks = set()
    for subset in range(1 << (n - 1)):
        z = (0, 0)
        for v in range(n - 1):
            if (subset >> v) & 1:
                z = mul(z, corrected[v])
        expected = cut_mask(n, edges, subset)
        assert z[1] == expected
        if subset:
            assert expected != 0
        assert z[1] not in seen_masks
        seen_masks.add(z[1])
    assert len(seen_masks) == 1 << (n - 1)

    # Multiplying all n stars leaves no Majorana factor, so the final star is
    # determined, up to a scalar sign, by the first n-1 on every joint sector.
    z = (0, 0)
    for s in corrected:
        z = mul(z, s)
    assert z[1] == 0 and z[0] in (0, 2)

    hilbert_exp = n * (n - 1) // 4
    sector_exp = hilbert_exp - (n - 1)
    assert sector_exp == (n - 1) * (n - 4) // 4
    assert sector_exp >= 0
    return z[0], sector_exp

def main():
    out = []
    for n in (4, 8, 12, 16):
        phase, sector_exp = check_n(n)
        out.append((n, '+' if phase == 0 else '-', sector_exp))
    print('VERIFY_OK', ' '.join(f'N={n}:full_product={sgn}I:sector_dim=2^{e}' for n, sgn, e in out))

if __name__ == '__main__':
    main()
