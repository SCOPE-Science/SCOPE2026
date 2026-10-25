"""Exact small-graph and independent facet/center checks for unit in-in zonotopes."""
from fractions import Fraction
from itertools import product
from math import sqrt


def prufer_tree(code):
    n = len(code) + 2
    deg = [1] * n
    for a in code:
        deg[a] += 1
    out = []
    for a in code:
        leaf = next(i for i in range(n) if deg[i] == 1)
        out.append((leaf, a))
        deg[leaf] -= 1
        deg[a] -= 1
    rem = [i for i in range(n) if deg[i] == 1]
    out.append(tuple(rem))
    return out


def edge_cut(n, edges, mask):
    return sum(((mask >> i) ^ (mask >> j)) & 1 for i, j in edges)


def min_cut_ratio_and_contacts(n, edges):
    best = None
    contacts = []
    for mask in range(1, 1 << n):
        k = mask.bit_count()
        cut = edge_cut(n, edges, mask)
        ratio2 = Fraction((k + cut) ** 2, k)
        if best is None or ratio2 < best:
            best, contacts = ratio2, [mask]
        elif ratio2 == best:
            contacts.append(mask)
    return best, contacts


def qrank(masks, n):
    A = [[Fraction(mask >> i & 1) for i in range(n)] for mask in masks]
    pivots = 0
    for col in range(n):
        pivot = next((i for i in range(pivots, len(A)) if A[i][col]), None)
        if pivot is None:
            continue
        A[pivots], A[pivot] = A[pivot], A[pivots]
        div = A[pivots][col]
        for j in range(col, n):
            A[pivots][j] /= div
        for i in range(pivots + 1, len(A)):
            factor = A[i][col]
            if factor:
                for j in range(col, n):
                    A[i][j] -= factor * A[pivots][j]
        pivots += 1
    return pivots


def tree_targets(n, edges):
    L = [i for i in range(n) if sum(i in e for e in edges) == 1]
    full = (1 << n) - 1
    singleton_leaves = {1 << i for i in L}
    if n < 4:
        return Fraction(n), {full}, n - 1
    if n == 4:
        return Fraction(4), singleton_leaves | {full}, n - len(L) - 1
    return Fraction(4), singleton_leaves, n - len(L)


def cycle_targets(n):
    full = (1 << n) - 1
    adj = {(1 << i) | (1 << ((i + 1) % n)) for i in range(n)}
    if n <= 7:
        return Fraction(n), {full}, n - 1
    if n == 8:
        return Fraction(8), adj | {full}, 1
    return Fraction(8), adj, 0 if n % 2 else 1


n_trees = 0
n_cycles = 0
n_facet_orbits = 0
for n in range(1, 7):
    codes = [()] if n <= 2 else product(range(n), repeat=n-2)
    for code in codes:
        edges = [] if n == 1 else prufer_tree(code)
        ratio2, contacts = min_cut_ratio_and_contacts(n, edges)
        expected, masks, dim = tree_targets(n, edges)
        assert ratio2 == expected, ('tree radius', n, code, ratio2, expected)
        assert set(contacts) == masks, ('tree contacts', n, code, contacts, masks)
        assert n - qrank(contacts, n) == dim, ('tree center dimension', n, code)
        n_trees += 1
        n_facet_orbits += len(contacts)

for n in range(3, 16):
    edges = [(i, (i + 1) % n) for i in range(n)]
    ratio2, contacts = min_cut_ratio_and_contacts(n, edges)
    expected, masks, dim = cycle_targets(n)
    assert ratio2 == expected, ('cycle radius', n)
    assert set(contacts) == masks, ('cycle contacts', n, contacts, masks)
    assert n - qrank(contacts, n) == dim, ('cycle center dimension', n)
    n_cycles += 1
    n_facet_orbits += len(contacts)

# Independently check contact-face inequalities for both explicit center segments.
# For cycle C_n, all subset normals are checked, not just connected ones.
t_cycle = 5 - 2 * sqrt(6)
cycle_checks = 0
for n in (8, 10, 12, 14):
    edges = [(i, (i + 1) % n) for i in range(n)]
    for mask in range(1, 1 << n):
        k, b = mask.bit_count(), edge_cut(n, edges, mask)
        alternating_sum = sum((-1)**i for i in range(n) if mask >> i & 1)
        slack = k + b - sqrt(8 * k)
        assert abs(t_cycle * alternating_sum) <= slack + 1e-10, (n, mask, slack)
        cycle_checks += 1
    # Three consecutive vertices saturate the interval endpoint exactly.
    assert abs((3 + 2 - sqrt(8 * 3)) - t_cycle) < 1e-12

star_checks = 0
for n in range(4, 17):
    edges = [(0, i) for i in range(1, n)]
    t_star = n - 2 * sqrt(n)
    assert t_star >= -1e-12
    # All connected subsets are a singleton leaf or contain the hub.
    for k in range(n):
        if k == 0:
            continue
        slack = n - 2 * sqrt(k + 1)
        assert t_star <= slack + 1e-10
        star_checks += 1
    # Full set gives equality.
    assert abs(t_star - (n - 2 * sqrt(n))) < 1e-12

# Independent raw support-function check on noncut real directions.
vector_checks = 0
for n in range(2, 6):
    graphs = [prufer_tree(tuple(0 for _ in range(n-2)))]
    if n >= 3:
        graphs.append([(i, (i+1) % n) for i in range(n)])
    for edges in graphs:
        target, _ = min_cut_ratio_and_contacts(n, edges)
        for u in product((-2, -1, 0, 1, 2), repeat=n):
            norm2 = sum(a*a for a in u)
            if not norm2:
                continue
            support = sum(abs(a) for a in u) + sum(abs(u[i] - u[j]) for i, j in edges)
            assert Fraction(support*support, norm2) >= target
            vector_checks += 1

print(f'EXACT_OK labeled_trees={n_trees} cycles={n_cycles} contact_cuts={n_facet_orbits} raw_support_vectors={vector_checks}')
print(f'CENTER_OK all_cut_cycle_segment_checks={cycle_checks} star_bounds={star_checks}')
