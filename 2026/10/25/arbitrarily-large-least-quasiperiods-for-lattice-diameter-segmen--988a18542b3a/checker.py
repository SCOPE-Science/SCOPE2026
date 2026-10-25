"""Reproduce exact finite consistency checks for a lattice parallelogram theorem.

Only standard Python 3 modules are required. The finite computation does not
prove the theorem for unrestricted integers: the general proof is in RESULT.md.
"""
from math import gcd


def test_case(m: int, n: int):
    determinant = m * (m + 2) - 1
    points = [
        (x, y)
        for y in range((m + 1) * n + 1)
        for x in range((m + 3) * n + 1)
        if 0 <= (m + 2) * y - x <= n * determinant
        and 0 <= m * x - y <= n * determinant
    ]
    diameter = 0
    for i, (x0, y0) in enumerate(points):
        for x1, y1 in points[i + 1:]:
            diameter = max(diameter, gcd(x1 - x0, y1 - y0))
    assert diameter > 0

    lines = set()
    directions = set()
    for i, (x0, y0) in enumerate(points):
        for x1, y1 in points[i + 1:]:
            if gcd(x1 - x0, y1 - y0) != diameter:
                continue
            dx = (x1 - x0) // diameter
            dy = (y1 - y0) // diameter
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            directions.add((dx, dy))
            lines.add((dx, dy, dx * y0 - dy * x0))

    p, t = divmod(n, m)
    expected_diameter = n * (m + 2) - p - int(t != 0)
    expected_count = n - p + 1 if t == 0 else (m - t + 1) * (n - p)
    assert diameter == expected_diameter, (m, n, diameter, expected_diameter)
    assert directions == {(1, 0)}, (m, n, directions)
    assert len(lines) == expected_count, (m, n, len(lines), expected_count)


def main():
    cases = 0
    for m in range(2, 9):
        for n in range(1, 7):
            test_case(m, n)
            cases += 1
    print(f"LATTICE_PERIOD_CHECK_OK cases={cases}")


if __name__ == "__main__":
    main()
