"""Exact-rational finite-instance checks for balanced multipartite graph projections.

Run with Python 3.10+; no third-party packages. Finite checks supplement,
not replace, the all-parameter argument in RESULT.md.
"""

from fractions import Fraction as F
from itertools import combinations


def edges(r, p):
    return [(u, v) for u, v in combinations(range(r * p), 2)
            if u // p != v // p]


def proposed_norms(r, p):
    assert r >= 3 and p >= 2
    z = F(3) + F(2, r) - F(8 * (r * p - 1), r * (r - 1) * p * p)
    b = F(2) + F(2, r) - F(4 * (r * p - 1), r * (r - 1) * p * p)
    return z, b


def column(r, p, e, all_edges):
    u, v = e
    coeff_b = F(1, (r - 1) * p * p)
    coeff_c = F(1, r * p * p)
    potentials = []
    for x in range(r * p):
        if x // p == u // p:
            potentials.append((p - 1 if x == u else -1) * coeff_b + coeff_c)
        elif x // p == v // p:
            potentials.append(-(p - 1 if x == v else -1) * coeff_b - coeff_c)
        else:
            potentials.append(F(0))
    laplacian = []
    for x in range(r * p):
        laplacian.append(sum((potentials[x] - potentials[y]
                              for y in range(r * p) if y // p != x // p), F(0)))
    assert laplacian == [F(int(x == u) - int(x == v)) for x in range(r * p)]
    cut = [potentials[x] - potentials[y] for x, y in all_edges]
    cyc = [F(int(f == e)) - t for f, t in zip(all_edges, cut)]
    for x in range(r * p):
        assert sum((cyc[k] if a == x else -cyc[k] if b == x else F(0)
                    for k, (a, b) in enumerate(all_edges)), F(0)) == 0
    return cut, cyc


def run():
    case_count = 0
    columns_checked = 0
    idempotence_checks = 0
    for r in range(3, 8):
        for p in range(2, 6):
            all_edges = edges(r, p)
            z_bound, b_bound = proposed_norms(r, p)
            z_columns = []
            for edge in all_edges:
                cut, cyc = column(r, p, edge, all_edges)
                assert sum(map(abs, cyc), F(0)) == z_bound
                assert sum(map(abs, cut), F(0)) == b_bound
                z_columns.append(cyc)
                columns_checked += 1
            # For smaller instances replay the projector identity via rational matrix multiplication.
            if len(all_edges) <= 48:
                for j in range(len(all_edges)):
                    for i in range(len(all_edges)):
                        assert sum((z_columns[k][i] * z_columns[j][k]
                                    for k in range(len(all_edges))), F(0)) == z_columns[j][i]
                        idempotence_checks += 1
            case_count += 1
    # Exact finite-difference identity underlying the part-count phase transition.
    for p in range(2, 22):
        for r in range(3, 42):
            z_next = proposed_norms(r + 1, p)[0]
            z_now = proposed_norms(r, p)[0]
            delta = F(-2 * (p*p*(r-1) - 4*p*(r+1) + 8), p*p*r*(r-1)*(r+1))
            assert z_next - z_now == delta
    print('PASS exact-rational checks')
    print('graph_parameter_cases', case_count)
    print('projector_columns', columns_checked)
    print('idempotence_entries', idempotence_checks)
    print('finite_difference_identities', 20 * 39)
    print('scope_of_tests', 'finite only; all-parameter conclusions are proved separately')


if __name__ == '__main__':
    run()
