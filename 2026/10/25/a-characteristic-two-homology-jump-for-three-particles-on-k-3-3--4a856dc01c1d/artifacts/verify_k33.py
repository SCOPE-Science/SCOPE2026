#!/usr/bin/env python3
"""Exact cellular homology check for three unordered points on K_{3,3}.

Uses the Abrams discretized configuration complex after subdividing every edge
of K_{3,3} once.  All rank calculations over Q use Fraction arithmetic; ranks
mod 2 use exact bitset elimination.  Standard-library only.
"""
from fractions import Fraction
from itertools import combinations

N_PARTICLES = 3
N_VERTICES = 15

# Original K_{3,3} has left vertices 0,1,2 and right vertices 3,4,5.
# Midpoint 6+3*i+j subdivides the edge joining i to 3+j.
EDGES = []
for i in range(3):
    for j in range(3):
        m = 6 + 3 * i + j
        EDGES.extend(((i, m), (3 + j, m)))
EDGES = sorted(tuple(sorted(e)) for e in EDGES)


def cells_of_dimension(k):
    """Cells are k pairwise endpoint-disjoint edges plus 3-k other vertices."""
    out = []
    for es in combinations(range(len(EDGES)), k):
        occupied = set()
        valid = True
        for ei in es:
            u, v = EDGES[ei]
            if u in occupied or v in occupied:
                valid = False
                break
            occupied.update((u, v))
        if not valid:
            continue
        free = [v for v in range(N_VERTICES) if v not in occupied]
        for vs in combinations(free, N_PARTICLES - k):
            out.append((tuple(es), tuple(vs)))
    return out


CELLS = [cells_of_dimension(k) for k in range(N_PARTICLES + 1)]
INDEX = [{cell: i for i, cell in enumerate(ck)} for ck in CELLS]


def boundary_columns(k):
    """Return columns of d_k:C_k -> C_{k-1}, as integer sparse dictionaries."""
    cols = []
    for es, vs in CELLS[k]:
        d = {}
        # Orient each edge from its lower-numbered endpoint to its higher one;
        # orient a product cell by increasing edge index.
        for p, ei in enumerate(es):
            u, v = EDGES[ei]
            remaining_edges = tuple(e for e in es if e != ei)
            for endpoint, endpoint_sign in ((u, -1), (v, 1)):
                face = (remaining_edges, tuple(sorted(vs + (endpoint,))))
                row = INDEX[k - 1][face]
                d[row] = d.get(row, 0) + ((-1) ** p) * endpoint_sign
        cols.append({r: c for r, c in d.items() if c})
    return cols


D = [None] + [boundary_columns(k) for k in range(1, N_PARTICLES + 1)]


def compose_column(d_lower, column):
    """Apply d_{k-1} to one sparse column of d_k over Z."""
    out = {}
    for row, coeff in column.items():
        for r2, c2 in d_lower[row].items():
            out[r2] = out.get(r2, 0) + coeff * c2
    return {r: c for r, c in out.items() if c}


def check_chain_condition():
    for k in range(2, N_PARTICLES + 1):
        for j, col in enumerate(D[k]):
            if compose_column(D[k - 1], col):
                raise AssertionError(f"d_{k-1} d_{k} != 0 at column {j}")


def rank_over_q(cols):
    """Exact sparse column elimination over Q; pivots are smallest row indices."""
    basis = {}
    for col in cols:
        d = {r: Fraction(v) for r, v in col.items() if v}
        while d:
            p = min(d)
            if p not in basis:
                pivot = d[p]
                basis[p] = {r: v / pivot for r, v in d.items()}
                break
            b = basis[p]
            factor = d[p]
            for r, v in b.items():
                nv = d.get(r, Fraction(0)) - factor * v
                if nv:
                    d[r] = nv
                elif r in d:
                    del d[r]
    return len(basis)


def rank_over_f2(cols):
    """Exact column elimination over F_2, represented by Python integers."""
    basis = {}
    for col in cols:
        x = 0
        for r, coeff in col.items():
            if coeff & 1:
                x ^= 1 << r
        while x:
            p = x.bit_length() - 1
            if p not in basis:
                basis[p] = x
                break
            x ^= basis[p]
    return len(basis)


def betti(cell_counts, ranks):
    return [cell_counts[0] - ranks[0]] + [
        cell_counts[k] - ranks[k - 1] - ranks[k]
        for k in range(1, N_PARTICLES)
    ] + [cell_counts[N_PARTICLES] - ranks[N_PARTICLES - 1]]


def main():
    counts = [len(ck) for ck in CELLS]
    expected_counts = [455, 1404, 1386, 432]
    if counts != expected_counts:
        raise AssertionError(("cell counts", counts, expected_counts))
    check_chain_condition()
    q_ranks = [rank_over_q(D[k]) for k in range(1, N_PARTICLES + 1)]
    f2_ranks = [rank_over_f2(D[k]) for k in range(1, N_PARTICLES + 1)]
    expected_q = [454, 946, 432]
    expected_f2 = [454, 945, 432]
    if q_ranks != expected_q:
        raise AssertionError(("Q ranks", q_ranks, expected_q))
    if f2_ranks != expected_f2:
        raise AssertionError(("F2 ranks", f2_ranks, expected_f2))
    bq = betti(counts, q_ranks)
    bf2 = betti(counts, f2_ranks)
    if bq != [1, 4, 8, 0] or bf2 != [1, 5, 9, 0]:
        raise AssertionError(("Betti vectors", bq, bf2))
    euler_cells = sum((-1) ** k * counts[k] for k in range(4))
    euler_q = sum((-1) ** k * bq[k] for k in range(4))
    euler_f2 = sum((-1) ** k * bf2[k] for k in range(4))
    if not (euler_cells == euler_q == euler_f2 == 5):
        raise AssertionError(("Euler characteristics", euler_cells, euler_q, euler_f2))
    print("cell_counts:", counts)
    print("ranks_over_Q:", q_ranks)
    print("ranks_over_F2:", f2_ranks)
    print("betti_over_Q:", bq)
    print("betti_over_F2:", bf2)
    print("Euler_characteristic:", euler_cells)
    print("chain_condition: PASS (integral d^2=0)")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
