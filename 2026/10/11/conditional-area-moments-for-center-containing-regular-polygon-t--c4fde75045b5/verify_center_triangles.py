"""Independent finite checks of the conditional regular-polygon triangle area laws.

Run: python3 verify_center_triangles.py
No third-party packages are required. The analytic proof covers all admissible orders.
"""
from itertools import combinations
from math import comb, cos, pi, sin, tan, isclose


def predicted(n):
    theta = pi / n
    if n % 2:
        count_probability = (n + 1) / (4 * (n - 2))
        first = 3 * n / ((n * n - 1) * sin(theta))
        second = (3 * (n * n - 1 + cos(theta) ** -2) / (8 * (n * n - 1))
                  + 3 * (1 + cos(theta)) / ((n * n - 1) * sin(theta) ** 2)
                  + 3 / (2 * (n * n - 1) * cos(theta)))
    elif n == 4:
        return 0.0, None, None
    else:
        cot = 1 / tan(theta)
        count_probability = (n - 4) / (4 * (n - 1))
        first = 3 * cot / (n - 2)
        second = (3 * n * (n - 8) / 8 + 6 * cot ** 2) / ((n - 2) * (n - 4))
    return count_probability, first, second


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def subtract(a, b):
    return a[0] - b[0], a[1] - b[1]


def inside_counterclockwise_triangle(points):
    # Test the origin against all three oriented edges, independently of arcs.
    return all(cross(subtract(q, p), (-p[0], -p[1])) > 1e-10
               for p, q in ((points[0], points[1]),
                            (points[1], points[2]),
                            (points[2], points[0])))


def assert_close(a, b, label):
    if not isclose(a, b, rel_tol=2e-11, abs_tol=3e-11):
        raise AssertionError((label, a, b))


def run():
    triangle_count = 0
    eligible_count = 0
    for n in range(3, 63):
        vertices = [(cos(2 * pi * j / n), sin(2 * pi * j / n))
                    for j in range(n)]
        areas = []
        for i, j, k in combinations(range(n), 3):
            a, b, c = vertices[i], vertices[j], vertices[k]
            triangle_count += 1
            if inside_counterclockwise_triangle((a, b, c)):
                area = cross(subtract(b, a), subtract(c, a)) / 2
                assert area > 0
                areas.append(area)
                eligible_count += 1
        prob, mean, second = predicted(n)
        assert_close(len(areas) / comb(n, 3), prob, (n, 'probability'))
        if not areas:
            assert n == 4 and mean is None and second is None
        else:
            assert_close(sum(areas) / len(areas), mean, (n, 'mean'))
            assert_close(sum(x * x for x in areas) / len(areas), second,
                         (n, 'second moment'))
        # Independent cyclic-gap trigonometric reductions, useful local checks.
        theta = pi / n
        admissible = [(a, b, n - a - b) for a in range(1, n)
                      for b in range(1, n - a)
                      if 2 * max(a, b, n - a - b) < n]
        assert len(admissible) * n == len(areas) * 3
        if admissible:
            gap_areas = [2 * sin(a * theta) * sin(b * theta) * sin(c * theta)
                         for a, b, c in admissible]
            assert_close(sum(gap_areas) / len(gap_areas), mean,
                         (n, 'gap mean'))
            assert_close(sum(x * x for x in gap_areas) / len(gap_areas),
                         second, (n, 'gap second moment'))
    target = 3 / 8 - 3 / pi ** 2
    for n in (1001, 10001, 100001):
        for order in (n, n + 1):
            _, first, second = predicted(order)
            var = second - first * first
            if order % 2:
                expected = target - (12 / pi ** 2 + 5 / 8) / order ** 2
                assert abs(var - expected) * order ** 2 < 0.0001
            else:
                expected = target - 3 / (4 * order)
                assert abs(var - expected) * order < 0.001
    print('VERIFY_OK')
    print(f'orders=3..62, triangles={triangle_count}, eligible={eligible_count}')
    print('independent oriented-edge membership, determinant areas, cyclic gaps,')
    print('conditional first and second moments, and asymptotic spot checks passed')


if __name__ == '__main__':
    run()
