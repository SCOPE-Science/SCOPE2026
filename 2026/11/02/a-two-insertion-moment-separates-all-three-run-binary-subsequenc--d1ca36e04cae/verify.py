#!/usr/bin/env python3
"""Independent exact checks for binary three-run subsequence moments.

Pure Python standard library; run: python3 verify.py
"""
from itertools import combinations, product
from math import comb


def choose(n, k):
    return comb(n, k) if n >= k >= 0 else 0


def claimed_moment(a, b, c):
    r = (a, b, c)
    length = sum(r)
    return (4 * comb(length + 2, 2)
            + 2 * (length + 2) * sum(x * (x + 1) for x in r)
            + 6 * sum(choose(x + 2, 4) for x in r)
            + 4 * sum(choose(r[i] + 1, 2) * choose(r[j] + 1, 2)
                      for i in range(3) for j in range(i + 1, 3))
            + 2 * (a * b + b * c + a * c)
            - 2 * a * c * (b >= 2))


def embeddings(a, b, c):
    pattern = '1' * a + '0' * b + '1' * c
    n = len(pattern) + 2
    out = {}
    for holes in combinations(range(n), 2):
        zero = one = 0
        index = 0
        for pos in range(n):
            if pos in holes:
                continue
            if pattern[index] == '0':
                zero |= 1 << pos
            else:
                one |= 1 << pos
            index += 1
        out[holes] = (zero, one)
    return out


def hole_pair_moment(a, b, c):
    maps = embeddings(a, b, c)
    total = 0
    for holes_a, (za, oa) in maps.items():
        for holes_b, (zb, ob) in maps.items():
            if za & ob or zb & oa:
                continue
            total += 1 << len(set(holes_a).intersection(holes_b))
    return total


def direct_host_moment(a, b, c):
    pat = '1' * a + '0' * b + '1' * c
    length = len(pat)
    n = length + 2
    ans = 0
    for host in product('01', repeat=n):
        counts = [0] * (length + 1)
        counts[0] = 1
        for ch in host:
            for i in range(length - 1, -1, -1):
                if pat[i] == ch:
                    counts[i + 1] += counts[i]
        ans += counts[-1] ** 2
    return ans


def shape_counts(a, b, c):
    maps = embeddings(a, b, c)
    length = a + b + c + 2
    forms = ('AABB', 'ABAB', 'ABBA', 'BAAB', 'BABA', 'BBAA')
    out = {form: 0 for form in forms}
    for positions in combinations(range(length), 4):
        for form in forms:
            A = tuple(positions[i] for i in range(4) if form[i] == 'A')
            B = tuple(positions[i] for i in range(4) if form[i] == 'B')
            za, oa = maps[A]
            zb, ob = maps[B]
            if not (za & ob or zb & oa):
                out[form] += 1
    return out


def predicted_shapes(a, b, c):
    r = (a, b, c)
    base = sum(choose(v + 2, 4) for v in r)
    u = base + a * b + b * c + a * c * (b == 1)
    v = base + sum(choose(r[i] + 1, 2) * choose(r[j] + 1, 2)
                   for i in range(3) for j in range(i + 1, 3))
    return {'AABB': u, 'BBAA': u, 'ABAB': v, 'BABA': v, 'ABBA': v, 'BAAB': v}


def run_all_checks():
    cases = 0
    for a in range(1, 7):
        for b in range(1, 7):
            for c in range(1, 7):
                pair = hole_pair_moment(a, b, c)
                assert pair == claimed_moment(a, b, c), ((a,b,c), pair)
                shape = shape_counts(a, b, c)
                assert shape == predicted_shapes(a, b, c), ((a,b,c), shape)
                cases += 1
    print('pair-and-shape checks:', cases)
    hosts = 0
    for a in range(1, 7):
        for b in range(1, 7):
            for c in range(1, 7):
                if a + b + c > 9:
                    continue
                direct = direct_host_moment(a, b, c)
                assert direct == claimed_moment(a, b, c), ((a,b,c), direct)
                hosts += 1
    print('independent direct-host checks:', hosts)
    assert [claimed_moment(*p) for p in [(1,2,3), (1,3,2), (2,1,3)]] == [592, 594, 598]
    print('example (1,2,3)/(1,3,2)/(2,1,3): 592/594/598')
    print('VERIFY_OK')


if __name__ == '__main__':
    run_all_checks()
