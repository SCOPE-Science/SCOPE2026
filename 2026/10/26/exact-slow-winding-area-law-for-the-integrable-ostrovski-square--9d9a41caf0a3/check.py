"""Finite-precision polygon-area checks for the Ostrovski square family.

Only standard-library arithmetic is used. These examples do not replace the proof
for every integer K>=3 and N>=0.
"""
from math import sin, cos, pi


def mmul(M, v):
    return (M[0][0] * v[0] + M[0][1] * v[1],
            M[1][0] * v[0] + M[1][1] * v[1])


def rotate(p):
    return (1.0 - p[1], p[0])


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def matrix_from_correspondences(a, b, ap, bp):
    D = det(a, b)
    U_inv = ((b[1] / D, -b[0] / D), (-a[1] / D, a[0] / D))
    V = ((ap[0], bp[0]), (ap[1], bp[1]))
    return tuple(tuple(V[i][0] * U_inv[0][j] + V[i][1] * U_inv[1][j]
                       for j in range(2)) for i in range(2))


def check_case(K, theta, N):
    s = sin(theta) * cos(theta)
    t = sin(theta) ** 2
    delta = 1 - 2 * s
    P1 = (s, t)
    P4 = (t, 1 - s)
    B = matrix_from_correspondences(P4, P1, (t, s), (1 - s, t))
    assert abs(det(B[0], B[1]) - 1) < 1e-10 or abs(
        B[0][0] * B[1][1] - B[0][1] * B[1][0] - 1) < 1e-10
    r = 1 / (1 + N * delta)
    z = (r * P4[0], r * P4[1])
    quarter = []
    for _ in range(K):
        quarter.append(z)
        z = mmul(B, z)
    assert abs(z[0] - r * s) + abs(z[1] - r * t) < 5e-9
    for _ in range(N):
        quarter.append(z)
        z = (z[0] + r * delta, z[1])
    endpoint = rotate((r * P4[0], r * P4[1]))
    assert abs(z[0] - endpoint[0]) + abs(z[1] - endpoint[1]) < 5e-9
    path = []
    block = quarter
    for _ in range(4):
        path.extend(block)
        block = [rotate(p) for p in block]
    area = 0.5 * abs(sum(det(a, b) for a, b in
                         zip(path, path[1:] + path[:1])))
    prediction = 1 - 4 * t * r + 2 * t * (1 - K * delta) * r * r
    assert abs(area - prediction) < 5e-9, (K, N, area, prediction)
    return area, 1 - area


def main():
    # Numerical angles for K>=4 solve the original break-line relation.
    parameter_angles = ((3, pi / 8), (4, 0.5069757592226116),
                        (5, 0.5685753250388403), (6, 0.607580269497842))
    for K, theta in parameter_angles:
        for N in (0, 1, 2, 3, 10, 100):
            area, tail = check_case(K, theta, N)
            print(f'K={K} N={N:3d} polygon_area={area:.12f} outer_area={tail:.12f}')
    print('all finite polygon tests passed')


if __name__ == '__main__':
    main()
