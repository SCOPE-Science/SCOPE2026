"""Exact finite F2 computation for the reduced Swiatkowski complex of B_4(K_5,5).
Standard library only. All matrix columns are constructed, and binary elimination is exact.
"""
from itertools import combinations, combinations_with_replacement, product
from math import comb

PART = 5
N = 4
EDGES = [(i, j) for i in range(PART) for j in range(PART)]
INCIDENT = [[] for _ in range(2 * PART)]
for edge_id, (i, j) in enumerate(EDGES):
    INCIDENT[i].append(edge_id)
    INCIDENT[PART + j].append(edge_id)


def basis(reference_last):
    reference = [incident[-1] if reference_last else incident[0]
                 for incident in INCIDENT]
    half_edges = [[(v, e) for e in INCIDENT[v] if e != reference[v]]
                  for v in range(2 * PART)]
    chain_bases = []
    for degree in range(N + 1):
        states = []
        for vertices in combinations(range(2 * PART), degree):
            for locals_ in product(*(half_edges[v] for v in vertices)):
                for monomial in combinations_with_replacement(range(len(EDGES)), N-degree):
                    states.append((locals_, monomial))
        chain_bases.append(states)
    return chain_bases, reference


def boundary_indices(state, lower_indices, reference):
    """Support of the boundary column, with repetitions allowed for XOR cancellation."""
    locals_, monomial = state
    for slot, (vertex, e) in enumerate(locals_):
        reduced = locals_[:slot] + locals_[slot + 1:]
        for target_edge in (e, reference[vertex]):
            yield lower_indices[(reduced, tuple(sorted(monomial + (target_edge,))))]


def rank_from_columns(states, lower, reference):
    indices = {state: i for i, state in enumerate(lower)}
    pivots = {}
    for state in states:
        vector = 0
        for index in boundary_indices(state, indices, reference):
            vector ^= 1 << index
        while vector:
            pivot_index = vector.bit_length()-1
            previous = pivots.get(pivot_index)
            if previous is None:
                pivots[pivot_index] = vector
                break
            vector ^= previous
    return len(pivots)


def test_boundary_squared(bases, reference):
    # Additional independent incidence sanity check, without relying on numerical ranks.
    # Algebraically, all degree-two cancellations follow from commuting edge variables.
    for q in range(2, 5):
        one_lower = {state: i for i, state in enumerate(bases[q - 1])}
        two_lower = {state: i for i, state in enumerate(bases[q - 2])}
        for state in bases[q][:200]:
            accumulator = set()
            for mid in boundary_indices(state, one_lower, reference):
                for low in boundary_indices(bases[q - 1][mid], two_lower, reference):
                    if low in accumulator: accumulator.remove(low)
                    else: accumulator.add(low)
            assert not accumulator, (q, state, accumulator)


def run(reference_last):
    bases, reference = basis(reference_last)
    dims = [len(level) for level in bases]
    expected_dims = [comb(10, q) * 4 ** q * comb(25+4-q-1, 4-q) for q in range(5)]
    assert dims == expected_dims
    test_boundary_squared(bases, reference)
    ranks = [0] + [rank_from_columns(bases[q], bases[q-1], reference)
                    for q in range(1, 5)]
    betti = [dims[q] - ranks[q] - (ranks[q+1] if q < 4 else 0)
             for q in range(5)]
    assert dims == [20475, 117000, 234000, 192000, 53760]
    assert ranks == [0, 20474, 96509, 136963, 53759]
    assert betti == [1, 17, 528, 1278, 1]
    # Gal's graph-braid Euler-characteristic formula:
    # [t^4](1-4t)^10/(1-t)^25.
    independent_chi = sum(comb(10, j) * (-4) ** j * comb(28-j, 4-j)
                          for j in range(5))
    assert independent_chi == -765
    assert sum((-1)**q * b for q, b in enumerate(betti)) == independent_chi
    print('reference_last', reference_last, 'chain_dims', dims, 'boundary_ranks', ranks,
          'F2_betti', betti, 'Euler', independent_chi, flush=True)


if __name__ == '__main__':
    run(False)
    run(True)
    print('VERIFY_OK')
