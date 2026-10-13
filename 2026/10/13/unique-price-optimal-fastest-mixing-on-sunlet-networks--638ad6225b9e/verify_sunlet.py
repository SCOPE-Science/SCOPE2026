#!/usr/bin/env python3
"""Reproducible finite checks for priced spectral-gap optimization on sunlet graphs.

Python standard library only. Finite checks support, but do not replace,
the universally quantified analytical proof in RESULT.md.
"""
from fractions import Fraction as F
from math import sin, pi, sqrt
from random import Random


def formula(n, t):
    mu = 4*sin(pi/n)**2
    chi = sqrt(mu*t)
    lam = mu/(n*(2+mu*t+2*chi))
    a = lam*(1+1/chi)
    b = lam*(2+chi)/mu
    return lam, a, b


def laplacian(n, spokes, rim):
    m = 2*n
    L = [[0.0]*m for _ in range(m)]
    for j in range(n):
        for p, q, weight in [(j, n+j, spokes[j]), (j, (j+1)%n, rim[j])]:
            L[p][p] += weight
            L[q][q] += weight
            L[p][q] -= weight
            L[q][p] -= weight
    return L


def jacobi_eigenvalues(A):
    A = [row[:] for row in A]
    N = len(A)
    # Classical max-pivot Jacobi method, converged to relative tolerance.
    for _ in range(50*N*N):
        p, q = 0, 1
        best = 0.0
        for i in range(N):
            for j in range(i+1,N):
                v = abs(A[i][j])
                if v > best:
                    p, q, best = i, j, v
        scale = max(1.0, max(abs(A[i][i]) for i in range(N)))
        if best < 2e-14*scale:
            break
        apq, app, aqq = A[p][q], A[p][p], A[q][q]
        tau = (aqq-app)/(2*apq)
        sign = 1 if tau >= 0 else -1
        tt = sign/(abs(tau)+sqrt(1+tau*tau))
        c = 1/sqrt(1+tt*tt)
        s = tt*c
        A[p][p] = app - tt*apq
        A[q][q] = aqq + tt*apq
        A[p][q] = A[q][p] = 0.0
        for k in range(N):
            if k != p and k != q:
                akp, akq = A[k][p], A[k][q]
                A[k][p] = A[p][k] = c*akp-s*akq
                A[k][q] = A[q][k] = s*akp+c*akq
    else:
        raise AssertionError('Jacobi did not converge')
    return sorted(A[i][i] for i in range(N))


def run():
    exact = 0
    for n, mu in [(3,F(3)),(4,F(2)),(6,F(1))]:
        for k in range(1, 15):
            chi = F(k)
            t = chi*chi/mu
            lam = mu/(n*(2+mu*t+2*chi))
            a = lam*(1+1/chi)
            b = lam*(2+chi)/mu
            y = mu*b/2
            assert n*(t*a+b) == 1
            assert (a-lam)*(y-lam) == lam*lam/2
            assert (a+b*mu-lam)*(a-lam)-a*a == 0
            assert a > lam > 0 and b > 0
            exact += 4
    rng = Random(420602)
    eig = 0
    feasible = 0
    max_error = 0.0
    for n in [3,4,5,6,8,11]:
        for t in [0.007, 0.1, 0.5, 1, 7, 70]:
            opt,a,b = formula(n,t)
            vals = jacobi_eigenvalues(laplacian(n,[a]*n,[b]*n))
            err = abs(vals[1]-opt)
            max_error = max(max_error,err)
            assert err < 1e-10*max(1,opt), (n,t,vals[1],opt)
            assert abs(n*(t*a+b)-1)<2e-13
            eig += 1
            for _ in range(30):
                raw = [rng.expovariate(1) for _ in range(2*n)]
                spend = t*sum(raw[:n])+sum(raw[n:])
                aa = [z/spend for z in raw[:n]]
                bb = [z/spend for z in raw[n:]]
                feasible_gap = jacobi_eigenvalues(laplacian(n,aa,bb))[1]
                assert feasible_gap <= opt+3e-11*max(1,opt), (n,t,feasible_gap,opt)
                feasible += 1
    print('VERIFY_OK', exact, 'exact rational identities;', eig,
          'optimized full Laplacian eigenspectra;', feasible,
          'nonsymmetric feasible comparisons; max absolute gap error',
          f'{max_error:.3e}')


if __name__ == '__main__':
    run()
