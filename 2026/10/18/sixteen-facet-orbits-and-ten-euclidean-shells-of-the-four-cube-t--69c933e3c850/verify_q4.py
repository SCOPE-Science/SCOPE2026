#!/usr/bin/env python3
"""Exact finite verification of the Q4 Lipschitz-free facet-orbit theorem.

Standard-library-only integer arithmetic. Vertex v is the 4-bit integer v.
The first method enumerates all 2^15 signed spanning-tree assignments.
The second independently extends integer heights in Hamming-weight order.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product

D = 4
V = tuple(range(1 << D))
EDGES = tuple((v, v ^ (1 << i)) for v in V for i in range(D) if not (v & (1 << i)))
assert len(EDGES) == 32


def candidate_heights_from_tree():
    """Complete by the 15-tree-edge sign parametrization."""
    children = tuple(range(1, 16))
    parent = {v: v ^ (v & (-v)) for v in children}
    assert all(parent[v] < v for v in children)
    result = set()
    for signs in product((-1, 1), repeat=15):
        f = [0] * 16
        for v, eps in zip(children, signs):
            f[v] = f[parent[v]] + eps
        if all(abs(f[u] - f[v]) == 1 for u, v in EDGES):
            result.add(tuple(f))
    return result


def candidate_heights_by_layers():
    """Independent backtracking: extend the intersection of parent-height sets."""
    order = sorted(V, key=lambda v: (v.bit_count(), v))
    assert order[0] == 0
    f = [0] * 16
    found = set()

    def visit(k):
        if k == len(order):
            found.add(tuple(f))
            return
        v = order[k]
        parents = [v ^ (1 << j) for j in range(D) if v & (1 << j)]
        allowed = set((f[parents[0]] - 1, f[parents[0]] + 1))
        for u in parents[1:]:
            allowed.intersection_update((f[u] - 1, f[u] + 1))
        for t in sorted(allowed):
            f[v] = t
            visit(k + 1)

    visit(1)
    return found


def cube_automorphisms():
    result = []
    for pi in permutations(range(D)):
        for shift in V:
            image = []
            for v in V:
                w = shift
                for i in range(D):
                    if v & (1 << i):
                        w ^= 1 << pi[i]
                image.append(w)
            result.append(tuple(image))
    assert len(set(result)) == 384
    assert all({tuple(sorted((m[u], m[v]))) for u, v in EDGES} ==
               {tuple(sorted(e)) for e in EDGES} for m in result)
    return result


def transform(f, sigma, sign):
    """Precompose by a graph automorphism, then sign, then root normalize."""
    t0 = f[sigma[0]]
    return tuple(sign * (f[sigma[v]] - t0) for v in V)


def norm_sq(f):
    """Exact squared Euclidean norm of the centered normal."""
    return Fraction(16 * sum(t * t for t in f) - sum(f)**2, 16)


EXPECTED_SHELLS = {
    Fraction(4): 2, Fraction(23, 4): 32, Fraction(7): 112,
    Fraction(31, 4): 224, Fraction(8): 204, Fraction(39, 4): 192,
    Fraction(11): 128, Fraction(47, 4): 32, Fraction(12): 48,
    Fraction(16): 16,
}
# (orbit size, squared centered-normal norm, height range, translated 16-digit code)
EXPECTED_ORBITS = (
    (192, Fraction(39, 4), 3, '3221211021101221'),
    (128, Fraction(31, 4), 2, '2110100110212110'),
    (128, Fraction(11), 3, '3221211021101021'),
    (96, Fraction(7), 2, '2110100110012110'),
    (96, Fraction(31, 4), 2, '2110100110012112'),
    (96, Fraction(8), 2, '2110100110212112'),
    (64, Fraction(8), 3, '3221211021121221'),
    (48, Fraction(12), 3, '3221211021103221'),
    (32, Fraction(23, 4), 2, '2110100110010110'),
    (32, Fraction(47, 4), 3, '3221211021101001'),
    (16, Fraction(7), 2, '2110100110010112'),
    (16, Fraction(8), 2, '2110100112212110'),
    (16, Fraction(8), 2, '2110102110212110'),
    (16, Fraction(16), 4, '4332322132212110'),
    (12, Fraction(8), 2, '2110102112010112'),
    (2, Fraction(4), 1, '1001011001101001'),
)


def main():
    a = candidate_heights_from_tree()
    b = candidate_heights_by_layers()
    assert a == b, 'independent exhaustive enumerations differ'
    assert len(a) == 990
    assert all(f[0] == 0 and all(abs(f[u] - f[v]) == 1 for u, v in EDGES)
               for f in a)
    shells = Counter(norm_sq(f) for f in a)
    assert shells == EXPECTED_SHELLS
    maps = cube_automorphisms()
    unclassified = set(a)
    orbits = []
    while unclassified:
        representative = min(unclassified)
        orbit = {transform(representative, m, s) for m in maps for s in (-1, 1)}
        assert orbit <= a
        assert orbit <= unclassified, 'overlapping orbits'
        assert all(norm_sq(z) == norm_sq(representative) for z in orbit)
        unclassified -= orbit
        code = ''.join(str(t - min(representative)) for t in representative)
        orbits.append((len(orbit), norm_sq(representative),
                       max(representative) - min(representative), code))
    orbits.sort(key=lambda t: (-t[0], t[1], t[3]))
    assert tuple(orbits) == EXPECTED_ORBITS
    assert len(orbits) == 16 and sum(row[0] for row in orbits) == 990
    # An independent orbit-count check by fixed-point double counting (Burnside).
    fixed_sum = 0
    for m in maps:
        for sign in (-1, 1):
            fixed_sum += sum(transform(f, m, sign) == f for f in a)
    assert fixed_sum == 16 * (384 * 2) == 12288
    assert sum(n for q, n in shells.items() if q == max(shells)) == 16
    print('32 graph edges, 32768 spanning-tree signs, 990 compatible facets')
    print('Independent layer enumeration equals spanning-tree enumeration')
    print('384 cube automorphisms, 768 signed actions, 16 orbits')
    print('Burnside fixed-point sum =', fixed_sum)
    print('Ten exact squared-normal shells:')
    for v, n in sorted(shells.items()):
        print('  ', str(v), n)
    print('ALL EXACT CHECKS PASSED')

if __name__ == '__main__':
    main()
