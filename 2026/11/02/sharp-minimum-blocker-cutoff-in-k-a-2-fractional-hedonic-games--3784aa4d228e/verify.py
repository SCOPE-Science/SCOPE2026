"""Standalone exact exhaustive verifier for the two-minority fractional hedonic cutoff.

All utilities are compared by integer cross multiplication. Standard library only.
Run: python verify.py
"""
from itertools import combinations
from math import comb


def partitions(n):
    # Restricted growth strings, partitions of labeled vertices 0,...,n-1.
    labels = [0] * n
    def rec(i, highest):
        if i == n:
            blocks = [[] for _ in range(highest + 1)]
            for v, b in enumerate(labels):
                blocks[b].append(v)
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(highest + 2):
            labels[i] = j
            yield from rec(i + 1, max(highest, j))
    yield from rec(1, 0)


def brute_blockers(a, blocks):
    n = a + 2
    # Vertex indices 0,...,a-1 are A; a,a+1 are B.
    olds = [None] * n
    for block in blocks:
        aa = sum(v < a for v in block)
        bb = len(block) - aa
        for v in block:
            olds[v] = (bb if v < a else aa, len(block))
    result = []
    for mask in range(1, 1 << n):
        aa = (mask & ((1 << a) - 1)).bit_count()
        bb = (mask >> a).bit_count()
        if aa == 0 or bb == 0:
            continue
        t = aa + bb
        if all((bb if v < a else aa) * olds[v][1] > olds[v][0] * t
               for v in range(n) if mask & (1 << v)):
            result.append((t, mask))
    return result


def predicted_min(a, blocks):
    block_of = {}
    for block in blocks:
        for v in block:
            block_of[v] = block
    b1, b2 = block_of[a], block_of[a+1]
    if b1 == b2:
        p = sum(v < a for v in b1)
        s = a - p
        t = p // 2 + 1
        return t + 1 if s >= t else None
    p = sum(v < a for v in b1)
    q = sum(v < a for v in b2)
    if p < q:
        p, q = q, p
    s = a - p - q
    return q + 2 if (p >= q + 2 or s >= q + 1) else None


def construction(a):
    q = (a - 2) // 2
    p = q + 2
    s = a - p - q
    blocks = [tuple(range(p)) + (a,), tuple(range(p, p + q)) + (a + 1,)]
    blocks += [(v,) for v in range(p + q, a)]
    return tuple(blocks), q, p, s


def main():
    profiles = 0
    blockers = 0
    for a in range(2, 7):
        max_min = 0
        for blocks in partitions(a + 2):
            b = brute_blockers(a, blocks)
            actual = min((t for t, mask in b), default=None)
            predicted = predicted_min(a, blocks)
            assert actual == predicted, (a, blocks, actual, predicted)
            if actual is not None:
                max_min = max(max_min, actual)
            profiles += 1
            blockers += len(b)
        assert max_min == a // 2 + 1, (a, max_min)
        blocks, q, p, s = construction(a)
        bs = brute_blockers(a, blocks)
        assert all(t == q + 2 for t, _ in bs), (a, bs)
        assert len(bs) == comb(p + s, q + 1), (a, len(bs))
        assert q + 2 == a // 2 + 1
        print('a=', a, 'max_min=', max_min, 'construction_blockers=', len(bs))
    print('PASS: distinct labeled partitions:', profiles)
    print('PASS: core-blocking coalitions evaluated:', blockers)
    print('PASS: exact count/size/phase classification and sharpness')

if __name__ == '__main__':
    main()
