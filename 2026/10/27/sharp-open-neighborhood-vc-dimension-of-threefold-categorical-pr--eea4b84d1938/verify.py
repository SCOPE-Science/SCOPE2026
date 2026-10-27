#!/usr/bin/env python3
"""Exact partition certificate for open-neighborhood VC dimension of three categorical clique factors.
No external packages or files are needed. Python 3.9+.
"""
from itertools import product
from collections import defaultdict


def partitions(n):
    """All set partitions via canonical restricted-growth strings."""
    out = []
    def rec(a, m):
        if len(a) == n:
            blocks = [0] * (m + 1)
            for j, z in enumerate(a):
                blocks[z] |= 1 << j
            out.append((tuple(a), tuple(blocks)))
            return
        for z in range(m + 2):
            rec(a + [z], max(m, z))
    rec([0], 0)
    assert len(out) == {3:5, 4:15, 5:52, 6:203}[n]
    return out


def profile(n, caps):
    """Independent exact enumeration for three bounded partition classes."""
    ps = partitions(n)
    choices = [[(0,) + b for a, b in ps if len(b) <= cap] for cap in caps]
    best = 0
    winners = 0
    for aa, bb, cc in product(*choices):
        ab = {a | b for a in aa for b in bb}
        nn = len({z | c for z in ab for c in cc})
        best = max(best, nn)
        winners += (nn == (1 << n))
    return tuple(len(v) for v in choices), best, winners


def no_six():
    """Complete six-point exclusion modulo relabeling and coordinate exchange.
    First partition is canonical for its block-size shape; the last two
    partitions run over unordered pairs. The two pruning tests are necessary
    conditions for all 64 traces, never conjectural sufficiency criteria.
    """
    n = 6
    all_partitions = partitions(n)
    reprs = {}
    for _, bb in all_partitions:
        shape = tuple(sorted((x.bit_count() for x in bb), reverse=True))
        reprs.setdefault(shape, (0,) + bb)
    assert len(reprs) == 11
    blocks = [(0,) + b for _, b in all_partitions]
    priv = [0] * len(blocks)
    for i, b in enumerate(blocks):
        for x in b:
            if x.bit_count() == 1:
                priv[i] |= x
    survivors = 0
    largest_survivor = 0
    full = (1 << n) - 1
    for a in reprs.values():
        ap = 0
        for x in a:
            if x.bit_count() == 1:
                ap |= x
        for j, b in enumerate(blocks):
            ab = {x | y for x in a for y in b}
            for k in range(j, len(blocks)):
                c = blocks[k]
                # To obtain a singleton excluded trace, some coordinate
                # partition must have that point as a singleton block.
                if (ap | priv[j] | priv[k]) != full:
                    continue
                # If there are fewer than 64 candidate unions,
                # all 64 traces are impossible.
                if len(ab) * len(c) < 64:
                    continue
                survivors += 1
                patterns = {v | z for v in ab for z in c}
                largest_survivor = max(largest_survivor, len(patterns))
                assert len(patterns) < 64, (a, b, c)
    return len(reprs), survivors, largest_survivor


def witnesses():
    """Directly evaluate every advertised lower witness in the original graph."""
    examples = [
        ((3, 3, 3), [(1,1,1),(1,2,2),(2,1,2)]),
        ((3, 4, 4), [(1,1,1),(1,1,2),(1,2,3),(2,3,3)]),
        ((4, 4, 5), [(1,1,1),(1,2,2),(1,3,3),(2,1,2),(3,1,4)]),
    ]
    for alph, sample in examples:
        centers = list(product(*(range(q) for q in alph)))
        patterns = {}
        for c in centers:
            pat = sum((1 << i) for i, x in enumerate(sample)
                      if all(x[j] != c[j] for j in range(3)))
            patterns.setdefault(pat, c)
        assert len(patterns) == 2 ** len(sample)
        assert len(set(sample)) == len(sample)
        print('LOWER_WITNESS', alph, 'points', len(sample), 'traces', len(patterns), 'PASS')


def main():
    for n, caps, want in [
        (4, (2, 2, 4), (960, 15, 0)),
        (5, (2, 5, 5), (43264, 28, 0)),
        (5, (3, 3, 3), (68921, 30, 0)),
    ]:
        counts, best, yes = profile(n, caps)
        assert (__import__('math').prod(counts), best, yes) == want
        print('FORBIDDEN', n, caps, 'partition_triples', want[0],
              'max_traces', best, 'shattered', yes, 'PASS')
    shapes, survivors, largest = no_six()
    assert (shapes, survivors, largest) == (11, 27375, 61)
    print('SIX_POINT_KERNEL', 'shapes', shapes, 'survivors', survivors,
          'max_survivor_traces', largest, 'shattered', 0, 'PASS')
    witnesses()
    print('VERIFY_OK exact_three_factor_tensor_neighborhood_vc=PASS')

if __name__ == '__main__':
    main()
