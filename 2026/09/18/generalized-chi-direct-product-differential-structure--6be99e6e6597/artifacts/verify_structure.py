#!/usr/bin/env python3
"""Finite checks for the direct-product structure of generalized chi maps."""
from collections import Counter
from math import gcd, lcm


def bits(x, n):
    return [(x >> i) & 1 for i in range(n)]


def from_bits(b):
    return sum((u & 1) << i for i, u in enumerate(b))


def chi(x, n):
    b = bits(x, n)
    return from_bits([
        b[i] ^ (b[(i + 1) % n] & b[(i + 2) % n]) ^ b[(i + 2) % n]
        for i in range(n)
    ])


def chi_nv(x, n, v):
    b = bits(x, n)
    return from_bits([
        b[i] ^ (b[(i + v) % n] & b[(i + 2 * v) % n]) ^ b[(i + 2 * v) % n]
        for i in range(n)
    ])


def chi_n_minus_2v(x, n, v):
    b = bits(x, n)
    return from_bits([
        b[i] ^ (b[(i - 2 * v) % n] & b[(i - v) % n]) ^ b[(i - v) % n]
        for i in range(n)
    ])


def group_blocks(x, n, v):
    d = gcd(n, v)
    ell = n // d
    b = bits(x, n)
    return [[b[(r + t * v) % n] for t in range(ell)] for r in range(d)]


def ungroup_blocks(blocks, n, v):
    d = gcd(n, v)
    ell = n // d
    b = [0] * n
    for r in range(d):
        for t in range(ell):
            b[(r + t * v) % n] = blocks[r][t]
    return from_bits(b)


def product_chi(x, n, v):
    out = []
    for block in group_blocks(x, n, v):
        out.append(bits(chi(from_bits(block), len(block)), len(block)))
    return ungroup_blocks(out, n, v)


def affine_A(block):
    ell = len(block)
    return [block[(-t) % ell] ^ 1 for t in range(ell)]


def product_affine_conjugate_chi(x, n, v):
    out = []
    for block in group_blocks(x, n, v):
        a = affine_A(block)
        mid = bits(chi(from_bits(a), len(a)), len(a))
        out.append(affine_A(mid))
    return ungroup_blocks(out, n, v)


def differential_uniformity(f, n):
    N = 1 << n
    table = [f(x) for x in range(N)]
    best = 0
    for a in range(1, N):
        counts = Counter(table[x] ^ table[x ^ a] for x in range(N))
        best = max(best, max(counts.values()))
    return best


def permutation_order(f, n):
    N = 1 << n
    seen = [False] * N
    ans = 1
    for x in range(N):
        if seen[x]:
            continue
        y = x
        length = 0
        while not seen[y]:
            seen[y] = True
            length += 1
            y = f(y)
        ans = lcm(ans, length)
    return ans


def main():
    cases = [(6, 2), (10, 2), (12, 4)]
    for n, v in cases:
        lhs_ok = all(chi_nv(x, n, v) == product_chi(x, n, v)
                     for x in range(1 << n))
        rhs_ok = all(chi_n_minus_2v(x, n, v) == product_affine_conjugate_chi(x, n, v)
                     for x in range(1 << n))
        print(f"n={n}, v={v}, d={gcd(n,v)}, ell={n//gcd(n,v)}: "
              f"chi_product={lhs_ok}, minus2v_affine_product={rhs_ok}")
        assert lhs_ok and rhs_ok

    for ell in (3, 5, 7):
        delta = differential_uniformity(lambda x, ell=ell: chi(x, ell), ell)
        order = permutation_order(lambda x, ell=ell: chi(x, ell), ell)
        print(f"base ell={ell}: delta={delta}, expected_delta={1 << (ell-2)}, order={order}")
        assert delta == 1 << (ell - 2)

    for n, v in ((6, 2), (10, 2)):
        delta1 = differential_uniformity(lambda x, n=n, v=v: chi_nv(x, n, v), n)
        delta2 = differential_uniformity(lambda x, n=n, v=v: chi_n_minus_2v(x, n, v), n)
        print(f"general n={n}, v={v}: delta_chi_nv={delta1}, "
              f"delta_minus2v={delta2}, expected={1 << (n-2)}")
        assert delta1 == delta2 == 1 << (n - 2)

    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
