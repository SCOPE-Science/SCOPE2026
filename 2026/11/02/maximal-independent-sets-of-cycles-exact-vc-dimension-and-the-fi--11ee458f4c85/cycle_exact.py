"""Independent exhaustive checks for maximal-independent-set learning on cycles.
Only the elementary mathematical objects and reproducible checks appear here.
Run: python cycle_exact.py certificate.json
"""
import json
import sys
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb


def maximal_independent_cycle(n):
    assert n >= 3
    result = []
    for m in range(1 << n):
        if any(((m >> i) & 1) and ((m >> ((i + 1) % n)) & 1)
               for i in range(n)):
            continue
        if any(not (((m >> i) & 1) or ((m >> ((i - 1) % n)) & 1)
                        or ((m >> ((i + 1) % n)) & 1)) for i in range(n)):
            continue
        result.append(m)
    return tuple(result)


def dimension_vc(concepts, n):
    found = 0
    witness = ()
    for support in range(1 << n):
        k = support.bit_count()
        if k <= found:
            continue
        trace_count = len({h & support for h in concepts})
        if trace_count == (1 << k):
            found = k
            witness = tuple(i for i in range(n) if support & (1 << i))
    return found, witness


def dimension_ld(concepts, n):
    @lru_cache(None)
    def rank(space):
        if len(space) < 2:
            return 0
        best = 0
        for query in range(n):
            yes = tuple(h for h in space if (h >> query) & 1)
            no = tuple(h for h in space if not (h >> query) & 1)
            if yes and no:
                best = max(best, 1 + min(rank(yes), rank(no)))
        return best
    return rank(tuple(concepts)), rank


def construct_tree(concepts, n, rank, remaining):
    if remaining == 0:
        return {'witness': concepts[0]}
    for q in range(n):
        yes = tuple(h for h in concepts if (h >> q) & 1)
        no = tuple(h for h in concepts if not (h >> q) & 1)
        if yes and no and rank(yes) >= remaining-1 and rank(no) >= remaining-1:
            return {'query': q,
                    'zero': construct_tree(no, n, rank, remaining-1),
                    'one': construct_tree(yes, n, rank, remaining-1)}
    raise AssertionError('No full tree exists')


def verify_tree(node, concepts, n, depth, previous=()):
    if depth == 0:
        assert set(node) == {'witness'}
        witness = node['witness']
        assert witness in concepts
        assert all(((witness >> q) & 1) == bit for q, bit in previous)
        return [witness]
    assert set(node) == {'query','zero','one'}
    q = node['query']
    assert type(q) is int and 0 <= q < n
    leaves = []
    for bit, name in [(0,'zero'),(1,'one')]:
        leaves.extend(verify_tree(node[name], concepts, n, depth-1, previous+((q,bit),)))
    return leaves


def trace_spectrum(concepts, n, k):
    hist = Counter()
    for xs in combinations(range(n),k):
        support = sum(1<<i for i in xs)
        hist[len({h & support for h in concepts})] += 1
    assert sum(hist.values()) == comb(n,k)
    return dict(sorted(hist.items()))


def main(cert_file):
    data = json.load(open(cert_file,encoding='utf8'))
    assert data['graph'] == 'C_13'
    assert data['n'] == 13
    table = []
    for n in range(3,14):
        concepts = maximal_independent_cycle(n)
        vc, support = dimension_vc(concepts,n)
        ld, rank = dimension_ld(concepts,n)
        assert ld >= vc
        table.append([n,len(concepts),vc,ld])
    assert table == data['small_cycle_table']
    concepts = maximal_independent_cycle(13)
    vc, witness = dimension_vc(concepts,13)
    assert vc==4 and len(witness)==4
    assert len(concepts)==39
    for k in (4,5):
        hist=trace_spectrum(concepts,13,k)
        assert hist == {int(a):v for a,v in data['trace_spectra'][str(k)].items()}
    assert max(int(x) for x in data['trace_spectra']['5'])==29
    assert data['trace_spectra']['5']['29']==13
    path_witnesses=verify_tree(data['depth_five_tree'],concepts,13,5)
    assert len(path_witnesses)==32 and len(set(path_witnesses))==32
    assert len(data['depth_five_tree']['zero'])==3
    assert set(data['depth_five_tree']['one'])=={'query','zero','one'}
    print('SMALL_CYCLE_EXHAUSTIVE_TABLE_PASS', table)
    print('C13_FIVE_QUERY_SPECTRUM_PASS max=29 count_at_max=13 supports=1287')
    print('C13_DEPTH5_DECISION_TREE_PASS leaves=32 distinct_witnesses=32 concepts=39')
    print('ALL_CYCLE_SHATTERING_CHECKS_PASS')

if __name__=='__main__':
    assert len(sys.argv)==2
    main(sys.argv[1])
