#!/usr/bin/env python3
"""Independent incidence-side verifier for stages zero through nine (stdlib only)."""
import json
from pathlib import Path

RULE = {48: b'01', 49: b'02', 50: b'0'}


def solve_by_position_factor_sets(w):
    n = len(w)
    all_factors = {w[i:j] for i in range(n) for j in range(i + 1, n + 1)}
    ids = {factor: k for k, factor in enumerate(sorted(all_factors))}
    all_bits = (1 << len(ids)) - 1
    cover = [0] * n
    # A factor ID is set in cover[p] iff an occurrence of that factor crosses p.
    for i in range(n):
        for j in range(i + 1, n + 1):
            bit = 1 << ids[w[i:j]]
            for p in range(i, j):
                cover[p] |= bit
    classes = [[i for i, letter in enumerate(w) if letter == c] for c in sorted(set(w))]
    if len(classes) < 3:
        return [list(range(n))]
    a, b, c = classes
    answer = []
    for i in a:
        for j in b:
            ab = cover[i] | cover[j]
            for k in c:
                if (ab | cover[k]) == all_bits:
                    answer.append(sorted([i, j, k]))
    return sorted(answer)


def run():
    data = json.loads((Path(__file__).resolve().parent / 'certificates' / 'attractors.json').read_text())
    w = b'0'
    for row in data['stages'][:10]:
        result = solve_by_position_factor_sets(w)
        assert result == row['attractors'], ('independent check', row['index'])
        print('Independent factor-by-position check:', row['index'], 'length', len(w), 'count', len(result))
        w = b''.join(RULE[x] for x in w)
    print('Two different exact incidence enumerations agree through order nine.')

if __name__ == '__main__':
    run()
