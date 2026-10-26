#!/usr/bin/env python3
"""Independent finite verification of majority-dynamics recurrent-state formulas.
Run with Python 3.9 or newer; uses only the standard library.
The proof for arbitrary sizes is mathematical, not an inference from these tests.
"""
from math import comb


def formula(r, s):
    assert r >= 2 and s >= 1
    c = comb(s, s // 2) if s % 2 == 0 else 0
    d = 2**s - 2
    balanced = sum(comb(r, k) * comb(r-k, (r-k)//2) * c**k
                   for k in range(r+1) if (r-k) % 2 == 0)
    extra = r * comb(r-1, (r-1)//2) * (d-c) if r % 2 else 0
    return 2 + c**r, 2 + balanced + extra


def direct(r, s):
    n = r * s
    assert n <= 16
    allmask = (1 << n) - 1
    partmasks = [sum(1 << i for i in range(p*s, (p+1)*s))
                 for p in range(r)]
    masks = [allmask ^ partmasks[i//s] for i in range(n)]
    deg = n-s

    def step(x):
        out = 0
        for i, adj in enumerate(masks):
            v = (x & adj).bit_count()
            bit = 1 if 2*v > deg else 0 if 2*v < deg else (x >> i) & 1
            out |= bit << i
        return out

    fixed, recurrent = 0, 0
    for x in range(1 << n):
        y = step(x)
        fixed += y == x
        recurrent += step(y) == x
        z = step(y)
        w = step(z)
        assert step(step(w)) == w, (r, s, x, "uniform transient bound")
    return fixed, recurrent


def group_count_check(r, s):
    # Entire periodic set classified by part populations, weighted by labels.
    from itertools import product
    n = r*s
    deg = n-s
    fixed, recurrent = 0, 0
    for pop in product(range(s+1), repeat=r):
        weight = 1
        for a in pop:
            weight *= comb(s, a)
        def F(p):
            total = sum(p)
            return tuple(s if 2*(total-t) > deg else 0 if 2*(total-t) < deg else t for t in p)
        y = F(pop)
        fixed += weight * (y == pop)
        recurrent += weight * (F(y) == pop)
    return fixed, recurrent


def main():
    cases = [(2,1),(3,1),(4,1),(5,1),
             (2,2),(3,2),(4,2),(5,2),(6,2),(7,2),
             (2,3),(3,3),(4,3),(5,3),
             (2,4),(3,4),(4,4),
             (2,5),(3,5),(2,6)]
    total = 0
    for r, s in cases:
        expected = formula(r,s)
        actual = direct(r,s)
        independently_weighted = group_count_check(r,s)
        assert actual == expected == independently_weighted, (r,s,expected,actual,independently_weighted)
        total += 1 << (r*s)
        print('r=%d s=%d fixed=%d periodic=%d cycles2=%d: OK' %
              (r,s,*actual,(actual[1]-actual[0])//2))
    sample = (0,3,3,3,4)
    assert [sample := tuple(5 if 2*(sum(sample)-v)>20 else 0 if 2*(sum(sample)-v)<20 else v for v in sample) for _ in range(3)] == [(5,3,3,3,0),(0,5,5,5,5),(5,5,5,5,5)]
    print('SHARP_TRANSIENT_EXAMPLE r=5 s=5: first periodic at update 3')
    print('TOTAL_CONFIGURATIONS', total)
    print('VERIFY_OK')

if __name__ == '__main__': main()
