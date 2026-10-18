#!/usr/bin/env python3
"""Exact certificate for third-order coextinction distinguishability.

Only standard-library integer arithmetic is used. Pollinator columns can have
identical neighborhoods but are distinct vertices, with at most one link to each plant.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import comb

A = ((0,1,2),(0,3,4),(1,3,5),(2,4,5),(0,1,2))
B = ((0,1,3),(0,2,4),(1,2,5),(3,4,5),(0,1,2))


def rows_for(columns, plants):
    rows = [0] * plants
    for j, triple in enumerate(columns):
        assert len(triple) == 3 and len(set(triple)) == 3
        for plant in triple:
            rows[plant] |= 1 << j
    return tuple(rows)


def connected(rows):
    """Connectivity of a bipartite graph whose other-vertex degree is 3."""
    if any(x == 0 for x in rows):
        return False
    reached = {0}
    stack = [0]
    while stack:
        i = stack.pop()
        for j in range(len(rows)):
            if j not in reached and rows[i] & rows[j]:
                reached.add(j)
                stack.append(j)
    return len(reached) == len(rows)


def pair_signature(rows):
    """Exponents for all labeled one- and two-plant joint failure laws."""
    v = len(rows)
    return (tuple(x.bit_count() for x in rows) +
            tuple((rows[i] | rows[j]).bit_count()
                  for i in range(v) for j in range(i+1, v)))


def triple_union_hist(rows, pollinators):
    out = [0] * (pollinators+1)
    for i,j,l in combinations(range(len(rows)), 3):
        out[(rows[i] | rows[j] | rows[l]).bit_count()] += 1
    return tuple(out)


def census():
    """Every connected labeled-plant, unlabeled-pollinator 3-uniform graph."""
    for n in range(4, 11):
        counts = []
        for v in range(3, n):
            p = n-v
            blocks = tuple(combinations(range(v), 3))
            if not blocks: continue
            possible = comb(len(blocks)+p-1, p)
            enumerated = 0
            checked = 0
            signatures = {}
            for choices in combinations_with_replacement(range(len(blocks)), p):
                enumerated += 1
                cols = tuple(blocks[i] for i in choices)
                rows = rows_for(cols, v)
                if not connected(rows): continue
                checked += 1
                sig = pair_signature(rows)
                third = triple_union_hist(rows, p)
                previous = signatures.setdefault(sig, third)
                assert previous == third, (n,v,p,cols,previous,third)
            assert enumerated == possible
            if checked:
                counts.append((v,p,checked,len(signatures)))
        print('n=', n, 'connected_by_(plants,pollinators)=', counts)


def exact_distribution(columns):
    rows = rows_for(columns, 6)
    hist = Counter()
    for failure_bits in product((0,1), repeat=5):
        z = sum(all(failure_bits[j] for j in range(5)
                    if row & (1 << j)) for row in rows)
        hist[z] += 1
    return tuple(hist.get(i, 0) for i in range(7))


def moments_at_half(hist):
    den = sum(hist)
    mean = sum((i*hist[i] for i in range(len(hist))), 0) * Fraction(1,den)
    e2 = sum((i*i*hist[i] for i in range(len(hist))), 0) * Fraction(1,den)
    e3 = sum((i**3*hist[i] for i in range(len(hist))), 0) * Fraction(1,den)
    return mean, e2 - mean**2, e3 - 3*mean*e2 + 2*mean**3


def witness():
    ra, rb = rows_for(A,6), rows_for(B,6)
    assert connected(ra) and connected(rb)
    assert [len(c) for c in A] == [3]*5 == [len(c) for c in B]
    assert pair_signature(ra) == pair_signature(rb)
    assert pair_signature(ra)[:6] == (3,3,3,2,2,2)
    assert triple_union_hist(ra,5) == (0,0,0,1,3,16)
    assert triple_union_hist(rb,5) == (0,0,0,0,5,15)
    # Distinct pollinator-neighborhood twins in A, none in B:
    assert len(set(A)) == 4 and len(set(B)) == 5
    ca,cb = exact_distribution(A),exact_distribution(B)
    assert ca == (13,12,0,6,0,0,1)
    assert cb == (14,9,3,5,0,0,1)
    ea,va,ta = moments_at_half(ca)
    eb,vb,tb = moments_at_half(cb)
    assert ea == eb == Fraction(9,8)
    assert va == vb == Fraction(123,64)
    assert ta == Fraction(1095,256) and tb == Fraction(1047,256)
    assert ta-tb == Fraction(3,16)
    # Polynomial identities from exact union-size counts for all 0<q<1:
    # M3(A)-M3(B) = q^3 - 2 q^4 + q^5 = q^3(1-q)^2.
    # E(Z)_3 = 6*M3, so third central moment difference = 6*M3 difference.
    print('witness pair signature equal; third union histograms differ',
          triple_union_hist(ra,5),triple_union_hist(rb,5))
    print('half-failure distributions',ca,cb)
    print('mean=',ea, 'variance=',va, 'third central moments=',ta,tb,
          'difference=',ta-tb)

if __name__ == '__main__':
    witness()
    census()
    print('PASS: sharp 11-vertex cutoff and exact witness')
