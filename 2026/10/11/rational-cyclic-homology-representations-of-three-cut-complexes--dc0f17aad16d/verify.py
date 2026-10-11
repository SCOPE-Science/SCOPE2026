#!/usr/bin/env python3
"""Independent exact finite checks for cyclic actions on 3-cut complexes of cycle powers.

Run with Python 3 standard library. Tests are finite corroboration, not an
independent proof of the stated all-parameter theorem.
"""
from collections import Counter
from itertools import combinations
from math import comb, gcd


def graph_adjacent(n, p, a, b):
    d = abs(a-b)
    return a != b and min(d, n-d) <= p


def dual_face(n, p, face):
    # A subset belongs to the Alexander dual iff every triple induces a
    # connected graph. Such a triple has at least two of its three edges.
    for triple in combinations(face, 3):
        if sum(graph_adjacent(n, p, a, b) for a, b in combinations(triple, 2)) < 2:
            return False
    return True


def enumerate_dual(n, p):
    faces = [()]
    for v in range(n):
        faces += [face + (v,) for face in tuple(faces) if dual_face(n, p, face + (v,))]
    return faces


def permutation_sign(order):
    return -1 if sum(order[i] > order[j] for i in range(len(order))
                     for j in range(i+1, len(order))) % 2 else 1


def fixed_signed_lefschetz(faces, n, shift, reduced=False):
    acc = -1 if reduced else 0
    for face in faces:
        if not face:
            continue
        rotated = [(v + shift) % n for v in face]
        if set(rotated) != set(face):
            continue
        index = {v:i for i,v in enumerate(face)}
        sign = permutation_sign([index[v] for v in rotated])
        acc += (-1 if len(face) % 2 == 0 else 1) * sign
    return acc


def predicted_betti(n, p):
    return 1 + n*(n-4*p-1)//2


def predicted_dual_trace(n, p, step):
    if step % n == 0:
        return predicted_betti(n,p)
    if n % 2 == 0 and step % n == n//2:
        return 1 - n//2
    return 1


def cyclic_orientation(n, step):
    return (-1)**(n-gcd(n, step))


def check_chain_betti_one(n, faces):
    # A connected 1-skeleton has H^1 over F_2 of rank
    # number_of_edges - (n-1) - rank(boundary_2). Every two vertices are
    # faces. Gaussian elimination on integer bitsets is exact mod 2.
    edges = list(combinations(range(n), 2))
    lookup = {edge:i for i,edge in enumerate(edges)}
    pivots = {}
    for face in faces:
        if len(face)!=3:
            continue
        b = 0
        for edge in combinations(face, 2):
            b ^= 1 << lookup[edge]
        while b:
            k = b.bit_length()-1
            if k in pivots:
                b ^= pivots[k]
            else:
                pivots[k] = b
                break
    return len(edges) - (n-1) - len(pivots)


def all_cut_faces(n,p):
    # Cut facets are complements of disconnected vertex triples.
    good_triples = []
    for tri in combinations(range(n), 3):
        if sum(graph_adjacent(n,p,a,b) for a,b in combinations(tri,2)) <= 1:
            good_triples.append(sum(1<<v for v in tri))
    full=(1<<n)-1
    facets = [full ^ tri for tri in good_triples]
    out = [()]
    for mask in range(1, 1<<n):
        if any((mask & facet) == mask for facet in facets):
            out.append(tuple(v for v in range(n) if (mask>>v)&1))
    return out


def verify():
    dual_test_count=0
    rotation_test_count=0
    betti_test_count=0
    cut_test_count=0
    for p in (2,3,4):
        lo=6*p-3
        for n in range(lo,lo+4):
            faces=enumerate_dual(n,p)
            assert () in faces
            assert len([s for s in faces if len(s)==1]) == n
            assert len([s for s in faces if len(s)==2]) == comb(n,2)
            # A topological invariant calculated from exact chain ranks,
            # entirely separately from the published sphere count.
            b=check_chain_betti_one(n,faces)
            assert b==predicted_betti(n,p), (n,p,b,predicted_betti(n,p))
            betti_test_count+=1
            counts=Counter(len(f) for f in faces)
            assert (sum((-1)**(size-1)*num for size,num in counts.items() if size)
                    == 1-predicted_betti(n,p))
            for s in range(1,n):
                trace_h1=1-fixed_signed_lefschetz(faces,n,s)
                expected=predicted_dual_trace(n,p,s)
                assert trace_h1==expected,(n,p,s,trace_h1,expected)
                rotation_test_count+=1
            dual_test_count+=len(faces)
    # Independently examine the original cut complex (no Alexander dual
    # construction), including equivariant simplex-orientation signs.
    for n,p in ((9,2),(10,2),(11,2),(12,2)):
        faces=all_cut_faces(n,p)
        for s in range(n):
            red_l=fixed_signed_lefschetz(faces,n,s,reduced=True)
            top_char=(-1)**(n-4)*red_l
            expectation=cyclic_orientation(n,s)*predicted_dual_trace(n,p,s)
            assert top_char==expectation,(n,p,s,top_char,expectation)
            cut_test_count+=1
    # Representation reconstruction check: integer characters of all
    # group elements, and dimensions of regular/induced summands.
    for p in range(2,7):
        for n in range(6*p-3,6*p+18):
            beta=predicted_betti(n,p)
            if n%2:
                a=(n-4*p-1)//2
                assert a>=0 and 1+n*a==beta
                char=lambda s: (1+n*a if s==0 else 1)
            else:
                b=n//2-2*p-1
                assert b>=0 and 1+n*b+n//2==beta
                char=lambda s: (1+n*b+n//2 if s==0 else
                                1-n//2 if s==n//2 else 1)
            for s in range(n):
                assert char(s)==predicted_dual_trace(n,p,s)
    print('VERIFY_OK dual_faces=%d dual_rotations=%d mod2_betti=%d direct_cut_actions=%d' %
          (dual_test_count,rotation_test_count,betti_test_count,cut_test_count))


if __name__=='__main__':
    verify()
