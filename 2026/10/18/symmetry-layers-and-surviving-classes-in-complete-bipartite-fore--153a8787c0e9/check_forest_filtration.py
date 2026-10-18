#!/usr/bin/env python3
"""Finite signed-chain checks for bipartite induced-forest filtrations.

All computations use ordered integer-labelled vertices and exact finite-field
elimination. The infinite-family statement requires the separate proof.
"""
from itertools import permutations
from math import comb, factorial


def faces_by_degree(a, b, d):
    n = a + b
    bydeg = {-1: [()]}
    for mask in range(1, 1 << n):
        s = tuple(i for i in range(n) if mask & (1 << i))
        na = sum(i < a for i in s)
        nb = len(s) - na
        if na and nb:
            if d == 0 or (na != 1 and nb != 1) or max(na, nb) > d:
                continue
        bydeg.setdefault(len(s) - 1, []).append(s)
    return bydeg


def sparse_rank(columns, p):
    pivots = {}
    for col in columns:
        v = {i: x % p for i, x in col.items() if x % p}
        while v:
            k = max(v)
            if k not in pivots:
                inv = pow(v[k], -1, p)
                pivots[k] = {r: x * inv % p for r, x in v.items()}
                break
            factor = v[k]
            for r, x in pivots[k].items():
                y = (v.get(r, 0) - factor * x) % p
                if y:
                    v[r] = y
                else:
                    v.pop(r, None)
    return len(pivots)


def betti(a, b, d, prime):
    fs = faces_by_degree(a, b, d)
    top = max(fs)
    rank = {}
    for k in range(0, top + 1):
        target = {f: i for i, f in enumerate(fs.get(k-1, []))}
        cols = []
        for s in fs.get(k, []):
            cols.append({target[s[:i]+s[i+1:]]: (-1) ** i
                         for i in range(len(s))})
        rank[k] = sparse_rank(cols, prime)
    rank[top+1] = 0
    return {k: len(fs.get(k, [])) - rank.get(k, 0) - rank.get(k+1, 0)
            for k in range(top+1) if len(fs.get(k, [])) - rank.get(k, 0) - rank.get(k+1, 0)}


def persistent_rectangle_rank(a,b,prime):
    """Rank of explicit four-cycle sphere classes in H_2(F_3)."""
    fs2 = faces_by_degree(a,b,2)
    fs3 = faces_by_degree(a,b,3)
    assert all(face in set(fs3.get(2,[])) for face in fs2.get(2,[]))
    idx={s:i for i,s in enumerate(fs3.get(2,[]))}
    boundaries=[]
    for face in fs3.get(3,[]):
        boundaries.append({idx[face[:i]+face[i+1:]]:(-1)**i
                           for i in range(4)})
    rank_boundary=sparse_rank(boundaries,prime)
    rectangles=[]
    for ai in range(1,a):
        for bj in range(1,b):
            simplex=(0,ai,a,a+bj)
            assert tuple(sorted(simplex))==simplex
            rectangles.append({idx[simplex[:i]+simplex[i+1:]]:(-1)**i
                               for i in range(4)})
    rank_with=sparse_rank(boundaries+rectangles,prime)
    assert rank_with-rank_boundary==(a-1)*(b-1), (a,b,prime)
    return rank_with-rank_boundary


def permutation_wedge_character(perm):
    n = len(perm)
    seen = set()
    coeff = [1]
    for i in range(n):
        if i in seen:
            continue
        length = 0
        j = i
        while j not in seen:
            seen.add(j)
            j = perm[j]
            length += 1
        term = [1] + [0]*(length-1) + [-(-1)**length]
        c = [0]*(len(coeff)+len(term)-1)
        for k, x in enumerate(coeff):
            for h, y in enumerate(term):
                c[k+h] += x*y
        coeff = c
    quotient = []
    for x in coeff:
        quotient.append(x - (quotient[-1] if quotient else 0))
    assert quotient[-1] == 0
    return quotient[:-1]


def inversion_sign(seq):
    parity = sum(seq[i] > seq[j] for i in range(len(seq))
                 for j in range(i+1, len(seq))) % 2
    return -1 if parity else 1


def lefschetz(a,b,d,p,q):
    action = p + tuple(a+i for i in q)
    fs = faces_by_degree(a,b,d)
    value = -1  # reduced empty face contribution
    for k, faces in fs.items():
        if k < 0:
            continue
        for face in faces:
            image = tuple(action[v] for v in face)
            if set(image) == set(face):
                value += (-1)**k * inversion_sign(image)
    return value


def expected_betti(a,b,d):
    base = (a-1)*(b-1)
    if d == 0:
        return {0:1}
    if d == 1:
        return {1:a*b-1}
    extra = a*comb(b-1,d) + b*comb(a-1,d) if d <= min(a-1,b-1) else (a*comb(b-1,d) if d<=b-1 else 0) + (b*comb(a-1,d) if d<=a-1 else 0)
    if d == 2:
        return {2:base+extra}
    result={2:base}
    if extra:
        result[d]=extra
    return result


def run():
    for a,b in ((2,2),(2,3),(3,3),(3,4),(4,4)):
        perma=list(permutations(range(a)))
        permb=list(permutations(range(b)))
        for prime in (2,3,5):
            persistent_rectangle_rank(a,b,prime)
        for d in range(0,max(a,b)+2):
            expected=expected_betti(a,b,d)
            for prime in (2,3,5):
                observed=betti(a,b,d,prime)
                assert observed==expected, (a,b,d,prime,observed,expected)
            for p in perma:
                for q in permb:
                    fp=sum(p[i]==i for i in range(a))
                    fq=sum(q[i]==i for i in range(b))
                    ca=permutation_wedge_character(p)
                    cb=permutation_wedge_character(q)
                    if d==0:
                        expected_lef=1
                    elif d==1:
                        expected_lef=1-fp*fq
                    else:
                        hi=(fp*(cb[d] if d<len(cb) else 0)
                            +fq*(ca[d] if d<len(ca) else 0))
                        expected_lef=(fp-1)*(fq-1)+(-1)**d*hi
                    actual=lefschetz(a,b,d,p,q)
                    assert actual==expected_lef, (a,b,d,p,q,actual,expected_lef)
        print(f'a={a} b={b}: all d=0..{max(a,b)+1}, three prime homology ranks, rectangle survival, {factorial(a)*factorial(b)} signed symmetry actions per stage PASS')
    print('ALL FINITE CHECKS PASSED')

if __name__=='__main__':run()
