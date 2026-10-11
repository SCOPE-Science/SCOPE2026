"""Exact finite checks for cactus directed-root-polytope asymmetry identities.

Runs with Python 3 standard library only. The theorem for all graphs rests on
its analytic affine-dependence and join arguments, not finite enumeration.
"""
from fractions import Fraction
from random import Random


def rank(columns, rows):
    if not columns:
        return 0
    mat = [[Fraction(columns[j][i]) for j in range(len(columns))]
           for i in range(rows)]
    pivots = 0
    for col in range(len(columns)):
        place = next((i for i in range(pivots, rows)
                      if mat[i][col] != 0), None)
        if place is None:
            continue
        mat[pivots], mat[place] = mat[place], mat[pivots]
        d = mat[pivots][col]
        mat[pivots] = [z / d for z in mat[pivots]]
        for i in range(rows):
            if i != pivots and mat[i][col]:
                x = mat[i][col]
                mat[i] = [a - x*b for a, b in zip(mat[i], mat[pivots])]
        pivots += 1
        if pivots == rows:
            break
    return pivots


def make_case(cycles, bridge_count, seed):
    r = Random(seed)
    number_vertices = 1
    edges = []
    cycle_parts = []
    bridge_ids = []
    actions = [('cycle', length) for length in cycles] + [('bridge', None)]*bridge_count
    r.shuffle(actions)
    for kind, length in actions:
        anchor = r.randrange(number_vertices)
        if kind == 'bridge':
            child = number_vertices
            number_vertices += 1
            bridge_ids.append(len(edges))
            edges.append((anchor, child) if r.randrange(2) else (child, anchor))
            continue
        assert length >= 4 and length % 2 == 0
        fresh = list(range(number_vertices, number_vertices + length - 1))
        number_vertices += length - 1
        traversal = [anchor] + fresh
        forward = set(r.sample(range(length), length // 2))
        plus, minus = [], []
        for j in range(length):
            u, v = traversal[j], traversal[(j + 1) % length]
            idx = len(edges)
            if j in forward:
                edges.append((u, v))
                plus.append(idx)
            else:
                edges.append((v, u))
                minus.append(idx)
        cycle_parts.append((plus, minus))
    return number_vertices, edges, cycle_parts, bridge_ids


def check_one(case):
    n, edges, cycles, bridges = case
    m = len(edges)
    if m < 2:
        return 0, 0
    vectors = []
    for tail, head in edges:
        a = [0]*n
        a[tail] = -1
        a[head] = 1
        vectors.append(a)
    H = len(bridges) + sum(len(x) for x, _ in cycles)
    expected_cyclomatic = len(cycles)
    assert m == n - 1 + expected_cyclomatic
    augmented = [v + [1] for v in vectors]
    assert rank(augmented, n + 1) == n-1
    for plus, minus in cycles:
        assert len(plus) == len(minus)
        assert rank([augmented[j] for j in plus], n+1) == len(plus)
        assert rank([augmented[j] for j in plus + minus], n+1) == len(plus + minus)-1
        assert [sum(vectors[j][a] for j in plus) for a in range(n)] == [
            sum(vectors[j][a] for j in minus) for a in range(n)]
    bridge_set = set(bridges)
    cyclic_set = {j for p, q in cycles for j in p + q}
    assert bridge_set.isdisjoint(cyclic_set)
    assert bridge_set | cyclic_set == set(range(m))
    weight = [Fraction(1, H) if j in bridge_set else Fraction(1, 2*H)
              for j in range(m)]
    assert sum(weight) == 1
    center = [sum(weight[j]*vectors[j][a] for j in range(m))
              for a in range(n)]
    contact_identities = 0
    for j in range(m):
        subset = [k for k in bridges if k != j]
        for plus, minus in cycles:
            chosen = minus if j in minus else plus
            subset.extend(k for k in chosen if k != j)
        assert len(subset) == H - 1
        assert len(set(subset)) == len(subset)
        assert all(H*center[a] - vectors[j][a]
                   == sum(vectors[k][a] for k in subset)
                   for a in range(n))
        contact_identities += 1
    return 1, contact_identities


def main():
    n_cases = n_reflections = 0
    lengths = [4, 6, 8, 10]
    for ncycles in range(4):
        for bridges in range(5):
            if ncycles == 0 and bridges < 2:
                continue
            for seed in range(15):
                cycles = [lengths[(seed + j*2) % len(lengths)]
                          for j in range(ncycles)]
                ok, refs = check_one(make_case(cycles, bridges, seed))
                n_cases += ok
                n_reflections += refs
    print('VERIFY_OK', 'cases=', n_cases, 'reflection_identities=', n_reflections)

if __name__ == '__main__':
    main()
