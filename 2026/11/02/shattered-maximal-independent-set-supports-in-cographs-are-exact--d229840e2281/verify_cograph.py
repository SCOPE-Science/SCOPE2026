"""Exhaustive checks for maximal-independent-set shattering on small graphs.

Only Python standard library is required. All finite domains used by this verifier
are fully enumerated. The all-order statement is proved separately in RESULT.md.
"""
from itertools import combinations, permutations


def edges_of(n):
    return list(combinations(range(n), 2))


def graph(n, code):
    edges = edges_of(n)
    return frozenset(e for j, e in enumerate(edges) if code >> j & 1)


def adjacency(n, es):
    adj = [0] * n
    for a, b in es:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    return adj


def maximal_independent_sets(n, es):
    adj = adjacency(n, es)
    out = []
    for s in range(1 << n):
        if any((s >> a & 1) and (s >> b & 1) for a, b in es):
            continue
        if any(not(s >> i & 1) and not (adj[i] & s) for i in range(n)):
            continue
        out.append(s)
    return out


def shattering(n, es):
    hypotheses = maximal_independent_sets(n, es)
    ans = set()
    for s in range(1 << n):
        if len({h & s for h in hypotheses}) == 1 << s.bit_count():
            ans.add(s)
    return ans


def induced_matching_transversals(n, es):
    edge_list = sorted(es)
    out = {0}
    for t in range(1, 1 << len(edge_list)):
        chosen = [edge_list[j] for j in range(len(edge_list)) if t >> j & 1]
        ends = {v for e in chosen for v in e}
        if len(ends) != 2 * len(chosen):
            continue
        if sum(a in ends and b in ends for a, b in edge_list) != len(chosen):
            continue
        for orientation in range(1 << len(chosen)):
            s = 0
            for k, e in enumerate(chosen):
                s |= 1 << e[(orientation >> k) & 1]
            out.add(s)
    return out


def is_p4_free(n, es):
    for q in combinations(range(n), 4):
        local = [e for e in es if e[0] in q and e[1] in q]
        if len(local) != 3:
            continue
        deg = [sum(v in e for e in local) for v in q]
        if sorted(deg) == [1, 1, 2, 2]:
            return False
    return True


def is_chordal_to_five(n, es):
    # On at most five vertices, all forbidden induced cycles have length 4 or 5.
    for k in (4, 5):
        for q in combinations(range(n), k):
            local = [e for e in es if e[0] in q and e[1] in q]
            if len(local) == k and all(sum(v in e for e in local) == 2 for v in q):
                return False
    return True


def is_gem(n, es):
    if n != 5:
        return False
    adj = adjacency(n, es)
    for root in range(5):
        if adj[root].bit_count() != 4:
            continue
        q = [v for v in range(5) if v != root]
        inside = [e for e in es if root not in e]
        if len(inside) == 3 and sorted(sum(v in e for e in inside) for v in q) == [1, 1, 2, 2]:
            return True
    return False


def components(n, es, complement=False):
    adj = adjacency(n, es)
    if complement:
        adj = [((1 << n) - 1) ^ (1 << v) ^ adj[v] for v in range(n)]
    unseen = set(range(n))
    out = []
    while unseen:
        start = next(iter(unseen))
        seen = {start}
        todo = [start]
        unseen.remove(start)
        while todo:
            v = todo.pop()
            for w in list(unseen):
                if adj[v] >> w & 1:
                    unseen.remove(w)
                    seen.add(w)
                    todo.append(w)
        out.append(sorted(seen))
    return out


def induced(n, es, q):
    mapping = {v: i for i, v in enumerate(q)}
    return len(q), frozenset(tuple(sorted((mapping[a], mapping[b]))) for a, b in es if a in mapping and b in mapping)


def shatter_polynomial_from_cotree(n, es):
    if n == 0 or n == 1:
        return [1]
    cs = components(n, es)
    if len(cs) > 1:
        p = [1]
        for c in cs:
            qn, qe = induced(n, es, c)
            r = shatter_polynomial_from_cotree(qn, qe)
            t = [0] * (len(p) + len(r) - 1)
            for i, a in enumerate(p):
                for j, b in enumerate(r):
                    t[i + j] += a * b
            p = t
        return p
    cs = components(n, es, complement=True)
    assert len(cs) > 1, 'Input must be a cograph.'
    # A join has no shattered support spanning two join-components.
    out = [1, n]
    for c in cs:
        qn, qe = induced(n, es, c)
        p = shatter_polynomial_from_cotree(qn, qe)
        if len(out) < len(p):
            out.extend([0] * (len(p) - len(out)))
        for k in range(2, len(p)):
            out[k] += p[k]
    return out


def same_isomorphism(n, es, reference):
    for perm in permutations(range(n)):
        mapped = frozenset(tuple(sorted((perm[a], perm[b]))) for a, b in es)
        if mapped == reference:
            return True
    return False


def verify():
    total = 0
    cographs = 0
    chordal_fails = 0
    all_fails = []
    templates = {
        'five-cycle': frozenset({(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)}),
        'house': frozenset({(0, 1), (1, 2), (2, 3), (0, 3), (0, 4), (3, 4)}),
        'gem': frozenset({(0, 1), (1, 2), (2, 3), (0, 4), (1, 4), (2, 4), (3, 4)}),
    }
    failure_counts = {k: 0 for k in templates}
    for n in range(0, 6):
        for code in range(1 << (n * (n - 1) // 2)):
            es = graph(n, code)
            total += 1
            shattered = shattering(n, es)
            im_trans = induced_matching_transversals(n, es)
            if is_p4_free(n, es):
                cographs += 1
                assert shattered == im_trans, ('support-characterization', n, code)
                polynomial = [sum(s.bit_count() == k for s in shattered) for k in range(n + 1)]
                predicted = shatter_polynomial_from_cotree(n, es)
                predicted += [0] * (n + 1 - len(predicted))
                assert polynomial == predicted, ('polynomial', n, code)
            vc = max(s.bit_count() for s in shattered)
            im = max(s.bit_count() for s in im_trans)
            if vc > im:
                all_fails.append((n, code))
                assert n == 5
                classes = [name for name, t in templates.items() if same_isomorphism(5, es, t)]
                assert len(classes) == 1, ('unclassified gap', n, code)
                failure_counts[classes[0]] += 1
                if is_chordal_to_five(n, es):
                    chordal_fails += 1
                    assert is_gem(n, es), ('non-gem chordal exception', code)
    assert cographs > 0 and chordal_fails == 60
    assert failure_counts == {'five-cycle': 12, 'house': 60, 'gem': 60}, failure_counts
    assert all(n == 5 for n, code in all_fails)
    assert len(all_fails) == 60 + 12 + 60, ('all five-vertex failures', len(all_fails))
    print('COGRAPH_COMPLETE_SMALL_GRAPH_CENSUS_PASS', 'all_labeled=', total, 'cographs=', cographs)
    print('INDUCED_MATCHING_SUPPORTS_AND_POLYNOMIALS_PASS')
    print('SMALLEST_FIVE_VERTEX_GAP_PASS', 'all_labeled=', len(all_fails), 'types=', failure_counts)
    return True


if __name__ == '__main__':
    verify()
