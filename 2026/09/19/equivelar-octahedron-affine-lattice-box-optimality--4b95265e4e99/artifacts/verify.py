"""Exact checks for the normalized genus-3 equivelar-octahedron coordinates."""
from math import gcd

V = {
    1: (-24, 28, 6), 2: (-12, 37, 34), 3: (24, -28, 6),
    4: (12, -38, 34), 5: (0, 100, 78), 6: (-28, 16, -6),
    7: (3, 49, 69), 8: (0, -100, 78), 9: (28, -16, -6),
    10: (-38, -12, -34), 11: (16, 28, 6), 12: (-49, 3, -69),
    13: (-3, -49, 69), 14: (28, 24, -6), 15: (37, 12, -34),
    16: (-16, -28, 6), 17: (49, -3, -69), 18: (-6, 42, 48),
    19: (-42, -6, -48), 20: (-100, 0, -78), 21: (-28, -24, -6),
    22: (6, -42, 48), 23: (42, 6, -48), 24: (100, 0, -78),
}


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def det3(a, b, c):
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def coordinate_range(j):
    values = [v[j] for v in V.values()]
    return min(values), max(values), max(values) - min(values)


base = V[1]
d15, d17, d23 = (sub(V[i], base) for i in (15, 17, 23))
d2, d12 = (sub(V[i], base) for i in (2, 12))
minor_1 = det3(d15, d17, d23)
minor_2 = det3(d2, d12, d15)

assert minor_1 == -8
assert minor_2 == 1325
assert gcd(abs(minor_1), abs(minor_2)) == 1
assert sub(V[5], V[8]) == (0, 200, 0)
assert sub(V[24], V[20]) == (200, 0, 0)

ranges = [coordinate_range(j) for j in range(3)]
assert ranges == [(-100, 100, 200), (-100, 100, 200), (-78, 78, 156)]

print("maximal minors:", minor_1, minor_2, "gcd =", gcd(abs(minor_1), abs(minor_2)))
print("coordinate ranges:", ranges)
print("forcing differences:", sub(V[5], V[8]), sub(V[24], V[20]))
print("sorted attained span profile:", tuple(sorted(r[2] for r in ranges)))
print("attained bounding-box volume product:", 200 * 200 * 156)
