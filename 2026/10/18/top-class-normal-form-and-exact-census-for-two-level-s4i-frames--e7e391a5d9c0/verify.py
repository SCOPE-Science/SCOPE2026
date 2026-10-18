#!/usr/bin/env python3
"""Exact finite verification of the two-level S4I-frame classification.

Only standard Python is required. Run: python3 verify.py
"""
from itertools import product


def preorders(n):
    """Independently enumerate reflexive, transitive relations as bitmask rows."""
    off = [(i, j) for i in range(n) for j in range(n) if i != j]
    for z in range(1 << len(off)):
        rows = [1 << i for i in range(n)]
        for k, (i, j) in enumerate(off):
            if (z >> k) & 1:
                rows[i] |= 1 << j
        if all(not ((rows[i] >> j) & 1) or not (rows[j] & ~rows[i])
               for i in range(n) for j in range(n)):
            yield tuple(rows)


def downsets(rows):
    n = len(rows)
    for mask in range(1 << n):
        if all(not ((mask >> j) & 1) or
               all(not ((rows[i] >> j) & 1) or ((mask >> i) & 1)
                   for i in range(n))
               for j in range(n)):
            yield mask


def top_class(rows):
    n = len(rows)
    return sum(1 << j for j in range(n)
               if all((rows[i] >> j) & 1 for i in range(n)))


def local_data(n):
    q = list(preorders(n))
    P = len(q)
    G = sum(bool(top_class(r)) for r in q)
    T = sum(sum(1 for _ in downsets(r)) for r in q)
    E = sum(sum(1 for _ in downsets(r)) for r in q if top_class(r))
    return q, (P, G, T, E)


def class_count(lp, lq):
    P, G, T, E = lp
    P2, G2, T2, E2 = lq
    return ((P - G) * (P2 - G2)
            + (T - E) * G2
            + G * (T2 - E2)
            + E * E2)


def valid_literal(rows, p, q):
    """Test reflexivity, transitivity, and both clauses literally on every triple."""
    n = p + q
    above = lambda x, y: x == y or (x < p <= y)
    if any(not ((rows[i] >> i) & 1) for i in range(n)):
        return False
    if any((rows[i] >> j) & 1 and rows[j] & ~rows[i]
           for i in range(n) for j in range(n)):
        return False
    for a in range(p):
        for b in range(p, n):
            for z in range(n):
                # Forth-up: a<=b, a R z -> b R some w>=z.
                if (rows[a] >> z) & 1:
                    if not any(((rows[b] >> w) & 1) and above(z, w)
                               for w in range(n)):
                        return False
                # Forth-down: a<=b, b R z -> a R some w<=z.
                if (rows[b] >> z) & 1:
                    if not any(((rows[a] >> w) & 1) and above(w, z)
                               for w in range(n)):
                        return False
    return True


def construct(p, q, A, B, U, V):
    n = p + q
    top_A, top_B = top_class(A), top_class(B)
    rows = list(A) + [z << p for z in B]
    for a in range(p):
        if (U >> a) & 1:
            rows[a] |= top_B << p
    for b in range(q):
        if (V >> b) & 1:
            rows[p + b] |= top_A
    return tuple(rows)


def check(p, q, lists):
    n = p + q
    expected = class_count(lists[p][1], lists[q][1])
    algebraic = set()
    for A, B in product(lists[p][0], lists[q][0]):
        us = list(downsets(A)) if top_class(B) else [0]
        vs = list(downsets(B)) if top_class(A) else [0]
        for U, V in product(us, vs):
            r = construct(p, q, A, B, U, V)
            assert valid_literal(r, p, q), ('invalid reconstruction', p, q, r)
            algebraic.add(r)
    assert len(algebraic) == expected, (p, q, len(algebraic), expected)

    direct = set()
    for R in preorders(n):
        if valid_literal(R, p, q):
            direct.add(R)
    assert direct == algebraic, ('failure of exhaustive classification', p, q,
                                 len(direct), len(algebraic),
                                 len(direct - algebraic), len(algebraic - direct))
    print('EXHAUSTIVE',p,q,len(direct))


def main():
    lists={n: local_data(n) for n in range(1,6)}
    expected={1:(1,1,2,2),2:(4,3,12,8),3:(29,16,130,59),
              4:(355,145,2338,746),5:(6942,2111,66304,15232)}
    for n in range(1,6):
        assert lists[n][1]==expected[n], (n,lists[n][1])
        print('LOCAL',n,*lists[n][1])
    for p,q in [(1,1),(1,2),(2,1),(2,2),(1,3),(3,1),(2,3),(3,2)]:
        check(p,q,lists)
    expected_counts={(2,2):89,(2,3):762,(3,3):5922,(2,4):11534,
                     (3,4):82511,(4,4):1062296,(5,5):470978369}
    for (p,q),want in expected_counts.items():
        got=class_count(lists[p][1],lists[q][1]); assert got==want,(p,q,got,want)
        print('FORMULA',p,q,got)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
