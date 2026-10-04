#!/usr/bin/env python3
import math


def c_r(r):
    return math.exp(r*math.log(r) - (r + 1.0)*math.log(r + 1.0))


def optimal_b(r):
    c = c_r(r)
    lo, hi = 1.0, 2.0
    def F(b):
        return (b - 1.0) * (b**r) - c
    assert F(lo) < 0.0 and F(hi) > 0.0
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if F(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def phi(r, b, t):
    return (t**r) * abs(1.0 - b*t)


def solve_w_einv():
    target = math.exp(-1.0)
    lo, hi = 0.0, 1.0
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if mid * math.exp(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main():
    # Exact branch formulas and equal-ripple condition for representative orders.
    rows = []
    for k in range(1, 21):
        r = k / 2.0
        c = c_r(r)
        b = optimal_b(r)
        t0 = r / ((r + 1.0) * b)
        A = phi(r, b, t0)
        B = phi(r, b, 1.0)
        expected = b - 1.0
        assert 1.0 < b < 1.0 + c < 2.0
        assert abs(A - B) < 2e-13
        assert abs(A - expected) < 2e-13

        # Dense-grid check of the scalar multiplier maximum.
        N = 20000
        grid_max = max(phi(r, b, j/N) for j in range(N + 1))
        assert grid_max <= expected + 2e-12
        assert expected - grid_max < 2e-7

        # Nonnegative-Fourier optimum b=1: maximum at r/(r+1).
        tn = r / (r + 1.0)
        nonneg = phi(r, 1.0, tn)
        assert abs(nonneg - c) < 2e-14
        for test_b in (-2.0, -0.5, 0.0, 0.5, 0.9, 1.0):
            # On b<=1, evaluation at the b=1 maximizer already shows no improvement.
            assert phi(r, test_b, tn) + 2e-14 >= c

        C_un = (2.0**k) * expected
        C_pos = (2.0**k) * c
        assert C_un < C_pos
        rows.append((k, b, C_un, C_pos))

    # Known low-order consistency checks.
    assert abs(rows[0][1] - 4.0/3.0) < 2e-14
    assert abs(rows[0][2] - 2.0/3.0) < 2e-14
    assert abs(rows[1][1] - ((1.0 + math.sqrt(2.0))/2.0)) < 2e-14
    assert abs(rows[1][2] - 2.0*(math.sqrt(2.0) - 1.0)) < 2e-14
    assert abs(rows[1][3] - 1.0) < 2e-14

    # Asymptotic constant r(b_r-1) -> W(e^{-1}).
    W = solve_w_einv()
    for k in (100, 200, 400, 800):
        r = k / 2.0
        b = optimal_b(r)
        y = r * (b - 1.0)
        assert abs(y - W) < 0.01
    ratio_limit = math.e * W
    assert 0.75 < ratio_limit < 0.77

    print('VERIFY_OK')
    print('k  b_r               C_unrestricted       C_nonnegative')
    for k, b, cu, cp in rows[:8]:
        print(f'{k:1d}  {b:.15f}  {cu:.15f}  {cp:.15f}')
    print(f'W(e^-1)={W:.15f}')
    print(f'e*W(e^-1)={ratio_limit:.15f}')


if __name__ == '__main__':
    main()
