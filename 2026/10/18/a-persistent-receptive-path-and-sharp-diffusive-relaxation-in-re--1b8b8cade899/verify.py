#!/usr/bin/env python3
"""Reproduce finite rational checks for repulsive bounded-confidence dynamics.

Requires Python 3 standard library only. The infinity-time assertions rest on the
analytic Perron and Markov-chain argument, not on finite iteration.
"""
from fractions import Fraction as F
from math import cos, sin, pi, sqrt
from random import Random


def step(x, c):
    z = []
    for i, xi in enumerate(x):
        neighbors = [j for j, xj in enumerate(x) if abs(xj - xi) < c]
        terms = []
        for j in neighbors:
            if j == i:
                terms.append(x[j])
            elif x[j] < xi:
                terms.append(x[j] + c)
            elif x[j] > xi:
                terms.append(x[j] - c)
            else:
                terms.append(x[j] + (c if j < i else -c))
        z.append(sum(terms, F(0)) / len(terms))
    return z


def qtimes(g):
    m = len(g)
    assert m >= 2
    z = []
    for j in range(m):
        d = F(1, 6) if j in (0, m - 1) else F(1, 3)
        v = d * g[j]
        if j:
            v += g[j-1] / 3
        if j < m - 1:
            v += g[j+1] / 3
        z.append(v)
    return z


def path_graph(x, c):
    n = len(x)
    return all((abs(x[i] - x[j]) < c) == (abs(i-j) == 1)
               for i in range(n) for j in range(i+1, n))


def sturm_count(z, m):
    """Number of eigenvalues strictly below z, via symmetric LDL pivots."""
    p = 1/6 - z
    count = int(p < 0)
    for j in range(1, m):
        if abs(p) < 1e-15:
            p = -1e-15
        diag = 1/6 if j == m-1 else 1/3
        p = diag - z - (1/9)/p
        count += int(p < 0)
    return count


def perron_eigenvalue(m):
    lo, hi = 0., 1.
    for _ in range(60):
        mid = (lo + hi)/2
        if sturm_count(mid, m) == m:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def run():
    rng = Random(20230105)
    count = 0
    for n in range(3, 13):
        c = F(7, 5)
        for trial in range(8):
            deficits = [F(rng.randint(1, 30), 100) * c for _ in range(n-1)]
            offset = F(rng.randint(-30, 30), 11)
            x = [offset]
            for g in deficits:
                x.append(x[-1] + c - g)
            y = [x[i] - i*c for i in range(n)]
            weights = [2] + [3]*(n-2) + [2]
            mean = sum((weights[i]*y[i] for i in range(n)), F(0))/sum(weights)
            for t in range(12):
                assert path_graph(x, c)
                assert deficits == [c - (x[j+1]-x[j]) for j in range(n-1)]
                assert all(F(0) < a <= c/2 for a in deficits)
                assert sum((weights[i]*(x[i]-i*c) for i in range(n)), F(0))/sum(weights) == mean
                nxt = step(x, c)
                next_deficits = qtimes(deficits)
                assert [c - (nxt[j+1]-nxt[j]) for j in range(n-1)] == next_deficits
                x, deficits = nxt, next_deficits
                count += 1
    for n in (3, 4):
        c = F(1)
        for trial in range(40):
            increments = [F(rng.randint(1, 10), 100) for _ in range(n-1)]
            init = [F(-1, 3)]
            for d in increments:
                init.append(init[-1] + d)
            assert init[-1]-init[0] < c
            t1 = step(init, c)
            avg = sum(init, F(0))/n
            assert t1 == [avg+c*F(2*i-n+1, n) for i in range(n)]
            assert path_graph(t1, c)
            assert all(F(0)<c-(t1[i+1]-t1[i])<=c/2 for i in range(n-1))
            count += 1
    expected = (3 + sqrt(33))/12
    assert abs(perron_eigenvalue(2) - .5) < 1e-12
    assert abs(perron_eigenvalue(3) - expected) < 1e-12
    for n in (3,4,5,8,12,20,50,100):
        rho = perron_eigenvalue(n-1)
        upper=(1 + 2*cos(pi/n))/3
        lower=upper-2*sin(pi/n)**2/(3*n)
        assert lower-2e-12 <= rho <= upper+2e-12
        assert 0 < rho < 1
    print('VERIFY_OK', 'rational_state_transitions', count, 'spectral_brackets', 8)
    print('rho3', perron_eigenvalue(2), 'rho4', perron_eigenvalue(3))
    print('n100_scaled_deficit', 10000*(1-perron_eigenvalue(99)), 'limit_pi_squared_over3',pi*pi/3)

if __name__=='__main__':
    run()
