"""Exact finite sanity checks for labelled grid/diagonal line arrangements.

This script does not prove the topological theorem; the proof uses a
connected parameter space, lattice isotopy, and the simple-triangle theorem.
"""
from fractions import Fraction as F
from itertools import combinations


def family(p, q, deformed):
    assert 2 <= p <= q
    lines = []
    for i in range(1, p):
        lines.append((F(1), F(0), -F(1, i)))  # y=1/i
    for j in range(2, q + 1):
        if deformed:
            h = F(1) - F(1, j) if j < p else F(1, 4 * (j - p + 2))
        else:
            h = F(1, j)
        lines.append((F(0), F(1), -h))  # z=h
    lines.append((F(1), F(1), -F(1)) if deformed else (F(-1), F(1), F(0)))
    return lines


def incidence(lines):
    points = {}
    for (i, l), (j, m) in combinations(enumerate(lines), 2):
        a, b, c = l
        d, e, f = m
        den = a * e - b * d
        if not den:  # parallel; their common point lies on the omitted line at infinity
            continue
        y = (b * f - c * e) / den
        z = (c * d - a * f) / den
        points[(y, z)] = None
    return sorted(
        tuple(i for i, (a, b, c) in enumerate(lines) if a * y + b * z + c == 0)
        for y, z in points
    )


def triangle_certificate(p, q):
    lines = family(p, q, True)
    b = F(1, 4 * (q - p + 2))
    vertices = ((F(1), F(0)), (F(1), b), (F(1) - b, b))
    assert 0 < b < F(1, 2)
    for vertex in vertices:
        y, z = vertex
        meeting = [i for i, (a, d, c) in enumerate(lines) if a*y + d*z+c == 0]
        assert len(meeting) == 2, (p, q, vertex, meeting)
    # No vertical or horizontal line crosses the open interior of the triangle.
    for i in range(2, p):
        assert F(1, i) < F(1) - b
    for j in range(2, q + 1):
        height = F(1)-F(1,j) if j < p else F(1,4*(j-p+2))
        assert height >= b
        if height == b:
            assert j == q
    return vertices


if __name__ == '__main__':
    samples = 0
    for p in range(2, 14):
        for q in range(p, 17):
            left, right = family(p, q, False), family(p, q, True)
            assert incidence(left) == incidence(right), (p, q)
            triangle_certificate(p, q)
            samples += 1
    print('PASS: 114 exact labelled-incidence and simple-triangle checks' if samples == 114 else f'PASS: {samples} exact sample checks')
