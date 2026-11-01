#!/usr/bin/env python3
"""Independent exact ranks over F_2, F_3 and F_5 for PG(3,2) cap complex.

Requires only Python 3 standard library; does not read the discrete-Morse certificate.
"""
from collections import defaultdict


def faces_by_degree():
    ls = {sum(1 << (x - 1) for x in (a, b, a ^ b))
          for a in range(1, 16) for b in range(a + 1, 16)}
    assert len(ls) == 35
    d = defaultdict(list)
    for mask in range(1, 1 << 15):
        if any(mask & L == L for L in ls):
            continue
        d[mask.bit_count() - 1].append(mask)
    return d


def rank_mod_p(upper, lower, p):
    lookup = {f: i for i, f in enumerate(lower)}
    pivots = {}
    for col in upper:
        coeff = {}
        rem = col
        j = 0
        while rem:
            bit = rem & -rem
            rem -= bit
            row = lookup[col - bit]
            val = 1 if j % 2 == 0 else p - 1
            coeff[row] = val
            j += 1
        while coeff:
            i = min(coeff)
            if i not in pivots:
                inv = pow(coeff[i], -1, p)
                pivots[i] = {r: (v * inv) % p for r, v in coeff.items()}
                break
            row = pivots[i]
            factor = coeff[i]
            for r, v in row.items():
                t = (coeff.get(r, 0) - factor * v) % p
                if t:
                    coeff[r] = t
                else:
                    coeff.pop(r, None)
    return len(pivots)


def main():
    d = faces_by_degree()
    assert [len(d[i]) for i in range(8)] == [15, 105, 420, 945, 1008, 420, 120, 15]
    for p in (2, 3, 5):
        rank = {k: rank_mod_p(d[k], d[k - 1], p) for k in range(1, 8)}
        expected = ([14, 91, 329, 615, 315, 105, 15] if p == 2
                    else [14, 91, 329, 616, 315, 105, 15])
        assert [rank[k] for k in range(1, 8)] == expected, (p, rank)
        bettis = {k: len(d[k])-rank.get(k, 0)-rank.get(k+1, 0)-(1 if k == 0 else 0)
                  for k in range(8)}
        wanted = {3: 1, 4: 78} if p == 2 else {4: 77}
        assert {k: v for k, v in bettis.items() if v} == wanted, (p, bettis)
        print('PRIME', p, 'BOUNDARY_RANKS', expected, 'REDUCED_BETTI', wanted)
    print('MODULAR_VERIFY_OK')


if __name__ == '__main__':
    main()
