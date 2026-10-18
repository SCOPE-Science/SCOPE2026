"""Reproduce finite checks for out-neighborhood complexes of cyclic tournament blow-ups.

Only standard Python is required. This code constructs faces directly from digraph arcs,
not from a specified target homotopy decomposition.
"""
from collections import defaultdict
from itertools import combinations


def c3():
    return [{1}, {2}, {0}]


def cyclic_5():
    return [{(i + j) % 5 for j in (1, 2)} for i in range(5)]


def transitive_3():
    return [set(range(i + 1, 3)) for i in range(3)]


def blowup(base):
    m = len(base)
    result = []
    for b in range(3):
        for u in range(m):
            result.append({b * m + v for v in base[u]} |
                          {((b + 1) % 3) * m + v for v in range(m)})
    return result


def faces(arcs):
    all_faces = {0}
    for neighbors in arcs:
        elems = list(neighbors)
        for k in range(len(elems) + 1):
            for subset in combinations(elems, k):
                bitmask = 0
                for i in subset:
                    bitmask |= 1 << i
                all_faces.add(bitmask)
    out = defaultdict(list)
    for mask in all_faces:
        out[mask.bit_count() - 1].append(mask)
    return out


def boundary_rank(source, targets):
    indexes = {f: i for i, f in enumerate(targets)}
    pivots = {}
    for sigma in source:
        col = 0
        z = sigma
        while z:
            bit = z & -z
            z ^= bit
            col ^= 1 << indexes[sigma ^ bit]
        while col:
            p = col.bit_length() - 1
            if p in pivots:
                col ^= pivots[p]
            else:
                pivots[p] = col
                break
    return len(pivots)


def betti_mod2(out):
    # reduced complex, including empty face in degree -1
    grades = range(-1, max(out) + 1)
    ranks = {}
    for i in grades:
        if i >= 0:
            ranks[i] = boundary_rank(out[i], out[i - 1])
    return {i: len(out[i]) - ranks.get(i, 0) - ranks.get(i + 1, 0)
            for i in range(0, max(out) + 1)
            if len(out[i]) - ranks.get(i, 0) - ranks.get(i + 1, 0)}


def run(name, arcs, expected, check_ranks=True):
    n = len(arcs)
    for u in range(n):
        assert u not in arcs[u]
        for v in range(u + 1, n):
            assert (v in arcs[u]) != (u in arcs[v]), (name, u, v)
    ff = faces(arcs)
    fvector = [len(ff[i]) for i in range(max(ff) + 1)]
    euler_reduced = -1 + sum((-1) ** i * len(ff[i]) for i in range(max(ff) + 1))
    predicted_euler = sum((-1) ** i * b for i, b in expected.items())
    assert euler_reduced == predicted_euler, (name, euler_reduced, predicted_euler)
    if check_ranks:
        got = betti_mod2(ff)
        assert got == expected, (name, got, expected)
    else:
        got = 'skipped; exact Euler test only'
    print(name, 'n=', n, 'faces=', sum(fvector) + 1,
          'f_vector=', fvector, 'Euler_reduced=', euler_reduced,
          'mod2_reduced_betti=', got)


if __name__ == '__main__':
    run('C3', c3(), {0: 2})
    run('C3[transitive3]', blowup(transitive_3()), {1: 1})
    run('C3[C3]', blowup(c3()), {1: 7})
    run('C3[regular5]', blowup(cyclic_5()), {1: 1, 2: 3})
    run('C3[C3[C3]]', blowup(blowup(c3())), {1: 1, 2: 21}, check_ranks=False)
    print('ALL_CHECKS_PASS')
