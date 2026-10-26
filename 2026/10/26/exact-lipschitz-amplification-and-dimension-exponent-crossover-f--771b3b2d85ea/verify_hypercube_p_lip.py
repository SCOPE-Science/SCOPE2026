"""Independent finite-graph checks for antipodal p-energy interpolation.

Run with Python 3 standard library: python verify_hypercube_p_lip.py.
The finite checks corroborate, but do not replace, the analytical theorem.
"""
from fractions import Fraction
from math import comb, isclose, log, exp


def vertices_edges(d):
    return [(x, x ^ (1 << j)) for x in range(1 << d)
            for j in range(d) if not (x & (1 << j))]


def scalar_profile(d, p):
    # Independent one-dimensional weighted-energy constrained solution.
    weights = [comb(d, k) * (d - k) for k in range(d)]
    gradients = [w ** (-1.0 / (p - 1.0)) for w in weights]
    z = sum(gradients)
    result = [0.0]
    for t in gradients:
        result.append(result[-1] + t / z)
    return result


def rational_solve(matrix, rhs):
    n = len(rhs)
    a = [[Fraction(v) for v in row] + [Fraction(rhs[i])]
         for i, row in enumerate(matrix)]
    for j in range(n):
        piv = next(i for i in range(j, n) if a[i][j])
        a[j], a[piv] = a[piv], a[j]
        scale = a[j][j]
        a[j] = [v / scale for v in a[j]]
        for i in range(n):
            if i == j:
                continue
            scale = a[i][j]
            if scale:
                a[i] = [a[i][h] - scale * a[j][h] for h in range(n + 1)]
    return [row[-1] for row in a]


def check_p2_exact(d):
    count = 1 << d
    s, t = 0, count - 1
    unknowns = [v for v in range(count) if v not in (s, t)]
    indexed = {v: i for i, v in enumerate(unknowns)}
    mat = [[0] * len(unknowns) for _ in unknowns]
    rhs = [0] * len(unknowns)
    for v in unknowns:
        i = indexed[v]
        mat[i][i] = d
        for j in range(d):
            w = v ^ (1 << j)
            if w == t:
                rhs[i] += 1
            elif w != s:
                mat[i][indexed[w]] -= 1
    sol = rational_solve(mat, rhs)
    vals = [Fraction(0) for _ in range(count)]
    vals[t] = Fraction(1)
    for v in unknowns:
        vals[v] = sol[indexed[v]]
    z = sum((Fraction(1, comb(d - 1, k)) for k in range(d)), Fraction(0))
    predicted = [Fraction(0)]
    for k in range(d):
        predicted.append(predicted[-1] + Fraction(1, comb(d - 1, k)) / z)
    assert all(vals[v] == predicted[v.bit_count()] for v in range(count))
    actual_slope = max(abs(vals[x] - vals[y]) for x, y in vertices_edges(d))
    assert actual_slope == 1 / z
    assert d * actual_slope == Fraction(d, 1) / z
    return len(unknowns), len(vertices_edges(d)), str(d / z)


def check_p_any(d, p):
    # Check the Euler--Lagrange equation directly at every unlabeled vertex,
    # without using the collapsed layer-edge multiplicities in the equation.
    u = scalar_profile(d, p)
    tol = 2e-11
    all_edges = vertices_edges(d)
    for v in range(1, (1 << d) - 1):
        uv = u[v.bit_count()]
        eq = 0.0
        for j in range(d):
            w = v ^ (1 << j)
            dw = uv - u[w.bit_count()]
            eq += (1 if dw >= 0 else -1) * abs(dw) ** (p - 1)
        assert abs(eq) < tol, (d, p, v, eq)
    observed = max(abs(u[x.bit_count()] - u[y.bit_count()]) for x, y in all_edges)
    closed = 1 / sum(comb(d - 1, k) ** (-1 / (p - 1)) for k in range(d))
    assert isclose(observed, closed, rel_tol=1e-11, abs_tol=1e-12)
    assert all(u[k + 1] > u[k] for k in range(d))
    assert isclose(u[d], 1, rel_tol=0, abs_tol=1e-12)
    return (1 << d) - 2, len(all_edges)


def entropy(t):
    if t <= 0 or t >= 1:
        return 0.0
    return -t * log(t) - (1 - t) * log(1 - t)


def critical_limit(alpha, grid=10000):
    return 1 / (sum(exp(-entropy(j / grid) / alpha)
                    for j in range(grid + 1)) / grid - 1 / grid)


def run():
    independent_exact_vertices = independent_exact_edges = 0
    for d in range(2, 6):
        v, e, norm = check_p2_exact(d)
        independent_exact_vertices += v
        independent_exact_edges += e
        print('exact p=2', d, 'norm', norm)
    nonlinear_vertices = nonlinear_edges = 0
    for d in range(3, 9):
        for p in (1.5, 3.0, 5.0, 11.0):
            v, e = check_p_any(d, p)
            nonlinear_vertices += v
            nonlinear_edges += e
    for alpha in (0.5, 1.0, 2.0):
        d = 300
        p = alpha * d
        norm = d / sum(comb(d - 1, k) ** (-1 / (p - 1)) for k in range(d))
        limit = critical_limit(alpha)
        assert abs(norm - limit) < 0.06, (alpha, norm, limit)
        print('critical scaling', alpha, 'finite', round(norm, 8),
              'limit', round(limit, 8))
    print('PASS: exact-rational full-graph interior vertices', independent_exact_vertices)
    print('PASS: exact-rational full-graph edges', independent_exact_edges)
    print('PASS: nonlinear full-graph interior Euler equations', nonlinear_vertices)
    print('PASS: nonlinear full-graph edge values', nonlinear_edges)


if __name__ == '__main__':
    run()
