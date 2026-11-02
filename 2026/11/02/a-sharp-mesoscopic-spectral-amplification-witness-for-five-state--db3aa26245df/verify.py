#!/usr/bin/env python3
"""Exact-rational checks for a five-state directed-cycle spectrum.

Requires only Python 3 standard library. Run: python verify.py
The mathematical proof and its limits are given in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def solve(a, b):
    n = len(b)
    c = [list(map(F, a[i])) + [F(b[i])] for i in range(n)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if c[i][j]), None)
        if pivot is None:
            raise ArithmeticError("singular rational matrix")
        c[j], c[pivot] = c[pivot], c[j]
        t = c[j][j]
        c[j] = [v / t for v in c[j]]
        for i in range(n):
            if i != j:
                t = c[i][j]
                if t:
                    c[i] = [u - t * v for u, v in zip(c[i], c[j])]
    return [c[i][-1] for i in range(n)]


def mats(e):
    rates = [e, F(1), e, F(1), F(1)]
    pi = [F(1), e, F(1), e, e]
    pi = [x / (2 + 3 * e) for x in pi]
    q = [[F(0)] * 5 for _ in range(5)]
    for i, a in enumerate(rates):
        q[i][i] = -a
        q[i][(i + 1) % 5] = a
    assert all(sum(row) == 0 for row in q)
    assert all(sum(pi[i] * q[i][j] for i in range(5)) == 0 for j in range(5))
    return q, pi


def spectrum(e, w, xyz):
    q, pi = mats(e)
    raw = [F(0), F(xyz[0]), F(0), F(xyz[1]), F(xyz[2])]
    mean = sum(pi[i] * raw[i] for i in range(5))
    f = [v - mean for v in raw]
    if w == 0:
        a = [[-q[i][j] + pi[j] for j in range(5)] for i in range(5)]
        u = solve(a, f)
    else:
        a = [[F(0)] * 10 for _ in range(10)]
        for i in range(5):
            for j in range(5):
                a[i][j] = -q[i][j]
                a[i + 5][j + 5] = -q[i][j]
            a[i][i + 5] = -w
            a[i + 5][i] = w
        u = solve(a, f + [F(0)] * 5)[:5]
    return 2 * sum(pi[i] * f[i] * u[i] for i in range(5))


def regenerative_spectrum_zero(e, xyz):
    x, y, z = map(F, xyz)
    m = e * (x + y + z) / (2 + 3 * e)
    var = (x - m)**2 + (y - m)**2 + (z - m)**2 + 2*(m/e)**2
    return var * e / (2 + 3 * e)


def explicit_special(e):
    g0 = 10*e*(15*e**2 + 20*e + 7)/(3*e+2)**3
    gw = 2*e*(25*e**4+133*e**3+224*e**2+129*e+21) / ((3*e+2)*(e**5+5*e**4+12*e**3+15*e**2+7*e+1))
    return g0, gw


def forms(xyz):
    x, y, z = map(F, xyz)
    s = x*x+y*y+z*z
    m = x+y+z
    b = s/2 + m*m/4
    a = s + y*z
    gap = (4*x+3*y+3*z)**2 / 4 + F(7,4)*(y-z)**2
    assert 12*b - 5*a == gap
    assert b >= 0
    if b == 0:
        assert (x, y, z) == (0,0,0)
    else:
        assert a/b <= F(12,5)
    return a,b


def run():
    tests = 0
    for xyz in product(range(-2,3), repeat=3):
        forms(xyz)
        tests += 1
    special=(-3,2,2)
    a,b = forms(special)
    assert (a,b,a/b) == (F(21),F(35,4),F(12,5))
    tests+=1
    for e,w in [(F(1,4),F(1,2)),(F(1,9),F(1,3)),(F(1,100),F(1,10)),(F(1,10000),F(1,100))]:
        g0 = spectrum(e,F(0),special)
        gw = spectrum(e,w,special)
        j0,jw=explicit_special(e)
        assert (g0,gw)==(j0,jw)
        assert g0==regenerative_spectrum_zero(e,special)
        assert gw>g0
        print('e=',str(e),'ratio=',format(float(gw/g0),'.12f'), 'eta_witness=',format(float(1-g0/gw),'.12f'))
        tests+=4
    for e in [F(1,3),F(1,8),F(1,23),F(1,100)]:
        for xyz in [(-3,2,2),(1,0,0),(0,1,1),(1,-1,0),(4,-2,3)]:
            assert spectrum(e,F(0),xyz)==regenerative_spectrum_zero(e,xyz)
            tests+=1
    e=F(1,10**6)
    g0,gw=explicit_special(e)
    assert abs(g0/e - F(35,4)) < F(1,10000)
    assert abs(gw/e - F(21)) < F(1,10000)
    assert abs(gw/g0 - F(12,5)) < F(1,10000)
    tests +=3
    print('PASS:',tests,'exact-rational groups; limiting ratio 12/5, efficiency lower bound 7/12')

if __name__ == '__main__':
    run()
