"""Exact finite checks for the first two EO supersingular-contact layers.

This is a cross-check of the symbolic all-genus proof, not an infinite certificate.
The cycle criterion used is Muller, arXiv:2609.15024, Definition 1.3--1.5
and Theorem 1.7. Standard-library Python 3.10+ only.
"""
from itertools import product


def cycle_reachability(bits):
    """Return whether every bad cycle is reachable from a good cycle."""
    g = len(bits)
    phi = 0
    permutation = []
    for i, bit in enumerate(bits, 1):
        phi += bit
        permutation.append((phi if bit else g + 1 - i + phi) - 1)
    assert sorted(permutation) == list(range(g))

    cycles = []
    member = {}
    visited = set()
    for start in range(g):
        if start in visited:
            continue
        cyc = []
        j = start
        while j not in visited:
            visited.add(j)
            cyc.append(j)
            j = permutation[j]
        assert j == start
        member.update({i: len(cycles) for i in cyc})
        cycles.append(cyc)

    bad = []
    orientations = []
    for cyc in cycles:
        positive = [i for i in cyc if bits[i]]
        if not positive:
            bad.append(False)
            orientations.append({})
            continue
        shift = cyc.index(positive[0])
        rotated = cyc[shift:] + cyc[:shift]
        sign = 1
        orientation = {}
        for i in rotated:
            orientation[i] = sign
            if not bits[i]:
                sign *= -1
        is_bad = sign == 1 and all(orientation[i] == 1 for i in positive)
        bad.append(is_bad)
        orientations.append(orientation)

    graph = [set() for _ in cycles]
    for target, cyc in enumerate(cycles):
        if not bad[target]:
            continue
        for j in cyc:
            if bits[j] or orientations[target][j] != 1:
                continue
            for i in range(j):
                source = member[i]
                if bits[i] and source != target:
                    graph[source].add(target)
    reached = set(i for i, b in enumerate(bad) if not b)
    queue = list(reached)
    for i in queue:
        for j in graph[i]:
            if j not in reached:
                reached.add(j)
                queue.append(j)
    return all(not b or i in reached for i, b in enumerate(bad))


def verify(max_genus=14):
    source_counts = {3: 3, 4: 6, 5: 11, 6: 22, 7: 44, 8: 89,
                     9: 181, 10: 370, 11: 753, 12: 1538,
                     13: 3137, 14: 6381}
    for g in range(3, max_genus + 1):
        k = g // 2
        h = (g + 1) // 2
        empty_at_first = set()
        empty_at_second = set()
        mixed_at_second = set()
        meets = 0
        for bits in product((0, 1), repeat=g):
            d = sum((g + 1 - i) * bit for i, bit in enumerate(bits, 1))
            contained = all(bit == 0 for bit in bits[:h])
            contact = cycle_reachability(bits)
            if bits[0] == 0:
                meets += contact
            if contained:
                assert contact, (g, bits)
            if d <= k:
                assert contained, (g, bits)
            if d == k + 1 and not contact:
                empty_at_first.add(tuple(i for i, b in enumerate(bits, 1) if b))
            if d == k + 2:
                if not contact:
                    empty_at_second.add(tuple(i for i, b in enumerate(bits, 1) if b))
                elif not contained:
                    mixed_at_second.add(tuple(i for i, b in enumerate(bits, 1) if b))
        assert empty_at_first == {(h,)}, (g, empty_at_first)
        assert empty_at_second == {(h - 1,)}, (g, empty_at_second)
        assert mixed_at_second == {(h, g)}, (g, mixed_at_second)
        assert meets == source_counts[g], (g, meets)
    print('EO_FIRST_TWO_CONTACT_LAYERS_EXACT_OK')


if __name__ == '__main__':
    verify()
