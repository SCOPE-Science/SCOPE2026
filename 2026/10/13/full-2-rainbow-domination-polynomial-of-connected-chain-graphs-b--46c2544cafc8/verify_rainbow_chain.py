#!/usr/bin/env python3
"""Independent enumeration checks for the 2-rainbow polynomial of chain graphs.

No third-party dependencies. A chain profile d contains the positive,
nondecreasing degrees of the ordered A-side vertices; d[-1] is |B|.
"""
from collections import Counter
from itertools import product
from math import comb


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i+j] += u*v
    return out


def add(a, b, sign=1):
    out = [0] * max(len(a), len(b))
    for i, u in enumerate(a):
        out[i] += u
    for j, v in enumerate(b):
        out[j] += sign*v
    return out


def h(typ, r):
    if typ == 'E':
        return [1]
    out = [comb(2-r, j) for j in range(3-r)]
    if typ == 'P':
        out[0] -= 1
    return out


def cover(types, indices):
    terms = [(0, 1)] if not indices else [(0, 1), (1, -2), (2, 1)]
    answer = [0]
    for r, sign in terms:
        poly = [1]
        for i, typ in enumerate(types):
            poly = mul(poly, h(typ, r if i in indices else 0))
        answer = add(answer, [sign*u for u in poly])
    return answer


def closed_form(d):
    p = len(d)
    q = d[-1]
    starts = {j:next(i for i in range(p) if d[i] >= j) for j in range(1,q+1)}
    answer = [0]
    for i in range(p+1):
        atypes = ['P' if a < i else 'E' if a == i else 'F'
                  for a in range(p)]
        for j in range(q+1):
            btypes = (['F' if b < j-1 else 'E' if b == j-1 else 'P'
                       for b in range(q)] if j else ['P']*q)
            ai = set(range(starts[j],p)) if j else set()
            bi = set(range(d[i])) if i < p else set()
            answer = add(answer, mul(cover(atypes, ai), cover(btypes, bi)))
    return answer


def brute(d):
    p = len(d)
    q = d[-1]
    n = p+q
    adj = [set() for _ in range(n)]
    for a in range(p):
        for b in range(d[a]):
            adj[a].add(p+b)
            adj[p+b].add(a)
    out = Counter()
    for labels in product(range(4), repeat=n):
        valid = True
        for u in range(n):
            if labels[u] == 0:
                colors = 0
                for v in adj[u]:
                    colors |= labels[v]
                if colors != 3:
                    valid = False
                    break
        if valid:
            out[sum(v.bit_count() for v in labels)] += 1
    return [out[w] for w in range(2*n+1)]


def main():
    profiles = 0
    labelings = 0
    coefficients = 0
    for p in range(1,6):
        for q in range(1,6):
            if p+q > 8:
                continue
            for d in product(range(1,q+1),repeat=p):
                if tuple(sorted(d)) != d or d[-1] != q:
                    continue
                got = closed_form(d)
                want = brute(d)
                padded = got + [0] * (len(want)-len(got))
                assert len(padded) == len(want)
                assert padded == want, (d, padded, want)
                assert padded[-1] == 1, d
                profiles += 1
                labelings += 4**(p+q)
                coefficients += len(want)
    assert tuple(closed_form((1,2))) == (0,0,0,12,48,52,28,8,1)
    assert tuple(closed_form((2,2))) == (0,0,4,24,62,56,28,8,1)
    print('VERIFY_OK profiles=%d labelings=%d coefficient_checks=%d max_order=8' %
          (profiles, labelings, coefficients))
    print('P4 nonzero coefficients: 3:12 4:48 5:52 6:28 7:8 8:1')
    print('K2,2 nonzero coefficients: 2:4 3:24 4:62 5:56 6:28 7:8 8:1')


if __name__ == '__main__':
    main()
