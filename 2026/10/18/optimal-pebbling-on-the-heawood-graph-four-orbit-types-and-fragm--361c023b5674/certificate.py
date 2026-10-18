"""Regenerate or verify complete finite reachability and exchange certificates.

Usage:
    python3 certificate.py --write
    python3 certificate.py --verify
The default graph is the point--line incidence graph of the Fano plane.
All files are relative to this script, with no external dependencies.
"""
import argparse
from collections import defaultdict
from functools import lru_cache
from itertools import combinations_with_replacement
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NEIGHBORS = [set() for _ in range(14)]
for line in range(7):
    for shift in (0, 1, 3):
        point = (line + shift) % 7
        NEIGHBORS[point].add(line + 7)
        NEIGHBORS[line + 7].add(point)

@lru_cache(None)
def reachable(state):
    mask = sum((1 << i) for i, c in enumerate(state) if c)
    for u, count in enumerate(state):
        if count >= 2:
            for v in NEIGHBORS[u]:
                child = list(state)
                child[u] -= 2
                child[v] += 1
                mask |= reachable(tuple(child))
    return mask


def distributions(k):
    for indices in combinations_with_replacement(range(14), k):
        v = [0] * 14
        for i in indices:
            v[i] += 1
        yield tuple(v)


def files():
    state_lines = []
    optima = []
    for k in range(7):
        for d in distributions(k):
            mask = reachable(d)
            state_lines.append(''.join(map(str, d)) + '\t' + f'{mask:04x}\n')
            if k == 6 and mask == 0x3fff:
                optima.append(d)
    assert len(state_lines) == 38760 and len(optima) == 161
    idx = {s: i for i, s in enumerate(optima)}
    exchange_edges = set()
    for i, s in enumerate(optima):
        for u, count in enumerate(s):
            if count == 0:
                continue
            for v in NEIGHBORS[u]:
                child = list(s)
                child[u] -= 1
                child[v] += 1
                j = idx.get(tuple(child))
                if j is not None and i < j:
                    exchange_edges.add((i, j))
    assert len(exchange_edges) == 42
    return {
        'reachability_states.tsv': ''.join(state_lines).encode('ascii'),
        'optimal_distributions.tsv': ''.join(''.join(map(str, d)) + '\n' for d in optima).encode('ascii'),
        'exchange_edges.tsv': ''.join(f'{i}\t{j}\n' for i, j in sorted(exchange_edges)).encode('ascii')
    }


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--write', action='store_true')
    group.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    produced = files()
    for name, raw in produced.items():
        path = ROOT / name
        if args.write:
            path.write_bytes(raw)
        else:
            assert path.read_bytes() == raw, f'Certificate differs from generated truth: {name}'
        print(f'{name}: {len(raw)} bytes, {raw.count(bytes([10]))} rows, checked')
    print(f'Exact reachability states checked: {reachable.cache_info().currsize}')

if __name__ == '__main__':
    main()
