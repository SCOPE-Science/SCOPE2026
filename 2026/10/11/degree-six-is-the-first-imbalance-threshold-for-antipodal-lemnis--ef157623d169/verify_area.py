"""Exact integer quadtree certificate for two-point polynomial lemniscate areas.

Run with Python 3, no dependencies: python verify_area.py
All comparisons use integer arithmetic. Each area interval encloses the
complete planar set, not a sample of grid points.
"""

from collections import defaultdict


def area_bounds(degree, plus_multiplicity, subdivisions=8):
    """Return rigorous area numerators in units of 2^(-2*subdivisions)."""
    assert 1 <= degree and 0 <= plus_multiplicity <= degree
    scale = 1 << subdivisions
    threshold = scale ** (2 * degree)
    pending = [(-2 * scale, 2 * scale, -2 * scale, 2 * scale)]
    inner = exterior = undecided = 0
    counts = defaultdict(int)

    while pending:
        left, right, bottom, top = pending.pop()

        def squared_min(center):
            dx = 0 if left <= center <= right else min(abs(left-center), abs(right-center))
            dy = 0 if bottom <= 0 <= top else min(abs(bottom), abs(top))
            return dx * dx + dy * dy

        def squared_max(center):
            return max((left-center)**2, (right-center)**2) + max(bottom**2, top**2)

        low = squared_min(scale)**plus_multiplicity * squared_min(-scale)**(degree-plus_multiplicity)
        high = squared_max(scale)**plus_multiplicity * squared_max(-scale)**(degree-plus_multiplicity)
        square_area = (right - left) * (top - bottom)

        if low >= threshold:
            exterior += square_area
            counts['outside'] += 1
        elif high < threshold:
            inner += square_area
            counts['inside'] += 1
        elif right-left == 1:
            undecided += square_area
            counts['undecided'] += 1
        else:
            mx = (left + right) // 2
            my = (bottom + top) // 2
            pending.extend([
                (left, mx, bottom, my), (mx, right, bottom, my),
                (left, mx, my, top), (mx, right, my, top),
            ])
    assert inner + exterior + undecided == 16 * scale * scale
    return inner, inner + undecided, scale * scale, dict(counts)


def check():
    cases = [(3, 1), (4, 1), (5, 1), (5, 2), (6, 1), (6, 2)]
    expected = {
        (3, 1): (126966, 129888),
        (4, 1): (138338, 140672),
        (5, 1): (149516, 151682),
        (5, 2): (125242, 128836),
        (6, 1): (158192, 160260),
        (6, 2): (126966, 129888),
    }
    readings = {}
    for degree, k in cases:
        lo, hi, denominator, counts = area_bounds(degree, k)
        assert denominator == 65536
        assert (lo, hi) == expected[(degree, k)]
        readings[degree, k] = (lo, hi)
        print(f"degree={degree}, k={k}: {lo}/65536 <= area <= {hi}/65536; {counts}")

    # Area of the Bernoulli lemniscate |z^2-1| < 1 is exactly 2.
    assert readings[3, 1][1] < 2 * 65536
    assert readings[4, 1][0] > 2 * 65536
    assert readings[5, 2][1] < readings[5, 1][0]
    assert readings[6, 2][1] < 2 * 65536 < readings[6, 1][0]
    print("ALL EXACT AREA ENCLOSURES AND OPTIMIZER COMPARISONS PASS")


if __name__ == '__main__':
    check()
