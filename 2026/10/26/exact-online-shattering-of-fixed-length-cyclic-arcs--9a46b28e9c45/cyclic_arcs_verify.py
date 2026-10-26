#!/usr/bin/env python3
"""Independent finite checking and a complete online-shattering witness.

Requires only Python 3.9+.  All indices are residues modulo n.
The general all-n proof is mathematical; exhaustive checks are finite cross-checks.
"""

from functools import lru_cache
from itertools import combinations
from math import floor, log2
import json
from pathlib import Path


def hypotheses(n, k):
    """Membership words for all length-k cyclic intervals."""
    return tuple(sum(1 << ((c + j) % n) for j in range(k)) for c in range(n))


def exact_ldim(n, k):
    """Direct minimax recurrence on arbitrary subsets of possible hypotheses."""
    h = hypotheses(n, k)
    queries = tuple(sum(1 << c for c in range(n) if (h[c] >> x) & 1)
                    for x in range(n))

    @lru_cache(maxsize=None)
    def rank(version_mask):
        best = 0
        for q in queries:
            pos = version_mask & q
            neg = version_mask & ~q
            if pos and neg:
                best = max(best, 1 + min(rank(pos), rank(neg)))
        return best

    return rank((1 << n) - 1)


def direct_vc(n, k):
    """Check traces of all point subsets of sizes <=3."""
    words = hypotheses(n, k)
    ans = 0
    for m in range(1, min(3, n) + 1):
        if any(len({tuple((h >> x) & 1 for x in sample) for h in words}) == 1 << m
               for sample in combinations(range(n), m)):
            ans = m
        else:
            break
    return ans


def balanced_threshold_tree(n, s):
    """Construct a depth 1+floor(log2(s)) full tree of center witnesses.

    The two root children use equal power-of-two-size blocks of centers.
    Each later query divides its surviving contiguous block exactly in half.
    """
    r = s.bit_length() - 1
    width = 1 << r
    assert n >= 2 * s and s >= 1

    def threshold(start, size):
        if size == 1:
            return {"center": start % n}
        left = size // 2
        return {"query": (start + left - 1) % n,
                "0": threshold(start + left, size - left),
                "1": threshold(start, left)}

    return {"n": n, "k": s, "depth": r + 1,
            "tree": {"query": s - 1,
                     "0": threshold(s, width),
                     "1": threshold(0, width)}}


def verify_tree(witness):
    n, k, depth = witness['n'], witness['k'], witness['depth']
    assert n >= 2 * k
    leaves = []

    def visit(node, labels):
        if 'center' in node:
            assert len(labels) == depth
            c = node['center']
            for x, bit in labels:
                assert int((x - c) % n < k) == bit, (n, k, c, x, bit)
            leaves.append(c)
            return
        assert set(node) == {'query', '0', '1'}
        q = node['query']
        assert 0 <= q < n
        for bit in (0, 1):
            visit(node[str(bit)], labels + ((q, bit),))

    visit(witness['tree'], tuple())
    assert len(leaves) == (1 << depth)
    assert len(set(leaves)) == len(leaves)
    return len(leaves)


def main():
    checks = 0
    for n in range(2, 17):
        for k in range(1, n):
            s = min(k, n - k)
            target = 1 + s.bit_length() - 1
            actual = exact_ldim(n, k)
            assert actual == target, ('Ldim', n, k, actual, target)
            checks += 1
    print('MINIMAX_OK', checks, 'all parameter pairs n=2..16')

    for n in (20, 24, 32, 40, 64):
        for k in (n // 2, n // 2 - 1):
            s = min(k, n-k)
            actual = exact_ldim(n, k)
            target = s.bit_length()
            assert actual == target, ('large', n, k, actual, target)
            print('LARGE_MINIMAX_OK', n, k, actual, flush=True)

    vc_checks = 0
    for n in range(2, 21):
        for k in range(1, n):
            s = min(k, n-k)
            target = 1 if s == 1 else 2
            actual = direct_vc(n, k)
            assert actual == target, ('VC', n, k, actual, target)
            vc_checks += 1
    print('VC_TRACES_OK', vc_checks, 'all parameter pairs n=2..20, tested through triples')

    examples = [(8, 4), (9, 4), (16, 8), (32, 16), (64, 32), (128, 64)]
    for n, s in examples:
        tree = balanced_threshold_tree(n, s)
        count = verify_tree(tree)
        print('TREE_OK', n, s, 'depth', tree['depth'], 'leaves', count)
    out = Path(__file__).with_name('cyclic_arcs_witness_n128_k64.json')
    out.write_text(json.dumps(balanced_threshold_tree(128, 64),
                              ensure_ascii=False, separators=(',', ':'))+'\n', encoding='utf-8')
    print('CERTIFICATE_WRITTEN', out.name)
    print('ALL_CHECKS_OK')

if __name__ == '__main__':
    main()
