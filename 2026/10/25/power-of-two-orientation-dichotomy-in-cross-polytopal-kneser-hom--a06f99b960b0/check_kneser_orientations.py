#!/usr/bin/env python3
"""Exact finite tests for cross-polytopal Kneser homology orientations.

Run with Python 3; uses only the standard library. Finite checks supplement,
not replace, the proof valid for all allowed parameters.
"""
from itertools import combinations
from math import comb


def flipped_face(n):
    ground = set(range(2*n))
    old = list(combinations(range(2*n-1),n))
    A = tuple(range(n))
    B = (0,)+tuple(range(n,2*n-1))
    assert A in old and B in old
    face = [tuple(s) for s in old if s != A and s != B]
    face += [tuple(sorted(ground - set(A))), tuple(sorted(ground - set(B)))]
    return list(map(frozenset,face))


def sign_of_permutation(images):
    seen=set(); cycles=0
    for i in range(len(images)):
        if i not in seen:
            cycles+=1; t=i
            while t not in seen:
                seen.add(t); t=images[t]
    return -1 if (len(images)-cycles)%2 else 1


def local_degree(n):
    ground=frozenset(range(2*n)); vertices=list(combinations(ground,n))
    vertices.sort(); index={s:i for i,s in enumerate(vertices)}
    perm={0:1,1:0}
    move=lambda S:tuple(sorted(perm.get(i,i) for i in S))
    vertex_sign=sign_of_permutation([index[move(s)] for s in vertices])
    pairs=[]; seen=set()
    for S in vertices:
        if S in seen: continue
        C=tuple(sorted(ground-set(S)))
        pairs.append(frozenset((S,C)))
        seen.update((S,C))
    idx={P:i for i,P in enumerate(pairs)}
    psign=sign_of_permutation([idx[frozenset((move(a),move(b)))] for a,b in [tuple(P) for P in pairs]])
    return vertex_sign*psign,vertex_sign,psign


def check_faces(n,m):
    assert m>=2*n
    face=flipped_face(n)
    assert len(face)==comb(2*n,n)//2
    assert len(set.union(*map(set,face)))==2*n
    assert all(A & B for A,B in combinations(face,2))
    ground=range(m)
    tested=0
    for T in combinations(ground,2*n):
        mapping=dict(enumerate(T))
        F={frozenset(mapping[x] for x in A) for A in face}
        assert len(F)==len(face)
        assert set().union(*F)==set(T)
        for B in combinations(ground,n):
            B=frozenset(B)
            if B not in F:
                assert any(B.isdisjoint(A) for A in F), (n,m,T,B)
            tested+=1
    return tested,comb(m,2*n)


def char_induced(n,m,cycles):
    # A fixed support must be a union of cycles; its internal sign is a
    # product of (-1)^(cyclelength-1) if n-1 is a power of two.
    exponent=int((n-1)&(n-2)==0)
    v=[0]*(2*n+1);v[0]=1
    for length in cycles:
        for j in range(2*n,length-1,-1):
            v[j]+=((-1)**((length-1)*exponent))*v[j-length]
    return v[2*n]


def main():
    checks=0
    for n in range(3,7):
        direct,v,p=local_degree(n)
        predicted=-1 if (n-1)&(n-2)==0 else 1
        assert direct==predicted,(n,direct,predicted)
        checks+=1
        print('orientation',n,'degree',direct,'vertex_sign',v,'pairs_sign',p,
              'central_binomial_half',comb(2*n-2,n-1)//2)
    for n,m in ((3,6),(3,7),(3,8),(4,8),(4,9),(5,10)):
        tested,supports=check_faces(n,m)
        checks+=tested
        print('maximal_witnesses',n,m,'supports',supports,'candidates_tested',tested)
    for n,m in ((3,6),(3,7),(3,8),(4,8),(4,9)):
        for cyc in ((1,)*m,(2,)+(1,)*(m-2),(3,)+(1,)*(m-3),
                    (2,2)+(1,)*(m-4),(m,)):
            val=char_induced(n,m,cyc)
            assert isinstance(val,int)
            print('character',n,m,cyc,val)
            checks+=1
    print('KNESER_CROSSPOLYTOPE_ORIENTATION_CHECKS_OK',checks)

if __name__=='__main__':main()
