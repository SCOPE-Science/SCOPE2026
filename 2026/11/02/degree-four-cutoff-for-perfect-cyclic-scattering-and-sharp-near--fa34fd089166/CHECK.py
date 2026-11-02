#!/usr/bin/env python3
"""Numerical consistency tests for circulant quantum-star scattering and leakage."""
import cmath
import math

PI = math.pi


def eigenvalues(n, t, alpha, k):
    assert n >= 2 and 0 <= t <= 1 and k > 0
    gamma = 2.0 * math.atan(alpha / n)
    lam = [cmath.exp(-1j * (1 - t) * gamma)]
    lam += [-cmath.exp(1j * PI * t * (2 * j / n - 1)) for j in range(1, n)]
    return [(k - 1 + (k + 1) * x) / (k + 1 + (k - 1) * x) for x in lam]


def first_row(n, t, alpha, k):
    vals = eigenvalues(n, t, alpha, k)
    return [sum(z * cmath.exp(-2j * PI * j * ell / n)
                for j, z in enumerate(vals)) / n for ell in range(n)]


def prob(n, t, alpha, k):
    return abs(first_row(n, t, alpha, k)[1]) ** 2


def constants(n):
    h = (n - 1) // 2
    vv = [PI / 2 - PI * j / n for j in range(1, h + 1)]
    ss = [math.sin(2 * PI * j / n) for j in range(1, h + 1)]
    vs = sum(x * y for x, y in zip(vv, ss))
    ss2 = sum(y * y for y in ss)
    d = 2 * vs / ss2
    c = (8 / n) * (sum(x * x for x in vv) - vs ** 2 / ss2)
    return d, c


def golden_maximum(fun, a=0.7, b=1.5, steps=110):
    ratio = (math.sqrt(5) - 1) / 2
    x = b - ratio * (b - a)
    y = a + ratio * (b - a)
    fx, fy = fun(x), fun(y)
    for _ in range(steps):
        if fx < fy:
            a, x, fx = x, y, fy
            y = a + ratio * (b - a)
            fy = fun(y)
        else:
            b, y, fy = y, x, fx
            x = b - ratio * (b - a)
            fx = fun(x)
    return (a + b) / 2


def matrix_inverse(a):
    n = len(a)
    work = [[complex(a[i][j]) for j in range(n)] + [complex(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot = max(range(j, n), key=lambda i: abs(work[i][j]))
        work[j], work[pivot] = work[pivot], work[j]
        z = work[j][j]
        assert abs(z) > 1e-12
        work[j] = [x / z for x in work[j]]
        for i in range(n):
            if i != j:
                f = work[i][j]
                work[i] = [u - f * v for u, v in zip(work[i], work[j])]
    return [r[n:] for r in work]


def matrix_entry(n, t, alpha, k):
    gamma = 2 * math.atan(alpha / n)
    lam = [cmath.exp(-1j * (1-t) * gamma)] + [-cmath.exp(1j * PI * t * (2*j/n - 1)) for j in range(1, n)]
    u = [[sum(lam[m] * cmath.exp(2j * PI * (i-j) * m/n) for m in range(n))/n for j in range(n)] for i in range(n)]
    aa = [[((k+1) if i==j else 0) + (k-1)*u[i][j] for j in range(n)] for i in range(n)]
    bb = [[((k-1) if i==j else 0) + (k+1)*u[i][j] for j in range(n)] for i in range(n)]
    inv = matrix_inverse(aa)
    return sum(inv[0][p] * bb[p][1] for p in range(n))


def check():
    nchecks = 0
    # Independent matrix inversion versus spectral representation.
    for n in range(2, 9):
        for t, alpha, k in [(0.19,0.0,0.8),(0.67,2.3,1.31),(0.96,-1.2,2.7),(1.0,0.0,1.0)]:
            got = first_row(n,t,alpha,k)[1]
            ref = matrix_entry(n,t,alpha,k)
            assert abs(got-ref)<2e-12, (n,t,alpha,k,got,ref)
            nchecks += 1
    # Exact directed permutation at all n for t=1,k=1; n=2 Kirchhoff.
    for n in range(2, 15):
        row = first_row(n,1,2.2,1)
        assert max(abs(z - (j==1)) for j,z in enumerate(row)) < 3e-14
        nchecks += 1
    for t in [0.0, 0.14, 0.5, 0.93, 1.0]:
        row=first_row(2,t,0,1.73)
        assert abs(row[1]-1)<2e-14 and abs(row[0])<2e-14
        nchecks += 1
    # Interpolated perfect routing in degree 3 and 4 at the predicted energy.
    for n in (3,4):
        v=PI/2-PI/n
        for t in (0.01, 0.2, 0.6, 0.89, 1.0):
            k=math.tan(v)/math.tan(t*v)
            row=first_row(n,t,0,k)
            assert max(abs(z-(j==1)) for j,z in enumerate(row))<3e-13
            nchecks += 1
    # Degree >=5: exact modal tuning of the first Fourier pair leaves an unavoidable mismatch.
    for n in range(5,15):
        for t in (0.13,0.4,0.7,0.94):
            v=PI/2-PI/n
            k=math.tan(v)/math.tan(t*v)
            assert prob(n,t,0,k)<1-1e-9
            nchecks += 1
    # Optimized leakage coefficient and optimizer slope; finite differences corroborate,
    # but the infinite-dimensional claim is justified by the analytic argument, not these tests.
    for n in range(3,13):
        d,c=constants(n)
        if n>=5:
            assert c>0
            delta=0.0004
            t=1-delta
            opt=golden_maximum(lambda k: prob(n,t,0,k))
            numc=(1-prob(n,t,0,opt))/delta**2
            assert abs(numc-c)<0.003, (n,c,numc)
            assert abs((opt-1)/delta-d)<0.005, (n,d,opt)
        else:
            assert abs(c)<1e-12
        nchecks += 1
    print('VERIFY_OK', nchecks, 'checks')
    print('n=5: d=%.12f, C=%.12f; n=6: d=%.12f, C=%.12f' % (*constants(5),*constants(6)))


if __name__ == '__main__':
    check()
