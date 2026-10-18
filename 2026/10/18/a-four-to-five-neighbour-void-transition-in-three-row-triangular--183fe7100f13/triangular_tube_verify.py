"""Exact independent checks for triangular-tube bootstrap-culling fixed points.

Requires Python 3 and SymPy; NumPy is used only for numerical Perron data.
Run: python triangular_tube_verify.py
"""
from collections import Counter
from itertools import product, combinations
from math import comb
import sympy as sp

COLUMN_MASKS = tuple(range(8))


def local_stable(left, middle, right, threshold):
    """Admissibility from occupied-neighbour counts in three adjacent columns."""
    for row in range(3):
        if not ((middle >> row) & 1):
            continue
        vertical = sum((middle >> s) & 1 for s in range(3) if s != row)
        incoming = ((left >> row) & 1) + ((left >> ((row + 1) % 3)) & 1)
        outgoing = ((right >> row) & 1) + ((right >> ((row - 1) % 3)) & 1)
        if vertical + incoming + outgoing < threshold:
            return False
    return True


def directed_graph(threshold):
    nodes = tuple(product(COLUMN_MASKS, repeat=2))
    successors = {u: [] for u in nodes}
    for a, b, c in product(COLUMN_MASKS, repeat=3):
        if local_stable(a, b, c, threshold):
            successors[(a, b)].append((b, c))
    return successors


def strongly_connected_components(edges):
    seen = {}
    low = {}
    stack = []
    on_stack = set()
    components = []
    clock = 0

    def visit(u):
        nonlocal clock
        seen[u] = low[u] = clock
        clock += 1
        stack.append(u)
        on_stack.add(u)
        for v in edges[u]:
            if v not in seen:
                visit(v)
                low[u] = min(low[u], low[v])
            elif v in on_stack:
                low[u] = min(low[u], seen[v])
        if low[u] == seen[u]:
            comp = []
            while True:
                v = stack.pop()
                on_stack.remove(v)
                comp.append(v)
                if v == u:
                    break
            components.append(tuple(sorted(comp)))

    for u in edges:
        if u not in seen:
            visit(u)
    return components


def recurrent_components(edges):
    return sorted(
        (c for c in strongly_connected_components(edges)
         if len(c) > 1 or c[0] in edges[c[0]]),
        key=lambda c: (-len(c), c),
    )


def integer_matrix(edges, component):
    ix = {v: i for i, v in enumerate(component)}
    out = sp.zeros(len(component))
    for u in component:
        for v in edges[u]:
            if v in ix:
                out[ix[u], ix[v]] = 1
    return out


def physical_neighbours(n):
    """Independent geometrical construction, without using local_stable."""
    output = []
    for col in range(n):
        for row in range(3):
            coords = {(col, other) for other in range(3) if other != row}
            coords.add(((col - 1) % n, row))
            coords.add(((col + 1) % n, row))
            coords.add(((col - 1) % n, (row + 1) % 3))
            coords.add(((col + 1) % n, (row - 1) % 3))
            assert len(coords) == 6
            output.append(sum(1 << (3 * a + b) for a, b in coords))
    return output


def physical_census(n, threshold):
    neighbor_masks = physical_neighbours(n)
    by_occupation = Counter()
    for state in range(1 << (3 * n)):
        if all((state & (1 << pos)) == 0 or
               (state & neighbor_masks[pos]).bit_count() >= threshold
               for pos in range(3 * n)):
            by_occupation[state.bit_count()] += 1
    return by_occupation


def cyclic_hard_core_count(n):
    """Empty state plus independently labelled vacancies separated by 3 columns."""
    total = 1  # globally empty state
    for k in range(n + 1):
        for subset in combinations(range(n), k):
            chosen = set(subset)
            if all(((i + j) % n) not in chosen for i in chosen for j in (1, 2)):
                total += 3 ** k
    return total


def row_sum_bracket(matrix, iterations=30):
    n = matrix.rows
    out = [[j for j in range(n) if matrix[i, j]] for i in range(n)]
    vec = [1] * n
    for _ in range(iterations):
        vec = [sum(vec[j] for j in out[i]) for i in range(n)]
    nxt = [sum(vec[j] for j in out[i]) for i in range(n)]
    return min(sp.Rational(nxt[i], vec[i]) for i in range(n)), max(
        sp.Rational(nxt[i], vec[i]) for i in range(n))


