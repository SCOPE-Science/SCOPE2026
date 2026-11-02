"""Exact-rational checks for the six-patch Turing stability example.

Run: python3 verify.py.  Python standard library only.
This program verifies the explicit finite certificates; the general
mode-selection statement is proved analytically in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations


def matrix_multiply(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def characteristic_coefficients(matrix):
    """Coefficients of det(t I - matrix), via Newton identities."""
    n = len(matrix)
    power = [[int(i == j) for j in range(n)] for i in range(n)]
    traces = [0]
    for _ in range(n):
        power = matrix_multiply(power, matrix)
        traces.append(sum(power[i][i] for i in range(n)))
    coefficients = [Q(1)]
    for k in range(1, n + 1):
        c = -sum(coefficients[k - j] * traces[j]
                 for j in range(1, k + 1)) / k
        coefficients.append(c)
    assert all(c.denominator == 1 for c in coefficients)
    return tuple(int(c) for c in coefficients)


def roots_to_coefficients(roots):
    c = [1]
    for x in roots:
        nxt = [0] * (len(c) + 1)
        for i, v in enumerate(c):
            nxt[i] += v
            nxt[i + 1] -= x * v
        c = nxt
    return tuple(c)


def laplacian(n, edges):
    L = [[0] * n for _ in range(n)]
    for a, b in edges:
        L[a][a] += 1
        L[b][b] += 1
        L[a][b] -= 1
        L[b][a] -= 1
    return L


# Fixed biological reaction kinetics.
alpha, A, beta, gamma, eta, e = Q(2, 3), Q(1, 50), Q(6), Q(1, 2), Q(1, 2), Q(1)
u, v = Q(1, 10), Q(6, 5)
f = alpha * (u * u * (1 - u) / (u + A) - u * v / (1 + beta * u))
g = beta * u * v / (1 + beta * u) - gamma * v * v / (e + eta * v)
assert (f, g) == (0, 0)

# Exact analytic partial derivatives, not finite differences.
N = u * u * (1 - u)
Np = 2 * u - 3 * u * u
a = alpha * ((Np * (u + A) - N) / (u + A)**2 - v / (1 + beta * u)**2)
b = -alpha * u / (1 + beta * u)
c = beta * v / (1 + beta * u)**2
d = beta * u / (1 + beta * u) - gamma * (2 * e * v + eta * v * v) / (e + eta * v)**2
assert (a, b, c, d) == (Q(31, 144), -Q(1, 24), Q(45, 16), -Q(15, 64))
delta = a * d - b * c
assert delta == Q(205, 3072)
assert a + d == -Q(11, 576) < 0 and delta > 0 and a > 0 and d < 0

prism = [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)] + [(i, i + 3) for i in range(3)]
bipartite = [(i, j) for i in range(3) for j in range(3, 6)]
for edges, expected in [(prism, [0, 2, 3, 3, 5, 5]),
                        (bipartite, [0, 3, 3, 3, 3, 6])]:
    L = laplacian(6, edges)
    assert all(L[i][i] == 3 for i in range(6))
    assert characteristic_coefficients(L) == roots_to_coefficients(expected)


def modal_det(q, du, dv):
    return delta - (a * dv + d * du) * q + du * dv * q * q


def modal_trace(q, du, dv):
    return a + d - (du + dv) * q

for du, dv, vals, prism_unstable, bipartite_unstable in [
    (Q(1, 20), Q(9, 20),
     {0: Q(205, 3072), 2: -Q(1043, 76800), 3: Q(1057, 76800),
      5: Q(625, 3072), 6: Q(28093, 76800)}, True, False),
    (Q(1, 60), Q(261, 2000),
     {0: Q(205, 3072), 2: Q(51949, 1920000), 3: Q(26389, 1920000),
      5: Q(13, 76800), 6: -Q(179, 1920000)}, False, True),
]:
    for q, value in vals.items():
        assert modal_det(q, du, dv) == value
        assert modal_trace(q, du, dv) < 0
    assert any(vals[q] < 0 for q in (2, 3, 5)) == prism_unstable
    assert any(vals[q] < 0 for q in (3, 6)) == bipartite_unstable

# Six is the first order with two nonisomorphic connected regular graphs
# of one common degree. For n <= 5, connected degree-2 regular graphs
# are cycles, degree-(n-1) graphs are complete, and any other possible
# regular degree is excluded by connectivity or parity.
# Among six-vertex cubic graphs, the complementary degree-2 graph is
# necessarily C6 or C3+C3, producing the two graphs above.
print('VERIFIED exact kinetics, graph spectra, both directional instability witnesses')
