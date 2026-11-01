"""Independent reproducible checks for a Haar central-section polygon law.

Python 3 standard library only. Uses direct edge intersection and Gaussian
sampling, independent of the analytic solid-angle integration.
"""
import math
import random


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def p_general(columns):
    gram = [[dot(columns[i], columns[j]) for j in range(3)] for i in range(3)]
    m = [[-1., 1., 1.], [1., -1., 1.], [1., 1., -1.]]
    total = 1.
    for a in (-1, 1):
        for b in (-1, 1):
            for c in (-1, 1):
                signs = (a, b, c)
                msign = [[m[i][j] * signs[j] for j in range(3)] for i in range(3)]
                cov = multiply(multiply(msign, gram), transpose(msign))
                for i in range(3):
                    for j in range(i + 1, 3):
                        rho = cov[i][j] / math.sqrt(cov[i][i] * cov[j][j])
                        total += math.asin(max(-1., min(1., rho))) / (4 * math.pi)
    return total


def cross(x, y):
    return [x[1]*y[2]-x[2]*y[1],
            x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0]]


def solve3(rows, b):
    a, c, d = rows
    ac = cross(c, d)
    ca = cross(d, a)
    da = cross(a, c)
    det = dot(a, ac)
    assert abs(det) > 1e-12
    return [(b[0]*ac[k]+b[1]*ca[k]+b[2]*da[k])/det for k in range(3)]


def p_spherical(columns):
    # Eight simplicial cones, evaluated by their spherical excess / solid angle.
    # This expression is algebraically independent of Gaussian orthant expansion.
    total = 0.0
    for s0 in (-1, 1):
        for s1 in (-1, 1):
            for s2 in (-1, 1):
                signs = (s0, s1, s2)
                rays = [solve3(columns, [signs[i]*(i != j) for i in range(3)])
                        for j in range(3)]
                x, y, z = rays
                denominator = (math.sqrt(dot(x,x)*dot(y,y)*dot(z,z))
                               +dot(x,y)*math.sqrt(dot(z,z))
                               +dot(x,z)*math.sqrt(dot(y,y))
                               +dot(y,z)*math.sqrt(dot(x,x)))
                numerator = abs(dot(x,cross(y,z)))
                omega = 2*math.atan2(numerator, denominator)
                total += omega/(4*math.pi)
    return total


def p_equi(r):
    assert -0.5 < r < 1
    x = (2*r - 1) / (3 - 2*r)
    y = -math.sqrt((1 + 2*r) / (3*(3 - 2*r)))
    return 1 + 3/math.pi * (math.asin(x) + math.asin(y))


def chol_columns(r):
    # Upper triangular matrix whose columns have Gram (1-r)I+rJ.
    g = [[1.0 if i == j else r for j in range(3)] for i in range(3)]
    l = [[0.] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(i + 1):
            x = g[i][j] - sum(l[i][k] * l[j][k] for k in range(j))
            l[i][j] = math.sqrt(x) if i == j else x/l[j][j]
    return l


def edge_vertices(w):
    # Each cube edge fixes two signs and frees one coordinate.
    count = 0
    for axis in range(3):
        others = [i for i in range(3) if i != axis]
        for s in (-1., 1.):
            for t in (-1., 1.):
                offset = s*w[others[0]] + t*w[others[1]]
                if abs(offset) < abs(w[axis]):
                    count += 1
    return count


def simulate(columns, samples, seed):
    rand = random.Random(seed)
    cnt = 0
    for sample in range(samples):
        normal = (rand.gauss(0, 1), rand.gauss(0, 1), rand.gauss(0, 1))
        w = [dot(v, normal) for v in columns]
        sides = edge_vertices(w)
        flag = max(map(abs, w)) < sum(map(abs, w)) - max(map(abs, w))
        if sides != (6 if flag else 4):
            raise AssertionError('edge/face mismatch')
        cnt += (sides == 6)
    return cnt / samples


def run():
    rhos = [-0.49, -0.4, -0.2, 0., 0.2, 0.6, 0.95]
    for i, r in enumerate(rhos):
        cols = chol_columns(r)
        p1 = p_general(cols)
        p2 = p_equi(r)
        p3 = p_spherical(cols)
        assert abs(p1-p3)<5e-12, (r, p1, p3)
        assert abs(p1-p2) < 5e-13, (r, p1, p2)
        mc = simulate(cols, 140000, seed=93001+i)
        error = abs(mc-p2)
        print('equi r=', r, 'formula=', round(p2, 10), 'sample=', round(mc, 7), 'error=', round(error, 7))
        assert error < 0.009
    regular = 1-6*math.asin(1/3)/math.pi
    assert abs(p_equi(0)-regular) < 1e-13
    a = [[1,0,0], [0.5,1.,0.], [-0.1,0.3,0.8]]
    # Three nonsymmetric generator vectors.
    predicted = p_general(a)
    actual = simulate(a, 220000, seed=180018)
    assert abs(predicted-p_spherical(a)) < 5e-12
    assert abs(predicted-actual) < 0.008
    print('general formula=', round(predicted, 10), 'sample=', round(actual, 7))
    # Differentiate the explicit 1D formula numerically away from boundaries.
    for r in [-0.4, -0.2, -0.01, 0.01, 0.2, 0.8]:
        h = 1e-5
        observed = (p_equi(r+h)-p_equi(r-h))/(2*h)
        derivative = (3*math.sqrt(2)/(math.pi*(3-2*r)*math.sqrt(1-r))) * (1-1/math.sqrt(1+2*r))
        assert abs(observed-derivative) < 1e-7
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
