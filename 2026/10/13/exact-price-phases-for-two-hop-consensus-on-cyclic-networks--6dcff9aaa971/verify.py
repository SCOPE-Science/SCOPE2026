#!/usr/bin/env python3
"""Numerical spot checks for a two-orbit Laplacian spectral-gap theorem.

The accompanying analytic proof, not these finite tests, establishes the theorem.
Run: python3 verify.py (Python 3 standard library only).
"""
import math
import random


def candidate(n, t):
    assert n >= 5 and t > 0
    mu = 4.0 * math.sin(math.pi / n)**2
    nu = 4.0 * math.sin(math.pi * (n // 2) / n)**2
    eta = mu + nu - 4.0
    r, q = max(0.0, 4.0 - nu), 4.0 - mu
    assert eta > 0 and 0 <= r < q
    if t <= r:
        a, b, mode = 0.0, 1.0 / (n * t), "two-hop"
        opt = nu * r / (n * t)
    elif t >= q:
        a, b, mode = 1.0 / n, 0.0, "nearest"
        opt = mu / n
    else:
        a, b, mode = eta / (n * (t + eta)), 1.0 / (n * (t + eta)), "balanced"
        opt = mu * nu / (n * (t + eta))
    return a, b, mode, opt, (mu, nu, eta, r, q)


def uniform_gap(n, a, b):
    return min(4.0 * a * math.sin(math.pi * k / n)**2
               + 4.0 * b * math.sin(2.0 * math.pi * k / n)**2
               for k in range(1, n))


def jacobi_eigenvalues(matrix):
    """Symmetric Jacobi diagonalization, for small numerical spot checks."""
    n = len(matrix)
    a = [row[:] for row in matrix]
    for unused in range(75 * n * n):
        p, q = 0, 1
        z = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > z:
                    p, q, z = i, j, abs(a[i][j])
        if z < 1e-13:
            break
        tau = (a[q][q] - a[p][p]) / (2.0 * a[p][q])
        rot = (1.0 if tau >= 0 else -1.0) / (abs(tau) + math.sqrt(1.0 + tau*tau))
        cs = 1.0 / math.sqrt(1.0 + rot*rot)
        sn = rot * cs
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        a[p][p] = app - rot * apq
        a[q][q] = aqq + rot * apq
        a[p][q] = a[q][p] = 0.0
        for k in range(n):
            if k == p or k == q:
                continue
            akp, akq = a[k][p], a[k][q]
            a[k][p] = a[p][k] = cs * akp - sn * akq
            a[k][q] = a[q][k] = sn * akp + cs * akq
    else:
        raise AssertionError("Jacobi iterations did not converge")
    return sorted(a[i][i] for i in range(n))


def laplacian_gap(n, one, two):
    m = [[0.0 for _ in range(n)] for _ in range(n)]
    for distance, rates in ((1, one), (2, two)):
        for i, rate in enumerate(rates):
            j = (i + distance) % n
            m[i][i] += rate
            m[j][j] += rate
            m[i][j] -= rate
            m[j][i] -= rate
    vals = jacobi_eigenvalues(m)
    assert abs(vals[0]) < 1e-10
    return max(0.0, vals[1])


def main():
    rng = random.Random(130617)
    uniform_tests = nonuniform_tests = boundary_tests = 0
    for n in range(5, 41):
        mu = 4.0 * math.sin(math.pi/n)**2
        nu = 4.0 * math.sin(math.pi*(n//2)/n)**2
        r, q = max(0.0, 4.0-nu), 4.0-mu
        prices = [1e-4, .005, .02, .2, .6, 1.0, 1.5, 2.0, 3.0, 4.0, 7.0, 80.0]
        if r > 0:
            prices.extend([r/2, r, r*1.5])
        prices.extend([q/2, q, q*1.5])
        for t in prices:
            a, b, mode, claimed, params = candidate(n, t)
            assert abs(n*(a+t*b)-1.0) < 1e-11
            gap = uniform_gap(n, a, b)
            assert abs(gap-claimed) <= 1e-10 * max(1.0, claimed), (n,t,mode,gap,claimed)
            for case in range(40):
                b0 = rng.random()/(n*t)
                a0 = (1.0/n)-t*b0
                assert uniform_gap(n,a0,b0) <= claimed + 5e-12
                uniform_tests += 1
        if r > 0:
            a,b,mode,claimed,_=candidate(n, r)
            assert abs(claimed-nu/n)<1e-9
            boundary_tests += 1
        a,b,mode,claimed,_=candidate(n,q)
        assert abs(claimed-mu/n)<1e-9
        boundary_tests += 1

    for n in range(5, 14):
        for t in (.05, .4, 1.0, 2.5, 4.0, 8.0):
            _,_,_,opt,_=candidate(n,t)
            for case in range(18):
                u=[.02+rng.random() for j in range(n)]
                v=[.02+rng.random() for j in range(n)]
                z = sum(u)+t*sum(v)
                u=[x/z for x in u]
                v=[x/z for x in v]
                value=laplacian_gap(n,u,v)
                assert value <= opt+2e-10, (n,t,case,value,opt)
                nonuniform_tests += 1

    for n in (5,7,9,11,13):
        a,b,mode,opt,_=candidate(n, 1e-4)
        assert mode == 'two-hop' and a == 0 and opt > 0
    for n in (6,8,10,12):
        assert abs(uniform_gap(n, 0, 1/n)) < 1e-12
    print('VERIFY_OK uniform_tests=%d nonuniform_matrix_tests=%d '
          'boundary_tests=%d parity_tests=9' % (uniform_tests, nonuniform_tests, boundary_tests))

if __name__ == '__main__':
    main()
