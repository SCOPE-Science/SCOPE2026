"""Independent exact-fraction checks for two-patch colonization allocation."""
from fractions import Fraction as F
from itertools import product


def solve_linear(matrix, vector):
    """Solve a nonsingular rational system by independent Gauss-Jordan elimination."""
    n = len(vector)
    rows = [[F(x) for x in matrix[i]] + [F(vector[i])] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        factor = rows[j][j]
        rows[j] = [v / factor for v in rows[j]]
        for i in range(n):
            if i == j:
                continue
            factor = rows[i][j]
            rows[i] = [rows[i][k] - factor * rows[j][k] for k in range(n+1)]
    return tuple(rows[i][-1] for i in range(n))


def backward_equation_solution(a, b, x, y):
    # States 11, 10, 01: joint -> 10 at b, joint -> 01 at a.
    matrix = [[a+b, -b, -a], [-x, a+x, 0], [-y, 0, b+y]]
    return solve_linear(matrix, [1, 1, 1])


def closed_form(a, b, x, y):
    den = a*b*(a+b+x+y)
    return ((a*a+a*b+b*b+(a+b)*(x+y)+x*y)/den,
            ((b+x)*(a+b+y))/den,
            ((a+y)*(a+b+x))/den)


def budget_objective(a, b, c, x, weights):
    w11, w10, w01 = weights
    constant = (w11*(a*a+a*b+b*b+(a+b)*c)
                + w10*b*(a+b+c) + w01*(a+c)*(a+b))
    return (constant+(c+a*w10-b*w01)*x-x*x)/(a*b*(a+b+c))


def projected_optimum(a, b, c, weights):
    _, w10, w01 = weights
    unconstrained = (c+a*w10-b*w01)/2
    return min(c, max(F(0), unconstrained))


def run():
    instances = equations = objectives = comparisons = 0
    for ai, bi, ci in product(range(1, 5), repeat=3):
        a, b, c = map(F, (ai, bi, ci))
        for j in range(9):
            x = c*F(j, 8)
            y = c-x
            exact_times = backward_equation_solution(a, b, x, y)
            formula_times = closed_form(a, b, x, y)
            assert exact_times == formula_times, (a, b, x, y)
            equations += 1
            for i in range(5):
                for k in range(5-i):
                    weights = (F(i, 4), F(k, 4), F(4-i-k, 4))
                    measured = sum(w*t for w, t in zip(weights, exact_times))
                    analytic = budget_objective(a, b, c, x, weights)
                    assert analytic == measured
                    objectives += 1
        for i in range(5):
            for k in range(5-i):
                weights = (F(i, 4), F(k, 4), F(4-i-k, 4))
                best_x = projected_optimum(a, b, c, weights)
                best = budget_objective(a, b, c, best_x, weights)
                # Evaluate all nine grid points and the unconstrained stationary point if feasible.
                for j in range(9):
                    x = c*F(j, 8)
                    assert best >= budget_objective(a, b, c, x, weights)
                    comparisons += 1
                unconstrained = (c+a*weights[1]-b*weights[2])/2
                if 0 <= unconstrained <= c:
                    assert best_x == unconstrained
                    assert best-budget_objective(a,b,c,unconstrained,weights)==0
                if 0 < best_x < c:
                    assert budget_objective(a,b,c,best_x+c*F(1,16),weights) < best
                    assert budget_objective(a,b,c,best_x-c*F(1,16),weights) < best
                instances += 1
    print(f'VERIFY_OK exact_backward_systems={equations} weighted_expectations={objectives} allocation_instances={instances} global_grid_inequalities={comparisons}')


if __name__ == '__main__':
    run()
