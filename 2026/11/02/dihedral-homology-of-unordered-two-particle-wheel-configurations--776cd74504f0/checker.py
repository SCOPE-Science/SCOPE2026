"""Finite exact checks of the two-particle wheel configuration chain complex.

Run with Python >=3.9. All arithmetic is integral or finite-field exact.
For arbitrary rim length the published proof, not these samples, establishes
injectivity of the two-dimensional boundary and its dihedral characters.
"""
from itertools import combinations


def model(k):
    assert k >= 5
    vertices = list(combinations(range(k + 1), 2))
    edges = [(i, (i + 1) % k) for i in range(k)] + [(i, k) for i in range(k)]
    ones = [(i, v) for i, e in enumerate(edges) for v in range(k + 1) if v not in e]
    twos = [(a, b) for a, b in combinations(range(len(edges)), 2)
            if not (set(edges[a]) & set(edges[b]))]
    vertex_index = {v: i for i, v in enumerate(vertices)}
    one_index = {e: i for i, e in enumerate(ones)}
    d1 = []
    for edge_index, v in ones:
        u, w = edges[edge_index]
        d1.append({vertex_index[tuple(sorted((w, v)))]: 1,
                   vertex_index[tuple(sorted((u, v)))]: -1})
    d2 = []
    for a, b in twos:
        u, v = edges[a]
        w, x = edges[b]
        d2.append({one_index[(b, v)]: 1, one_index[(b, u)]: -1,
                   one_index[(a, x)]: -1, one_index[(a, w)]: 1})
    return edges, vertices, ones, twos, d1, d2


def rank_mod_prime(columns, modulus):
    pivots = {}
    for source in columns:
        col = {i: x % modulus for i, x in source.items() if x % modulus}
        while col:
            pivot = min(col)
            if pivot not in pivots:
                inverse = pow(col[pivot], -1, modulus)
                pivots[pivot] = {i: (v * inverse) % modulus for i, v in col.items()}
                break
            mult = col[pivot]
            for i, val in pivots[pivot].items():
                new = (col.get(i, 0) - mult * val) % modulus
                if new:
                    col[i] = new
                else:
                    col.pop(i, None)
    return len(pivots)


def cellular_trace(edges, vertices, ones, twos, permutation):
    inverted_edges = {frozenset(e): i for i, e in enumerate(edges)}
    images = []
    signs = []
    for u, v in edges:
        j = inverted_edges[frozenset((permutation[u], permutation[v]))]
        images.append(j)
        signs.append(1 if (permutation[u], permutation[v]) == edges[j] else -1)
    t0 = sum(tuple(sorted((permutation[u], permutation[v]))) == (u, v)
             for u, v in vertices)
    t1 = sum(signs[a] for a, v in ones if images[a] == a and permutation[v] == v)
    t2 = 0
    for a, b in twos:
        x, y = images[a], images[b]
        if (min(x, y), max(x, y)) == (a, b):
            t2 += signs[a] * signs[b] * (1 if x < y else -1)
    return (t0, t1, t2)


def check(k):
    edges, vertices, ones, twos, d1, d2 = model(k)
    assert len(vertices) == k * (k + 1) // 2
    assert len(ones) == 2 * k * (k - 1)
    assert len(twos) == k * (3 * k - 7) // 2
    for square_column in d2:
        net = {}
        for one_index, square_sign in square_column.items():
            for zero_index, boundary_sign in d1[one_index].items():
                net[zero_index] = net.get(zero_index, 0) + square_sign * boundary_sign
        assert all(value == 0 for value in net.values())
    for modulus in (2, 3, 1000003):
        assert rank_mod_prime(d1, modulus) == len(vertices) - 1
        assert rank_mod_prime(d2, modulus) == len(twos)
    for shift in range(k):
        for reversed_orientation in (False, True):
            if reversed_orientation:
                p = [(shift - i) % k for i in range(k)] + [k]
            else:
                p = [(shift + i) % k for i in range(k)] + [k]
            traces = cellular_trace(edges, vertices, ones, twos, p)
            character = 1 - traces[0] + traces[1] - traces[2]
            fixed_rim_edges = sum(
                frozenset((p[i], p[(i + 1) % k])) == frozenset((i, (i + 1) % k))
                for i in range(k))
            expected = (1 if not reversed_orientation else -1) * (1 + fixed_rim_edges)
            assert character == expected, (k, shift, reversed_orientation, character, expected)
    # Representation-theoretic quotient character averages, rational exact.
    rotations = [cellular_trace(edges, vertices, ones, twos,
                [(shift + i) % k for i in range(k)] + [k]) for shift in range(k)]
    rotations_sum = sum(1 - t[0] + t[1] - t[2] for t in rotations)
    reflections = [cellular_trace(edges, vertices, ones, twos,
                   [(shift - i) % k for i in range(k)] + [k]) for shift in range(k)]
    reflection_sum = sum(1 - t[0] + t[1] - t[2] for t in reflections)
    assert rotations_sum == 2 * k and reflection_sum == -2 * k
    return k, (len(vertices), len(ones), len(twos)), (len(vertices) - 1, len(twos))


if __name__ == "__main__":
    for rim_size in range(5, 13):
        print(check(rim_size))
    print("WHEEL_TWO_PARTICLE_DIHEDRAL_CHECKS_OK")
