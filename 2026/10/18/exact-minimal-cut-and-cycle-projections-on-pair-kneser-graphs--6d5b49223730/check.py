#!/usr/bin/env python3
"""Exact integer/rational consistency checks for cut/cycle projections of KG(n,2).

No third-party modules are required. This finite check does not prove the infinite-family theorem.
"""
from fractions import Fraction
from itertools import combinations


def verify(n):
    assert isinstance(n, int) and n >= 5
    vs = list(combinations(range(n), 2))
    vv = len(vs)
    es = [(i, j) for i, a in enumerate(vs) for j, b in enumerate(vs)
          if i < j and set(a).isdisjoint(b)]
    adjacency = [[] for _ in vs]
    for i, j in es:
        adjacency[i].append(j)
        adjacency[j].append(i)
    d = (n - 2) * (n - 3) // 2
    r = n - 4
    a = d + r - 1
    D = (d + 1) * a - 2 * r
    assert 4 * D == r * (r + 1) * (r + 3) * (r + 4)
    expected_cut = Fraction(2 * (n - 3) * (n + 6), n * (n - 1))
    expected_cycle = 1 + expected_cut - Fraction(8 * (n + 1), n * (n - 1) * (n - 3))
    cnt = 0
    assert vv == n * (n - 1) // 2
    assert len(es) == vv * d // 2
    cnt += 2
    for v in adjacency:
        assert len(v) == d
        cnt += 1
    for ek, (ia, ib) in enumerate(es):
        A = set(vs[ia]); B = set(vs[ib]); R = set(range(n)) - A - B
        # D times the solution of the graph Poisson equation is integral:
        # h(AB)=a, h(CD)=-a, h(AB--R)=-1, h(CD--R)=+1,
        # h(cross)=h(R--R)=0.
        h = []
        for pair in vs:
            s = set(pair)
            if s == A:
                h.append(a)
            elif s == B:
                h.append(-a)
            elif len(s & A) == 1 and len(s & R) == 1:
                h.append(-1)
            elif len(s & B) == 1 and len(s & R) == 1:
                h.append(1)
            else:
                h.append(0)
        assert sum(h) == 0
        cnt += 1
        for i in range(vv):
            lh = d * h[i] - sum(h[j] for j in adjacency[i])
            expect = D if i == ia else (-D if i == ib else 0)
            assert lh == expect, (n, ek, i, lh, expect)
            cnt += 1
        cutsum = 0; cyclesum = 0
        for j, (ix, iy) in enumerate(es):
            diff = h[ix] - h[iy]
            cutsum += abs(diff)
            cyclesum += abs((D if j == ek else 0) - diff)
            cnt += 1
        assert Fraction(cutsum, D) == expected_cut, (n, ek, 'cut', cutsum, D)
        assert Fraction(cyclesum, D) == expected_cycle, (n, ek, 'cycle', cyclesum, D)
        cnt += 2
    return cnt, len(es), expected_cut, expected_cycle


def main():
    total = 0
    for n in range(5, 11):
        assertions, edges, cut, cycle = verify(n)
        total += assertions
        print(f'n={n} edges={edges} cut={cut} cycle={cycle} checks={assertions}')
    assert Fraction(2 * (8 - 3) * (8 + 6), 8 * 7) == Fraction(5, 2)
    assert Fraction(2 * (9 - 3) * (9 + 6), 9 * 8) == Fraction(5, 2)
    assert Fraction(3 * 12**3 - 4 * 12**2 - 59 * 12 + 100,
                    12 * (12 - 3) * (12 - 1)) == Fraction(1000, 297)
    total += 3
    print(f'OK: {total} exact finite checks. Universal claims require the written proof.')


if __name__ == '__main__':
    main()
