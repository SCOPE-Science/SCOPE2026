#!/usr/bin/env python3
"""Finite independent checks of the run-allocation/linear-equality reduction.
Only the finite tests use brute force. They are not the fixed-dimensional ILP solver.
"""
from itertools import combinations, product


def compress(word):
    out = []
    for symbol in word:
        if out and out[-1][0] == symbol:
            out[-1] = (symbol, out[-1][1] + 1)
        else:
            out.append((symbol, 1))
    return out


def profile(runs, allocations, first):
    out = []
    for (symbol, total), left in zip(runs, allocations):
        amount = left if first else total - left
        if amount:
            if out and out[-1][0] == symbol:
                out[-1] = (symbol, out[-1][1] + amount)
            else:
                out.append((symbol, amount))
    return out


def symbolic(runs, mask, first):
    # Terms are (constant, tuple of coefficients of x_0,...,x_{r-1}).
    k = len(runs)
    out = []
    for i, (letter, total) in enumerate(runs):
        if (first and mask[i] == 0) or ((not first) and mask[i] == 1):
            continue
        coeff = [0] * k
        coeff[i] = 1 if first else -1
        const = 0 if first else total
        if out and out[-1][0] == letter:
            prev_letter, prev_const, prev_coeff = out[-1]
            out[-1] = (prev_letter, prev_const + const,
                       tuple(a + b for a, b in zip(prev_coeff, coeff)))
        else:
            out.append((letter, const, tuple(coeff)))
    return out


def mask_of(runs, alloc):
    return tuple(0 if v == 0 else 1 if v == runs[i][1] else 2
                 for i, v in enumerate(alloc))




def degree_system(runs, mask):
    """Return exact-degree graph and edge bounds for a fixed three-way mask.
    Each variable interior to a run is one graph edge, possibly a loop.
    """
    left = symbolic(runs, mask, True)
    right = symbolic(runs, mask, False)
    if [v[0] for v in left] != [v[0] for v in right]:
        return None
    r = len(runs)
    demand = []
    columns = [[] for _ in range(r)]
    for row, ((_, ac, av), (_, bc, bv)) in enumerate(zip(left, right)):
        coeff = [u - v for u, v in zip(av, bv)]
        rhs = bc - ac
        for i, mode in enumerate(mask):
            if mode != 2:
                rhs -= coeff[i] * (runs[i][1] if mode == 1 else 0)
            else:
                assert coeff[i] in (0, 1, 2)
                columns[i].extend([row] * coeff[i])
        demand.append(rhs)
    edges = {}
    for i, mode in enumerate(mask):
        if mode == 2:
            assert len(columns[i]) == 2
            edges[i] = (tuple(columns[i]), 1, runs[i][1] - 1)
    return demand, edges


def check_degrees(runs, alloc):
    graph = degree_system(runs, mask_of(runs, alloc))
    if graph is None:
        return False
    demand, edges = graph
    actual = [0] * len(demand)
    for i, (ends, lower, upper) in edges.items():
        assert lower <= alloc[i] <= upper
        for vertex in ends:
            actual[vertex] += alloc[i]
    return actual == demand

def check_constraint(runs, alloc):
    mask = mask_of(runs, alloc)
    a = symbolic(runs, mask, True)
    b = symbolic(runs, mask, False)
    if [x[0] for x in a] != [x[0] for x in b]:
        return False
    for (_, ac, av), (_, bc, bv) in zip(a, b):
        if ac - bc + sum((u - v) * x for u, v, x in zip(av, bv, alloc)):
            return False
    return True


def brute_subset(word):
    n = len(word)
    if n % 2:
        return False
    for chosen in combinations(range(n), n // 2):
        marked = set(chosen)
        a = ''.join(word[i] for i in chosen)
        b = ''.join(word[i] for i in range(n) if i not in marked)
        if a == b:
            return True
    return False


def compressed_search(word):
    runs = compress(word)
    for alloc in product(*(range(length + 1) for _, length in runs)):
        equal = profile(runs, alloc, True) == profile(runs, alloc, False)
        matrix_equal = check_constraint(runs, alloc)
        assert equal == matrix_equal, (word, alloc, equal, matrix_equal)
        graph_equal = check_degrees(runs, alloc)
        assert graph_equal == equal, (word, alloc, graph_equal, equal)
        if equal:
            return True
    return False


def run():
    total = 0
    for alphabet, maximum in [('01', 10), ('012', 7)]:
        for length in range(maximum + 1):
            for chars in product(alphabet, repeat=length):
                word = ''.join(chars)
                expect = brute_subset(word)
                got = compressed_search(word)
                assert expect == got, (word, expect, got)
                total += 1
    # Huge input: compressed allocation and roots, without expansion.
    big = 10**35 + 1
    runs = [('A', big + 1), ('B', big + 1), ('A', big + 1), ('B', big + 1)]
    split = [(big + 1)//2] * 4
    assert profile(runs, split, True) == profile(runs, split, False)
    assert check_constraint(runs, split)
    assert check_degrees(runs, split)
    print('RLE_SHUFFLE_REDUCTION_PASS', 'words=', total,
          'max_binary_length=10', 'max_ternary_length=7',
          'huge_run_bits=', big.bit_length())

if __name__ == '__main__':
    run()
