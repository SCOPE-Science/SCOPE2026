"""Reproduce finite triangle nodal-clipping energy checks.

Only Python 3 and NumPy are required. The analytic all-triangle proof is in
RESULT.md; the finite tests below are corroboration, not a proof by sampling.
"""
from fractions import Fraction as F
import math
import numpy as np


def stiffness(vertices):
    vertices = np.asarray(vertices, dtype=float)
    B = np.column_stack((vertices[1] - vertices[0], vertices[2] - vertices[0]))
    determinant = np.linalg.det(B)
    assert abs(determinant) > 1.e-12
    R = np.linalg.inv(B).T
    gradients = np.vstack((-(R[:, 0] + R[:, 1]), R[:, 0], R[:, 1]))
    return abs(determinant) / 2 * (gradients @ gradients.T), gradients


def e(K, values):
    values = np.asarray(values, dtype=float)
    return float(values @ K @ values)


def triangle(angle_degrees, side2=1.0):
    t = math.radians(angle_degrees)
    return np.array([[0., 0.], [1., 0.],
                     [side2 * math.cos(t), side2 * math.sin(t)]])


def sharp_constant(angle_degrees):
    return 1 if angle_degrees <= 90 else 1 / math.sin(math.radians(angle_degrees))**2


def check():
    # A single 120-degree triangle, with stiffness normalized by a common factor.
    K = [[F(4), F(-2), F(-2)],
         [F(-2), F(4, 3), F(2, 3)],
         [F(-2), F(2, 3), F(4, 3)]]
    def exact(z):
        return sum(z[i] * K[i][j] * z[j] for i in range(3) for j in range(3))
    before = [F(1), F(0), F(3, 2)]
    after = [F(1), F(0), F(1)]
    assert exact(before) == F(1)
    assert exact(after) == F(4, 3)

    rng = np.random.default_rng(67819)
    trial_count = 0
    sharp_count = 0
    for angle in [35., 59., 89., 90., 91., 101., 115., 120., 140., 169.]:
        for side in [0.65, 1., 2.1]:
            vertices = triangle(angle, side)
            matrix, grad = stiffness(vertices)
            # The other two angles are acute for the geometries tested.
            other = []
            for j in range(3):
                left = vertices[(j + 1) % 3] - vertices[j]
                right = vertices[(j + 2) % 3] - vertices[j]
                other.append(math.degrees(math.acos(np.clip(
                    np.dot(left, right) / np.linalg.norm(left) / np.linalg.norm(right), -1., 1.))))
            C = max([1.] + [1 / math.sin(math.radians(t))**2 for t in other if t > 90.])
            if angle > 90:
                assert np.argmax(other) == 0
                # Upper clipping: sorted vertex values x_1 < x_0 < x_2.
                d1 = .4
                d2 = -d1 * np.linalg.norm(grad[1]) * math.cos(math.radians(angle)) / np.linalg.norm(grad[2])
                x = np.array([1., 1. - d1, 1. + d2])
                y = np.clip(x, 0, 1)
                assert abs(e(matrix, y) / e(matrix, x) - C) < 2.e-10
                # Lower clipping uses the reverse saturated interval.
                d2 = .4
                d1 = -d2 * np.linalg.norm(grad[2]) * math.cos(math.radians(angle)) / np.linalg.norm(grad[1])
                x = np.array([0., -d1, d2])
                y = np.maximum(x, 0)
                assert abs(e(matrix, y) / e(matrix, x) - C) < 2.e-10
                sharp_count += 2
            for _ in range(2200):
                x = rng.uniform(-3, 3, size=3)
                ex = e(matrix, x)
                if ex < 1.e-10:
                    continue
                ys = [np.clip(x, 0, 1), np.maximum(x, 0), np.tanh(x)]
                for y in ys:
                    ey = e(matrix, y)
                    assert ey <= (C + 2.e-9) * ex, (angle, side, ex, ey, C)
                    trial_count += 1
    # Constant anisotropic diffusion: transform triangle by D^(-1/2).
    for angle in [55., 80., 105., 120., 150.]:
        vertices = triangle(angle, side2=1.4)
        _, grad = stiffness(vertices)
        for D in [np.diag([4., .7]), np.diag([.3, 2.]),
                  np.array([[2., .5], [.5, 1.5]])]:
            eigenvalues, eigvec = np.linalg.eigh(D)
            transform = (eigvec * eigenvalues**(-.5)) @ eigvec.T
            vertices_t = vertices @ transform.T
            metric_angles = []
            for j in range(3):
                l = vertices_t[(j+1)%3] - vertices_t[j]
                r = vertices_t[(j+2)%3] - vertices_t[j]
                metric_angles.append(math.degrees(math.acos(np.clip(
                    np.dot(l,r)/np.linalg.norm(l)/np.linalg.norm(r), -1,1))))
            C = max([1.] + [1/math.sin(math.radians(t))**2
                            for t in metric_angles if t>90])
            area = abs(np.linalg.det(np.column_stack((vertices[1]-vertices[0],
                                                     vertices[2]-vertices[0]))))/2
            K = area * grad @ D @ grad.T
            j = int(np.argmax(metric_angles))
            if metric_angles[j] > 90:
                i, k = (j + 1) % 3, (j + 2) % 3
                gi = math.sqrt(grad[i] @ D @ grad[i])
                gk = math.sqrt(grad[k] @ D @ grad[k])
                d1 = .4
                d2 = -d1 * gi * math.cos(math.radians(metric_angles[j])) / gk
                x = np.ones(3)
                x[i], x[k] = 1-d1, 1+d2
                assert abs(e(K,np.clip(x,0,1))/e(K,x)-C) < 5.e-10
                sharp_count += 1
            for _ in range(400):
                x = rng.uniform(-4,4,3)
                qx = e(K,x)
                for y in [np.clip(x,-1,2),np.maximum(x,0)]:
                    assert e(K,y) <= (C+2e-9)*qx
                    trial_count += 1
    print('VERIFY_OK: exact_example=4/3, random_energy_comparisons=%d, sharp_upper_lower_examples=%d' %
          (trial_count, sharp_count))

if __name__ == '__main__':
    check()
