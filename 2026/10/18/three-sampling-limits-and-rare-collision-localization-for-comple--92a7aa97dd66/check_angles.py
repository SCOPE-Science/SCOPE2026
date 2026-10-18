"""Exact finite checks of complete-bipartite graph-associahedron angular spectra.

Requires Python 3 standard library only. Independent counts via simplex-sum
support vertices and graph-elimination trees, not random simulation.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def connected_tubes(p, q):
    n = p + q
    A = (1 << p) - 1
    B = ((1 << n) - 1) ^ A
    tubes = []
    for mask in range(1, 1 << n):
        if mask.bit_count() == 1 or (mask & A and mask & B):
            tubes.append(tuple(i for i in range(n) if (mask >> i) & 1))
    return tubes


def search_tree_key_and_leaf_count(order, p, q):
    remaining_a, remaining_b = p, q
    for j, i in enumerate(order):
        if i < p:
            remaining_a -= 1
        else:
            remaining_b -= 1
        if not remaining_a or not remaining_b:
            leaves = tuple(sorted(order[j + 1:]))
            assert len(leaves) >= 1
            return (tuple(order[:j + 1]), leaves), len(leaves)
    raise AssertionError("Every bipartite elimination has a first exhaustion")


def direct_support_vertex(order, tubes, n):
    pos = {i: j for j, i in enumerate(order)}
    v = [0] * n
    for tube in tubes:
        v[min(tube, key=pos.__getitem__)] += 1
    return tuple(v)


def theoretical_counts(p, q):
    n = p + q
    return {
        r: ((p * comb(q, r) if r <= q else 0)
            + (q * comb(p, r) if r <= p else 0)) * factorial(n-r-1)
        for r in range(1, max(p, q)+1)
    }


def test_one(p, q):
    n = p + q
    tubes = connected_tubes(p, q)
    tree_to_support = {}
    support_to_tree = {}
    fibers = Counter()
    leaf_counts = {}
    for order in permutations(range(n)):
        key, r = search_tree_key_and_leaf_count(order, p, q)
        vertex = direct_support_vertex(order, tubes, n)
        if key in tree_to_support:
            assert tree_to_support[key] == vertex
        else:
            assert vertex not in support_to_tree
            tree_to_support[key] = vertex
            support_to_tree[vertex] = key
            leaf_counts[key] = r
        fibers[key] += 1
    nr = Counter(leaf_counts.values())
    theory = theoretical_counts(p, q)
    assert all(nr[r] == count for r, count in theory.items()), (p,q,nr,theory)
    assert sum(nr.values()) == len(tree_to_support)
    assert all(fibers[key] == factorial(leaf_counts[key]) for key in fibers)
    assert sum(count * factorial(r) for r, count in nr.items()) == factorial(n)
    collision_direct = sum(Fraction(freq * freq, factorial(n)**2)
                           for freq in fibers.values())
    collision_formula = sum(Fraction(count * factorial(r)**2, factorial(n)**2)
                            for r, count in theory.items())
    assert collision_direct == collision_formula
    print('p,q=',p,q,'n_vertices=',len(fibers),'number_tubes=',len(tubes),
          'N_r=',dict(sorted(nr.items())), 'collision=',collision_formula)


def check_asymptotic_ratios():
    # Illustrative finite consistency only. The proof of convergence is analytic.
    for m in (5, 10, 20, 50):
        ratio = sum(Fraction(factorial(m+k-1)*factorial(m-k),
                             factorial(m-1)*factorial(m)*factorial(k))
                    for k in range(m))
        print('m=',m,'collision_to_endpoint_ratio=',float(ratio))


if __name__ == '__main__':
    for p, q in ((1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3),(3,4)):
        test_one(p,q)
    check_asymptotic_ratios()
    print('ALL EXACT CHECKS PASSED')
