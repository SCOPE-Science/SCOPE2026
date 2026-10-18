"""Finite tests of the explicit antichain and paired-vertex incidence colorings.

Run: python3 verify.py.  Uses only the Python standard library.  These tests
corroborate, but do not replace, the general mathematical proof.
"""
from itertools import combinations
from math import comb


def middle_codes(t):
    k = t // 2
    return [sum(1 << c for c in C) for C in combinations(range(t), k)]


def least_bit(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def verify_arcs(n, edges, colors, palette):
    E = {tuple(sorted(e)) for e in edges}
    assert set(colors) == {(u, v) for a, b in E for u, v in ((a, b), (b, a))}
    assert all(0 <= c < palette for c in colors.values())
    triples = 0
    for b in range(n):
        nbr = [v for v in range(n) if v != b and tuple(sorted((v, b))) in E]
        for a in nbr:
            for c in nbr:
                if a == c:
                    continue
                triples += 1
                assert colors[a, b] != colors[b, c], (a, b, c, palette)
    return triples


def sperner_coloring(n, edges, vertex_colors, t):
    codes = middle_codes(t)
    assert max(vertex_colors) < len(codes)
    arcs = {}
    for a, b in edges:
        s, r = codes[vertex_colors[a]], codes[vertex_colors[b]]
        assert s != r
        arcs[a, b] = least_bit(s & ~r)
        arcs[b, a] = least_bit(r & ~s)
    return arcs


def paired_clique_coloring(n, t):
    r = t - 1
    labels = middle_codes(r)
    assert n <= 2 * len(labels)
    codes = [labels[i // 2] for i in range(n)]
    arcs = {}
    for a, b in combinations(range(n), 2):
        if a // 2 == b // 2:
            arcs[a, b] = arcs[b, a] = r
        else:
            arcs[a, b] = least_bit(codes[a] & ~codes[b])
            arcs[b, a] = least_bit(codes[b] & ~codes[a])
    return arcs


def run():
    checks = arcs_total = triple_total = 0
    for t in range(2, 9):
        codes = middle_codes(t)
        assert len(codes) == comb(t, t // 2)
        for q in (2, min(3, len(codes)), min(6, len(codes)), len(codes)):
            if q < 2:
                continue
            edges = list(combinations(range(q), 2))
            c = sperner_coloring(q, edges, list(range(q)), t)
            triple_total += verify_arcs(q, edges, c, t)
            checks += 1
            arcs_total += len(c)
    for t in range(1, 9):
        cap = 2 * len(middle_codes(t - 1))
        if t == 1:
            ns = [2]
        else:
            ns = sorted({2, max(2, cap // 2), cap})
        for n in ns:
            E = list(combinations(range(n), 2))
            c = paired_clique_coloring(n, t)
            triple_total += verify_arcs(n, E, c, t)
            checks += 1
            arcs_total += len(c)
    for n in range(2, 31):
        E = [(i, (i + 1) % n) for i in range(n)] if n >= 3 else [(0, 1)]
        if n % 2 == 0:
            cv = [i % 2 for i in range(n)]
        else:
            cv = [i % 2 for i in range(n - 1)] + [2]
        t = next(k for k in range(2, 6) if len(middle_codes(k)) >= max(cv) + 1)
        c = sperner_coloring(n, E, cv, t)
        triple_total += verify_arcs(n, E, c, t)
        checks += 1
        arcs_total += len(c)
    print('VERIFY_OK')
    print('complete_general_and_paired_tests:', checks - 29)
    print('cycle_and_path_tests:', 29)
    print('oriented_incidences_checked:', arcs_total)
    print('ordered_length_two_walk_checks:', triple_total)
    print('paired_clique_t5_capacity:', 2 * comb(4, 2))
    print('sperner_t5_capacity:', comb(5, 2))
    print('sperner_t6_capacity:', comb(6, 3))

if __name__ == '__main__':
    run()
