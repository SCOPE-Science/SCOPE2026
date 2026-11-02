"""Exact-arithmetic finite tests for the Braess-network extremizer theorem.

Run: python verify_braess.py
These tests do not replace the theorem's proof.
"""
from fractions import Fraction as Q
from itertools import combinations
from random import Random

ROUTES = ((0, 1), (0, 4, 3), (2, 3))
ZERO = Q(0)
ONE = Q(1)


def edge_load(flow):
    u, m, d = flow
    q = u + m + d
    return (q - d, u, d, q - u, m)


def edge_values(flow, laws):
    return tuple(alpha + beta * amount for (alpha, beta), amount in zip(laws, edge_load(flow)))


def path_costs(flow, laws):
    edge = edge_values(flow, laws)
    return tuple(sum((edge[j] for j in path), ZERO) for path in ROUTES)


def gap(flow, laws):
    c = path_costs(flow, laws)
    used = [c[i] for i in range(3) if flow[i] > 0]
    return max(used) - min(c)


def welfare(flow, laws):
    c = path_costs(flow, laws)
    return sum((x * y for x, y in zip(flow, c)), ZERO)


def solve(a, b):
    n = len(a)
    matrix = [list(a[i]) + [b[i]] for i in range(n)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if matrix[i][j]), None)
        if pivot is None:
            return None
        matrix[j], matrix[pivot] = matrix[pivot], matrix[j]
        z = matrix[j][j]
        matrix[j] = [v / z for v in matrix[j]]
        for i in range(n):
            if i == j:
                continue
            z = matrix[i][j]
            matrix[i] = [v - z * w for v, w in zip(matrix[i], matrix[j])]
    return tuple(row[-1] for row in matrix)


def wardrop(laws):
    """Enumerate active sets and solve linear Wardrop equations exactly."""
    zero = (ZERO, ZERO, ZERO)
    const = path_costs(zero, laws)
    basis = [path_costs(tuple(ONE if i == j else ZERO for i in range(3)), laws) for j in range(3)]
    slope = [[basis[j][i] - const[i] for j in range(3)] for i in range(3)]
    for m in (1, 2, 3):
        for support in combinations(range(3), m):
            rows = [[ONE] * m + [ZERO]]
            rhs = [ONE]
            for p in support:
                rows.append([slope[p][j] for j in support] + [-ONE])
                rhs.append(-const[p])
            ans = solve(rows, rhs)
            if ans is None:
                continue
            flow = tuple(ans[support.index(i)] if i in support else ZERO for i in range(3))
            if min(flow) < ZERO or sum(flow, ZERO) != ONE:
                continue
            c = path_costs(flow, laws)
            low = min(c)
            if all(flow[i] == 0 or c[i] == low for i in range(3)):
                return flow
    return None


def check_case(flow_f, flow_g, laws):
    l = min(path_costs(flow_f, laws))
    costs_f = path_costs(flow_f, laws)
    assert all(flow_f[i] == 0 or costs_f[i] == l for i in range(3))
    epsilon = gap(flow_g, laws)
    excess = welfare(flow_g, laws) - welfare(flow_f, laws)
    assert excess <= 2 * epsilon, (flow_f, flow_g, laws, excess, epsilon)
    if flow_g[0] < flow_f[0] and flow_g[2] < flow_f[2]:
        e_f = edge_values(flow_f, laws)
        e_g = edge_values(flow_g, laws)
        r = (costs_f[1] - l) + (e_f[1] - e_g[1]) + (e_f[2] - e_g[2]) + (e_g[4] - e_f[4])
        assert r >= ZERO
        assert excess <= 2 * epsilon - r, (flow_f, flow_g, laws, excess, epsilon, r)
    else:
        assert excess <= epsilon, (flow_f, flow_g, laws, excess, epsilon)
    if epsilon > 0 and excess == 2 * epsilon:
        assert flow_g[0] == flow_g[2] == ZERO
        assert flow_f[0] > 0 and flow_f[2] > 0
        c = path_costs(flow_g, laws)
        assert c[0] == c[2] == l + epsilon and c[1] == l + 2 * epsilon
        loads_f = edge_load(flow_f)
        loads_g = edge_load(flow_g)
        e_f = edge_values(flow_f, laws)
        e_g = edge_values(flow_g, laws)
        for j in (1, 2, 4):
            assert e_f[j] == e_g[j]
        assert costs_f[1] == l
    return epsilon, excess


def sharp_examples():
    # Both outer paths positive at the reference equilibrium; middle may be positive.
    count = 0
    for nu in (Q(0), Q(1, 5), Q(1, 2), Q(4, 5)):
        outer = (ONE - nu) / 2
        f = (outer, nu, outer)
        g = (ZERO, ONE, ZERO)
        for theta in (Q(1, 10), Q(1, 2), Q(2)):
            # Endpoints chosen so all three path costs at f are exactly one.
            b = ((Q(1, 2), ZERO), (Q(1, 2), ZERO),
                 (Q(1, 2), ZERO), (Q(1, 2), ZERO), (ZERO, ZERO))
            # An affine law A(x)=D(x)=1/2+(theta/outer)*(x-(1-outer))
            # would be negative at zero when outer is tiny; use a flat-then-linear
            # piecewise law, checked directly rather than through the affine test.
            def a(x): return Q(1, 2) + (theta / outer) * max(ZERO, x - (ONE - outer))
            edges_f = edge_load(f)
            edges_g = edge_load(g)
            cf = [a(edges_f[0]) + Q(1, 2), a(edges_f[0]) + a(edges_f[3]), Q(1, 2) + a(edges_f[3])]
            cg = [a(edges_g[0]) + Q(1, 2), a(edges_g[0]) + a(edges_g[3]), Q(1, 2) + a(edges_g[3])]
            assert cf == [ONE, ONE, ONE]
            assert cg == [ONE + theta, ONE + 2 * theta, ONE + theta]
            assert cg[1] - min(cg) == theta
            assert cg[1] - sum((f[i] * cf[i] for i in range(3)), ZERO) == 2 * theta
            count += 1
    return count


def run():
    r = Random(240600295)
    counts = dict(models=0, flows=0, positive_equalities=0, skipped_degenerate=0)
    for _ in range(600):
        # Rational coefficients, including flat edges and nonzero constants.
        laws = tuple((Q(r.randrange(5), 4), Q(r.randrange(5), 4)) for _ in range(5))
        f = wardrop(laws)
        if f is None:
            counts['skipped_degenerate'] += 1
            continue
        counts['models'] += 1
        for denom in (2, 3, 4, 5, 7, 9):
            for iu in range(denom + 1):
                for im in range(denom - iu + 1):
                    idn = denom - iu - im
                    g = (Q(iu, denom), Q(im, denom), Q(idn, denom))
                    epsilon, excess = check_case(f, g, laws)
                    counts['flows'] += 1
                    if epsilon > 0 and excess == 2 * epsilon:
                        counts['positive_equalities'] += 1
    counts['explicit_sharp_examples'] = sharp_examples()
    print(counts)
    assert counts['models'] >= 550 and counts['flows'] > 50000
    assert counts['explicit_sharp_examples'] == 12


if __name__ == '__main__':
    run()
