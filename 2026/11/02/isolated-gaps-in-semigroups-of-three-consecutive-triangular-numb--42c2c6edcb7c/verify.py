#!/usr/bin/env python3
"""Independent integer verification of isolated gaps in triangular triples.

For each n this script computes Apéry representatives by Dijkstra on residue
classes, not from the proposed rectangular formula. It then constructs every
isolated gap using the Apéry criterion and compares it with the claimed list.
Small parameters receive a separate coin-membership dynamic-programming check.
"""
from heapq import heappush, heappop


def params(n):
    assert n >= 3
    a = n * (n + 1) // 2
    b = (n + 1) * (n + 2) // 2
    c = (n + 2) * (n + 3) // 2
    if n % 2:
        m = (n + 1) // 2
        A, B, d, e = 2*m - 1, 2*m + 1, m, m+1
    else:
        m = n // 2
        A, B, d, e = m, m+1, 2*m+1, 2*m+3
    assert (a, b, c) == (A*d, B*d, B*e)
    assert c == 2*b - a + 1
    return a, b, c, A, B, d


def apery_dijkstra(a, b, c):
    w = [None] * a
    w[0] = 0
    heap = [(0, 0)]
    while heap:
        x, r = heappop(heap)
        if w[r] != x:
            continue
        for step in (b, c):
            nr, nx = (r + step) % a, x + step
            if w[nr] is None or nx < w[nr]:
                w[nr] = nx
                heappush(heap, (nx, nr))
    assert all(x is not None for x in w)
    return w


def isolated_from_apery(w, a):
    output = set()
    for r, x in enumerate(w):
        left = w[(r-1) % a]
        right = w[(r+1) % a]
        kmax = min((x-left-1)//a, (x-right+1)//a)
        for k in range(1, max(0, kmax) + 1):
            output.add(x-k*a)
    return output


def predicted(n):
    a,b,c,A,B,d = params(n)
    if n in (3,4,6):
        return None
    out = set()
    for y in (A-2,A-1):
        for z in range(1,d-1):
            out.add(y*b+z*c-a)
        for k in range(1,B):
            out.add(y*b+(d-1)*c-k*a)
    return out


def direct_membership(a,b,c,F):
    in_s = bytearray(F+2)
    in_s[0] = 1
    for v in range(1,F+2):
        in_s[v] = any(v >= q and in_s[v-q] for q in (a,b,c))
    return {v for v in range(1,F+1) if not in_s[v] and in_s[v-1] and in_s[v+1]}


def main():
    checked_residues = 0
    direct_cases = 0
    for n in range(3,151):
        a,b,c,A,B,d = params(n)
        w = apery_dijkstra(a,b,c)
        assert len(set(w)) == a
        assert len({x % a for x in w}) == a
        actual = isolated_from_apery(w,a)
        expected_size = {3:5,4:4,6:11}.get(n, 3*n-1 if n % 2 else 3*n-2)
        assert len(actual) == expected_size, (n,len(actual),expected_size)
        p = predicted(n)
        if p is not None:
            assert p == actual, (n,sorted(p ^ actual)[:10])
        if n <= 16:
            F = max(w)-a
            assert direct_membership(a,b,c,F) == actual, n
            direct_cases += 1
        checked_residues += a
    print('VERIFY_OK n=3..150 inclusive; exact isolated sets and counts;'
          f' {checked_residues} Apéry residues;'
          f' {direct_cases} direct-membership cases')

if __name__ == '__main__':
    main()
