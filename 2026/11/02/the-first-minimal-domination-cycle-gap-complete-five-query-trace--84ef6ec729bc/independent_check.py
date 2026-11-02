#!/usr/bin/env python3
"""Independent removal-based enumeration and exact online recursion."""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def is_dominating(n, chosen):
    return all(any(((chosen >> j) & 1) for j in ((i - 1) % n, i, (i + 1) % n))
               for i in range(n))


def concepts(n):
    return tuple(mask for mask in range(1 << n)
                 if is_dominating(n, mask)
                 and all(not is_dominating(n, mask ^ (1 << i))
                         for i in range(n) if mask & (1 << i)))


def depth_of_tree(node):
    return 0 if 'witness' in node else 1 + min(depth_of_tree(node['0']), depth_of_tree(node['1']))


def exact_online_dimension(n, classes):
    membership_masks = tuple(sum(((c >> query) & 1) << j
                                 for j, c in enumerate(classes)) for query in range(n))
    @lru_cache(maxsize=None)
    def rank(version_space):
        if version_space.bit_count() < 2:
            return 0
        best = 0
        for row in membership_masks:
            yes = version_space & row
            no = version_space & ~row
            if yes and no:
                best = max(best, 1 + min(rank(yes), rank(no)))
        return best
    return rank((1 << len(classes)) - 1)


def main():
    expected = {3:(3,1),4:(6,2),5:(5,2),6:(5,2),7:(14,3),
                8:(14,3),9:(21,4),10:(27,4),11:(44,5)}
    for n, (count, ldim) in expected.items():
        cs = concepts(n)
        assert len(cs) == count, (n, len(cs))
        assert exact_online_dimension(n, cs) == ldim, n
    print('REMOVAL_BASED_EXACT_ONLINE_RECURRENCE_PASS n=3..11')

    cs = concepts(11)
    # A second direct method for the full five-query histogram.
    hist = Counter()
    for S in combinations(range(11), 5):
        observed = 0
        for c in cs:
            signature = 0
            for bit, coordinate in enumerate(S):
                signature |= ((c >> coordinate) & 1) << bit
            observed |= 1 << signature
        hist[observed.bit_count()] += 1
    assert sorted(hist.items()) == sorted({11:11,14:22,15:44,16:11,18:11,19:88,
        20:33,21:77,22:44,23:11,24:66,25:33,29:11}.items())
    print('INDEPENDENT_FIVE_QUERY_SPECTRUM_PASS supports=462')

    certificate = json.loads((HERE / 'cycle11_certificate.json').read_text(encoding='utf8'))
    assert depth_of_tree(certificate['tree']) == 5
    def check(node, path=()):
        if 'witness' in node:
            m = int(node['witness'], 16)
            assert m in cs and all((m >> i & 1) == b for i, b in path)
            return {m}
        i = node['query']
        A = check(node['0'], path + ((i,0),))
        B = check(node['1'], path + ((i,1),))
        assert len(A | B) == len(A) + len(B)
        return A | B
    assert len(check(certificate['tree'])) == 32
    print('INDEPENDENT_CERTIFICATE_REPLAY_PASS leaves=32')
    print('ALL_INDEPENDENT_CYCLE11_CHECKS_PASS')

if __name__ == '__main__':
    main()
