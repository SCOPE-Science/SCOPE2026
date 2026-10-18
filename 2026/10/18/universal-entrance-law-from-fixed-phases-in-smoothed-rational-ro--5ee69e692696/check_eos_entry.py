"""Finite numerical checks for the fixed-phase entrance law in EOS maps.

Run: python check_eos_entry.py
Standard library only; numerical tests do not prove asymptotic statements.
"""
import math


def logistic(z):
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    e = math.exp(z)
    return e / (1.0 + e)


def f(x, a, k, n):
    return x + k / n - logistic(a * x)


def return_map(x, a, k, n):
    for _ in range(n):
        x = f(x, a, k, n)
    return x


def entry(n, k, a, x0, tau):
    h = 1 / (2 * n)
    q = math.exp(-a * h)
    m = int(math.floor(tau / (a * q)))
    x = x0
    for _ in range(m):
        x = return_map(x, a, k, n)
    return m, a * (x - h)


def hitting(n, k, a, x0, theta):
    h = 1 / (2 * n)
    q = math.exp(-a * h)
    x = x0
    m = 0
    while math.exp(-a * abs(x - h)) < theta:
        x = return_map(x, a, k, n)
        m += 1
        assert m < 200000, 'diagnostic run exceeded bounded range'
    return a * q * m


def main():
    tests = 0
    for n, k in [(2, 1), (3, 1), (5, 2), (7, 3)]:
        h = 1 / (2 * n)
        for a_scale, tolerance in [(24, 0.045), (30, 0.017)]:
            a = a_scale * n
            q = math.exp(-a * h)
            for frac in [-0.18, +0.18]:
                x0 = h + frac / n
                for tau in [0.4, 0.7, 1.2]:
                    m, observed = entry(n, k, a, x0, tau)
                    expected = math.copysign(-math.log(math.tanh(tau)), frac)
                    assert abs(observed - expected) < tolerance, (n, k, a, frac, tau, observed, expected)
                    tests += 1
                theta = 0.5
                measured = hitting(n, k, a, x0, theta)
                target = math.atanh(theta)
                assert abs(measured - target) < 0.030, (n, k, a, frac, measured, target)
                tests += 1
            for frac in [0.18, 0.50, 0.82]:
                x = frac / n
                disp = return_map(x, a, k, n) - x
                p = lambda z: 1 / (1 + math.exp(a * z))
                approx = p(x) - p(1 / n - x)
                error = abs(disp - approx)
                assert error < 150 * a * q * q, (n, k, a, frac, error, a * q * q)
                tests += 1
    print('PASS:', tests, 'finite diagnostics; exact theorem requires analysis')


if __name__ == '__main__':
    main()
