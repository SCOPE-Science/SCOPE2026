#!/usr/bin/env python3
"""Standard-library checks of the weighted odd-cycle onset coefficient."""
import math
from fractions import Fraction


def exact_parameters(weights):
    s = sum((Fraction(1, b) for b in weights), Fraction(0))
    t = sum((Fraction(1, b**3) for b in weights), Fraction(0))
    d = s**3 - t
    assert d > 0 and len(weights) % 2 == 0
    return 1 / s, Fraction(3, 4) * s**4 / d


def stationary_gap(weights, eps):
    ws = [float(b) for b in weights]
    wc, coefficient = exact_parameters(weights)
    w = float(wc) + eps
    upper = min(ws) * 0.25
    def equation(z):
        return w * math.sin(sum(math.asin(z / b) for b in ws)) - z
    assert equation(upper) < 0
    low = 0.0
    for _ in range(130):
        mid = (low + upper) / 2
        if equation(mid) > 0:
            low = mid
        else:
            upper = mid
    z = (low + upper) / 2
    angles = [math.asin(z / b) for b in ws]
    theta = sum(angles)
    # 1-cos theta = 2 sin(theta/2)^2 avoids cancellation.
    gain = w * math.sin(theta / 2)**2 - sum(
        b * math.sin(angle / 2)**2 for b, angle in zip(ws, angles)
    )
    return gain, float(coefficient)


def main():
    for weights in ([1, 1], [1, 1, 1, 1], [1, 2, 3, 4]):
        wc, coeff = exact_parameters(weights)
        print('weights:', list(weights), 'threshold:', wc, 'coefficient:', coeff)
        for eps in (1e-2, 1e-3, 1e-4):
            val, coef = stationary_gap(weights, eps)
            ratio = val / (eps**2)
            print('  epsilon:', eps, 'gap/epsilon^2:', '%.12g' % ratio)
            assert val > 0
            assert abs(ratio / coef - 1) < 5.0 * eps + 2e-6
    wc, coeff = exact_parameters([1, 2, 3, 4])
    assert (wc, coeff) == (Fraction(12,25), Fraction(78125,43488))
    print('EXAMPLE_CHECKS_OK')


if __name__ == '__main__':
    main()
