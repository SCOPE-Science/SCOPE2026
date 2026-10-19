"""Exact rational exhaustive certificate for the third iterate of a toral shear."""
from fractions import Fraction as Q
from itertools import product
from math import floor

ZERO, ONE = Q(0), Q(1)
CUT = Q(2, 3)
I = ((ONE, ZERO), (ZERO, ONE))
A = ((ONE, Q(3, 2)), (ONE, Q(5, 2)))
B = ((ONE, Q(-3)), (ONE, Q(-2)))


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def apply(m, v, t=(ZERO, ZERO)):
    return tuple(sum(m[i][j] * v[j] for j in range(2)) + t[i]
                 for i in range(2))


def clip(vertices, m, t, component, threshold, lower):
    """Exact closed half-plane intersection; drop only zero-area cells."""
    if len(vertices) < 3:
        return []

    def f(p):
        return apply(m, p, t)[component] - threshold

    out = []
    for u, v in zip(vertices, vertices[1:] + vertices[:1]):
        fu, fv = f(u), f(v)
        inside_u = fu >= 0 if lower else fu <= 0
        inside_v = fv >= 0 if lower else fv <= 0
        if inside_u:
            out.append(u)
        if inside_u != inside_v:
            out.append(tuple((-fv * u[j] + fu * v[j]) / (fu - fv)
                             for j in range(2)))
    unique = []
    for v in out:
        if not unique or unique[-1] != v:
            unique.append(v)
    if len(unique) > 1 and unique[0] == unique[-1]:
        unique.pop()
    return unique if len(set(unique)) >= 3 and signed_area(unique) != 0 else []


def signed_area(p):
    return sum(p[i][0] * p[(i + 1) % len(p)][1]
               - p[(i + 1) % len(p)][0] * p[i][1]
               for i in range(len(p))) / 2


def norm(z):
    return tuple(u % 1 for u in z)


def shear(z):
    x, y = norm(z)
    f = Q(3, 2) * y if y <= CUT else 3 * (1 - y)
    xp = (x + f) % 1
    return xp, (y + xp) % 1


class Cell:
    def __init__(self, polygon, m, t, word, history):
        self.polygon = polygon
        self.m = m
        self.t = t
        self.word = word
        self.history = history


def cells_at_depth_three():
    start = [(ZERO, ZERO), (ONE, ZERO), (ONE, ONE), (ZERO, ONE)]
    cells = [Cell(start, I, (ZERO, ZERO), '', [(I, (ZERO, ZERO))])]
    counts = []
    for _ in range(3):
        children = []
        for c in cells:
            for branch, b, offset in [('L', A, (ZERO, ZERO)),
                                      ('H', B, (Q(3), Q(3)))]:
                polygon = clip(c.polygon, c.m, c.t, 1, CUT, branch == 'H')
                if not polygon:
                    continue
                new_m = mul(b, c.m)
                new_t = tuple(apply(b, c.t)[i] + offset[i] for i in range(2))
                ranges = []
                for component in range(2):
                    vals = [apply(new_m, v, new_t)[component] for v in polygon]
                    ranges.append(range(floor(min(vals)), floor(max(vals)) + 1))
                for nx, ny in product(*ranges):
                    p = polygon
                    for i, n in enumerate((nx, ny)):
                        p = clip(p, new_m, new_t, i, Q(n), True)
                        if p:
                            p = clip(p, new_m, new_t, i, Q(n + 1), False)
                        if not p:
                            break
                    if p:
                        shift_t = (new_t[0] - nx, new_t[1] - ny)
                        children.append(Cell(p, new_m, shift_t,
                                             c.word + branch,
                                             c.history + [(new_m, shift_t)]))
        cells = children
        assert sum(abs(signed_area(c.polygon)) for c in cells) == ONE
        counts.append(len(cells))
    assert counts == [7, 32, 128], counts
    return cells


def in_polygon(v, p):
    cross = [(b[0] - a[0]) * (v[1] - a[1])
             - (b[1] - a[1]) * (v[0] - a[0])
             for a, b in zip(p, p[1:] + p[:1])]
    return all(t >= 0 for t in cross) or all(t <= 0 for t in cross)


