#!/usr/bin/env python3
"""Independent numerical diagnostics for a two-agent adaptive opinion ODE.

Standard library only. Finite computations support but cannot replace the proof.
"""
import math


def phi(d):
    return 1.0 / (1.0 + d)


def potential(d):
    return 0.5 * (d - 1.0 - math.log(d))


def atanh(w):
    return 0.5 * math.log((1.0 + w) / (1.0 - w))


def right_side(d, w):
    p = phi(d)
    return (-2.0 * w * p * d / (1.0 + w),
            w * (1.0 - w) * (2.0 * p - 1.0))


def step(d, w, h):
    a, b = right_side(d, w)
    c, e = right_side(d + 0.5*h*a, w + 0.5*h*b)
    f, g = right_side(d + 0.5*h*c, w + 0.5*h*e)
    j, k = right_side(d + h*f, w + h*g)
    return (d + h*(a+2*c+2*f+j)/6, w + h*(b+2*e+2*g+k)/6)


def solve(d, w, horizon, h=0.025):
    invariant0 = atanh(w) - potential(d)
    max_err = 0.0
    steps = round(horizon/h)
    assert abs(steps*h-horizon) < 1e-10
    for idx in range(steps):
        d, w = step(d, w, h)
        assert 0 < d <= 2.0 and 0 < w < 1.0
        if (idx+1) % 80 == 0 and w < 0.999999:
            max_err = max(max_err, abs(atanh(w)-potential(d)-invariant0))
    return d, w, max_err


def polarization_limit(d0, w0):
    target = potential(d0) - atanh(w0)
    assert 0 < target < potential(d0)
    lo, hi = 1.0, d0
    for _ in range(90):
        mid = (lo+hi)/2
        if potential(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def main():
    d0 = 2.0
    threshold = math.tanh(potential(d0))
    assert abs(threshold - 0.15223376953165824) < 2e-14

    # Critical invariant and local exponent coefficient: F''(1) = 1/4.
    for n in range(2, 120):
        d = 1.0 + n/100
        w = n/121.0
        dd, ww = right_side(d, w)
        fp = (d-1.0)/(2.0*d)  # F'(d) for rational interaction.
        delta = ww/(1.0-w*w) - fp*dd
        assert abs(delta) < 3e-15
        assert abs(fp - (1.0-2.0*phi(d))/(2.0*d*phi(d))) < 3e-15

    down_w = 0.7 * threshold
    up_w = 1.3 * threshold
    d_down, w_down, e_down = solve(d0, down_w, 300.0)
    d_crit, w_crit, e_crit = solve(d0, threshold, 300.0)
    d_up, w_up, e_up = solve(d0, up_w, 300.0)
    expected_down = polarization_limit(d0, down_w)
    assert abs(d_down-expected_down) < 0.0001
    assert w_down < 1e-7
    assert d_up < 1e-12 and w_up > 0.999
    assert abs(300.0*(d_crit-1.0)-4.0) < 0.2
    assert abs(300.0*300.0*w_crit-4.0) < 0.18
    assert abs(math.log(w_down)/300.0 - (2.0*phi(expected_down)-1.0)) < 0.04
    assert abs(math.log(d_up)/300.0 + phi(0.0)) < 0.11
    assert max(e_down, e_crit, e_up) < 1e-7
    print('rational kernel: threshold =', format(threshold, '.15g'))
    print('polarized limit =', format(d_down,'.12g'),
          'expected =', format(expected_down,'.12g'))
    print('critical t*gap =', format(300*(d_crit-1),'.9g'),
          't^2*weight =', format(90000*w_crit,'.9g'))
    print('consensus gap =', format(d_up,'.9g'),
          'weight =', format(w_up,'.9g'))
    print('maximum invariant error =', format(max(e_down,e_crit,e_up),'.5g'))
    print('All finite numerical checks passed; asymptotic proof is analytical.')


if __name__ == '__main__':
    main()