def main():
    x = sp.symbols('x')
    poly9 = x ** 9 - 3*x ** 8 - 10*x ** 6 + 12*x ** 5 + 12*x ** 4 + \
            8*x ** 3 - 14*x ** 2 + 3*x - 1
    poly14 = x ** 14 - x ** 13 - 5*x ** 11 + 6*x ** 10 - x ** 9 + \
             10*x ** 8 - 11*x ** 7 + x ** 6 - 8*x ** 5 + 7*x ** 4 + \
             6*x ** 3 - 3*x ** 2 + 1
    e4 = directed_graph(4)
    e5 = directed_graph(5)
    s4 = recurrent_components(e4)
    s5 = recurrent_components(e5)
    assert tuple(map(len, s4)) == (31,)
    assert tuple(map(len, s5)) == (7, 1)
    assert s5[1] == ((0, 0),)
    T4 = integer_matrix(e4, s4[0])
    T5 = integer_matrix(e5, s5[0])
    assert sum(T4) == 79
    assert sum(T5) == 10
    assert sp.expand(T4.charpoly(x).as_expr() - x**7*(x-1)*poly9*poly14) == 0
    assert sp.expand(T5.charpoly(x).as_expr() - x**4*(x**3-x**2-3)) == 0
    assert (0, 0) in s4[0] and (0, 0) in e4[(0, 0)]
    assert (7, 7) in s5[0] and (7, 7) in e5[(7, 7)]
    print('Exact strongly connected component and polynomial checks: PASS')

    for n, expected4, expected5 in [(4,151,14),(5,455,17),(6,1754,47)]:
        p4 = physical_census(n, 4)
        p5 = physical_census(n, 5)
        assert sum(p4.values()) == expected4 == sp.trace(T4**n)
        assert sum(p5.values()) == expected5 == sp.trace(T5**n) + 1
        assert expected5 == cyclic_hard_core_count(n)
        print('Independent physical-bitmask, transfer, hard-core cross-check at n=%d: PASS' % n)
    assert int(sp.trace(T4**7)) == 5997
    assert int(sp.trace(T5**7)) + 1 == 86 == cyclic_hard_core_count(7)
    print('Seventh-length recurrence cross-check: PASS')

    lo, hi = row_sum_bracket(T4, 30)
    assert sp.Rational(34541746,10000000) < lo < hi < sp.Rational(34541748,10000000)
    print('Rigorous Perron radius bracket:', float(lo), float(hi))
    assert sp.count_roots(poly9, sp.Rational(345417,100000),
                               sp.Rational(345418,100000)) == 1
    assert sp.count_roots(poly14, sp.Rational(345417,100000),
                                sp.Rational(345418,100000)) == 0
    a4 = float(sp.nsolve(poly9, 3.45))
    assert lo < a4 < hi

    import numpy as np
    def weighted_stats(mat, comp):
        m = np.asarray(mat.tolist(), dtype=float)
        lam, u = np.linalg.eig(m)
        pos = np.argmax(lam.real)
        pr = u[:, pos].real
        lv, v = np.linalg.eig(m.T)
        lp = np.argmin(np.abs(lv-lam[pos]))
        pl = v[:, lp].real
        stationary = pl * pr
        stationary /= stationary.sum()
        n_occ = sum(stationary[j]*comp[j][1].bit_count()
                    for j in range(len(comp)))
        p_empty = sum(stationary[j] for j in range(len(comp))
                      if comp[j][1] == 0)
        return float(lam[pos].real), float(n_occ / 3), float(p_empty)
    a, rho, empty = weighted_stats(T4, s4[0])
    assert abs(a - a4) < 1e-10
    assert abs(rho - 0.7969487456890811) < 1e-9
    assert abs(empty - 0.00833835118453382) < 1e-9
    b = float(sp.nsolve(x**3-x**2-3, 1.86))
    rho5 = 1-(b-1)/(3*(3*b-2))
    assert abs(rho5-0.9198294099517192) < 1e-10
    print('Perron numerical entropy/density/empty-column constants: PASS')
    print('alpha_4=%.12f rho_4=%.12f void_4=%.12f'% (a,rho,empty))
    print('alpha_5=%.12f rho_5=%.12f'%(b,rho5))
    print('All exact and numerical checks passed.')

if __name__ == '__main__':
    main()
