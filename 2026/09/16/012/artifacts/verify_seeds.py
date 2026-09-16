"""Independent subset-DP verification of all construction certificates.

Run from workspace root: python3 output/artifacts/verify_seeds.py
No matching code or link classification is imported.
"""
from itertools import combinations
from pathlib import Path
import json
import math


def rank(pairs):
    states = {0}
    for a, b in pairs:
        updated = set(states)
        for state in states:
            for v in (a, b):
                if not state >> v & 1:
                    new = state | (1 << v)
                    if new.bit_count() == 5:
                        return 5
                    updated.add(new)
        states = updated
    return max(map(int.bit_count, states))


def verify(n, edges):
    assert all(len(e) == 3 and len(set(e)) == 3 and min(e) >= 0 and max(e) < n
               for e in edges)
    edges = [tuple(sorted(e)) for e in edges]
    assert len(edges) == len(set(edges))
    edges = set(edges)
    links = [[tuple(x for x in e if x != v) for e in edges if v in e]
             for v in range(n)]
    ranks = [rank(link) for link in links]
    assert max(ranks, default=0) <= 4
    for e in combinations(range(n), 3):
        if e not in edges:
            assert any(rank(links[v] + [tuple(x for x in e if x != v)]) == 5 for v in e), e
    return ranks


def main():
    data = json.loads(Path(__file__).with_name('seeds.json').read_text())
    seeds = {}
    for g in data['seeds']:
        n, m, edges = g['n'], g['m'], g['edges']
        assert m == len(edges) and g['d'] == 2 * n - m and g['r'] == n % 5
        ranks = verify(n, edges)
        assert g['aggressive'] == all(x == 4 for x in ranks)
        seeds[g['r'], g['d']] = g
    needed = [(r, d) for r in range(1, 5) for d in range(5, 12)]
    assert all(key in seeds for key in needed)
    assert max(seeds[key]['n'] for key in needed) <= 16
    lantern = [(0, 1, 2), (3, 4, 5)]
    for i in range(3):
        group = tuple(range(6 + 3 * i, 9 + 3 * i))
        lantern.append(group)
        lantern.extend((v, x, y) for v in (i, i + 3) for x, y in combinations(group, 2))
    sun = [(w, 2 + j, 2 + (j + 1) % 4) for w in range(2) for j in range(4)]
    assert len(lantern) == 2 + 3 * (math.comb(4, 3) + math.comb(3, 2)) == 23
    assert len(sun) == 8
    assert verify(15, lantern) == [4] * 15
    assert verify(6, sun) == [4] * 6
    assert verify(5, list(combinations(range(5), 3))) == [4] * 5
    # Direct checks of the lower endpoint formula, distinct from symbolic simplification.
    for n in range(5, 301):
        values = [(4 * (n - a) + 2) // 3 + math.comb(a, 3) for a in range(1, 5)]
        assert min(values) == (4 * n + 2) // 3 - 3
    # Check construction arithmetic over all residues and many lantern counts.
    checked = 0
    for n in range(56, 501):
        if n % 5 == 0:
            continue
        for d in range(5, n // 3 + 1):
            d0 = 5 + (d - 5) % 7
            g = seeds[n % 5, d0]
            q = (d - d0) // 7
            unused = n - g['n'] - 15 * q
            assert unused >= 0 and unused % 5 == 0
            assert g['m'] + 23 * q + 10 * (unused // 5) == 2 * n - d
            checked += 1
    print(json.dumps({'all_seed_records_checked': len(seeds), 'required_seeds': len(needed),
                      'max_required_order': max(seeds[k]['n'] for k in needed),
                      'lantern': [15, 23, 7], 'sun': [6, 8, 4],
                      'lower_endpoint_comparisons': 296, 'construction_counts_checked': checked}))
    print('Seed orders, columns d=5,...,11:')
    for r in range(1, 5):
        print(r, [seeds[r, d]['n'] for d in range(5, 12)])


if __name__ == '__main__':
    main()
