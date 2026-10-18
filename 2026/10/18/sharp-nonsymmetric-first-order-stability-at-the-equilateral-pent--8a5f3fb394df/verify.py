"""Independent finite checks for the local first-variation formulas.
Analytical proof is in RESULT.md; sampled calculations are diagnostics only.
"""
import itertools
import math

SQ3 = math.sqrt(3.0)
H = SQ3 / 2
S0 = 9 + 2 * SQ3
A = 2 * S0 / 3
K = (A - 1) / 2


def vector(angle):
    return (math.cos(angle), math.sin(angle))


def pentagon(d, a):
    e0, e1, e2 = vector(0), vector(d), vector(2 * math.pi / 3 + a)
    rx = -(e0[0] + e1[0] + e2[0])
    ry = -(e0[1] + e1[1] + e2[1])
    radius = math.hypot(rx, ry)
    assert radius < 2 and radius > 0
    phase = math.atan2(ry, rx)
    beta = math.acos(radius / 2)
    edges = (e0, e1, e2, vector(phase - beta), vector(phase + beta))
    vertices = [(0.0, 0.0)]
    for x, y in edges[:4]:
        u, v = vertices[-1]
        vertices.append((u+x, v+y))
    assert math.hypot(sum(v[0] for v in edges), sum(v[1] for v in edges)) < 3e-14
    assert all(abs(math.hypot(*v)-1) < 3e-14 for v in edges)
    distances = sum(math.dist(vertices[i], vertices[j]) for i, j in itertools.combinations(range(5), 2))
    edge_widths = []
    for ex, ey in edges:
        projections = [-ey*x + ex*y for x, y in vertices]
        edge_widths.append(max(projections) - min(projections))
    return min(edge_widths), distances, edge_widths


def check():
    cases = [(1., 0.), (1., .3), (1., 1.), (1., 2.), (1., -1.), (0., 1.), (0., -1.), (1., 4.), (.25, -4.)]
    for scale in [1e-3, 3e-4, 1e-4, 3e-5, 1e-5]:
        for d0, a0 in cases:
            d, a = d0 * scale, a0 * scale
            width, summation, _ = pentagon(d, a)
            m = max(d, a, d-a)
            approximate_width = H + m/2
            approximate_sum = S0 + H*d
            approximate_ratio = S0/H - (A*m-d)
            assert abs(width-approximate_width) < 40 * (abs(d)+abs(a))**2 + 1e-12
            assert abs(summation-approximate_sum) < 40 * (abs(d)+abs(a))**2 + 1e-12
            assert abs(summation/width-approximate_ratio) < 120 * (abs(d)+abs(a))**2 + 1e-11
            assert A*m-d >= K*(d+abs(a)) - 1e-13
    print('VERIFY_OK cases=45 first_order_uniform_O(r^2)_diagnostics=135 sharp_constant=', K)


if __name__ == '__main__':
    check()
