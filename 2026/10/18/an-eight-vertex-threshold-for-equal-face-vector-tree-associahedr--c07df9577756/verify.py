"""Exact enumeration of graph-associahedron face vectors and Gaussian angular collisions.

Uses only Python's standard library. Labels of each graph are 0,...,n-1.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product

A = ((0, 1), (0, 2), (1, 4), (2, 3), (4, 5), (4, 6), (4, 7))
B = ((0, 1), (0, 2), (1, 4), (1, 7), (2, 3), (4, 5), (4, 6))
EXPECTED_F = (2952, 10332, 14336, 10010, 3680, 676, 52, 1)
EXPECTED_A = Fraction(14239, 4838400)
EXPECTED_B = Fraction(76393, 33868800)


def adjacency(n, edges):
    a = [0] * n
    for x, y in edges:
        assert 0 <= x < n and 0 <= y < n and x != y
        a[x] |= 1 << y
        a[y] |= 1 << x
    return tuple(a)


def components(a, rem):
    """Components of vertices in bitset rem; each output is a bitset."""
    out = []
    while rem:
        s = rem & -rem
        rem ^= s
        comp = s
        frontier = s
        while frontier:
            b = frontier & -frontier
            frontier -= b
            v = b.bit_length() - 1
            nbr = a[v] & rem
            frontier |= nbr
            rem -= nbr
            comp |= nbr
        out.append(comp)
    return out


def induced(a, subset):
    ids = [i for i in range(len(a)) if subset & (1 << i)]
    idx = {v: i for i, v in enumerate(ids)}
    return tuple(sum(1 << idx[v] for v in ids if a[u] & (1 << v)) for u in ids)


@lru_cache(maxsize=None)
def vertex_and_collision(a):
    """Elimination-root recursion: vertex count, Gaussian collision (exact)."""
    n = len(a)
    if n <= 1:
        return 1, Fraction(1)
    vertices, weight = 0, Fraction(0)
    for root in range(n):
        prod_v, prod_c = 1, Fraction(1)
        for sub in components(a, ((1 << n) - 1) ^ (1 << root)):
            vc, cc = vertex_and_collision(induced(a, sub))
            prod_v *= vc
            prod_c *= cc
        vertices += prod_v
        weight += prod_c
    return vertices, weight / (n * n)


def tubes(a, proper=True):
    all_v = (1 << len(a)) - 1
    return [s for s in range(1, all_v if proper else all_v + 1)
            if len(components(a, s)) == 1]


def compatible(a, s, t):
    if (s & t) == s or (s & t) == t:
        return True
    if s & t:
        return False
    return not any((a[i] & t) for i in range(len(a)) if (s >> i) & 1)


def face_vector(a):
    ts = tubes(a)
    t = len(ts)
    links = [sum(1 << j for j in range(i + 1, t)
                 if compatible(a, ts[i], ts[j])) for i in range(t)]
    levels = [0] * len(a)
    levels[0] = 1

    def visit(possible, k):
        while possible:
            first = possible & -possible
            i = first.bit_length() - 1
            possible -= first
            levels[k + 1] += 1
            visit(possible & links[i], k + 1)

    visit((1 << t) - 1, 0)
    return tuple(reversed(levels))


def direct_vertex_angles(a):
    """Independently compute exposed coordinate-sum vertices over every ranking."""
    n = len(a)
    ts = tubes(a, proper=False)
    tally = Counter()
    for order in permutations(range(n)):
        rank = [0] * n
        for i, v in enumerate(order):
            rank[v] = i
        x = [0] * n
        for s in ts:
            best = min((v for v in range(n) if s & (1 << v)), key=rank.__getitem__)
            x[best] += 1
        tally[tuple(x)] += 1
    from math import factorial
    fact = factorial(n)
    assert sum(tally.values()) == fact
    return len(tally), Fraction(sum(q * q for q in tally.values()), fact * fact)


def prufer_edges(n, sequence):
    if n <= 1:
        return ()
    deg = [1] * n
    for x in sequence:
        deg[x] += 1
    ans = []
    for x in sequence:
        leaf = next(i for i in range(n) if deg[i] == 1)
        ans.append((leaf, x))
        deg[leaf] -= 1
        deg[x] -= 1
    last = [i for i in range(n) if deg[i] == 1]
    assert len(last) == 2
    ans.append(tuple(last))
    return tuple(ans)


def unlabelled_tree_code(a):
    """AHU center-rooted canonical isomorphism code for finite trees."""
    n = len(a)
    if n == 1:
        return '()'
    deg = [int(x).bit_count() for x in a]
    active = set(range(n))
    while len(active) > 2:
        leaves = {x for x in active if deg[x] <= 1}
        assert leaves and len(leaves) < len(active)
        active -= leaves
        for u in leaves:
            for v in range(n):
                if a[u] & (1 << v):
                    deg[v] -= 1
    centers = sorted(active)

    def rooted(u, parent):
        branches = [rooted(v, u) for v in range(n)
                    if (a[u] & (1 << v)) and v != parent]
        return '(' + ''.join(sorted(branches)) + ')'

    if len(centers) == 1:
        return rooted(centers[0], -1)
    return '<' + ''.join(sorted((rooted(centers[0], centers[1]),
                                 rooted(centers[1], centers[0])))) + '>'


def complete_unlabelled_trees(n):
    found = {}
    for seq in product(range(n), repeat=max(n - 2, 0)):
        ed = prufer_edges(n, seq)
        a = adjacency(n, ed)
        cod = unlabelled_tree_code(a)
        if cod not in found:
            found[cod] = a
    return found


def main():
    a, b = adjacency(8, A), adjacency(8, B)
    assert unlabelled_tree_code(a) != unlabelled_tree_code(b)
    for name, graph, expected in [('A', a, EXPECTED_A), ('B', b, EXPECTED_B)]:
        num, collision = vertex_and_collision(graph)
        assert num == 2952 and collision == expected
        fv = face_vector(graph)
        assert fv == EXPECTED_F
        direct_num, direct_collision = direct_vertex_angles(graph)
        assert (direct_num, direct_collision) == (num, collision)
        print(name, 'f_vector', fv, 'collision', collision,
              'direct_vertices', direct_num)
    assert EXPECTED_A - EXPECTED_B == Fraction(97, 141120)
    print('exact angular gap', EXPECTED_A - EXPECTED_B)
    standard_counts = (1, 1, 1, 2, 3, 6, 11, 23)
    target_a = unlabelled_tree_code(a)
    target_b = unlabelled_tree_code(b)
    for n in range(1, 9):
        trees = complete_unlabelled_trees(n)
        assert len(trees) == standard_counts[n - 1]
        nums = Counter(vertex_and_collision(x)[0] for x in trees.values())
        if n < 8:
            assert max(nums.values()) == 1
        else:
            assert nums[2952] == 2
            assert sum(t - 1 for t in nums.values()) == 1
            assert target_a in trees and target_b in trees
        print('order', n, 'nonisomorphic', len(trees), 'vertex_count_duplicates',
              sum(t - 1 for t in nums.values()))
    print('ALL EXACT CHECKS PASSED')

if __name__ == '__main__':
    main()
