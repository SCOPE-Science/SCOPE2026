#!/usr/bin/env python3
"""Independent binary cut-rank enumeration for cyclic local graph states."""
from itertools import product

def rank_gf2(rows):
    piv = {}
    for row in rows:
        x = row
        while x:
            p = x.bit_length() - 1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p] = x
                break
    return len(piv)

def matrix(n):
    return [sum(1 << ((i + t) % n) for t in (-2, -1, 0, 1)) for i in range(n)]

def predicted(d, t, u):
    if d % 4:
        return 1 if (d + u - t) % 4 == 0 else 2
    return 0 if t == u and t in (-1, 0) else 1

def check():
    cnt = [0, 0, 0]
    tested = 0
    for n in range(4, 65, 4):
        B = matrix(n)
        r = rank_gf2(B)
        assert r == n - 3, (n, r)
        for d, t, u in product(range(1, n), (-2,-1,0,1), (-2,-1,0,1)):
            rows = B.copy()
            rows[0] ^= 1 << (t % n)
            rows[d] ^= 1 << ((d + u) % n)
            got = rank_gf2(rows) - r
            want = predicted(d, t, u)
            assert got == want, (n,d,t,u,got,want)
            cnt[got] += 1
            tested += 1
        print(f'n={n}: base={r}, all {16*(n-1)} distinct-row pairs pass')
    print(f'PASS: {tested} complete double-deletion configurations; outcome counts 0,1,2 = {tuple(cnt)}')
if __name__ == '__main__':
    check()
