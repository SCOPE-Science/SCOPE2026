#!/usr/bin/env python3
"""Independent shortest-path enumeration checks for caterpillar general-position counting.

Run with Python >=3.9: python verify_caterpillars.py
The finite tests are not a proof of the unrestricted identity.
"""
from collections import deque
from itertools import combinations, product
from math import comb


def sum_poly(a, b):
    out = [0] * max(len(a), len(b))
    for i, c in enumerate(a):
        out[i] += c
    for i, c in enumerate(b):
        out[i] += c
    return out


def product_poly(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            out[i + j] += c * d
    return out


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def binomial_poly(a):
    return [comb(a, k) for k in range(a + 1)]


def formula(profile):
    r = len(profile)
    A = [binomial_poly(a) for a in profile]
    E = []
    out = [1 - r]
    for a, w in zip(profile, A):
        e = w + [0] * max(0, 2-len(w))
        e[0] -= 1
        e[1] += 1
        E.append(e)
        same = w + [0] * max(0, 3-len(w))
        same[1] += 1
        same[2] += a
        out = sum_poly(out, same)
    for left in range(r):
        intermediate = [1]
        for right in range(left + 1, r):
            out = sum_poly(out, product_poly(product_poly(E[left], intermediate), E[right]))
            intermediate = product_poly(intermediate, A[right])
    return trim(out)


def recurrence(profile):
    out = [1]
    h = [0]
    for a in profile:
        w = binomial_poly(a)
        e = sum_poly(w, [0, 1])
        e[0] -= 1
        same = sum_poly(w, [0, 1, a])
        same[0] -= 1
        out = sum_poly(out, same)
        out = sum_poly(out, product_poly(h, e))
        h = sum_poly(e, product_poly(h, w))
    return trim(out)


def brute(profile):
    r = len(profile)
    n = r + sum(profile)
    adj = [set() for _ in range(n)]
    for j in range(r - 1):
        adj[j].add(j + 1)
        adj[j + 1].add(j)
    cursor = r
    for j, leaves in enumerate(profile):
        for _ in range(leaves):
            adj[j].add(cursor)
            adj[cursor].add(j)
            cursor += 1
    dist = []
    for root in range(n):
        d = [-1] * n
        d[root] = 0
        todo = deque([root])
        while todo:
            at = todo.popleft()
            for to in adj[at]:
                if d[to] == -1:
                    d[to] = d[at] + 1
                    todo.append(to)
        dist.append(d)
    forbidden_triples = set()
    for i, j, k in combinations(range(n), 3):
        if (dist[i][j] + dist[j][k] == dist[i][k] or
            dist[i][k] + dist[k][j] == dist[i][j] or
            dist[j][i] + dist[i][k] == dist[j][k]):
            forbidden_triples.add((1 << i) | (1 << j) | (1 << k))
    tally = [0] * (n + 1)
    for mask in range(1 << n):
        if all((mask & bad) != bad for bad in forbidden_triples):
            tally[mask.bit_count()] += 1
    return trim(tally)


def main():
    cases = 0
    examined = 0
    for r in range(1, 6):
        for a in product(range(4), repeat=r):
            n = r + sum(a)
            if n > 13:
                continue
            lhs = formula(a)
            rhs = recurrence(a)
            actual = brute(a)
            if lhs != actual or rhs != actual:
                raise AssertionError((a, lhs, rhs, actual))
            cases += 1
            examined += 1 << n
    known = 0
    for n in range(1, 13):
        coefficients = formula([1] * n)
        for k in range(3, n + 1):
            assert coefficients[k] == 4 * comb(n, k), (n, k)
        known += 1
    for q in range(1, 10):
        for s in range(1, 12):
            coefficients = formula([q] + [0] * s)
            order = s + q + 1
            assert coefficients[:3] == [1, order, comb(order, 2)]
            for k in range(3, len(coefficients)):
                count = (s * comb(q, k - 1) if k - 1 <= q else 0)
                count += comb(q, k) if k <= q else 0
                assert coefficients[k] == count, (q, s, k)
            known += 1
    print(f'VERIFICATION_OK exhaustive_profiles={cases} subsets_tested={examined} known_family_cases={known}')


if __name__ == '__main__':
    main()
