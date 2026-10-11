"""Numerical diagnostics for a geometric pentagon-width inequality.

All statements of the theorem are established analytically in RESULT.md;
finite sampling here is not a proof of the continuum claim.
"""
import math
from fractions import Fraction


def geometry(x):
    y = math.sqrt(1.0 - (x - 0.5) ** 2)
    u = math.sqrt(1.0 - x * x)
    z = y + u
    pts = [(0.0, z), (x, y), (0.5, 0.0), (-0.5, 0.0), (-x, y)]
    widths = []
    for i in range(5):
        p, q = pts[i], pts[(i + 1) % 5]
        dx, dy = q[0] - p[0], q[1] - p[1]
        n = (-dy, dx)
        proj = [v[0]*n[0] + v[1]*n[1] for v in pts]
        widths.append((max(proj) - min(proj)) / math.hypot(dx, dy))
    measured = min(widths)
    formula_width = min(x*z + 0.5*u, (y if x <= 0.5 else 2*x*y), z)
    s_direct = sum(math.dist(pts[i], pts[j]) for i in range(5)
                   for j in range(i + 1, 5))
    s_formula = 5.0 + 2.0*math.sqrt(z*z + 0.25) + 2*x + 2*math.sqrt(1+2*x)
    return measured, formula_width, s_direct, s_formula, z


def main():
    threshold = 4 + 6 * math.sqrt(3)
    max_ratio = -1.0
    tests = 0
    for i in range(30001):
        x = 0.25 + i * 0.75 / 30000
        wm, wf, sm, sf, z = geometry(x)
        assert abs(wm - wf) < 1e-10, (i, wm, wf)
        assert abs(sm - sf) < 1e-10, (i, sm, sf)
        if i != 30000:
            assert sm / wm < threshold + 1e-10
        max_ratio = max(max_ratio, sm / wm)
        tests += 1
    w, _, s, _, _ = geometry(1.0)
    assert abs(w - math.sqrt(3)/2) < 1e-12
    assert abs(s - (9 + 2*math.sqrt(3))) < 1e-12
    assert abs(max_ratio - threshold) < 1e-10
    # The algebraic identity behind the convexity threshold is exact.
    for num in range(1, 201):
        x = Fraction(num, 200)
        y2 = 1 - (x - Fraction(1,2))**2
        u2 = 1 - x*x
        lhs = x*x*y2 - (Fraction(1,2)-x)**2*u2
        assert lhs == (4*x-1)/4
    print(f"VERIFY_OK sampled_pentagons={tests} exact_rational_identities=200 "
          f"sharp_ratio={threshold:.12f}")


if __name__ == '__main__':
    main()
