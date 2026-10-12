#!/usr/bin/env python3
import cmath
import math


def beta(n, j):
    return math.pi * (2.0*j/n - 1.0)


def lambda_j(n, alpha, t, j):
    gamma = cmath.phase((n + 1j*alpha)/(n - 1j*alpha))
    if j == 0:
        return cmath.exp(-1j*(1.0-t)*gamma)
    return -cmath.exp(1j*beta(n,j)*t)


def mu_source(n, alpha, k, t, j):
    lam = lambda_j(n, alpha, t, j)
    return (k - 1.0 + (k + 1.0)*lam)/(k + 1.0 + (k - 1.0)*lam)


def mu_half_angle(n, k, t, j):
    b = beta(n,j)
    if abs(b) < 1e-15:
        return -1.0 + 0j
    c = 1.0/math.tan(b*t/2.0)
    return (k - 1j*c)/(k + 1j*c)


def nu(n, xi, j):
    if j == 0:
        return 1.0 + 0j
    b = beta(n,j)
    return (b*xi - 2j)/(b*xi + 2j)


def r_from_modes(n, xi):
    return sum(nu(n,xi,j) for j in range(n))/n


def f(b, xi):
    return (b*b*xi*xi - 4.0)/(b*b*xi*xi + 4.0)


def r_paired(n, xi):
    if n % 2:
        return (1.0 + 2.0*sum(f(beta(n,j),xi) for j in range(1,(n-1)//2+1)))/n
    return (2.0/n)*sum(f(beta(n,j),xi) for j in range(1,n//2))


def bisect_root(n):
    lo, hi = 0.0, 10.0
    for _ in range(100):
        mid = (lo+hi)/2.0
        if r_paired(n,mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2.0


def main():
    # Exact source-vs-half-angle identity for all nonzero beta modes, tested numerically.
    for n in range(3,10):
        for j in range(1,n):
            for k,t in [(2.7,0.17),(19.0,0.031)]:
                a = mu_source(n, 1.3, k, t, j)
                b = mu_half_angle(n, k, t, j)
                assert abs(a-b) < 2e-12, (n,j,k,t,a,b)

    # Joint limit kt -> xi, including alpha independence of the limit.
    for n in [3,4,5,6,9]:
        for xi in [0.4,1.2,3.0]:
            for alpha in [-7.0,0.0,2.5]:
                k = 2.0e6
                t = xi/k
                errs = [abs(mu_source(n,alpha,k,t,j)-nu(n,xi,j)) for j in range(n)]
                assert max(errs) < 3e-6, (n,xi,alpha,max(errs))

    # Paired closed form and reality.
    for n in range(3,13):
        for xi in [0.1,0.8,1.7,5.0]:
            a = r_from_modes(n,xi)
            b = r_paired(n,xi)
            assert abs(a.imag) < 2e-14
            assert abs(a.real-b) < 2e-14

    # Strict monotonicity on representative grids; analytic proof is in RESULT.md.
    for n in range(3,13):
        xs = [0.02 + 0.02*i for i in range(600)]
        rs = [r_paired(n,x) for x in xs]
        assert all(rs[i+1] > rs[i] for i in range(len(rs)-1))

    x3 = bisect_root(3)
    x4 = bisect_root(4)
    assert abs(x3 - 2.0*math.sqrt(3.0)/math.pi) < 2e-13
    assert abs(x4 - 4.0/math.pi) < 2e-13
    assert abs(r_paired(3,x3)) < 1e-14
    assert abs(r_paired(4,x4)) < 1e-14

    # Endpoint reflection/transmission checks.
    for n in range(3,11):
        r0 = -(n-2.0)/n
        T0 = 1.0-r0*r0
        assert abs(T0 - 4.0*(n-1)/(n*n)) < 1e-15

    print('VERIFY_OK', 'xi3=%.15g' % x3, 'xi4=%.15g' % x4)


if __name__ == '__main__':
    main()
