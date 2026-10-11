"""Independent finite checks of the analytic maximum-area rectangle law.

Rectangles are centered, written as +/-a*u +/-b*v with orthogonal
unit directions u,v. A uniform angle/aspect grid is diagnostic only;
the proof of the all-parameter bound is analytic.
"""
import math


def best_grid(A, B, angles=181, aspects=401):
    best = (0.0, 0.0, 0.0)
    for i in range(angles):
        theta = (math.pi / 4) * i / (angles - 1)
        co, si = math.cos(theta), math.sin(theta)
        for j in range(aspects):
            r = math.exp((j - (aspects - 1) / 2) / 60)
            # Corners r*u +/- v, scale set by the gauge |x|/A+|y|/B.
            plus = abs(r * co - si) / A + abs(r * si + co) / B
            minus = abs(r * co + si) / A + abs(r * si - co) / B
            area = 4*r/max(plus, minus)**2
            if area > best[0]:
                best = (area, theta, r)
    return best


def boundary_regime_inequality(A, B, samples=401):
    s0 = A*A/(A*A+B*B)
    max_b = max(A*B/2, B*B)
    for i in range(samples):
        s = i/(samples-1)
        equal_s = 2*A*B*s*(1-s)
        assert equal_s <= max_b*(1+1e-12)
        t = 2*s0 - s
        if 0 <= t <= 1:
            different_s = 2*A*B*(s0*(1-s0)+(s-s0)**2)
            assert different_s <= max_b*(1+1e-12)


def verify():
    for B in (0.20, 0.40, 0.49, 0.50, 0.51, 0.60, 0.80, 1.0):
        A=1.0
        expected=max(A*B, 2*B*B)
        achieved, theta, ratio = best_grid(A, B)
        assert achieved <= expected*(1+1e-11), (A,B,achieved,expected)
        assert achieved >= expected*(1-2e-4), (A,B,achieved,expected)
        boundary_regime_inequality(A,B)
    for A, B in ((3.0,1.0),(7.0,2.0),(5.0,4.0),(2.0,1.0)):
        expected=max(A*B,2*B*B)
        achieved,_,_=best_grid(A,B)
        assert achieved <= expected*(1+1e-11)
        assert achieved >= expected*(1-2e-4)
        boundary_regime_inequality(A,B)
    print('VERIFY_OK: 12 dimensions, centered rectangle grids, and boundary regimes')

if __name__ == '__main__':
    verify()
