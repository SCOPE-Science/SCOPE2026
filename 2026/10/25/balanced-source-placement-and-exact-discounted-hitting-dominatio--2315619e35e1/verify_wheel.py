"""Exact independent small-wheel checks for discounted hitting source placement.

Run with Python 3 standard library: python verify_wheel.py.
"""
from fractions import Fraction
from itertools import product


def solve_rational(matrix, vector):
    """Exact Gaussian elimination, independently of transfer formulas."""
    n = len(vector)
    rows = [list(map(Fraction, row)) + [Fraction(v)] for row, v in zip(matrix, vector)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if rows[i][col]), None)
        assert pivot is not None
        rows[col], rows[pivot] = rows[pivot], rows[col]
        div = rows[col][col]
        rows[col] = [v / div for v in rows[col]]
        for i in range(n):
            if i != col and rows[i][col]:
                factor = rows[i][col]
                rows[i] = [u - factor * v for u, v in zip(rows[i], rows[col])]
    return [row[-1] for row in rows]


def direct_potential(n, lam, source_mask):
    # Rim vertices 0..n-1, hub n; wheel with n+1 vertices.
    neighbours = [{(i - 1) % n, (i + 1) % n, n} for i in range(n)]
    neighbours.append(set(range(n)))
    missing = [v for v in range(n + 1) if not (source_mask >> v) & 1]
    if not missing:
        return [Fraction(1) for _ in range(n + 1)]
    mat = []
    rhs = []
    for v in missing:
        deg = len(neighbours[v])
        mat.append([Fraction(v == w) - (lam / deg if w in neighbours[v] else 0)
                    for w in missing])
        rhs.append(lam * sum(bool((source_mask >> u) & 1) for u in neighbours[v]) / deg)
    sol = solve_rational(mat, rhs)
    h = [Fraction(1) for _ in range(n + 1)]
    for v, x in zip(missing, sol):
        h[v] = x
    return h


def transfers(n, lam):
    # Segment Dirichlet solutions, derived from a recurrence and not from graph inversion.
    p = [Fraction(0), Fraction(1)]
    for m in range(2, n + 1):
        p.append(3 * p[-1] / lam - p[-2])
    D, psi = {1: Fraction(0)}, {1: Fraction(1)}
    for m in range(2, n + 1):
        f = [(p[m - j] + p[j]) / p[m] for j in range(1, m)]
        D[m] = sum((1 - u for u in f), Fraction(0))
        psi[m] = min(f)
    return D, psi


def best_floors_formula(n, lam):
    D, psi = transfers(n, lam)
    pstar = lam / (3 - 2 * lam)
    hub = [pstar]
    nohub = [None]
    for k in range(1, n + 1):
        longest = (n + k - 1) // k
        hub.append(pstar + (1 - pstar) * psi[longest])
        q, r = divmod(n, k)
        total_deficit = (k - r) * D[q] + (r * D[q + 1] if r else 0)
        x = lam * (n - total_deficit) / (n - lam * lam * total_deficit / (3 - 2 * lam))
        p = lam * x / (3 - 2 * lam)
        y = p + (1 - p) * psi[longest]
        nohub.append(min(x, y))
    for i in range(2, n):
        if i + 1 <= n:
            assert D[i + 1] - D[i] >= D[i] - D[i - 1]
    return hub, nohub


def main():
    lambdas = [Fraction(1, 3), Fraction(3, 5), Fraction(4, 5)]
    thresholds = [Fraction(1, 5), Fraction(1, 3), Fraction(2, 5),
                  Fraction(1, 2), Fraction(3, 5), Fraction(4, 5), Fraction(1)]
    checked_sets = 0
    checked_floors = 0
    checked_optima = 0
    examples = []
    for n in range(3, 9):
        for lam in lambdas:
            expected_hub, expected_rim = best_floors_formula(n, lam)
            best_hub = [None] * (n + 1)
            best_rim = [None] * (n + 1)
            for mask in range(1, 1 << (n + 1)):
                k = (mask & ((1 << n) - 1)).bit_count()
                hub = bool(mask & (1 << n))
                floor = min(direct_potential(n, lam, mask))
                array = best_hub if hub else best_rim
                if array[k] is None or floor > array[k]:
                    array[k] = floor
                checked_sets += 1
            for k in range(0, n + 1):
                assert best_hub[k] == expected_hub[k], (n, lam, k, best_hub[k], expected_hub[k])
                checked_floors += 1
                if k:
                    assert best_rim[k] == expected_rim[k], (n, lam, k, best_rim[k], expected_rim[k])
                    checked_floors += 1
            for tau in thresholds:
                direct = min([k+1 for k, floor in enumerate(best_hub) if floor >= tau] +
                             [k for k, floor in enumerate(best_rim) if floor is not None and floor >= tau])
                derived = min([k+1 for k, floor in enumerate(expected_hub) if floor >= tau] +
                              [k for k, floor in enumerate(expected_rim) if floor is not None and floor >= tau])
                assert direct == derived, (n, lam, tau, direct, derived)
                checked_optima += 1
                if n in (6, 8) and lam == Fraction(3, 5) and tau == Fraction(2, 5):
                    examples.append((n, str(lam), str(tau), derived))
    # A nontrivial hub-exclusion example, checked from the full linear equations.
    lam = Fraction(3, 5)
    nohub_opposite = min(direct_potential(4, lam, (1 << 0) | (1 << 2)))
    hub_with_one_rim = min(direct_potential(4, lam, (1 << 0) | (1 << 4)))
    hub_alone = min(direct_potential(4, lam, (1 << 4)))
    assert nohub_opposite == Fraction(21, 47)
    assert hub_with_one_rim == Fraction(9, 23)
    assert hub_alone == Fraction(1, 3)
    assert hub_with_one_rim < Fraction(2, 5) <= nohub_opposite
    print('hub_exclusion_wheel_n4=', (str(hub_alone), str(hub_with_one_rim), str(nohub_opposite)))
    print('checked_exact_vertex_subsets=', checked_sets)
    print('checked_exact_maximin_floors=', checked_floors)
    print('checked_exact_threshold_optima=', checked_optima)
    print('examples=', examples)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
