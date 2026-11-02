#!/usr/bin/env python3
"""Exact finite chain certificate for a Petersen matching-complex symmetry theorem.
No external packages. Run: python3 petersen_matching_s5_verify.py
"""
from itertools import combinations
from collections import defaultdict, Counter
from fractions import Fraction
from math import factorial, gcd, lcm

FIVE = range(5)
VERTICES = tuple(combinations(FIVE, 2))
EDGES = tuple((a,b) for a,b in combinations(range(10),2)
              if set(VERTICES[a]).isdisjoint(VERTICES[b]))
FACES = {d:tuple(t for t in combinations(range(len(EDGES)), d+1)
          if all(set(EDGES[a]).isdisjoint(EDGES[b])
                 for a,b in combinations(t,2))) for d in range(5)}
assert tuple(len(FACES[d]) for d in range(5)) == (15,75,145,90,6)


def representative(partition):
    p=list(FIVE); at=0
    for size in partition:
        block=list(range(at,at+size));at+=size
        for a,b in zip(block,block[1:]+block[:1]):p[a]=b
    return tuple(p)


def induced_edge_permutation(g):
    vertex={v:i for i,v in enumerate(VERTICES)}
    vperm=[vertex[tuple(sorted((g[a],g[b])))] for a,b in VERTICES]
    edge={e:i for i,e in enumerate(EDGES)}
    return tuple(edge[tuple(sorted((vperm[a],vperm[b])))] for a,b in EDGES)


def act(face, edge_perm):
    mapped=[edge_perm[e] for e in face]
    inversions=sum(mapped[i]>mapped[j] for i in range(len(mapped))
                   for j in range(i+1,len(mapped)))
    return tuple(sorted(mapped)), -1 if inversions%2 else 1


def invariant_orbit_bases(g,d):
    edgeperm=induced_edge_permutation(g)
    unseen=set(FACES[d]); out=[]
    while unseen:
        initial=min(unseen); cur=initial;sgn=1; orbit=[]
        while cur in unseen:
            orbit.append((cur,sgn));unseen.remove(cur)
            cur,edge_sign=act(cur,edgeperm);sgn*=edge_sign
        assert cur == initial
        if sgn == 1:
            out.append((initial,orbit))
    return out


def sparse_fraction_rank(columns):
    """Gauss elimination over Q on column dictionaries, normalized sparse pivots."""
    pivots={}
    for c in columns:
        v={i:Fraction(x) for i,x in c.items() if x}
        while v:
            r=min(v)
            if r not in pivots:
                scale=v[r]
                pivots[r]={i:x/scale for i,x in v.items()}
                break
            multiple=v[r]
            for i,x in pivots[r].items():
                y=v.get(i,0)-multiple*x
                if y: v[i]=y
                elif i in v: del v[i]
    return len(pivots)


def chain_data(g):
    bs=[invariant_orbit_bases(g,d) for d in range(5)]
    sizes=[len(b) for b in bs]
    ranks=[0]
    for d in range(1,5):
        destination={face:i for i,(face,_) in enumerate(bs[d-1])}
        columns=[]
        for rep,orbit in bs[d]:
            counts=Counter()
            for face,weight in orbit:
                for k in range(len(face)):
                    counts[face[:k]+face[k+1:]]+=weight*(-1)**k
            columns.append({row:counts[face] for face,row in destination.items()
                            if counts[face]})
        ranks.append(sparse_fraction_rank(columns))
    ranks.append(0)
    betti=[sizes[d]-ranks[d]-ranks[d+1] for d in range(5)]
    return tuple(sizes),tuple(ranks),tuple(betti)


def signed_face_trace(g,d):
    edgeperm=induced_edge_permutation(g)
    return sum(sign for face in FACES[d]
               for mapped,sign in (act(face,edgeperm),) if mapped==face)


def character_h2(g):
    inversion=sum(g[i]>g[j] for i in FIVE for j in range(i+1,5))
    return (-1 if inversion%2 else 1) * sum(g[i]==i for i in FIVE)


