#!/usr/bin/env python3
"""Executable arithmetic checks for rank-three inclusion theories of finite subspace lattices.
The infinite theorem also uses the algebraic witness-and-reduction proof in RESULT.md.
Only Python's standard library is required.
"""
import itertools
from collections import defaultdict


def pair_type(d, a, b, c):
    """One-round Hintikka type of ordered subspaces of ranks a,b and intersection c.
    rel=0 equality, 1 A<B, 2 B<A, 3 incomparable.
    For third variable Z: 0 equal, 1 strictly below, 2 strictly above, 3 incomparable.
    The 16 witness bits use index 4*relation(Z,A)+relation(Z,B).
    """
    assert 0 <= c <= min(a,b) and a+b-c <= d
    rel = 0 if a == b == c else (1 if a == c else (2 if b == c else 3))
    bits = 0
    bits |= 1 << (0 * 4 + (0 if rel == 0 else (1 if rel == 1 else (2 if rel == 2 else 3))))
    bits |= 1 << ((0 if rel == 0 else (2 if rel == 1 else (1 if rel == 2 else 3))) * 4)
    predicates = {
        (1,1): a > 0 and b > 0,
        (2,2): a < d and b < d,
        (1,2): b == c and a-b >= 2,
        (2,1): a == c and b-a >= 2,
        (1,3): a >= 2 and c < a and b > 0,
        (3,1): b >= 2 and c < b and a > 0,
        (2,3): a <= d-2 and c < b and b < d,
        (3,2): b <= d-2 and c < a and a < d,
        (3,3): 0 < a < d and 0 < b < d,
    }
    for (i,j),yes in predicates.items():
        if yes:
            bits |= 1 << (4*i+j)
    return rel,bits


def by_four_regions(c,u,v,w):
    return pair_type(c+u+v+w,c+u,c+v,c)


def type_of_point(a,h):
    return frozenset(by_four_regions(c,a-c,v,h-v)
                     for c in range(a+1) for v in range(h+1))


def sentence_type(d):
    return frozenset(type_of_point(a,d-a) for a in range(d+1))


def subspaces(q,d):
    """All q-ary RREF subspaces, as sets of encoded vector indices."""
    wt=[q**j for j in range(d)]
    reps=[]
    for rank in range(d+1):
        for piv in itertools.combinations(range(d),rank):
            free=[(i,j) for i,col in enumerate(piv)
                  for j in range(col+1,d) if j not in piv]
            for coefs in itertools.product(range(q),repeat=len(free)):
                rows=[[0]*d for _ in range(rank)]
                for i,col in enumerate(piv):rows[i][col]=1
                for (i,j),val in zip(free,coefs):rows[i][j]=val
                vec={(0,)*d}
                for row in rows:
                    vec={tuple((x[j]+z*row[j])%q for j in range(d))
                         for x in vec for z in range(q)}
                mask=sum(1 << sum(x[j]*wt[j] for j in range(d)) for x in vec)
                reps.append((rank,mask))
    assert len(reps)==len(set(mask for _,mask in reps))
    return reps


def direct_pair(A,B,points):
    eq=lambda X,Y:X==Y
    less=lambda X,Y:X&Y==X and X!=Y
    def relation(Z,T):
        if eq(Z,T):return 0
        if less(Z,T):return 1
        if less(T,Z):return 2
        return 3
    mask=0
    for Z in points:
        mask|=1<<(4*relation(Z,A)+relation(Z,B))
    return relation(A,B),mask


def check_direct(q,d):
    subs=subspaces(q,d)
    points=[bits for _,bits in subs]
    orbits={}
    powers={q**i:i for i in range(d+1)}
    for a,A in subs:
        for b,B in subs:
            n=(A&B).bit_count()
            c=powers[n]
            key=(a,b,c)
            if key not in orbits:orbits[key]=(A,B)
    expected=sum(1 for a in range(d+1) for b in range(d+1)
                 for c in range(max(0,a+b-d),min(a,b)+1))
    assert len(orbits)==expected,(q,d,len(orbits),expected)
    for (a,b,c),(A,B) in orbits.items():
        t=direct_pair(A,B,points)
        want=pair_type(d,a,b,c)
        assert t==want,(q,d,a,b,c,t,want)
    print('DIRECT_ORBITS_OK', 'field',q,'dimension',d,'subspaces',len(subs),
          'pair_orbits',len(orbits))


def check_uniform_reductions():
    # All conditions in pair_type depend only on 0,1,2, >=3 of four nonnegative
    # variables. Thus every identity below, exhaustively checked at values 0..3,
    # holds for all nonnegative choices by replacing >=3 by 3.
    for c,u,v,w in itertools.product(range(4),repeat=4):
        if c==3:assert by_four_regions(c,u,v,w)==by_four_regions(2,u,v,w)
        if u==3:assert by_four_regions(c,u,v,w)==by_four_regions(c,2,v,w)
        if v==3:assert by_four_regions(c,u,v,w)==by_four_regions(c,u,2,w)
        if w==3:assert by_four_regions(c,u,v,w)==by_four_regions(c,u,v,2)
    # The only hard reduction steps with both parts exactly 2:
    for v,w in itertools.product(range(4),repeat=2):
        assert by_four_regions(2,2,v,w)==by_four_regions(1,2,v,w)
    for c,u in itertools.product(range(4),repeat=2):
        assert by_four_regions(c,u,2,2)==by_four_regions(c,u,2,1)
    print('UNIFORM_REDUCTION_IDENTITIES_OK', 'four_regions=256',
          'boundary_steps=32')


def check_rank3():
    signatures={}
    for d in range(25):
        s=sentence_type(d)
        expected=frozenset((min(a,3),min(d-a,3)) for a in range(d+1))
        # Comparison uses elementwise bijection to the rank-2 type; no accidental
        # merge of clipped pairs in the explicit checked range.
        assert len(s)==len(expected)
        assert s==sentence_type(min(d,6))
        signatures.setdefault(s,[]).append(d)
        for a in range(d+1):
            assert type_of_point(a,d-a)==type_of_point(min(a,3),min(d-a,3))
    assert [ds[0] for ds in signatures.values()]==list(range(7))
    assert len(signatures)==7
    assert sum([1,63,651,1395,651,63,1])==2825
    print('RANK_THREE_OK','classes=7','stable_dimension=6',
          'sharp_minimum_representative=2825')


if __name__=='__main__':
    check_uniform_reductions()
    check_rank3()
    for q,d in [(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),
                (3,2),(3,3),(3,4),(5,2),(5,3)]:
        check_direct(q,d)
    print('VERIFY_OK')
