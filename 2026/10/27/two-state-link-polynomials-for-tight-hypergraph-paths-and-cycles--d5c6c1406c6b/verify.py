#!/usr/bin/env python3
"""Exact finite checks for the tight-path/tight-cycle one-type polynomial."""
from itertools import combinations
from math import comb


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    return out


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def matmul(a, b):
    return [[add(mul(a[i][0], b[0][j]), mul(a[i][1], b[1][j]))
             for j in range(2)] for i in range(2)]


def mpow(n):
    M = [[[1, 1], [0, 1, 1]], [[1, 1], [0, 1]]]
    result = [[[1], [0]], [[0], [1]]]
    for _ in range(n):
        result = matmul(result, M)
    return result


def power_1u(n):
    out = [1]
    for _ in range(n):
        out = mul(out, [1, 1])
    return out


def transfer_poly(n, kind):
    assert (kind == 'path' and n >= 3) or (kind == 'cycle' and n >= 5)
    if kind == 'cycle':
        m = mpow(n)
        z = add(m[0][0], m[1][1])
        free = comb(n, 2) - 2*n
    else:
        m = mpow(n-2)
        # left boundary vector (1,u), right boundary vector (1,1)
        z = add(add(m[0][0], m[0][1]),
                mul([0,1], add(m[1][0], m[1][1])))
        free = comb(n, 2) - (2*n-3)
    out = mul(power_1u(free), z)
    while len(out)>1 and out[-1]==0:
        out.pop()
    return out


def edge_triples(n, kind):
    if kind == 'cycle':
        return [frozenset((i,(i+1)%n,(i+2)%n)) for i in range(n)]
    return [frozenset((i,i+1,i+2)) for i in range(n-2)]


def brute_poly(n, kind):
    pairs = list(combinations(range(n), 2))
    ix = {p:i for i,p in enumerate(pairs)}
    forbidden = [sum(1 << ix[p] for p in combinations(sorted(e),2))
                 for e in edge_triples(n,kind)]
    out = [0] * (len(pairs)+1)
    for mask in range(1 << len(pairs)):
        if all((mask & f) != f for f in forbidden):
            out[mask.bit_count()] += 1
    while len(out)>1 and out[-1]==0:
        out.pop()
    return out


def check():
    for n in range(3,7):
        want = transfer_poly(n, 'path')
        got = brute_poly(n, 'path')
        assert want == got, ('path', n, want, got)
    for n in (5,6):
        want = transfer_poly(n, 'cycle')
        got = brute_poly(n, 'cycle')
        assert want == got, ('cycle', n, want, got)
    # An extra independent two-million-mask computation for the unweighted size-seven cycle.
    assert sum(brute_poly(7,'cycle')) == 930432
    for n in range(5,12):
        edges = [frozenset(e) for e in edge_triples(n,'cycle')]
        for four in combinations(range(n),4):
            assert sum(set(t).issubset(four) for t in edges) < 4
    traces = [2,3]
    for n in range(2,31):
        traces.append(3*traces[-1]+2*traces[-2])
    for n in range(5,20):
        assert sum(transfer_poly(n,'cycle')) == (1 << (comb(n,2)-2*n))*traces[n]
    assert [sum(transfer_poly(n,'cycle')) for n in (5,6,7)] == [573,16328,930432]
    assert [sum(transfer_poly(n,'path')) for n in (3,4,5)] == [7,50,712]
    print('ALL_CHECKS_PASS path_polynomials=4 cycle_polynomials=2')
    print('CYCLE_N5_N6_N7 573 16328 930432')
    print('PATH_N3_N4_N5 7 50 712')
    print('CYCLE_N7_BRUTE_2097152_MASKS_PASS')
    print('K4_FREE_N5_THROUGH_N11_PASS')
    print('TRACE_RECURRENCE_N5_THROUGH_N19_PASS')

if __name__ == '__main__':
    check()
