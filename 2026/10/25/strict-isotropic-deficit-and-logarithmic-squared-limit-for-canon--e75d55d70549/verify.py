"""Exact rational diagnostics for uniform-volume moments of a canonical sign polytope.

Run: python3 verify.py  (Python standard library only).
Finite checks support but do not replace the all-dimensional analytical proof.
"""
from fractions import Fraction as F
from math import factorial


def moments(d):
    m = d + 1
    h = sum((F(1, k) for k in range(1, m + 1)), F(0))
    h2 = sum((F(1, k * k) for k in range(1, m + 1)), F(0))
    v = (2 * m - h * h - h2) / (d * m * (m + 1))
    return h, h2, v


def trace_via_dirichlet(d):
    total = F(0)
    for i in range(1, d + 1):
        weights = [F(1, j + 1) for j in range(i, d + 1)]
        total += (sum(weights, F(0)) ** 2 + sum((w * w for w in weights), F(0)))
    return total / ((d + 1) * (d + 2))


# Independent chamber second-moment expansion and harmonic formula.
for d in range(1, 61):
    h, h2, v = moments(d)
    assert trace_via_dirichlet(d) == d * v
    assert v > 0
    assert F(2**d, factorial(d + 1)) > 0

# Each rational inequality is exact. They exhaust dimensions 2 through 18.
for d in range(2, 19):
    h, h2, v = moments(d)
    m = d + 1
    R_to_power_2d = F(m*m) * ((2*m - h*h - h2) / (2*d)) ** d
    assert R_to_power_2d < 1, (d, R_to_power_2d)

# The analytic tail argument only needs these rational inequalities.
h6, _, _ = moments(5)
assert h6 == F(49, 20)
h20, h20_2, _ = moments(19)
assert h20*h20 + h20_2 - 2 > 12
assert sum((F(3**j, factorial(j)) for j in range(9)), F(0)) > 20

# A separate planar polygon shoelace computation confirms area and variance.
p = [(F(1,2),F(0)),(F(1,3),F(1,3)),(F(0),F(1,2)),
     (F(-1,3),F(1,3)),(F(-1,2),F(0)),(F(-1,3),F(-1,3)),
     (F(0),F(-1,2)),(F(1,3),F(-1,3))]
cross = lambda a,b: a[0]*b[1]-a[1]*b[0]
twice_area = sum((cross(p[i], p[(i+1)%len(p)]) for i in range(len(p))), F(0))
area = twice_area/2
int_x2 = sum((cross(p[i],p[(i+1)%len(p)]) *
             (p[i][0]**2+p[i][0]*p[(i+1)%len(p)][0]+p[(i+1)%len(p)][0]**2)
             for i in range(len(p))), F(0)) / 12
assert area == F(2,3)
assert int_x2/area == moments(2)[2] == F(23,432)

print('VERIFY_OK exact_dirichlet_traces=60 strict_ratios=17 planar_area=2/3 planar_variance=23/432 tail_base=20')
