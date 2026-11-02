"""Exact finite verification of edge-membership shattering for complete-graph Hamiltonian cycles.

Run: python check_hamiltonian_cycle_gap.py cycle_depth5_certificate.json
"""
import itertools
import json
import sys
from functools import lru_cache


def cycles(n):
    """Unoriented Hamiltonian cycles, represented by a canonical permutation and edge set."""
    for rest in itertools.permutations(range(1, n)):
        if rest[0] > rest[-1]:
            continue
        perm = (0,) + rest
        edges = {tuple(sorted((perm[i], perm[(i + 1) % n]))) for i in range(n)}
        yield perm, frozenset(edges)


def evaluate(n):
    cc = list(cycles(n))
    edges = list(itertools.combinations(range(n), 2))
    q = {e: sum(1 << j for j, (_, c) in enumerate(cc) if e in c) for e in edges}
    full = (1 << len(cc)) - 1
    def shattered(S):
        signatures = {sum((1 << i) for i, e in enumerate(S) if e in c) for _, c in cc}
        return len(signatures) == (1 << len(S))
    vc = 0
    counts = {}
    for k in range(1, n):
        cnt = sum(shattered(S) for S in itertools.combinations(edges, k))
        counts[k] = cnt
        if cnt:
            vc = k
    @lru_cache(None)
    def ldim(mask):
        val = 0
        for e in edges:
            pos = mask & q[e]
            neg = mask & (full ^ q[e])
            if pos and neg:
                val = max(val, 1 + min(ldim(pos), ldim(neg)))
        return val
    return cc, edges, q, full, vc, counts, ldim


def make_certificate():
    cc, edges, q, full, vc, counts, ldim = evaluate(6)
    assert vc == 4
    assert ldim(full) == 5
    def tree(mask, depth):
        if depth == 0:
            idx = (mask & -mask).bit_length() - 1
            return {'leaf_cycle': list(cc[idx][0])}
        for e in edges:
            pos = mask & q[e]
            neg = mask & (full ^ q[e])
            if pos and neg and ldim(pos) >= depth - 1 and ldim(neg) >= depth - 1:
                return {'query_edge': list(e), 'zero': tree(neg, depth - 1), 'one': tree(pos, depth - 1)}
        raise AssertionError('no depth certificate')
    cert = {'n': 6, 'depth': 5, 'tree': tree(full, 5)}
    return cert


def verify_certificate(cert):
    assert cert['n'] == 6 and cert['depth'] == 5
    valid = {c for _, c in cycles(6)}
    nodes = [0, 0]
    def visit(t, depth, history):
        if depth == 0:
            p = t['leaf_cycle']
            assert len(p) == 6 and len(set(p)) == 6 and set(p) == set(range(6))
            edge_set = frozenset(tuple(sorted((p[i], p[(i + 1) % 6]))) for i in range(6))
            assert edge_set in valid
            for e, label in history:
                assert (e in edge_set) == bool(label)
            nodes[1] += 1
            return
        e = tuple(t['query_edge'])
        assert len(e) == 2 and 0 <= e[0] < e[1] < 6
        nodes[0] += 1
        visit(t['zero'], depth - 1, history + [(e, 0)])
        visit(t['one'], depth - 1, history + [(e, 1)])
    visit(cert['tree'], 5, [])
    assert nodes == [31, 32]
    return nodes


def main():
    expected_vc = {3: 0, 4: 1, 5: 3, 6: 4}
    expected_ldim = {3: 0, 4: 1, 5: 3, 6: 5}
    for n in range(3, 7):
        cc, es, q, full, vc, counts, ld = evaluate(n)
        assert vc == expected_vc[n], (n, vc)
        assert ld(full) == expected_ldim[n], (n, ld(full))
        print('n', n, 'cycles', len(cc), 'VC', vc, 'Ldim', ld(full), 'shattered_counts', counts)
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding='utf-8') as f:
            cert = json.load(f)
        nodes = verify_certificate(cert)
        print('certificate_internal_nodes', nodes[0], 'leaves', nodes[1])
    print('ALL_HAMILTONIAN_CYCLE_GAP_CHECKS_PASS')


if __name__ == '__main__':
    main()
