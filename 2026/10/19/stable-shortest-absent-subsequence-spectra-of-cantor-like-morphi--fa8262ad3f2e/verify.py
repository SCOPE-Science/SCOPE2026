#!/usr/bin/env python3
"""Independent finite checks for the Cantor-like shortest absent subsequence theorem.

Run: python3 verify.py
Exact full missing-spectrum count uses deterministic earliest-occurrence automaton:
for distinct subsequences, each nonempty string chooses its first symbol
at the earliest possible position, so no duplicate strings are counted.
"""
from itertools import product


def morphic(r, k):
    w = '1'
    for _ in range(k):
        w = ''.join('1' + '0' * r + '1' if c == '1' else '0' * (r + 2) for c in w)
    return w


def digital(r, k):
    b = r + 2
    ans = []
    for n in range(b**k):
        v = n
        mark = '1'
        for _ in range(k):
            if v % b not in (0, b - 1):
                mark = '0'
                break
            v //= b
        ans.append(mark)
    return ''.join(ans)


def is_subsequence(u, w):
    it = iter(w)
    return all(c in it for c in u)


def arch_count(w):
    got = set()
    count = 0
    for c in w:
        got.add(c)
        if len(got) == 2:
            count += 1
            got.clear()
    return count


def count_absent(w, ell):
    n = len(w)
    next0 = [n] * (n + 1)
    next1 = [n] * (n + 1)
    for i in range(n - 1, -1, -1):
        next0[i] = next0[i+1]
        next1[i] = next1[i+1]
        if w[i] == '0':
            next0[i] = i
        else:
            next1[i] = i
    old = [1] * (n + 1)
    for j in range(1, ell + 1):
        old = [(old[next0[i] + 1] if next0[i] < n else 0)
                + (old[next1[i] + 1] if next1[i] < n else 0)
                for i in range(n + 1)]
    return (1 << ell) - old[0]


def expected_absent(r, m):
    if r == 1:
        L = ('00', '01', '11')
        R = ('00', '10', '11')
        return {a + '1' * (m - 3) + z for a in L for z in R}
    return {a + '1' * (m - 1) + z for a in '01' for z in '01'}


def main():
    for r, kmax in ((1, 8), (2, 6), (3, 5), (4, 4), (5, 4), (7, 3)):
        for k in range(2, kmax + 1):
            w = morphic(r, k)
            assert w == digital(r, k), ('generators',r,k)
            m = 1 << k
            assert len(w) == (r+2)**k
            assert w.count('1') == m
            assert arch_count(w) == m, ('arches',r,k)
            wanted = expected_absent(r, m)
            assert len(wanted) == (9 if r == 1 else 4)
            assert all(not is_subsequence(p, w) for p in wanted), ('forbidden',r,k)
            assert count_absent(w, m+1) == len(wanted), ('exact count',r,k)
            if k == 2 and r in (1, 2):
                empirical = {''.join(x) for x in product('01', repeat=5)
                             if not is_subsequence(''.join(x), w)}
                assert empirical == wanted, ('complete base', r)
            print(f'PASS r={r} k={k} length={len(w)} ones={m} missing={len(wanted)}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
