#!/usr/bin/env python3
"""Exact, dependency-free checks for dimension-only maxima of classical NODF.

No numerical floating-point calculations are used. NODF normalization is by
all unordered within-guild vertex pairs (rather than only eligible pairs).
"""
from itertools import product, combinations
from fractions import Fraction
from collections import Counter
from math import comb, lcm


def formula(m, n):
    a, b = sorted((m, n))
    q, r = divmod(b, a)
    ties = (a-r)*comb(q, 2) + r*comb(q+1, 2)
    pairs = comb(m, 2) + comb(n, 2)
    return Fraction(pairs-ties, pairs), ties, comb(a, r)


def canonical_ferrers(a, b, chosen):
    q, r = divmod(b, a)
    assert len(chosen) == r
    col_degrees = tuple(k for k in range(1,a+1)
                        for _ in range(q + (k in chosen)))
    assert len(col_degrees) == b
    # Matrix has a rows and b columns; shorter-guild rows are initial segments
    # of the larger-guild species neighborhoods. Every column of degree d is
    # adjacent to the first d rows.
    rows = tuple(sum(1 << j for j,d in enumerate(col_degrees) if i < d)
                 for i in range(a))
    return rows, col_degrees


def integer_nodf(rows, n):
    m = len(rows)
    rowdeg = [x.bit_count() for x in rows]
    cols = [sum(1 << i for i, row in enumerate(rows) if row & (1 << j))
            for j in range(n)]
    coldeg = [x.bit_count() for x in cols]
    if min(rowdeg + coldeg) == 0:
        return None
    scale = lcm(*range(1, max(m, n) + 1))
    total = 0
    for i in range(m):
        for j in range(i+1,m):
            if rowdeg[i] != rowdeg[j]:
                total += ((rows[i]&rows[j]).bit_count() * scale
                          // min(rowdeg[i],rowdeg[j]))
    for i in range(n):
        for j in range(i+1,n):
            if coldeg[i] != coldeg[j]:
                total += ((cols[i]&cols[j]).bit_count() * scale
                          // min(coldeg[i],coldeg[j]))
    K = comb(m, 2)+comb(n, 2)
    return Fraction(total, scale*K)


def is_ferrers(rows, n):
    masks = sorted(rows, key=lambda x:x.bit_count(), reverse=True)
    return all((masks[i+1] & ~masks[i]) == 0
               for i in range(len(masks)-1))


def verify_shape(m, n):
    formula_max, ties, expected_types = formula(m, n)
    pattern_list = list(range(1, 1<<n))
    covered = 0
    max_seen = Fraction(-1)
    maximizer_count = 0
    signatures = set()
    winners = []
    for rows in product(pattern_list, repeat=m):
        union = 0
        for row in rows:
            union |= row
        if union != (1 << n)-1:
            continue
        covered += 1
        v = integer_nodf(rows, n)
        assert v is not None
        if v > max_seen:
            max_seen = v
            maximizer_count = 0
            signatures = set()
            winners = []
        if v == max_seen:
            maximizer_count += 1
            winners.append(rows)
    for rows in winners:
        assert is_ferrers(rows, n)
        if m <= n:
            degs = [sum(bool(x & (1<<j)) for x in rows) for j in range(n)]
        else:
            degs = [x.bit_count() for x in rows]
        signatures.add(tuple(Counter(degs)[d] for d in range(1, min(m,n)+1)))
    assert covered > 0
    assert max_seen == formula_max, (m,n, max_seen, formula_max)
    assert len(signatures) == expected_types, (m,n,signatures,expected_types)
    for sig in signatures:
        q, r = divmod(max(m,n),min(m,n))
        assert all(c in (q,q+1) for c in sig)
        assert sum(c == q+1 for c in sig) == r
    census.append((m,n,covered,str(max_seen),maximizer_count,len(signatures)))


census=[]
for a,b in [(2,2),(2,3),(2,4),(2,5),(2,6),
            (3,3),(3,4),(3,5),(3,6),(4,4)]:
    for chosen in combinations(range(1,a+1), b%a):
        rows,degs = canonical_ferrers(a,b,chosen)
        assert integer_nodf(rows, b) == formula(a,b)[0]
    verify_shape(a,b)

for a in range(2,15):
    for b in range(a,60):
        optimum,tie,types = formula(a,b)
        assert 0 <= optimum <= 1
        assert types == comb(a,b%a)
        assert (optimum == 1) if a == b else (optimum < 1)
        if b < 24:
            for chosen in combinations(range(1,a+1), b%a):
                rows, _ = canonical_ferrers(a,b,chosen)
                assert integer_nodf(rows,b)==optimum

print('VERIFY_OK')
for m,n,checked,optimum,extremizers,classes in census:
    print('EXHAUSTIVE',m,n,'matrices',checked,'maximum',optimum,
          'labeled_extremizers',extremizers,'types',classes)
