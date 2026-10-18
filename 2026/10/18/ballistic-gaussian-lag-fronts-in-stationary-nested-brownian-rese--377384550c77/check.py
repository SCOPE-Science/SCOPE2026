"""Reproduce finite algebraic and numerical checks for a directed resetting chain.

Requires Python >=3.9 and only standard-library packages.
All universal conclusions are proved analytically in the accompanying result.
"""
import math
from fractions import Fraction


def forward(j, u):
    assert j >= 2 and u >= 0
    n = j - 1
    term = math.exp(-u) * (0.5 ** n)
    ans = term
    for k in range(1, n + 1):
        term *= (2.0 * u) / k
        ans += term
    return ans   # normalized by q=2D/r


def reverse(j, u):
    return (0.5 ** (j - 1)) * math.exp(-u)


def peak_equation(j, u):
    # H_n(u)-1, where H_n is strictly decreasing in u.
    n = j - 1
    term = 1.0
    ans = 0.0
    for m in range(1, n + 1):
        term *= (n - m + 1) / (2.0 * u)
        ans += term
    return ans - 1.0


def peak(j):
    lo, hi = 1e-3, float(2 * j)
    assert peak_equation(j, lo) > 0 and peak_equation(j, hi) < 0
    for _ in range(85):
        mid = (lo + hi) / 2
        if peak_equation(j, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def close(a, b, atol=1e-12, rtol=1e-10):
    return abs(a - b) <= atol + rtol * max(abs(a), abs(b))


def main():
    ntests = 0
    # Exact finite sums prove the integrated forward/backward imbalance.
    for j in range(2, 39):
        a = sum(Fraction(1, 2 ** (j - 1 - k)) for k in range(j))
        b = Fraction(1, 2 ** (j - 1))
        assert a == 2 * (1 - Fraction(1, 2 ** j))
        assert b == 2 * Fraction(1, 2 ** j)
        assert a / b == 2 ** j - 1
        ntests += 3
    # Kernel differential system and boundary condition; each test independent
    # of simulation and includes positive and zero times.
    for j in range(2, 31):
        for u in (0.0, .125, .5, 1.0, 2.5, 8.0, 20.0):
            c = forward(j, u)
            assert c <= 1 + 1e-12
            assert c > 0
            assert reverse(j, u) <= c * (1 + 1e-12)
            if u == 0:
                assert close(c, 2 ** (1 - j))
            else:
                # d C_j /du = C_{j-1} - C_j; at j=2 upstream
                # C_1(u)=exp(-u) (time covariance of upstream X_1).
                h = 1e-5
                upstream = (math.exp(-u) if j == 2 else forward(j - 1, u))
                numerical = (forward(j, u + h) - forward(j, u - h)) / (2 * h)
                assert close(numerical, upstream - c, atol=5e-9, rtol=5e-7)
            ntests += 4
    # Unique peak and monotonicity on either side, exact small cases.
    for j in range(2, 121):
        u = peak(j)
        assert abs(peak_equation(j, u)) < 3e-13
        assert forward(j, .9 * u) < forward(j, u)
        assert forward(j, 1.1 * u) < forward(j, u)
        if j == 2:
            assert close(u, .5)
        if j == 3:
            assert close(u, (1 + math.sqrt(3)) / 2)
        ntests += 5
    # Quantitative asymptotics: mean directed propagation and Gaussian front.
    for j in (80, 120, 180, 260):
        u = peak(j)
        assert abs(u - (j - 2)) < 3 / j
        scaled = math.sqrt(j) * forward(j, u)
        assert abs(scaled - math.sqrt(2 / math.pi)) < .04
        for s in (-1.5, -.5, 0.0, .5, 1.5):
            value = math.sqrt(j) * forward(j, j + s * math.sqrt(j))
            predicted = math.sqrt(2 / math.pi) * math.exp(-s * s / 2)
            assert abs(value - predicted) < .10
            ntests += 1
        ntests += 2
    print(f'PASS: {ntests} deterministic assertions; no external packages')
    for j in (2, 3, 10, 30, 100, 260):
        u = peak(j)
        print(f'j={j:3d} peak_rt={u:.9f}  peak_normalized={forward(j,u):.10f}')


if __name__ == '__main__':
    main()
