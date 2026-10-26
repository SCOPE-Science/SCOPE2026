#!/usr/bin/env python3
"""Exact finite graph certificate for cyclic binary length-four complement avoidance.
Standard library only. All loops are bounded explicitly (3**8 support sets,
2**16 words), and no precomputed scientific result is imported.
"""
from itertools import combinations
from math import comb

# Edges are four-bit integers: source is the leading three bits,
# destination the trailing three bits; bitwise complement is 15-e.
TEMPLATES = tuple(frozenset(int(c, 16) for c in s) for s in
    ('012568bc', '013468ad', '2579bcef', '3479adef', '012489', '67bdef'))


def reachable(edges, initial, reverse=False):
    found, todo = {initial}, [initial]
    while todo:
        v = todo.pop()
        for e in edges:
            a, b = ((e & 7, e >> 1) if reverse else (e >> 1, e & 7))
            if a == v and b not in found:
                found.add(b)
                todo.append(b)
    return found


def connected_edge_support(edges):
    if not edges:
        return False
    nodes = {v for e in edges for v in (e >> 1, e & 7)}
    return all(reachable(edges, v) == nodes and
               reachable(edges, v, True) == nodes for v in nodes)


def enumerate_connected_supports():
    connected = set()
    for ternary in range(3**8):
        k, edges = ternary, []
        for i in range(8):
            digit, k = k % 3, k // 3
            if digit == 1:
                edges.append(i)
            elif digit == 2:
                edges.append(15-i)
        support = frozenset(edges)
        if connected_edge_support(support):
            connected.add(support)
    return connected


def adjacency(edges):
    A = [[0] * 8 for _ in range(8)]
    for e in edges:
        A[e >> 1][e & 7] += 1
    return A


def traces(A, N):
    power = [[int(i == j) for j in range(8)] for i in range(8)]
    out = []
    for _ in range(N):
        power = [[sum(power[i][v] * A[v][j] for v in range(8))
                  for j in range(8)] for i in range(8)]
        out.append(sum(power[i][i] for i in range(8)))
    return out


def determinant_coefficients_from_traces(t):
    # Newton recurrence for det(I-z A)=sum_{k=0}^8 a_k z^k.
    a = [1]
    for k in range(1,9):
        numerator = -sum(a[k-i]*t[i-1] for i in range(1,k+1))
        assert numerator % k == 0
        a.append(numerator // k)
    return a


def separated_one_count(m, n):
    # 1 all-zero word and circular gap compositions for j>=1 markers.
    count = 1
    for j in range(1, n//m + 1):
        numerator = n * comb(n-(m-1)*j-1, j-1)
        assert numerator % j == 0
        count += numerator // j
    return count


def formula(n):
    return 2*separated_one_count(3, n) + 4*separated_one_count(7, n) - 4


def direct(n):
    good = 0
    for w in range(1 << n):
        bits = [(w >> i) & 1 for i in range(n)]
        factors = {sum(bits[(i+j) % n] << (3-j) for j in range(4))
                   for i in range(n)}
        if not any(15-e in factors for e in factors):
            good += 1
    return good


def main():
    supports = enumerate_connected_supports()
    assert len(supports) == 20
    assert {frozenset((0,)), frozenset((15,))} <= supports
    maximal = {s for s in supports if not any(s < t for t in supports)}
    assert maximal == set(TEMPLATES)
    assert sum(len(s) > 1 for s in supports) == 18
    assert all(sum(s <= t for t in TEMPLATES) == (3 if len(s) == 1 else 1)
               for s in supports)
    # Every cyclic factor-support is strongly connected, so the 20-element
    # finite classification implies the six-template disjoint decomposition.
    polynomials = []
    for i, t in enumerate(TEMPLATES):
        assert connected_edge_support(t)
        tr = traces(adjacency(t), 36)
        poly = determinant_coefficients_from_traces(tr[:8])
        expected = [1] + [-1] + [0] * ((7 if i < 4 else 3) - 2) + [-1]
        expected += [0]*(9-len(expected))
        assert poly == expected, (i, poly, expected)
        polynomials.append(poly)
        for n in range(1, 37):
            assert tr[n-1] == separated_one_count(7 if i < 4 else 3, n)
    assert polynomials[:4] == [[1,-1,0,0,0,0,0,-1,0]] * 4
    assert polynomials[4:] == [[1,-1,0,-1,0,0,0,0,0]] * 2
    # Completely independent bit-string check, including all short periods.
    for n in range(1, 17):
        assert direct(n) == formula(n), (n, direct(n), formula(n))
    expected = [2,2,8,10,12,20,58,74,98,132,178,244,340,506,738,1066,1532,2198,3156,4540]
    assert [formula(n) for n in range(1,21)] == expected
    print('COMPLEMENT4_CYCLIC_PASS supports=20 maximal=6 orientations=6561 direct=1..16 traces=1..36')
    print('c_1..20=', expected)

if __name__ == '__main__':
    main()
