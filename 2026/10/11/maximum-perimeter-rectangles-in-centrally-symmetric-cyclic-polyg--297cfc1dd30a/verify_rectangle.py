"""Deterministic finite checks for the centered cyclic-polygon rectangle theorem.

This diagnostic is not a substitute for the proof for arbitrary polygons.
Run: python3 verify_rectangle.py
"""
import math
import random


def norm(v):
    return math.hypot(v[0], v[1])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def perimeter_from_diagonals(p, q):
    return 2 * (norm(add(p, q)) + norm(sub(p, q)))


def radius_in_direction(verts, angle):
    e = (math.cos(angle), math.sin(angle))
    bound = float('inf')
    for j, v in enumerate(verts):
        w = verts[(j + 1) % len(verts)]
        normal = (w[1] - v[1], v[0] - w[0])
        h = normal[0] * v[0] + normal[1] * v[1]
        ne = normal[0] * e[0] + normal[1] * e[1]
        if ne > 1e-12:
            bound = min(bound, h / ne)
    return bound


def vertex_bound(verts):
    return max(perimeter_from_diagonals(a, b) for a in verts for b in verts)


def orthogonality_defect(angles):
    best = math.pi / 2
    for i, a in enumerate(angles):
        for b in angles[i + 1:]:
            delta = abs(a - b) % math.pi
            delta = min(delta, math.pi - delta)
            best = min(best, abs(math.pi / 2 - delta))
    return best


def linear_nearest_defect(angles):
    m = len(angles)
    doubled = angles + [a + math.pi for a in angles]
    j = 0
    best = math.pi / 2
    for a in angles:
        target = a + math.pi / 2
        while j + 1 < 2 * m and doubled[j + 1] <= target:
            j += 1
        for k in (j, min(j + 1, 2 * m - 1)):
            best = min(best, abs(doubled[k] - target))
    return best


def regular_test(n, R=1):
    angles = [2 * math.pi * j / n for j in range(n // 2)]
    verts = [(R * math.cos(2 * math.pi * j / n),
              R * math.sin(2 * math.pi * j / n)) for j in range(n)]
    exact = 4 * math.sqrt(2) * R
    if n % 4:
        exact *= math.cos(math.pi / (2 * n))
    ans = vertex_bound(verts)
    if abs(ans - exact) > 1e-11 * R:
        raise AssertionError(('regular formula', n, ans, exact))
    eps = orthogonality_defect(angles)
    if abs(linear_nearest_defect(angles) - eps) > 1e-12:
        raise AssertionError(('linear defect algorithm', n))
    if abs(ans - 4 * math.sqrt(2) * R * math.cos(eps / 2)) > 1e-11:
        raise AssertionError(('regular angular defect', n))


def random_cyclic_test(rng, m):
    line_angles = sorted(rng.sample(range(1, 1000000), m))
    line_angles = [math.pi * j / 1000000 for j in line_angles]
    verts = sorted([(math.cos(a + offset), math.sin(a + offset))
                    for a in line_angles for offset in (0, math.pi)],
                   key=lambda v: math.atan2(v[1], v[0]) % (2 * math.pi))
    bv = vertex_bound(verts)
    eps = orthogonality_defect(line_angles)
    if abs(linear_nearest_defect(line_angles) - eps) > 1e-12:
        raise AssertionError(('linear defect algorithm', m))
    exact = 4 * math.sqrt(2) * math.cos(eps / 2)
    if abs(bv - exact) > 3e-12:
        raise AssertionError(('cyclic angular defect', m, bv, exact))
    for _ in range(250):
        a, b = rng.uniform(0, 2 * math.pi), rng.uniform(0, 2 * math.pi)
        r = rng.random() * min(radius_in_direction(verts, a),
                                radius_in_direction(verts, b))
        p = (r * math.cos(a), r * math.sin(a))
        q = (r * math.cos(b), r * math.sin(b))
        val = perimeter_from_diagonals(p, q)
        if val > bv + 2e-10:
            raise AssertionError(('interior rectangle violates bound', m, val, bv))


def main():
    for n in range(4, 604, 2):
        regular_test(n)
    rng = random.Random(781965)
    for m in range(2, 15):
        for _ in range(8):
            random_cyclic_test(rng, m)
    print('VERIFY_OK regular_cases=300 cyclic_polygons=104 interior_rectangle_checks=26000')


if __name__ == '__main__':
    main()
