#!/usr/bin/env python3
"""Direct edge-once depth-first enumeration of weight-[1,2] binary universal cycles.
Each cyclic tour has the unique edge 0^(n-1)1 fixed as its first edge.
"""
from collections import defaultdict
from math import comb


def count_cyclic_universal_cycles(n):
    if n < 2:
        raise ValueError('n>=2 required')
    mask = (1 << (n-1)) - 1
    edge_labels = [i for i in range(1 << n) if i.bit_count() in (1,2)]
    edge_no = {x:k for k,x in enumerate(edge_labels)}
    outgoing = defaultdict(list)
    for word in edge_labels:
        outgoing[word >> 1].append((word & mask,1 << edge_no[word]))
    root = 0
    first = 1  # word 0^(n-1)1; the unique outgoing edge at root
    assert edge_no[first] >= 0
    full = (1 << len(edge_labels)) - 1
    count = 0
    def visit(vertex, used):
        nonlocal count
        if used == full:
            if vertex == root:
                count += 1
            return
        for target, bit in outgoing[vertex]:
            if not used & bit:
                visit(target, used | bit)
    visit(1, 1 << edge_no[first])
    return count

if __name__ == '__main__':
    for n in range(2,12):
        found = count_cyclic_universal_cycles(n)
        expected = 1 << ((n-1)//2)
        assert found == expected, (n, found, expected)
        print(f'n={n:2d} length={n*(n+1)//2:3d} cyclic_count={found:5d} expected={expected:5d}')
    print('DIRECT_DFS_OK')
