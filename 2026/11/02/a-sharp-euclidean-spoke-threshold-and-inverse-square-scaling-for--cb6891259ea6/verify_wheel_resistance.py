#!/usr/bin/env python3
"""Exact finite replay and independent numerical checks of a wheel resistance theorem.

Requires Python >=3.10 and only its standard library. The analytic all-orders
argument is in RESULT.md; finite computations do not substitute for that proof.
"""
from fractions import Fraction as F
from math import cos, pi, acosh, sinh, sqrt, tanh, cosh


def inverse_fraction(a):
    n = len(a)
    b = [[a[i][j] for j in range(n)] + [F(i == j) for j in range(n)]
         for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if b[i][col] != 0)
        b[col], b[pivot] = b[pivot], b[col]
        scale = b[col][col]
        b[col] = [v / scale for v in b[col]]
        for i in range(n):
            if i == col:
                continue
            factor = b[i][col]
            if factor:
                b[i] = [v - factor * w for v, w in zip(b[i], b[col])]
    return [row[n:] for row in b]


def wheel_resistance_exact(m, r):
    assert m >= 3 and r > 0
    A = [[F(r + 2) if i == j else
          F(-1) if (i - j) % m in (1, m - 1) else F(0)
          for j in range(m)] for i in range(m)]
    G = inverse_fraction(A)
    alpha = G[0][0]
    D = [[G[i][i] + G[j][j] - 2 * G[i][j]
          for j in range(m)] for i in range(m)]
    assert all(G[i][i] == alpha for i in range(m))
    assert all(D[i][j] == D[0][(j-i) % m]
               for i in range(m) for j in range(m))
    return alpha, [D[0][k] for k in range(m)]


def threshold_function(m, a):
    # exp representation prevents cosh overflow when m*a is large
    from math import exp
    t = exp(-a)
    denominator = 1 + t ** m
    return 2.0/m * sum((1-(t**k+t**(m-k))/denominator)**2
                       for k in range(m))


def threshold(m):
    lo, hi = 0.0, 20.0
    for _ in range(85):
        mid = (lo+hi)/2
        if threshold_function(m, mid) < 1:
            lo = mid
        else:
            hi = mid
    a = (lo+hi)/2
    return 4*sinh(a/2)**2, a


def continuum_threshold(c):
    if c == 0:
        return 0.0
    return 2*(1+1/(1+cosh(c))-3*tanh(c/2)/c)


def main():
    tests = 0
    for m in range(3, 12):
        crit, ac = threshold(m)
        assert abs(threshold_function(m, ac)-1) < 2e-13
        for r in (F(1, 10), F(1, 2), F(1), F(3), F(8)):
            alpha, dist = wheel_resistance_exact(m, r)
            circ2 = sum(v*v for v in dist)/(2*m)
            rad = alpha*alpha-circ2
            full = [[F(0) for _ in range(m+1)] for _ in range(m+1)]
            for i in range(m):
                full[0][i+1] = full[i+1][0] = alpha*alpha
                for j in range(m):
                    full[i+1][j+1] = dist[(j-i)%m]**2
            def quadratic(u, v):
                return sum(u[i]*full[i][j]*v[j]
                           for i in range(m+1) for j in range(m+1))
            radial = [F(m)] + [F(-1)]*m
            assert quadratic(radial, radial) == -2*m*m*rad
            for j in range(m):
                contrast = [F(0)]*(m+1)
                contrast[j+1] = F(1)
                contrast[(j+1)%m+1] = F(-1)
                assert quadratic(radial, contrast) == 0
            assert (rad > 0) == (float(r) < crit)
            assert (rad < 0) == (float(r) > crit)
            # independent exact resistance via grounded inverse, compared to
            # the closed hyperbolic Green function and Fourier coefficient.
            rf = float(r)
            t = 2/(rf+2+sqrt(rf*(rf+4)))
            C = t/((1-t*t)*(1-t**m))
            predicted_hub = C*(1+t**m)
            assert abs(float(alpha)-predicted_hub) < 3e-9*max(1,float(alpha))
            for k, d in enumerate(dist):
                predicted = 2*C*(1-t**k)*(1-t**(m-k))
                assert abs(float(d)-predicted) < 3e-9*max(1,float(d))
            for j in range(1, m):
                x = cos(2*pi*j/m)
                eig = sum(float(dist[k]**2)*cos(2*pi*j*k/m)
                          for k in range(m))
                formula = (-4*C*C*(1-t**(2*m))*(1-t*t)*(1-t)**2
                           *((1+t)**2+2*t*x)/
                           ((1-2*t*x+t*t)*(1-2*t*t*x+t**4)))
                assert eig < -1e-11
                assert abs(eig-formula) < 3e-9*max(1,abs(formula))
            tests += 1
        print('FINITE_OK', 'rim_vertices=',m, 'threshold=',f'{crit:.10f}')
    assert abs(threshold(3)[0]-(3+2*sqrt(3))) < 1e-12
    low, high = 2.0, 12.0
    for _ in range(100):
        middle = (low+high)/2
        if continuum_threshold(middle)<1:low=middle
        else: high=middle
    c=(low+high)/2
    assert 5.90319161<c<5.90319163
    for m in (20,50,100,200):
        r,a = threshold(m)
        assert abs(m*a-c) < 1e-3
        if m==200:
            assert abs(m*m*r-c*c)<0.01
    print('ASYMPTOTIC_OK c=',f'{c:.12f}','c_squared=',f'{c*c:.12f}')
    print('ALL_WHEEL_RESISTANCE_CHECKS_OK exact_cases=',tests)

if __name__ == '__main__':
    main()