def solve_fixed(c, shift):
    """Solve (M-I)z=shift-t, allowing periodic boundary representatives."""
    m = c.m
    t = c.t
    target = (shift[0] - t[0], shift[1] - t[1])
    a, b = m[0][0] - 1, m[0][1]
    d, e = m[1][0], m[1][1] - 1
    determinant = a * e - b * d
    if determinant:
        z = ((e * target[0] - b * target[1]) / determinant,
             (-d * target[0] + a * target[1]) / determinant)
        return ('point', z) if in_polygon(z, c.polygon) else ('empty',)
    if a == b == d == e == 0:
        assert target != (ZERO, ZERO), 'Open periodic polygon would need a separate case'
        return ('empty',)
    coeff = (a, b) if (a, b) != (ZERO, ZERO) else (d, e)
    rhs = target[0] if (a, b) != (ZERO, ZERO) else target[1]
    # Consistency with the second affine equation, including dependent rows.
    intersections = []
    for u, v in zip(c.polygon, c.polygon[1:] + c.polygon[:1]):
        fu = coeff[0] * u[0] + coeff[1] * u[1] - rhs
        fv = coeff[0] * v[0] + coeff[1] * v[1] - rhs
        if fu == 0:
            intersections.append(u)
        if fu * fv < 0:
            intersections.append(tuple((-fv * u[j] + fu * v[j]) / (fu - fv)
                                       for j in range(2)))
    intersections = sorted(set(intersections))
    if not intersections:
        return ('empty',)
    if not all(d * z[0] + e * z[1] == target[1] for z in intersections):
        return ('empty',)
    if len(intersections) == 1:
        return ('point', intersections[0])
    assert len(intersections) == 2, intersections
    return ('segment', intersections[0], intersections[1])


BASE = [(Q(2, 9), Q(2, 9), Q(4, 9)),
        (Q(4, 9), Q(5, 9), Q(7, 9))]
SPECIAL = {(ZERO, ZERO), (ZERO, CUT)}
for seed in [(ZERO, Q(4, 27)), (ZERO, Q(14, 27))]:
    p = seed
    for _ in range(3):
        SPECIAL.add(p)
        p = shear(p)
    assert p == seed
assert len(SPECIAL) == 8


def in_base(z):
    return any(z[1] == y and xmin <= z[0] <= xmax
               for y, xmin, xmax in BASE)


def known(z):
    z = norm(z)
    if z in SPECIAL:
        return True
    for _ in range(3):
        if in_base(z):
            return True
        z = shear(z)
    return False


def check():
    cells = cells_at_depth_three()
    point_cells, segment_cells = 0, 0
    point_candidates, segment_candidates = set(), set()
    for c in cells:
        for shift in product((Q(-1), ZERO, ONE), repeat=2):
            solution = solve_fixed(c, shift)
            if solution[0] == 'empty':
                continue
            if solution[0] == 'point':
                point_cells += 1
                p = solution[1]
                point_candidates.add(p)
                assert shear(shear(shear(norm(p)))) == norm(p)
                assert known(p), (p, c.word)
                continue
            segment_cells += 1
            u, v = solution[1:]
            segment_candidates.add((u, v))
            # Within each cell, first and second iterates are affine lifts.
            # One image must lie inside one of the two base segments.
            witnesses = []
            for m, t in c.history[:3]:
                zu, zv = apply(m, u, t), apply(m, v, t)
                for y, xmin, xmax in BASE:
                    ky = zu[1] - y
                    kx = floor(zu[0])
                    if (ky.denominator == 1 and zv[1] - y == ky
                            and xmin + kx <= zu[0] <= xmax + kx
                            and xmin + kx <= zv[0] <= xmax + kx):
                        witnesses.append((y, xmin, xmax))
            assert witnesses, (u, v, c.word)
            middle = tuple((u[i] + v[i]) / 2 for i in range(2))
            assert known(u) and known(v) and known(middle)
            assert shear(shear(shear(norm(middle)))) == norm(middle)
    assert len(point_candidates) == 32
    assert len(segment_candidates) == 12
    assert segment_cells == 12
    # Conversely the two complete base segments and their iterates are period 3.
    # For interior points the exact low-high-high return is
    # (x,y) -> (x + (9/2)*y, y) modulo one.
    for y, xmin, xmax in BASE:
        assert Q(9, 2) * y in (Q(1), Q(2))
        for x in [xmin, (xmin + xmax) / 2, xmax]:
            z = (x, y)
            assert shear(shear(shear(z))) == z
            assert shear(z) != z
    assert shear((ZERO, ZERO)) == (ZERO, ZERO)
    assert shear((ZERO, CUT)) == (ZERO, CUT)
    print('PASS: 7/32/128 rational polygons partition the unit square')
    print('PASS: 32 point representatives and 12 exact rank-one segments all classified')
    print('PASS: exactly two fixed points, two isolated three-cycles, two interval families')
    print('PASS: all claimed families and their boundary points are periodic')


if __name__ == '__main__':
    check()
