#!/usr/bin/env python3
"""Finite regression checks for the bipartite block-ordering theorem."""
from itertools import combinations, product, permutations


def regular_bipartite_graphs(m, d):
    masks = []
    for comb in combinations(range(m), d):
        masks.append(sum(1 << j for j in comb))
    for rows in product(masks, repeat=m):
        col_sums = [0] * m
        for r in rows:
            for j in range(m):
                col_sums[j] += (r >> j) & 1
        if all(x == d for x in col_sums):
            yield tuple(rows)


def perfect_matchings(rows):
    m = len(rows)
    for p in permutations(range(m)):
        if all((rows[i] >> p[i]) & 1 for i in range(m)):
            yield p


def proper_d_edge_colourings(rows, d):
    """All proper d-edge-colourings with colours 0,...,d-1."""
    def rec(state, colour, acc):
        if colour == d:
            yield dict(acc)
            return
        for p in perfect_matchings(state):
            nxt = list(state)
            acc2 = list(acc)
            for i, j in enumerate(p):
                nxt[i] &= ~(1 << j)
                acc2.append(((i, j), colour))
            yield from rec(tuple(nxt), colour + 1, acc2)
    yield from rec(tuple(rows), 0, [])


def construct_order(rows, colouring):
    """Apply the theorem's one-sided block construction."""
    m = len(rows)
    left = list(range(m))
    right = list(range(m))

    right_sequence = {
        j: tuple(colouring[(i, j)] for i in left if (rows[i] >> j) & 1)
        for j in right
    }

    block_orders = {}
    for i in left:
        incident = [(i, j) for j in right if (rows[i] >> j) & 1]
        forbidden = {right_sequence[j] for _, j in incident}
        chosen = None
        for p in permutations(incident):
            seq = tuple(colouring[e] for e in p)
            if seq not in forbidden:
                chosen = p
                break
        if chosen is None:
            raise AssertionError("no admissible block order")
        block_orders[i] = chosen

    order = [e for i in left for e in block_orders[i]]
    pos = {e: k for k, e in enumerate(order)}

    left_sequence = {}
    for i in left:
        inc = [e for e in order if e[0] == i]
        left_sequence[i] = tuple(colouring[e] for e in sorted(inc, key=pos.get))

    right_sequence_replayed = {}
    for j in right:
        inc = [e for e in order if e[1] == j]
        right_sequence_replayed[j] = tuple(colouring[e] for e in sorted(inc, key=pos.get))

    if right_sequence_replayed != right_sequence:
        raise AssertionError("right-side sequence changed under within-block ordering")

    for i, j in order:
        if left_sequence[i] == right_sequence_replayed[j]:
            raise AssertionError("adjacent endpoints received the same sequence")


def main():
    # The proof's only numerical inequality.
    fact = 1
    for d in range(1, 11):
        fact *= d
        if d >= 3 and not (fact > d):
            raise AssertionError("factorial inequality failed")

    strata = [(3, 3), (4, 3), (5, 3), (4, 4)]
    total_graphs = 0
    total_colourings = 0
    details = []
    for m, d in strata:
        graph_count = 0
        colouring_count = 0
        for rows in regular_bipartite_graphs(m, d):
            graph_count += 1
            for colouring in proper_d_edge_colourings(rows, d):
                construct_order(rows, colouring)
                colouring_count += 1
        total_graphs += graph_count
        total_colourings += colouring_count
        details.append((m, d, graph_count, colouring_count))

    expected = [
        (3, 3, 1, 12),
        (4, 3, 24, 576),
        (5, 3, 2040, 66240),
        (4, 4, 1, 576),
    ]
    if details != expected:
        raise AssertionError((details, expected))
    if total_colourings != 67404:
        raise AssertionError(total_colourings)

    for m, d, gc, cc in details:
        print(f"m={m} d={d}: graphs={gc} proper_colourings={cc} PASS")
    print(f"TOTAL proper_colourings={total_colourings}")
    print("FINITE REGRESSION CHECKS PASSED")
    print("NOTE: the universal theorem is proved deductively; these finite checks are not the proof.")


if __name__ == "__main__":
    main()
