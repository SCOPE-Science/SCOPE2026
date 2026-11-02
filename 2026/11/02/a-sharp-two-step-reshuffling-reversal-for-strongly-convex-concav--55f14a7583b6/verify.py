#!/usr/bin/env python3
"""Exact-rational checks for the two-component saddle reshuffling comparison.

Uses only the Python standard library. Random examples corroborate but do not
replace the dimension-free matrix-identity proof in RESULT.md.
"""
from fractions import Fraction as F
from random import Random


def transpose(a):
    return list(map(list, zip(*a)))


def multiply(a, b):
    bt = transpose(b)
    return [[sum(x*y for x, y in zip(row, col)) for col in bt] for row in a]


def frob2(a):
    return sum(x*x for row in a for x in row)


def add(a, b, sign=1):
    return [[x+sign*y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def scalar(a, c):
    return [[c*x for x in row] for row in a]


def vec2(a, v):
    return sum(sum(x*y for x, y in zip(row, v))**2 for row in a)


def make_spd(rng, n):
    a = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            a[i][j] = a[j][i] = F(rng.randint(-2, 2))
    for i in range(n):
        a[i][i] = F(2 + sum(abs(a[i][j]) for j in range(n) if j != i))
    return a


def blocks(a, b, c):
    nx, ny = len(a), len(b)
    d = nx + ny
    h = [[F(0) for _ in range(d)] for _ in range(d)]
    k = [[F(0) for _ in range(d)] for _ in range(d)]
    for i in range(nx):
        for j in range(nx):
            h[i][j] = a[i][j]
        for j in range(ny):
            k[i][nx+j] = c[i][j]
            k[nx+j][i] = -c[i][j]
    for i in range(ny):
        for j in range(ny):
            h[nx+i][nx+j] = b[i][j]
    return h, k


def rr_iid(m, mt):
    mm = multiply(m, m)
    mtt = multiply(mt, mt)
    ab = multiply(m, mt)
    ba = multiply(mt, m)
    rr = (frob2(ab) + frob2(ba)) / 2
    iid = (frob2(mm) + frob2(mtt) + frob2(ab) + frob2(ba)) / 4
    return rr, iid


def main():
    rng = Random(424242)
    count = 0
    for n in range(1, 6):
        for i in range(80):
            m = [[F(rng.randint(-5, 5), rng.randint(1, 5))
                  for _ in range(n)] for _ in range(n)]
            mt = transpose(m)
            rr, iid = rr_iid(m, mt)
            comm = add(multiply(m, mt), multiply(mt, m), -1)
            assert rr-iid == frob2(comm)/4
            count += 1
    for nx in range(1, 4):
        for ny in range(1, 4):
            for _ in range(45):
                a, b = make_spd(rng, nx), make_spd(rng, ny)
                c = [[F(rng.randint(-3, 3)) for _ in range(ny)]
                     for _ in range(nx)]
                h, k = blocks(a, b, c)
                step = F(1, rng.randint(5, 17))
                mp = add(eye(nx+ny), scalar(add(h, k), step), -1)
                mm = add(eye(nx+ny), scalar(add(h, k, -1), step), -1)
                assert mm == transpose(mp)
                rr, iid = rr_iid(mp, mm)
                ac_cb = add(multiply(a, c), multiply(c, b), -1)
                assert rr-iid == 2*step**4*frob2(ac_cb)
                assert rr >= iid
                count += 1
    a, b, coupling, step = F(3), F(1), F(1), F(1, 8)
    mp = [[1-step*a, -step*coupling],
          [step*coupling, 1-step*b]]
    mm = transpose(mp)
    assert mp == [[F(5,8),F(-1,8)],[F(1,8),F(7,8)]]
    delta = lambda v: (vec2(multiply(mm,mp),v)
                     + vec2(multiply(mp,mm),v)
                     - vec2(multiply(mp,mp),v)
                     - vec2(multiply(mm,mm),v))/4
    assert delta([F(1),F(0)]) == F(-5, 1024)
    assert delta([F(0),F(1)]) == F(7, 1024)
    assert sum(delta([F(int(i==j)) for i in range(2)])
               for j in range(2)) == F(1,512)
    contraction = add(eye(2), multiply(transpose(mp), mp), -1)
    assert contraction == [[F(19,32),F(-1,32)],
                           [F(-1,32),F(7,32)]]
    assert contraction[0][0] > 0
    assert contraction[0][0]*contraction[1][1]-contraction[0][1]**2 > 0
    count += 6
    for _ in range(200):
        mu, delt = F(rng.randint(3, 9)), F(rng.randint(1, 2))
        coupling = F(rng.randint(1, 5))
        step = F(1, rng.randint(10, 25))
        x, y = F(rng.randint(-5, 5)), F(rng.randint(-5, 5))
        a, b = mu+delt, mu-delt
        mp = [[1-step*a, -step*coupling],
              [step*coupling, 1-step*b]]
        mm = transpose(mp)
        lhs = (vec2(multiply(mm,mp),[x,y])
              +vec2(multiply(mp,mm),[x,y])
              -vec2(multiply(mp,mp),[x,y])
              -vec2(multiply(mm,mm),[x,y]))/4
        expected = 4*step**3*delt*coupling**2*((1-step*b)*y**2-(1-step*a)*x**2)
        assert lhs == expected
        count += 1
    print(f'PASS: {count} exact-rational matrix and vector assertions')


if __name__ == '__main__':
    main()