def character_h3(g):
    f=sum(g[i]==i for i in FIVE)
    square=tuple(g[g[i]] for i in FIVE)
    f2=sum(square[i]==i for i in FIVE)
    assert ((f-1)**2+f2-1)%2 == 0
    return ((f-1)**2+f2-1)//2-f


def invariant_from_character(g, fun):
    cur=tuple(FIVE); orbit=[]
    while True:
        orbit.append(fun(cur))
        cur=tuple(g[cur[i]] for i in FIVE)
        if cur==tuple(FIVE):break
    assert sum(orbit)%len(orbit)==0
    return sum(orbit)//len(orbit)


def cycle_classes():
    return [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),
            (3,2),(4,1),(5,)]


def cycle_type(g):
    seen=set();lengths=[]
    for i in FIVE:
        if i in seen:continue
        x=i;steps=0
        while x not in seen:
            seen.add(x);steps+=1;x=g[x]
        lengths.append(steps)
    return tuple(sorted(lengths,reverse=True))


def power(g,k):
    q=tuple(FIVE)
    for _ in range(k):q=tuple(g[q[i]] for i in FIVE)
    return q


def recovered_characters(invariant_betti_by_class):
    chars={}
    for part in sorted(cycle_classes(),key=lambda p:(lcm(*p),p)):
        g=representative(part); order=lcm(*part)
        inv=invariant_betti_by_class[part]
        if order==1:
            chars[part]=(inv[2],inv[3]);continue
        primitive=sum(gcd(j,order)==1 for j in range(order))
        known=[chars[cycle_type(power(g,j))]
               for j in range(order) if gcd(j,order)>1]
        actual=tuple((order*inv[d]-sum(row[d-2] for row in known))//primitive
                     for d in (2,3))
        assert all((order*inv[d]-sum(row[d-2] for row in known))%primitive==0 for d in (2,3))
        chars[part]=actual
    return chars


def main():
    print('PETERSEN_MATCHING_S5_CERTIFICATE_V1')
    print('face_vector',tuple(len(FACES[d]) for d in range(5)))
    print('class | invariant_chain_sizes | boundary_ranks | invariant_betti | (chi2,chi3) | fixed_signed_lefschetz')
    all_betti={}
    for part in cycle_classes():
        g=representative(part)
        size,ranks,betti=chain_data(g)
        all_betti[part]=betti
        c2=character_h2(g);c3=character_h3(g)
        assert betti==(1,0,invariant_from_character(g,character_h2),
                       invariant_from_character(g,character_h3),0),(part,betti)
        lefschetz=sum((-1)**d*signed_face_trace(g,d) for d in range(5))
        assert lefschetz==1+c2-c3,(part,lefschetz,1+c2-c3)
        print(part,size,ranks,betti,(c2,c3),lefschetz)
    recovered=recovered_characters(all_betti)
    for part in cycle_classes():
        prediction=(character_h2(representative(part)),character_h3(representative(part)))
        assert recovered[part]==prediction,(part,recovered[part],prediction)
    print('characters_recovered_from_cyclic_invariant_chain_ranks',recovered)
    assert all(character_h2(representative(part)) for part in [(1,1,1,1,1),(2,1,1,1)])
    # Trivial component under S5 is 0 in both degrees: average both characters over all 120 permutations.
    from itertools import permutations
    chars=[(character_h2(g),character_h3(g)) for g in permutations(FIVE)]
    assert len(chars)==factorial(5)
    assert tuple(sum(c[d] for c in chars) for d in (0,1))==(0,0)
    even=[c for g,c in zip(permutations(FIVE),chars)
          if sum(g[i]>g[j] for i in FIVE for j in range(i+1,5))%2==0]
    assert len(even)==60
    assert tuple(sum(c[d] for c in even)//len(even) for d in (0,1))==(1,0)
    print('S5_quotient_reduced_rational_betti_2_3',(0,0))
    print('A5_quotient_reduced_rational_betti_2_3',(1,0))
    print('PETERSEN_MATCHING_S5_EXACT_OK')

if __name__=='__main__':main()
