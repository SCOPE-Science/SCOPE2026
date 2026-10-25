"""Finite checks for the quadrilateral multiple-illumination classification.

The mathematical proof is analytic and covers all strictly convex quadrilaterals.
These checks sample rational angular fans; they are not a proof for all fans.
"""
from collections import deque
from itertools import product
from math import pi, cos


def masks(turn_units, modulus):
    """Vertex-illumination masks for angular cells between sign changes."""
    beta = [0.0]
    for t in turn_units[:3]:
        beta.append(beta[-1] + 2*pi*t/modulus)
    critical = sorted({round((b + side*pi/2) % (2*pi), 12)
                       for b in beta for side in (-1, 1)})
    result = set()
    for j, lo in enumerate(critical):
        hi = critical[(j+1) % len(critical)]
        if j == len(critical)-1:
            hi += 2*pi
        theta = (lo+hi)/2
        bitset = 0
        for i in range(4):
            if cos(theta-beta[(i-1) % 4]) < -1e-8 and cos(theta-beta[i]) < -1e-8:
                bitset |= 1 << i
        if bitset:
            result.add(bitset)
    return tuple(sorted(result))


def minimum_multicover(available, multiplicity):
    """Breadth-first exact search on all capped coverage vectors."""
    goal = (multiplicity,)*4
    origin = (0,)*4
    queue = deque([(origin, 0)])
    visited = {origin}
    while queue:
        state, length = queue.popleft()
        if state == goal:
            return length
        for mask in available:
            nxt = tuple(min(multiplicity, state[i] + ((mask >> i) & 1))
                        for i in range(4))
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, length+1))
    raise AssertionError('Every vertex should be individually illuminable')


def main():
    trials = 0
    # Exhaust each integral normal-angle fan on three moderately fine meshes.
    for modulus in (10, 12, 14):
        for t1 in range(1, modulus//2):
            for t2 in range(1, modulus//2):
                for t3 in range(1, modulus//2):
                    t4 = modulus-t1-t2-t3
                    if not 1 <= t4 < modulus/2:
                        continue
                    turns = (t1,t2,t3,t4)
                    attainable = masks(turns, modulus)
                    is_parallelogram = (
                        t1+t2 == modulus/2 and t2+t3 == modulus/2)
                    pair_sets = [frozenset(i for i in range(4) if mask>>i & 1)
                                 for mask in attainable if mask.bit_count()==2]
                    assert all(mask.bit_count() <= 2 for mask in attainable)
                    assert all(pair1 & pair2 for pair1 in pair_sets
                               for pair2 in pair_sets)
                    assert bool(pair_sets) == (not is_parallelogram)
                    for m in (1,2,3,4):
                        assert minimum_multicover(attainable, m) == (
                            4 if is_parallelogram else 3)*m, (turns,m,attainable)
                    trials += 1
    print('PASS: %d finite normal-fan/multicover instances per multiplicity' % trials)
    print('PASS: four multiplicities, opposite-pair prohibition and common-pivot tests')


if __name__ == '__main__':
    main()
