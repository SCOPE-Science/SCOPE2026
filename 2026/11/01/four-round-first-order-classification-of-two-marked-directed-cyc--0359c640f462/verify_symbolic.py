"""Exact first-order type calculation for successor cycles with two constants.

Requires Python 3.9+ standard library only. For the rank-four theorem, the
infinite input family reduces mathematically to the 32-by-32 gap rectangle.
"""
from functools import lru_cache
from collections import defaultdict
import csv
import sys

_types = {}

def intern(key):
    if key not in _types:
        _types[key] = len(_types) + 1
    return _types[key]

@lru_cache(None)
def typ(vertices, gaps, rank):
    # vertices are cyclically ordered blocks of tuple-variable labels,
    # starting with label 0; labels 0 and 1 denote two distinct constants.
    # gaps[i] is the positive forward distance to the following block.
    cap = 2 ** (rank + 1)
    gaps = tuple(min(z, cap) for z in gaps)
    size = sum(len(block) for block in vertices)
    where = [-1] * size
    for position, block in enumerate(vertices):
        for label in block:
            where[label] = position
    assert sorted(x for block in vertices for x in block) == list(range(size))
    count = len(vertices)
    atomic = tuple(
        (where[a] == where[b],
         where[a] != where[b] and where[b] == (where[a] + 1) % count
         and gaps[where[a]] == 1)
        for a in range(size) for b in range(size)
    )
    if rank == 0:
        return intern((0, atomic))
    children = set()
    for i in range(count):
        nxt = list(vertices)
        nxt[i] = vertices[i] + (size,)
        children.add(typ(tuple(nxt), gaps, rank - 1))
    for i, gap in enumerate(gaps):
        for left in range(1, gap):
            nxt = list(vertices)
            nxt.insert(i + 1, (size,))
            splits = list(gaps)
            splits[i] = left
            splits.insert(i + 1, gap - left)
            children.add(typ(tuple(nxt), tuple(splits), rank - 1))
    return intern((rank, atomic, frozenset(children)))

def class_partition(rank):
    cap = 2 ** (rank + 1)
    buckets = defaultdict(list)
    for left in range(1, cap + 1):
        for right in range(1, cap + 1):
            buckets[typ(((0,), (1,)), (left, right), rank)].append((left, right))
    buckets = sorted(buckets.values(), key=lambda group:
                     min(group, key=lambda x: (sum(x), x)))
    reps = [min(group, key=lambda x: (sum(x), x)) for group in buckets]
    label = {pair: number for number, group in enumerate(buckets, 1)
             for pair in group}
    return buckets, reps, label

def main():
    if len(sys.argv) > 2 or (len(sys.argv) == 2 and sys.argv[1] != '--write-tables'):
        raise SystemExit('usage: python verify_symbolic.py [--write-tables]')
    expected = [(4, 4), (14, 7), (40, 11), (108, 19), (340, 35)]
    for rank, (count_expected, bound_expected) in enumerate(expected):
        buckets, reps, label = class_partition(rank)
        count = len(buckets)
        bound = max(map(sum, reps))
        assert count == count_expected, (rank, count)
        assert bound == bound_expected, (rank, bound)
        print(f'RANK_{rank}_OK classes={count} sharp_minimum_representative_bound={bound}')
        if rank == 4 and len(sys.argv) == 2:
            with open('class_table.csv', 'w', newline='', encoding='utf-8') as f:
                out = csv.writer(f)
                out.writerow(('forward_gap', 'return_gap', 'type_id'))
                for left in range(1, 33):
                    for right in range(1, 33):
                        out.writerow((left, right, label[(left, right)]))
            with open('class_representatives.csv', 'w', newline='', encoding='utf-8') as f:
                out = csv.writer(f)
                out.writerow(('type_id', 'forward_gap', 'return_gap', 'vertices'))
                for k, (left, right) in enumerate(reps, 1):
                    out.writerow((k, left, right, left + right))
    print('EXACT_FINITE_CLASSIFICATION_OK')

if __name__ == '__main__':
    main()
