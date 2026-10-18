#!/usr/bin/env python3
"""Standalone exhaustive verifier for the finite-chain involution certificate.

Requires only the Python 3 standard library. Input: INVOLUTION_CERT.json
in the same directory (or an explicitly supplied path).
"""
from bisect import bisect_left
from itertools import combinations
from math import comb
from pathlib import Path
import json
import sys


def isotone_map(n, cuts, image):
    return tuple(image[bisect_left(cuts, x)] for x in range(1, n + 1))


def after(f, g):
    """Apply f, then g; both encode maps on {1,...,n}."""
    return tuple(g[y - 1] for y in f)


def verify(path):
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    assert data['schema'] == 'isotone_involution_matching_certificate_v1'
    assert data['max_n'] == 8
    rows = data['rank_blocks']
    assert len(rows) == 36
    seen = set()
    totals = []
    for row in rows:
        n, r = row['n'], row['rank']
        assert 1 <= r <= n <= 8
        assert (n, r) not in seen
        seen.add((n, r))
        partitions = list(combinations(range(1, n), r - 1))
        images = list(combinations(range(1, n + 1), r))
        image_count = len(images)
        maps = [isotone_map(n, cuts, image) for cuts in partitions for image in images]
        # Complete and nonduplicated representation of every rank-r isotone map.
        assert len(maps) == comb(n - 1, r - 1) * comb(n, r)
        assert len(set(maps)) == len(maps)
        assert all(len(set(f)) == r and tuple(sorted(f)) == f for f in maps)
        idempotent_count = sum(after(f, f) == f for f in maps)
        assert idempotent_count == comb(n + r - 1, 2 * r - 1)
        partners = row['partners']
        assert len(partners) == len(maps)
        assert set(type(i) for i in partners) == {int}
        assert all(0 <= i < len(maps) for i in partners)
        for u, v in enumerate(partners):
            assert partners[v] == u, (n, r, u, v, 'not an involution')
            f, g = maps[u], maps[v]
            assert after(after(f, g), f) == f, (n, r, u, v, 'f g f')
            assert after(after(g, f), g) == g, (n, r, u, v, 'g f g')
            if u == v:
                assert after(f, f) == f, (n, r, u, 'fixed point not idempotent')
        fixed = sum(u == v for u, v in enumerate(partners))
        nonidempotent_count = len(maps) - idempotent_count
        # Every non-idempotent must be paired; parity is a sharp lower bound
        # on the number of idempotents that must be moved.
        assert fixed == idempotent_count - (nonidempotent_count % 2)
        totals.append((n, r, len(maps), sum(u != v for u, v in enumerate(partners))))
    assert seen == {(n, r) for n in range(1, 9) for r in range(1, n + 1)}
    for n in range(1, 9):
        assert sum(x[2] for x in totals if x[0] == n) == comb(2 * n - 1, n)
    for n in range(1, 9):
        entries = [x for x in totals if x[0] == n]
        paired = sum(x[3] for x in entries)
        print('n=%d maps=%d paired_nonfixed=%d fixed=%d ranks=%d' % (
            n, sum(x[2] for x in entries), paired,
            sum(x[2] - x[3] for x in entries),len(entries)))
    print('PASS: exhaustive rank-preserving involution inverse matching, n=1,...,8')


if __name__ == '__main__':
    verify(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name('INVOLUTION_CERT.json'))
