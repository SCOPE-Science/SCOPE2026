#!/usr/bin/env python3
"""Independent numerical sanity checks of an analytic two-opinion adaptive-edge theorem.

The assertions verify the first-integral algebra and representative trajectories;
they do not substitute for the global phase-classification proof.
"""
from math import atanh, exp, log, tanh


def psi(alpha, d):
    if alpha <= 0 or d <= 0:
        raise ValueError('alpha and d must be positive')
    z = alpha * d
    term = 1.0
    series = 0.0
    for k in range(1, 180):
        term *= z / k
        series += term / k
        if abs(term / k) <= 2.e-17 * max(1.0, abs(series)):
            break
    return log(d) - series


def critical_weight(alpha, d):
    dc = log(2) / alpha
    if d <= dc:
        return 0.0
    return tanh(0.5 * (psi(alpha, dc) - psi(alpha, d)))


def field(alpha, d, w):
    q = exp(-alpha * d)
    return (-2 * w / (1 + w) * q * d,
            w * (1 - w) * (2 * q - 1))


def rk4(alpha, d, w, h):
    a1, b1 = field(alpha, d, w)
    a2, b2 = field(alpha, d + h*a1/2, w + h*b1/2)
    a3, b3 = field(alpha, d + h*a2/2, w + h*b2/2)
    a4, b4 = field(alpha, d + h*a3, w + h*b3)
    return (d + h*(a1+2*a2+2*a3+a4)/6,
            w + h*(b1+2*b2+2*b3+b4)/6)


def integrate(alpha, d, w, t_end, h=0.2):
    n = round(t_end/h)
    step = t_end/n
    for _ in range(n):
        d, w = rk4(alpha, d, w, step)
        assert d > 0 and 0 < w < 1 + 1.e-13, (d, w)
    return d, w


def root_polarized(alpha, d0, w0):
    dc = log(2)/alpha
    target = psi(alpha, d0) + 2 * atanh(w0)
    left, right = dc, d0
    for _ in range(100):
        mid = (left + right)/2
        if psi(alpha, mid) > target:
            left = mid
        else:
            right = mid
    return (left + right)/2


def check():
    count = 0
    # Independently test the claimed gradient and the first-integral identity.
    for alpha in (0.37, 0.8, 1.0, 1.6):
        for d in (0.15, 0.4, 0.65, 0.9, 1.5, 1.9):
            eps = 1.e-5
            derivative = (psi(alpha, d+eps)-psi(alpha, d-eps))/(2*eps)
            exact = (2-exp(alpha*d))/d
            assert abs(derivative-exact) < 2.e-8
            count += 1
            for w in (0.08, 0.25, 0.62, 0.83):
                dd, ww = field(alpha, d, w)
                invariant_derivative = exact*dd+2*ww/(1-w*w)
                assert abs(invariant_derivative) < 2.e-13
                count += 1
    # The critical boundary is nontrivial for admissible initial opinions.
    alpha, d0 = 1.0, 1.5
    dc = log(2)/alpha
    wc = critical_weight(alpha, d0)
    assert 0.341758 < wc < 0.341760
    count += 1
    # Weak initial relationship: positive residual opinion gap and vanishing edge.
    d, w = integrate(alpha, d0, 0.2, 80.0, h=0.05)
    predicted = root_polarized(alpha, d0, 0.2)
    assert abs(d-predicted) < 2.e-9 and w < 1.e-8, (d, w, predicted)
    count += 1
    # Strong initial relationship: both opinions converge and tie becomes maximal.
    d, w = integrate(alpha, d0, 0.9, 40.0)
    assert d < 1.e-14 and w > 1-1.e-14, (d, w)
    count += 1
    # Critical algebraic slowing, including universal weight asymptotic factor.
    d, w = integrate(alpha, d0, wc, 1000.0, h=0.2)
    assert abs(1000*(d-dc)-2/alpha) < 0.025
    assert abs(1.e6*w-2/log(2)) < 0.035
    count += 2
    # The critical interaction exponent is sharp for the physical gap domain.
    assert log(2)/(0.33) > 2 and log(2)/(0.40) < 2
    assert critical_weight(0.33, 2.0) == 0.0
    assert critical_weight(0.40, 2.0) > 0.0
    count += 3
    print(f'VERIFICATION_OK: {count} independently evaluated numerical/algebraic assertions')
    print(f'two-agent threshold: alpha={alpha}, d0={d0}, critical_weight={wc:.12f}')
    print(f'critical t=1000: d={d:.12f}, weight={w:.12e}')

if __name__ == '__main__':
    check()
