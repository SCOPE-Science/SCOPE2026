"""Exact-rational coefficient certificate for a critical affine-quermassintegral profile.

Run with Python 3.9 or later, no third-party dependencies.
"""
from fractions import Fraction as Q
from math import comb


def add(p, q):
    out = [Q(0)] * max(len(p), len(q))
    for i, v in enumerate(p):
        out[i] += v
    for i, v in enumerate(q):
        out[i] += v
    return out


def scale(p, s):
    return [s * x for x in p]


def mul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def power(p, k):
    ans = [Q(1)]
    for _ in range(k):
        ans = mul(ans, p)
    return ans


def rising(a, n):
    ans = Q(1)
    for k in range(n):
        ans *= a + k
    return ans


def moment(p, alpha):
    return sum((c * rising(alpha, k) / rising(Q(5), k) for k, c in enumerate(p)), Q(0))


Y = [Q(1, 56), -Q(3, 7), Q(1)]  # variable is s^2
A = [Q(1, 56), -Q(3, 14), Q(3, 8)]  # variable is z
B = [Q(0), -Q(3, 14), Q(1, 2)]
C = [Q(0), Q(0), Q(1, 8)]
D = add(add(mul(A, A), scale(mul(B, B), -Q(3, 2))),
        scale(mul(C, C), -Q(15, 2)))
assert D == [Q(1, 3136), -Q(3, 392), -Q(15, 1568),
             Q(9, 56), -Q(45, 128)]

N = 10
c_line = []
c_plane = []
for degree in range(5):
    c_line.append((-1) ** degree * comb(N + degree - 1, degree)
                  * moment(power(Y, degree), Q(1, 2)))
    c = Q(0)
    for r in range(degree // 2 + 1):
        q = degree - 2*r
        m = q+r
        c += (-1) ** m * comb(N+m-1, m) * comb(m, q) * (2**q) * moment(
            mul(power(A, q), power(D, r)), Q(1))
    c_plane.append(c)

assert c_line[:5] == [Q(1), Q(0), Q(363, 12544),
                      -Q(1573, 153664), Q(4492917, 550731776)]
assert c_plane[:5] == [Q(1), Q(0), Q(363, 6272),
                       -Q(1573, 76832), Q(4968273, 275365888)]
assert c_plane[2] == 2*c_line[2]
assert c_plane[3] == 2*c_line[3]
coefficient = (c_plane[4] - 2*c_line[4] - c_line[2]**2)/20
assert coefficient == Q(139863, 3147038720)
assert coefficient > 0

# Principal curvature radii are 1+t*tau(v) and 1+t*mu(v).
# The following endpoint/critical-point evaluations bound both polynomials.
def tau(v):
    return -3*v*v+Q(3, 7)*v+Q(1, 56)
def mu(v):
    return -15*v*v+Q(93, 7)*v-Q(47, 56)
assert tau(Q(1)) == mu(Q(1)) == -Q(143, 56)
assert tau(Q(1, 14)) == Q(13, 392)
assert mu(Q(31, 70)) == Q(4121, 1960)
assert max(abs(tau(Q(0))), abs(tau(Q(1))), abs(tau(Q(1, 14))),
           abs(mu(Q(0))), abs(mu(Q(1))), abs(mu(Q(31, 70)))) == Q(143, 56)
print('VERIFY_OK')
print('critical_quartic_coefficient =', coefficient)
