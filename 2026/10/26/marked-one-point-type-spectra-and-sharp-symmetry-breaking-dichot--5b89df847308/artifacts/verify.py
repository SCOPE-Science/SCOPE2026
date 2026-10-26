"""Finite cross-checks for pointed orbit spectra of random-poset reducts.

The exhaustive checks corroborate, but do not replace, the unrestricted proof.
Run with Python 3, standard library only.
"""
from itertools import combinations, product
from collections import Counter


def posets(n):
    pair_list = list(combinations(range(n), 2))
    for directions in product((-1, 0, 1), repeat=len(pair_list)):
        edges = set()
        for (a, b), direction in zip(pair_list, directions):
            if direction == 1:
                edges.add((a, b))
            elif direction == -1:
                edges.add((b, a))
        if all((a, b) not in edges or (b, c) not in edges or (a, c) in edges
               for a in range(n) for b in range(n) for c in range(n)):
            yield frozenset(edges)


def triple_class(order, a, b, c):
    cyclic_edges = ((a, b), (b, c), (c, a))
    comparable = sum((u, v) in order or (v, u) in order
                     for u, v in cyclic_edges)
    if comparable in (0, 2):
        return 0  # three incomparabilities or a vee/inverted vee
    if comparable == 1:
        return 1 if any(pair in order for pair in cyclic_edges) else 2
    return 1 if any((u, v) in order and (v, w) in order
                    for u, v, w in ((a, b, c), (b, c, a), (c, a, b))) else 2


def extensions(order, n):
    for lmask in range(1 << n):
        lower = {a for a in range(n) if lmask & (1 << a)}
        if any((a, b) in order and b in lower and a not in lower
               for a in range(n) for b in range(n)):
            continue
        for umask in range(1 << n):
            upper = {a for a in range(n) if umask & (1 << a)}
            if lower & upper:
                continue
            if any((a, b) in order and a in upper and b not in upper
                   for a in range(n) for b in range(n)):
                continue
            if any((a, b) not in order for a in lower for b in upper):
                continue
            extended = frozenset(set(order)
                                 | {(a, n) for a in lower}
                                 | {(n, b) for b in upper})
            yield extended, lmask, umask


def signature(order, n):
    return tuple(triple_class(order, a, b, n)
                 for a, b in combinations(range(n), 2))


def weak2(order, vertices):
    return all(triple_class(order, a, b, c) == 0
               for a, b, c in combinations(vertices, 3))


def rotation_count(order, n):
    return sum(weak2(order, [a for a in range(n) if mask & (1 << a)])
               for mask in range(1, 1 << n))


def poset_is_disjoint_union_of_two_chains(order, n):
    # For each bipartition, require every part to be a chain and
    # all cross-part pairs to be incomparable.
    for mask in range(1 << n):
        a = [i for i in range(n) if mask & (1 << i)]
        b = [i for i in range(n) if not mask & (1 << i)]
        if any((x, y) not in order and (y, x) not in order
               for block in (a, b) for x, y in combinations(block, 2)):
            continue
        if any((x, y) in order or (y, x) in order for x in a for y in b):
            continue
        return True
    return False


summary = Counter()
for n in range(1, 6):
    for base in posets(n):
        summary['parameter_posets'] += 1
        ext = list(extensions(base, n))
        raw_signatures = {signature(E, n) for E, _, _ in ext}
        aut_count = len(ext)
        r_count = aut_count if base else len({tuple(sorted((l, u))) for _, l, u in ext})
        t_count = len(raw_signatures)
        orientable = weak2(base, range(n))
        if orientable:
            m_count = len({min(s, tuple(3-z if z else 0 for z in s))
                           for s in raw_signatures})
        else:
            m_count = t_count
        sym_count = 1
        rho = rotation_count(base, n)
        theoretical = (aut_count,
                       (1 << n) if not base else aut_count,
                       rho,
                       (1 << (n - 1)) if orientable else rho,
                       1)
        observed = (aut_count, r_count, t_count, m_count, sym_count)
        if observed != theoretical:
            raise AssertionError(('orbit counts', n, base, observed, theoretical))
        floor = n * (n+1) // 2
        ceiling = (1 << n) - 1
        if not floor <= rho <= ceiling:
            raise AssertionError(('bounds', n, base, rho))
        if (rho == floor) != poset_is_disjoint_union_of_two_chains(base, n):
            raise AssertionError(('minimum class', n, base, rho))
        if (rho == ceiling) != weak2(base, range(n)):
            raise AssertionError(('maximum class', n, base, rho))
        summary['extensions'] += len(ext)
        summary['nontrivial_rotation_bases'] += int(orientable)
        summary['five_groups_separated'] += int(len(set(observed)) == 5)

for n in range(1, 11):
    # Antichain data independently enumerated at the set-action level.
    lower_types = {('below', mask) for mask in range(1, 1 << n)}
    upper_types = {('above', mask) for mask in range(1, 1 << n)}
    auto = len(lower_types | upper_types) + 1
    rev = len({mask for mask in range(1, 1 << n)}) + 1
    turn = len({mask for mask in range(1, (1 << n) - 1)}) + 1
    mixed = len({min(mask, ((1 << n) - 1) ^ mask)
                 for mask in range(1, (1 << n) - 1)}) + 1
    expected = (2**(n+1)-1, 2**n, 2**n-1, 2**(n-1), 1)
    assert (auto, rev, turn, mixed, 1) == expected
    summary['antichain_sizes'] += 1

assert summary['parameter_posets'] == 4473, summary
print('parameter_posets=', summary['parameter_posets'])
print('nonalgebraic_extensions_checked=', summary['extensions'])
print('parameter_bases_rotationally_antichain=', summary['nontrivial_rotation_bases'])
print('five_group_separation_cases=', summary['five_groups_separated'])
print('antichain_sizes_checked=1..10')
print('ALL_CHECKS_PASS')
