#!/usr/bin/env python3
from fractions import Fraction
from itertools import product


def rank_q(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = a[r][c]
        a[r] = [x / inv for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                f = a[i][c]
                a[i] = [x - f*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def marginal_constraint_nullity(q, n):
    states = list(range(q))
    cells = list(product(states, repeat=n))
    index = {x:i for i,x in enumerate(cells)}
    rows = []
    for coord in range(n):
        other = [j for j in range(n) if j != coord]
        for vals in product(states, repeat=n-1):
            row = [0] * len(cells)
            for s in states:
                x = [None] * n
                x[coord] = s
                for j, v in zip(other, vals):
                    x[j] = v
                row[index[tuple(x)]] = 1
            rows.append(row)
    return len(cells) - rank_q(rows)


def parity_law(theta, n):
    theta = Fraction(theta)
    law = {}
    for x in product((0,1), repeat=n):
        sign = -1 if sum(x) % 2 else 1
        law[x] = Fraction(1, 2**n) * (1 + theta * sign)
    assert sum(law.values()) == 1
    assert all(v >= 0 for v in law.values())
    return law


def marginal(law, keep):
    out = {}
    for x, p in law.items():
        key = tuple(x[i] for i in keep)
        out[key] = out.get(key, Fraction(0)) + p
    return out


cases = [(2,3),(2,4),(3,3),(3,4),(4,3)]
for q, n in cases:
    got = marginal_constraint_nullity(q, n)
    want = (q-1)**n
    print(f'q={q} n={n} nullity={got} expected={want}')
    assert got == want

for n in range(3,8):
    for theta in (Fraction(-1,2), Fraction(0), Fraction(1,2)):
        law = parity_law(theta, n)
        for r in range(1, n):
            # Checking one representative is enough by symmetry, but check all subsets.
            from itertools import combinations
            for keep in combinations(range(n), r):
                mar = marginal(law, keep)
                target = Fraction(1, 2**r)
                assert len(mar) == 2**r
                assert all(v == target for v in mar.values())
print('VERIFY_OK')
