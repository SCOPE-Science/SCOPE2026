"""Exact rational checks for box-constrained social-network disagreement."""
from fractions import Fraction as F
from itertools import product, combinations


def solve(a, b):
    n = len(b)
    m = [[F(x) for x in row] + [F(b[i])] for i, row in enumerate(a)]
    for j in range(n):
        piv = next(i for i in range(j, n) if m[i][j] != 0)
        m[j], m[piv] = m[piv], m[j]
        factor = m[j][j]
        m[j] = [v / factor for v in m[j]]
        for i in range(n):
            if i != j:
                factor = m[i][j]
                m[i] = [u - factor * v for u, v in zip(m[i], m[j])]
    return [row[-1] for row in m]


def laplacian(n, weighted_edges):
    l = [[F(0) for _ in range(n)] for _ in range(n)]
    for (i, j), w in weighted_edges:
        w = F(w)
        l[i][i] += w
        l[j][j] += w
        l[i][j] -= w
        l[j][i] -= w
    return l


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def mul(a, x):
    return [dot(row, x) for row in a]


def energy(l, z):
    return dot(z, mul(l, z))


def matrix_plus_diag(l, k):
    return [[x+(k[i] if i == j else 0) for j, x in enumerate(row)] for i, row in enumerate(l)]


def disagreement(n, edges, k, s):
    l = laplacian(n, edges)
    z = solve(matrix_plus_diag(l, k), [a*b for a, b in zip(k, s)])
    return energy(l, z)


assertions = 0
n_cases = 0
positive_q_cases = 0
flat_cases = 0

for n in (2, 3, 4, 5):
    pairs = list(combinations(range(n), 2))
    base_choices = [list(zip(pairs, weights)) for weights in product((F(0), F(1, 3), F(2)), repeat=min(len(pairs), 3))]
    for idx, setting in enumerate(base_choices[:32]):
        k = [F(1 + (i + idx) % 4, 1 + (i + 2*idx) % 2) for i in range(n)]
        s = [F((i*i + idx) % 5, 4) for i in range(n)]
        l0 = laplacian(n, setting)
        mat = matrix_plus_diag(l0, k)
        z0 = solve(mat, [a*b for a, b in zip(k, s)])
        test_pair = pairs[(3*idx + n) % len(pairs)]
        i, j = test_pair
        b = [F((t == i) - (t == j)) for t in range(n)]
        h = solve(mat, b)
        r = dot(b, h)
        q = dot(b, z0)
        a = dot(z0, mul(l0, h))
        c = dot(h, [ki*hi for ki, hi in zip(k, h)])
        assert r > 0 and c > 0
        assertions += 2
        base = energy(l0, z0)
        end_weights = (F(0), F(5, 3))
        end_vals = []
        for t in (F(0), F(1, 8), F(1, 4), F(1, 2), F(1), F(5, 3)):
            lam = t/(1+r*t)
            formula = base + (q*q - 2*q*a)*lam - q*q*c*lam*lam
            direct = disagreement(n, setting + [(test_pair, t)], k, s)
            assert direct == formula
            assertions += 1
            if t in end_weights:
                end_vals.append(direct)
            if q == 0:
                assert direct == base
                flat_cases += 1
                assertions += 1
            else:
                positive_q_cases += 1
        end_min = min(end_vals)
        for t in (F(1, 8), F(1, 4), F(1, 2), F(1)):
            assert disagreement(n, setting + [(test_pair, t)], k, s) >= end_min
            assertions += 1
        n_cases += 1

# Exact nontrivial two-edge box optimum, distinct from both uniform corners.
base_edges = [(0, 1), (1, 2)]
values = {}
for first, second in product((F(1, 4), F(3)), repeat=2):
    values[(first, second)] = disagreement(3, [(base_edges[0], first), (base_edges[1], second)], [F(1)]*3, [F(0), F(0), F(1)])
assert values[(F(1, 4), F(1, 4))] == F(148, 1225)
assert values[(F(1, 4), F(3))] == F(16, 169)
assert values[(F(3), F(1, 4))] == F(199, 1521)
assert values[(F(3), F(3))] == F(87, 800)
assert min(values, key=values.get) == (F(1, 4), F(3))
assertions += 5

# At zero base weight, an added edge creates an exact rise then fall.
for t in (F(0), F(1, 8), F(1, 2), F(1), F(3)):
    val = disagreement(2, [((0, 1), t)], [F(1), F(1)], [F(0), F(1)])
    assert val == t/(1+2*t)**2
    assertions += 1

# Multivariate check on a 3-edge path with three levels per edge.
for s in ([F(0), F(0), F(1), F(1)], [F(0), F(1), F(0), F(1)], [F(1), F(1), F(1), F(1)]):
    k = [F(1), F(2), F(3), F(4)]
    e = [(0, 1), (1, 2), (2, 3)]
    corners = [disagreement(4, list(zip(e, ww)), k, s) for ww in product((F(1, 4), F(3)), repeat=3)]
    m = min(corners)
    for ww in product((F(1, 4), F(1), F(3)), repeat=3):
        assert disagreement(4, list(zip(e, ww)), k, s) >= m
        assertions += 1

print('PASS')
print('exact_fraction_assertions:', assertions)
print('rank_one_network_cases:', n_cases)
print('nonzero_contrast_parameter_checks:', positive_q_cases)
print('zero_contrast_parameter_checks:', flat_cases)
print('three_vertex_mixed_corner_optimum:', values)
