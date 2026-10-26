#!/usr/bin/env python3
"""Exact four-quantifier-rank profiles of finite binary hypercube graphs.

The recurrence is a finite orbit version of ordinary first-order Hintikka
profiles (not a counting or finite-variable logic). No external packages.
"""
import hashlib
from functools import lru_cache
from itertools import product


def clip_distance(d):
    return 0 if d == 0 else 1 if d == 1 else 2


def atomic(distances):
    code = 0
    for d in distances:
        code = 3 * code + clip_distance(d)
    return code


@lru_cache(maxsize=None)
def triple_rank1(c):
    a, b, e, f = c
    d12, d13, d23 = e+f, b+f, b+e
    children = set()
    for y0 in range(a+1):
        for y1 in range(b+1):
            for y2 in range(e+1):
                for y3 in range(f+1):
                    # yj is the number of y-bits equal to one in the
                    # four coordinate classes (x2,x3)=00,01,10,11.
                    d14 = y0 + y1 + y2 + y3
                    d24 = y0 + y1 + e-y2 + f-y3
                    d34 = y0 + b-y1 + y2 + f-y3
                    children.add(atomic((d12,d13,d14,d23,d24,d34)))
    return atomic((d12,d13,d23)), tuple(sorted(children))


@lru_cache(maxsize=None)
def pair_rank2(c):
    same, different = c
    children = {
        triple_rank1((same-j,j,different-k,k))
        for j in range(same+1)
        for k in range(different+1)
    }
    return atomic((different,)), tuple(sorted(children))


def vertex_rank3(d):
    return tuple(sorted({pair_rank2((d-k,k)) for k in range(d+1)}))


def signature(d):
    # A single orbit of starting vertices, hence the vertex rank-3
    # profile determines the complete rank-4 sentence profile.
    return vertex_rank3(d)


def direct_atom(vertices):
    ds = ((u^v).bit_count() for i,u in enumerate(vertices) for v in vertices[i+1:])
    return atomic(ds)


def column_counts(x,y,z,d):
    counts = [0,0,0,0]
    for i in range(d):
        column = ((((y^x)>>i)&1)<<1) | (((z^x)>>i)&1)
        counts[column] += 1
    return tuple(counts)


def independent_crosscheck():
    # Graph-level enumeration rather than the split recurrence:
    # every ordered triple and extension in Q_1,...,Q_6; also every
    # ordered pair and its extension-rank type.
    for d in range(1,7):
        n = 1 << d
        for x,y,z in product(range(n),repeat=3):
            expected = (
                direct_atom((x,y,z)),
                tuple(sorted({direct_atom((x,y,z,w)) for w in range(n)}))
            )
            assert triple_rank1(column_counts(x,y,z,d)) == expected
        for x,y in product(range(n),repeat=2):
            k=(x^y).bit_count()
            expected = (
                direct_atom((x,y)),
                tuple(sorted({triple_rank1(column_counts(x,y,z,d)) for z in range(n)}))
            )
            assert pair_rank2((d-k,k)) == expected
        print(f"DIRECT_CROSSCHECK_OK d={d} triples={n**3} pairs={n**2}")


def check():
    # By the two-way coordinate-splitting lemma, rank-r types
    # depend only on coordinate-class counts truncated at 2^(r+1).
    # Thus dimensions >=16 share one vertex rank-3 type. The loop
    # below decides the remaining finite cases exactly.
    rep_for = {}
    rows=[]
    for d in range(1,18):
        sig=signature(d)
        rep_for.setdefault(sig,d)
        representative=rep_for[sig]
        rows.append((d,representative))
        fingerprint=hashlib.sha256(repr(sig).encode('ascii')).hexdigest()
        print(f"d={d:2d} representative={representative} vertex_profile_size={len(sig)} sha256={fingerprint}")
    assert rows == [(d,d if d<=5 else 6) for d in range(1,18)],rows
    assert len(rep_for)==6
    # More explicit dimension-independent pair-type table after d>=6.
    # Pair profiles depend only on whether their Hamming distance is
    # 0,1,2,3,4 or at least 5.
    base=[pair_rank2((6-k,k)) for k in range(7)]
    assert base[5]==base[6]
    assert len(set(base))==6
    for d in range(6,18):
        assert [pair_rank2((d-k,k)) for k in range(d+1)] == base[:5]+[base[5]]*(d-4)
    print('FINITE_PROFILE_CLASSIFICATION_OK classes=6 stabilization_dimension=6')
    independent_crosscheck()
    print('VERIFY_OK')


if __name__=='__main__':
    check()
