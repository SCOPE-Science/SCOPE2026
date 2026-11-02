#!/usr/bin/env python3
"""Exact integer checks for the semigroup of odd-support-free scalar quotients.

The tests corroborate, but do not replace, the valuation and invariant-ring proof.
Run: python3 verify_semigroup.py
"""
from math import gcd


def parameters(r, h):
    assert r >= 3 and r % 2 == 1 and h >= 2 and h % 2 == 0
    d = 2 * (r - 1)
    s = r ** h + 1
    assert (s - 2 * r) % d == 0
    ell = (s - 2 * r) // d
    assert ell >= 1 and gcd(ell, r) == 1
    return d, s, ell


def exact_monomial_apery(r, h):
    d, s, ell = parameters(r, h)
    entries = []
    for j in range(r):
        i = (-2 * j) % d
        assert (i + 2 * j) % d == 0
        assert i < d
        pole_num = i * r + j * s
        assert pole_num % d == 0
        entries.append(pole_num // d)
    return entries


def enumerate_semigroup(generators, limit):
    seen = [False] * (limit + 1)
    seen[0] = True
    for a in range(limit + 1):
        if seen[a]:
            for gen in generators:
                if a + gen <= limit:
                    seen[a + gen] = True
    return seen


def verify(r, h):
    d, s, ell = parameters(r, h)
    apery = exact_monomial_apery(r, h)
    predicted = [0] + [r + j * ell for j in range(1, r)]
    assert apery == predicted
    assert {x % r for x in apery} == set(range(r))
    gens = [r] + predicted[1:]
    conductor = (r - 1) * ell + 1
    genus = (r ** h - 1) // 4
    assert sum(apery) // r - (r - 1) // 2 == genus
    assert sum(apery) % r == 0
    limit = conductor + r * (ell + 2) + 10
    semigroup = enumerate_semigroup(gens, limit)
    for m in range(limit + 1):
        residue = m % r
        apery_min = next(a for a in apery if a % r == residue)
        assert semigroup[m] == (m >= apery_min), (r, h, m)
    gaps = [a for a in range(conductor) if not semigroup[a]]
    assert len(gaps) == genus and gaps[-1] == conductor - 1
    # Full finite test of pseudo-Frobenius numbers and embedding dimension.
    pf = [a for a in gaps if all(semigroup[a + gen] for gen in gens)]
    assert pf == [j * ell for j in range(1, r)]
    assert 2 * genus == (conductor - 1) + len(pf)
    for j, v in enumerate(gens):
        assert not any(semigroup[k] and semigroup[v-k]
                       for k in range(1, v)), (r, h, j)
    return {'r': r, 'h': h, 'L': ell, 'genus': genus,
            'F': conductor - 1, 'type': len(pf), 'generators': gens}


def main():
    cases = [(r, h) for r in [3, 5, 7, 9, 11, 13] for h in [2, 4]]
    cases += [(3, 6), (5, 6)]
    for r, h in cases:
        info = verify(r, h)
        print(f"r={r} h={h} L={info['L']} g={info['genus']} "
              f"F={info['F']} type={info['type']}")
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
