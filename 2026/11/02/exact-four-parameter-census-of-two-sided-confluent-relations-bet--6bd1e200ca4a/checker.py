#!/usr/bin/env python3
"""Exact confluence census: closed form versus literal finite enumeration."""
from itertools import product
from math import comb


def closed(a, c, b, d):
    assert min(a, c, b, d) >= 1
    l = (2**b - 1)**a - 2**(a*b) + (2**a - 1 + 2**c)**b
    u = (2**d - 1)**c + (2**c + 2**a - 1)**d - 2**(c*d)
    cross = sum(comb(b, t) * ((1 + 2**t*(2**d-1))**c - (2**t*(2**d-1))**c)
                for t in range(1, b + 1))
    zero = sum(comb(d, s) * ((1 + (2**b - 1)*2**s)**a - ((2**b-1)*2**s)**a)
               for s in range(1, d + 1))
    return 1 + l*u + cross + zero


def literal_count(a, c, b, d):
    # Source is a lower a-point antichain followed by an upper c-point antichain.
    # Target is a lower b-point antichain followed by an upper d-point antichain.
    # The only nontrivial source comparable pairs join the different levels.
    n, m = a+c, b+d
    upward = [({t} | (set(range(b, m)) if t < b else set())) for t in range(m)]
    ans = 0
    for rows in product(range(1 << m), repeat=n):
        sets = [set(t for t in range(m) if rows[i] & (1 << t)) for i in range(n)]
        good = True
        for x in range(a):
            for y in range(a, n):
                # FC: for every target in lower row find a >= target in upper row.
                if any(not (upward[z] & sets[y]) for z in sets[x]):
                    good = False
                    break
                # DC: for every target in upper row find a <= target in lower row.
                if any(not any(z in upward[w] for w in sets[x]) for z in sets[y]):
                    good = False
                    break
            if not good:
                break
        ans += good
    return ans


def run():
    comparisons = 0
    for a in range(1, 4):
        for c in range(1, 4):
            for b in range(1, 4):
                for d in range(1, 4):
                    if a + c > 4 or b + d > 4:
                        continue
                    f, e = closed(a,c,b,d), literal_count(a,c,b,d)
                    assert f == e, ((a,c,b,d),f,e)
                    comparisons += 1
    assert comparisons == 36
    dual = 0
    for a in range(1,6):
        for c in range(1,6):
            for b in range(1,6):
                for d in range(1,6):
                    assert closed(a,c,b,d) == closed(c,a,d,b)
                    dual += 1
    assert dual == 625
    for params, target in [
        ((1,1,1,1),7),((1,1,2,2),71),((2,1,1,2),69),
        ((2,2,2,2),1867),((2,2,3,3),108327),
        ((2,1,2,1),89),((3,1,3,1),5119),
    ]:
        assert closed(*params) == target
    print('EXHAUSTIVE_COMPARISONS', comparisons)
    print('REVERSAL_COMPARISONS', dual)
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    run()
