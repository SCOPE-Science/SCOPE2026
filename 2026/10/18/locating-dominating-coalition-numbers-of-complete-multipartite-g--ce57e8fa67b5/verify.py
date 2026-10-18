"""Exhaustive finite checks for locating-dominating coalition partitions.

Run with Python 3.10+: python verify_ldc_04.py
Brute force is finite corroboration, not a proof for arbitrary orders.
"""
from itertools import combinations_with_replacement
from collections import Counter


def partitions_of_vertices(n):
    # Canonical (restricted-growth) representation of unordered nonempty blocks.
    blocks = []
    def visit(i):
        if i == n:
            yield tuple(blocks)
            return
        for j in range(len(blocks)):
            blocks[j] |= 1 << i
            yield from visit(i + 1)
            blocks[j] ^= 1 << i
        blocks.append(1 << i)
        yield from visit(i + 1)
        blocks.pop()
    yield from visit(0)


def check_graph(sizes):
    n = sum(sizes)
    p = tuple(i for i, c in enumerate(sizes) for _ in range(c))
    adj = tuple(sum(1 << j for j in range(n) if i != j and p[i] != p[j]) for i in range(n))
    h_edges = []
    for i in range(n):
        for j in range(i+1, n):
            if p[i] == p[j] or (sizes[p[i]] == sizes[p[j]] == 1):
                h_edges.append((i, j))

    full = (1 << n) - 1
    loc = [False] * (1 << n)
    for d in range(1, 1 << n):
        signatures = []
        for v in range(n):
            if d >> v & 1:
                continue
            signature = adj[v] & d
            if not signature or signature in signatures:
                break
            signatures.append(signature)
        else:
            loc[d] = True

    star = len(sizes) == 2 and min(sizes) == 1 and max(sizes) >= 2
    if not star:
        for d in range(1, 1 << n):
            cover = all((d >> i & 1) or (d >> j & 1) for i,j in h_edges)
            assert loc[d] == cover, (sizes, d, 'cover disagreement')

    best = 0
    for blocks in partitions_of_vertices(n):
        if len(blocks) <= best or any(loc[b] for b in blocks):
            continue
        if all(any(loc[b|c] for j, c in enumerate(blocks) if k != j)
               for k, b in enumerate(blocks)):
            best = len(blocks)

    sizes_h = [z for z in sizes if z >= 2]
    s = sizes.count(1)
    if s >= 2:
        sizes_h.append(s)
    should_be_four = (max(sizes_h, default=0) <= 2 and
                      len([x for x in sizes_h if x == 2]) >= 2)
    expected = 4 if should_be_four else 3
    assert best == expected, (sizes,best,expected)
    return n, len(h_edges)


def main():
    cases = 0
    for n in range(3, 10):
        for r in range(2, n+1):
            for sizes in combinations_with_replacement(range(1,n+1),r):
                if sum(sizes) != n:
                    continue
                check_graph(sizes)
                cases += 1
    print(f'PASS: {cases} isomorphism-type part-size profiles for 3 <= n <= 9;')
    print('each possible vertex subset and every set partition was checked.')
    # A generic graph-lemma check on five-vertex quotient graphs.
    for mask in range(1 << 10):
        edges = [(i,j) for k,(i,j) in enumerate(( (i,j) for i in range(5) for j in range(i+1,5) )) if mask >> k & 1]
        covers = [set((i,j)) for i in range(5) for j in range(i+1,5)
                  if all(i in e or j in e for e in edges)]
        if not any(all(v in e for e in edges) for v in range(5)):
            assert not all(any(v in c for c in covers) for v in range(5))
    print('PASS: 1,024 five-index loopless quotient graphs satisfy the cover-support lemma.')

if __name__ == '__main__':
    main()
