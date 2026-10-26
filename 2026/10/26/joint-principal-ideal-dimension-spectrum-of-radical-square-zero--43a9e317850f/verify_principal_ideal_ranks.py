#!/usr/bin/env python3
"""Independent finite-field checks of principal one-sided ideal rank enumerators.

Requires only Python 3. Counts literal ranks of matrices of left/right
multiplication, comparing them with independently enumerated edge supports.
"""
from collections import Counter
from itertools import product


def add(a, b, q):
    return (a ^ b) if q == 4 else (a + b) % q


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    # F_4 = F_2[t]/(t^2+t+1), elements a0+a1*t.
    a0, a1, b0, b1 = a & 1, a >> 1, b & 1, b >> 1
    return ((a0*b0+a1*b1) & 1) | (((a0*b1+a1*b0+a1*b1) & 1) << 1)


def inv(a, q):
    if q == 4:
        return next(b for b in range(1, 4) if mul(a, b, 4) == 1)
    return pow(a, -1, q)


def neg(a, q):
    return a if q == 4 else (-a) % q


def rank(columns, q):
    m = len(columns[0])
    a = [list(row) for row in zip(*columns)]
    nr, nc, r = len(a), len(a[0]), 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if a[i][c]), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        z = inv(a[r][c], q)
        a[r] = [mul(z, t, q) for t in a[r]]
        for i in range(nr):
            if i == r or a[i][c] == 0:
                continue
            f = neg(a[i][c], q)
            a[i] = [add(x, mul(f, y, q), q) for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def literal_bivariate(n, arrows, q):
    m = len(arrows)
    total = Counter()
    for scalars in product(range(q), repeat=n):
        for coeff in product(range(q), repeat=m):
            # Multiplication basis e_0,...,e_(n-1), arrows a_0,...,a_(m-1).
            left, right = [], []
            for v in range(n):
                lcol, rcol = [0]*(n+m), [0]*(n+m)
                lcol[v] = rcol[v] = scalars[v]
                for i, (u, w) in enumerate(arrows):
                    if w == v:
                        lcol[n+i] = coeff[i]
                    if u == v:
                        rcol[n+i] = coeff[i]
                left.append(lcol)
                right.append(rcol)
            for i, (u, v) in enumerate(arrows):
                lcol, rcol = [0]*(n+m), [0]*(n+m)
                lcol[n+i], rcol[n+i] = scalars[u], scalars[v]
                left.append(lcol)
                right.append(rcol)
            total[(rank(left, q), rank(right, q))] += 1
    return total


def support_bivariate(n, arrows, q):
    out = Counter(u for u, v in arrows)
    inc = Counter(v for u, v in arrows)
    answer = Counter()
    for bits in product((0, 1), repeat=n):
        zero = {v for v, b in enumerate(bits) if b}
        internal = [(u, v) for u, v in arrows if u in zero and v in zero]
        baseL = sum(1+out[v] for v in range(n) if v not in zero)
        baseR = sum(1+inc[v] for v in range(n) if v not in zero)
        outside = (q-1)**(n-len(zero)) * q**(len(arrows)-len(internal))
        for active in product((0, 1), repeat=len(internal)):
            F = [e for e, flag in zip(internal, active) if flag]
            k = len(F)
            rl = baseL + len({v for u, v in F})
            rr = baseR + len({u for u, v in F})
            answer[(rl, rr)] += outside*(q-1)**k
    return answer


def run():
    configs = [
        (1, []), (1, [(0,0)]), (1, [(0,0),(0,0)]),
        (2, [(0,1)]), (2, [(1,0)]), (2, [(0,0)]),
        (2, [(0,1),(0,1)]), (2, [(0,1),(1,0)]),
        (2, [(0,0),(0,1)]), (2, [(0,0),(1,1)]),
        (3, [(0,1),(0,2)]), (3, [(1,0),(2,0)]),
        (3, [(0,1),(1,2)]), (3, [(0,1),(2,1)]),
        (3, [(0,1),(1,0)]), (3, [(0,0),(1,2)]),
        (3, [(0,0),(0,0),(0,1)]),
        (3, [(0,1),(1,2),(2,0)]),
        (3, [(0,1),(0,1),(1,2)]),
        (4, [(0,1),(0,2),(0,3)])
    ]
    checked = 0
    for q in (2,3,4):
        for n, edges in configs:
            if q == 4 and (n + len(edges) > 5):
                continue
            expected = support_bivariate(n, edges, q)
            actual = literal_bivariate(n, edges, q)
            assert actual == expected, (q, n, edges, actual, expected)
            assert sum(expected.values()) == q**(n+len(edges))
            checked += 1
    assert {r: v for (r,s),v in literal_bivariate(3, [(0,1),(0,2)], 2).items() if False} == {}
    for arrows, expected in [
        ([(0,1),(0,2)], {0:1,1:6,2:9,3:4,4:8,5:4}),
        ([(1,0),(2,0)], {0:1,1:7,2:4,3:12,4:4,5:4}),
        ([(0,1),(1,2)], {0:1,1:4,2:9,3:10,4:4,5:4}),
    ]:
        got = Counter()
        for (rl, rr), count in literal_bivariate(3, arrows, 2).items():
            got[rl] += count
        assert got == expected
    print('VERIFY_OK_PRINCIPAL_RANK_BIVARIATE', checked, 'finite-field graph configurations')
    print('VERIFIED_ORIENTATION_STAR_PATH', 'F2 3-vertex marginal counts')


if __name__ == '__main__':
    run()
