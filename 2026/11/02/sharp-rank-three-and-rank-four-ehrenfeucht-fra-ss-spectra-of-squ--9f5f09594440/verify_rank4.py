#!/usr/bin/env python3
"""Exact bounded-rank first-order types of powers of finite cycles.

Only the simple undirected adjacency vocabulary is used.  No sampling or
floating-point arithmetic.  Run: python3 verify_rank4.py
"""
from itertools import product

def calculate(rank, maximum, power=2):
    # Intern nested finite types globally across sizes; no hashes are used as
    # substitutes for exact equality.  The bottom level records the complete
    # equality/adjacency diagram of the selected tuple.
    interning = [dict() for _ in range(rank + 1)]
    out = {}
    for n in range(3, maximum + 1):
        current = {}
        for chosen in product(range(n), repeat=rank):
            signature = []
            for i in range(rank):
                for j in range(i + 1, rank):
                    gap = (chosen[i] - chosen[j]) % n
                    entry = (0 if gap == 0 else
                             1 if min(gap, n - gap) <= power else 2)
                    signature.append(entry)
            sig = tuple(signature)
            table = interning[0]
            if sig not in table:
                table[sig] = len(table)
            current[chosen] = table[sig]
        for remaining in range(1, rank + 1):
            updated = {}
            table = interning[remaining]
            for chosen in product(range(n), repeat=rank - remaining):
                # Full back-and-forth condition: each one-point extension
                # type in one structure must occur in the other.
                key = tuple(sorted({current[chosen + (v,)] for v in range(n)}))
                if key not in table:
                    table[key] = len(table)
                updated[chosen] = table[key]
            current = updated
        out[n] = current[()]
    return out

def classes(t):
    result = {}
    for n, label in t.items():
        result.setdefault(label, []).append(n)
    return sorted(result.values(), key=lambda g: g[0])

def main():
    rank3 = classes(calculate(3, 24))
    rank4 = classes(calculate(4, 24))
    assert rank3 == [list(range(3, 6))] + [[n] for n in range(6, 11)] + [list(range(11,25))], rank3
    assert rank4 == [[3], [4, 5]] + [[n] for n in range(6,19)] + [list(range(19,25))], rank4
    print('RANK3_CLASSES', rank3)
    print('RANK4_CLASSES', rank4)
    print('RANK4_BOUNDARY',18,19,'distinct')
    print('RANK4_STABILIZATION',19,24,'equivalent')
    print('RANK4_SQUARE_CYCLES_ALL_CHECKS_PASS')

if __name__ == '__main__':
    main()
