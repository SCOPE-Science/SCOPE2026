"""Standalone verification of rooted-triplet query shattering on up to six leaves.

Run: python verify_rooted_triples.py depth9_certificate.json
No external packages are required.
"""
import itertools
import functools
import json
import sys
from collections import Counter


def trees_by_splitting(n):
    @functools.lru_cache(None)
    def build(leaves):
        if len(leaves) == 1:
            return (frozenset(),)
        root = leaves[0]
        out = []
        others = leaves[1:]
        for k in range(len(leaves) - 1):
            for part in itertools.combinations(others, k):
                left = (root,) + part
                right = tuple(x for x in leaves if x not in left)
                if not right:
                    continue
                for la in build(left):
                    for rb in build(right):
                        internals = set(la) | set(rb)
                        if len(left) >= 2:
                            internals.add(sum(1 << x for x in left))
                        if len(right) >= 2:
                            internals.add(sum(1 << x for x in right))
                        out.append(frozenset(internals))
        return tuple(out)
    return build(tuple(range(n)))


def trees_by_insertion(n):
    def canonical(a, b):
        return (a, b) if minimum(a) < minimum(b) else (b, a)

    def minimum(t):
        return t if isinstance(t, int) else min(minimum(t[0]), minimum(t[1]))

    def insert_everywhere(t, new_leaf):
        out = [canonical(t, new_leaf)]
        if isinstance(t, tuple):
            for a in insert_everywhere(t[0], new_leaf):
                out.append(canonical(a, t[1]))
            for b in insert_everywhere(t[1], new_leaf):
                out.append(canonical(t[0], b))
        return out

    def proper_clusters(t, n):
        clusters = []
        def recurse(node):
            if isinstance(node, int):
                return 1 << node
            bitmask = recurse(node[0]) | recurse(node[1])
            if bitmask.bit_count() >= 2 and bitmask != (1 << n) - 1:
                clusters.append(bitmask)
            return bitmask
        assert recurse(t) == (1 << n) - 1
        return frozenset(clusters)

    objects = [(0, 1)]
    if n == 1:
        return (frozenset(),)
    for new_leaf in range(2, n):
        objects = [new_t for t in objects for new_t in insert_everywhere(t, new_leaf)]
    return tuple(proper_clusters(t, n) for t in objects)


def triplets(n):
    return tuple((a, b, c) for abc in itertools.combinations(range(n), 3)
                 for c in abc for a, b in [tuple(i for i in abc if i != c)])


def responses(trees, qs):
    answer = []
    for a, b, c in qs:
        ab = (1 << a) | (1 << b)
        cbit = (1 << c)
        bits = 0
        for k, cs in enumerate(trees):
            if any((cl & ab) == ab and (cl & cbit) == 0 for cl in cs):
                bits |= 1 << k
        answer.append(bits)
    return tuple(answer)


def vc_audit(n, masks):
    full = (1 << (len(trees_by_splitting(n)))) - 1
    seen = Counter()
    witness = {}
    def extend(parts, start, chosen):
        seen[len(chosen)] += 1
        witness[len(chosen)] = chosen
        for i in range(start, len(masks)):
            one = masks[i]
            new_parts = []
            for old in parts:
                p = old & one
                if p == 0 or p == old:
                    break
                new_parts.extend((p, old ^ p))
            else:
                extend(new_parts, i + 1, chosen + (i,))
    if masks:
        extend([full ^ masks[0], masks[0]], 1, (0,))
    return seen, witness


def ldim_exact(masks, nconcept):
    if not masks:
        return 0
    full = (1 << nconcept) - 1
    @functools.lru_cache(None)
    def depth(state):
        if state.bit_count() == 1:
            return 0
        bound = state.bit_count().bit_length() - 1
        best = 0
        for q in masks:
            yes = state & q
            if yes == 0 or yes == state:
                continue
            no = state ^ yes
            if min(yes.bit_count(), no.bit_count()) < (1 << best):
                continue
            value = 1 + min(depth(yes), depth(no))
            if value > best:
                best = value
            if best == bound:
                break
        return best
    return depth(full)


def verify_certificate(doc, masks, nconcept):
    assert doc['n'] == 6 and doc['depth'] == 9
    depth = doc['depth']
    full = (1 << nconcept) - 1
    seen_leaf_ids = set()
    nodes = 0
    def run(node, state, remaining):
        nonlocal nodes
        assert state.bit_count() >= (1 << remaining)
        if remaining == 0:
            assert set(node) == {'leaf'}
            index = node['leaf']
            assert isinstance(index, int) and 0 <= index < nconcept
            assert ((state >> index) & 1) == 1
            assert index not in seen_leaf_ids
            seen_leaf_ids.add(index)
            return
        assert set(node) == {'query', 'zero', 'one'}
        j = node['query']
        assert isinstance(j, int) and 0 <= j < len(masks)
        yes = state & masks[j]
        no = state ^ yes
        nodes += 1
        run(node['zero'], no, remaining - 1)
        run(node['one'], yes, remaining - 1)
    run(doc['tree'], full, depth)
    assert nodes == 511 and len(seen_leaf_ids) == 512
    return nodes, len(seen_leaf_ids)


def main(filename):
    answers = {}
    for n in range(3, 7):
        one = trees_by_splitting(n)
        two = trees_by_insertion(n)
        assert len(one) == len(two) == {3: 3, 4: 15, 5: 105, 6: 945}[n]
        assert len(set(one)) == len(one)
        assert len(set(two)) == len(two)
        assert set(one) == set(two)
        qs = triplets(n)
        masks = responses(one, qs)
        assert len(masks) == 3 * __import__('math').comb(n, 3)
        signatures = [sum(1 << j for j, mask in enumerate(masks) if (mask >> i) & 1)
                      for i in range(len(one))]
        assert len(set(signatures)) == len(one)
        for triple in itertools.combinations(range(n), 3):
            inds = [i for i, q in enumerate(qs) if set(q) == set(triple)]
            assert len(inds) == 3
            assert masks[inds[0]] | masks[inds[1]] | masks[inds[2]] == (1 << len(one)) - 1
            assert not (masks[inds[0]] & masks[inds[1]] | masks[inds[0]] & masks[inds[2]] | masks[inds[1]] & masks[inds[2]])
        counts, witness = vc_audit(n, masks)
        vc = max(counts)
        assert vc == n - 2
        if n <= 5:
            ld = ldim_exact(masks, len(one))
            assert ld == {3: 1, 4: 3, 5: 5}[n]
        else:
            with open(filename, encoding='utf-8') as f:
                cert = json.load(f)
            internals, leaves = verify_certificate(cert, masks, len(one))
            assert len(one) < (1 << 10)
            ld = 9
        answers[n] = (len(one), vc, ld)
        if n == 6:
            assert counts == {1: 1, 2: 57, 3: 1458, 4: 18144}
            four = witness[4]
            assert four == (0, 47, 56, 59)
            print('FOUR_QUERY_WITNESS', [(j, qs[j]) for j in four])
            print('EXHAUSTIVE_FIXED_QUERY_COUNTS', sorted(counts.items()))
            print('NINE_LEVEL_TREE', internals, leaves)
    print('EXACT_TRIPLET_DIMENSIONS', answers)
    print('ROOTED_TRIPLET_ALL_CHECKS_PASS')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python verify_rooted_triples.py depth9_certificate.json')
    main(sys.argv[1])
