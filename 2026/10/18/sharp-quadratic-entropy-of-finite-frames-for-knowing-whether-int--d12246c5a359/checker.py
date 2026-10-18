#!/usr/bin/env python3
"""Independent finite truth-table and structural verification of noncontingency introspection."""
from itertools import product

def brute_frame(n, edges):
    rows = [sum(1 << j for j in range(n) if edges & (1 << (i*n+j))) for i in range(n)]
    for val in range(1 << n):
        delta = [int((r & val) == 0 or (r & val) == r) for r in rows]
        for r in rows:
            truth = {delta[j] for j in range(n) if r & (1 << j)}
            if len(truth) > 1:
                return False
    return True

def classified_frame(n, edges):
    rows = [sum(1 << j for j in range(n) if edges & (1 << (i*n+j))) for i in range(n)]
    types = [0 if r.bit_count() <= 1 else r for r in rows]
    for r in rows:
        if len({types[j] for j in range(n) if r & (1 << j)}) > 1:
            return False
    return True

def lower_witness(n, choices):
    a = n//2
    A = (1 << a)-1
    fixed = 3
    rows = [0]*a
    for mask in choices:
        rows.append(fixed | ((mask << 2) & A))
    edges = sum((r << (i*n)) for i,r in enumerate(rows))
    return edges

def main():
    counts = []
    for n in range(1,5):
        yes = 0
        for e in range(1 << (n*n)):
            c = classified_frame(n,e)
            assert c == brute_frame(n,e), (n,e,c)
            yes += c
        counts.append(yes)
        print(f'n={n}, admissible={yes}, exhaustive_frames={1<<(n*n)}')
    assert counts == [2, 10, 128, 3070], f'Actual counts: {counts}'
    for n in range(4,12):
        free = max(0,n//2-2)
        for masks in product(range(1 << free), repeat=n-n//2):
            e = lower_witness(n,masks)
            assert classified_frame(n,e)
            if n <= 6:
                assert brute_frame(n,e)
        print('lower-bound construction',n, 'families', (1<<free)**(n-n//2), 'verified')
    print('OK')

if __name__ == '__main__':
    main()
