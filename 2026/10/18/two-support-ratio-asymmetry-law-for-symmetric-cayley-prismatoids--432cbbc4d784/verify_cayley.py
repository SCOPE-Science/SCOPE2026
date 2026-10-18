"""Reproducibility checks for support-ratio formulas of symmetric Cayley prismatoids.

Standard-library exact arithmetic. Execute: python verify_cayley.py
Finite checks do not establish the dimension-independent theorem.
"""
from fractions import Fraction as F
from itertools import product, combinations
from random import Random


def optimum(a, b):
    ratios_ab = [F(y, x) for x, y in zip(a, b)]
    alpha = min([F(1)] + ratios_ab)
    beta = min([F(1)] + [F(x, y) for x, y in zip(a, b)])
    if alpha * (2 - beta) >= 1:
        U, V = F(0), 1 - beta
    elif beta * (2 - alpha) >= 1:
        U, V = 1 - alpha, F(0)
    else:
        U = (1 - 2 * alpha + alpha * beta) / (1 - alpha * beta)
        V = (1 - 2 * beta + alpha * beta) / (1 - alpha * beta)
    Q = 2 + U + V
    delta = [((1 + U) * x + (1 + V) * y - 2 * max(x, y)) / Q
             for x, y in zip(a, b)]
    return alpha, beta, U, V, Q, delta


def independent_vertex_optimum(alpha, beta):
    # Enumerate all vertices of the 2D LP without using its closed-form solution.
    lines = [(F(1), F(0), F(0)), (F(0), F(1), F(0)),
             (F(1), alpha, 1-alpha), (beta, F(1), 1-beta)]
    candidates = []
    for (a, b, c), (d, e, f) in combinations(lines, 2):
        det = a*e-b*d
        if det == 0:
            continue
        U, V = (c*e-b*f)/det, (a*f-c*d)/det
        if U >= 0 and V >= 0 and U + alpha*V >= 1-alpha and beta*U+V >= 1-beta:
            candidates.append((U+V, U, V))
    return min(candidates)


def run():
    rng = Random(191)
    checked_profiles = checked_directions = checked_centers = 0
    for d in range(1, 7):
        for trial in range(220):
            a = [rng.randint(1, 20) for _ in range(d)]
            b = [rng.randint(1, 20) for _ in range(d)]
            if trial % 11 == 0:
                b = a[:]
            if trial % 13 == 0:
                b = [max(x, y) for x, y in zip(a, b)]
            alpha, beta, U, V, Q, delta = optimum(a, b)
            obj, UU, VV = independent_vertex_optimum(alpha, beta)
            assert (U+V, U, V) == (obj, UU, VV)
            assert Q >= 2 and all(z >= 0 for z in delta)
            for _ in range(35):
                direction = [rng.randint(-4, 4) for _ in range(d)]
                if all(x == 0 for x in direction):
                    direction[0] = 1
                hK = sum(x*abs(u) for x, u in zip(a, direction))
                hL = sum(x*abs(u) for x, u in zip(b, direction))
                # Test a vertex of the claimed incenter product box.
                z = [v if rng.randrange(2) else -v for v in delta]
                lhs = Q * abs(sum(u*v for u, v in zip(direction, z)))
                rhs = (1+U)*hK+(1+V)*hL-2*max(hK, hL)
                assert lhs <= rhs, (a, b, direction, lhs, rhs)
                checked_directions += 1
                # Moving beyond an active coordinate slab must violate an axis test.
                for j in range(d):
                    if delta[j] == 0:
                        hKj, hLj = a[j], b[j]
                        bound = (1+U)*hKj+(1+V)*hLj-2*max(hKj, hLj)
                        assert bound == 0
                checked_centers += 1
            checked_profiles += 1
    print('PASS:', checked_profiles, 'exact rational profiles;',
          checked_directions, 'support constraints;',
          checked_centers, 'center checks')


if __name__ == '__main__':
    run()
