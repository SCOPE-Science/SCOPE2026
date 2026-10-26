"""Numerical cross-checks for the finite-cycle mean-zero mixed Sobolev constant.

Requires Python 3 standard library. Numerical checks complement but do not replace
analytical proof of the all-order asymptotic and sharpness.
"""
import math


def h_spectral(n, t):
    return 2 * math.sqrt(t) / n * sum(
        1 / (t + 4 * math.sin(math.pi * k / n) ** 2)
        for k in range(1, n)
    )


def h_closed(n, t):
    y = math.asinh(math.sqrt(t) / 2)
    a = 1 / math.cosh(y)
    z = 2 * n * y
    tail = 0 if z > 740 else 2 / math.expm1(z)
    return a * (1 + tail) - 2 / (n * math.sqrt(t))


def maximize(n):
    # Golden-section search on logarithmic t; independent of any eigenvectors.
    aa, bb = -35.0, 5.0
    phi = (math.sqrt(5) - 1) / 2
    c = bb - phi * (bb - aa)
    d = aa + phi * (bb - aa)
    fc, fd = h_closed(n, math.exp(c)), h_closed(n, math.exp(d))
    for _ in range(220):
        if fc > fd:
            bb, d, fd = d, c, fc
            c = bb - phi * (bb - aa)
            fc = h_closed(n, math.exp(c))
        else:
            aa, c, fc = c, d, fd
            d = aa + phi * (bb - aa)
            fd = h_closed(n, math.exp(d))
    t = math.exp((aa + bb) / 2)
    return t, h_closed(n, t)


def green(n, t):
    return [sum(math.cos(2 * math.pi * k * j / n) /
                (t + 4 * math.sin(math.pi * k / n) ** 2)
                for k in range(1, n)) / n
            for j in range(n)]


def norm_ratio(n, t):
    u = green(n, t)
    sqnorm = sum(x*x for x in u)
    grad = sum((u[(j + 1) % n] - u[j]) ** 2 for j in range(n))
    return u[0]**2 / math.sqrt(sqnorm * grad), grad / sqnorm


def main():
    for n in [3, 4, 5, 6, 7, 9, 12, 20, 30, 50, 80]:
        t, constant = maximize(n)
        direct = h_spectral(n, t)
        check, energy_ratio = norm_ratio(n, t)
        assert abs(constant-direct) < 1e-10, (n,'resolvent',constant,direct)
        assert abs(check-constant) < 2e-9, (n,'sharpness',check,constant)
        assert abs(energy_ratio-t) < 2e-7, (n,'stationarity',energy_ratio,t)
        assert constant < 1, (n,'strict',constant)
        if n == 3:
            assert abs(constant - 2 / (3*math.sqrt(3))) < 1e-10
            assert abs(t - 3) < 1e-6
        print('N=%d t=%.10f C=%.12f ratio=%.12f'%(n,t,constant,check))
    for n in [100, 500, 1000, 10000, 100000]:
        t, constant = maximize(n)
        eps = n ** (-2/3)
        approx = 1-1.5*eps+0.375*eps**2+0.0625*eps**3
        assert abs(constant - approx) < 3 * eps**4, (n,constant,approx)
        assert abs(t/eps-4-4*eps) < 20*eps**2, (n,t/eps,eps)
        print('N=%d N^(2/3)*t=%.10f C=%.12f expansion=%.12f'%(n,t/eps,constant,approx))
    print('all checks passed')


if __name__ == '__main__':
    main()
