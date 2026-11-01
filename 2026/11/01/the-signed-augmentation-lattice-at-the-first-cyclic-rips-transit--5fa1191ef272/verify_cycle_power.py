#!/usr/bin/env python3
"""Standalone exact checks of the signed augmentation action in a cyclic Rips family.

No external dependencies. All integers are exact. The theorem itself uses the
cover/attachment argument in RESULT.md; finite checks are corroboration, not
an extrapolation to arbitrary parameters.
"""
from itertools import combinations
from collections import Counter


def datasets(k):
    n=3*k
    interval_facets=[frozenset((i+j)%n for j in range(k+1)) for i in range(n)]
    extra=[frozenset((a,a+k,a+2*k)) for a in range(k)]
    A=set();X=set()
    for F in interval_facets:
        z=sorted(F)
        for q in range(1,len(z)+1):
            A.update(combinations(z,q))
    X=set(A)
    for t in extra:X.add(tuple(sorted(t)))
    return n,A,X,extra


def direct_faces(k):
    n=3*k
    ans=set()
    for mask in range(1,1<<n):
        v=[i for i in range(n) if mask>>i&1]
        if all(min((j-i)%n,(i-j)%n)<=k for i,j in combinations(v,2)):
            ans.add(tuple(v))
    return ans


def lefschetz(faces,n,a,sgn):
    value=-1
    for face in faces:
        transformed=tuple((sgn*x+a)%n for x in face)
        if set(face)!=set(transformed):continue
        inversion=sum(transformed[i]>transformed[j] for i in range(len(face)) for j in range(i+1,len(face)))
        value+=(-1)**(len(face)-1+inversion)
    return value


def predicted(k,a,sgn):
    # Character on ker(e_0+...+e_{k-1} -> 1), with reflection sign.
    if sgn==1:
        permutation_fixed = k if a%k==0 else 0
    else:
        permutation_fixed = sum((2*j-a)%k==0 for j in range(k))
    return sgn*(permutation_fixed-1)


def main():
    for k in range(2,9):
        n,A,X,extra=datasets(k)
        assert len(X)==len(A)+k
        assert len(set(extra))==k
        assert all(tuple(sorted(t)) not in A for t in extra)
        euler_A=sum((-1)**(len(f)-1) for f in A)
        assert euler_A==0, (k,euler_A)
        # The new triangles each attach their three boundary edges to A.
        assert all(all(tuple(sorted(e)) in A for e in combinations(t,2)) for t in extra)
        # Exhaustively verify the clique classification for small n.
        if k<=4:assert X==direct_faces(k), k
        # Signed fixed-simplex traces equal the asserted H_2 character.
        for sign in (1,-1):
            for a in range(n):
                actual=lefschetz(X,n,a,sign)
                expected=predicted(k,a,sign)
                assert actual==expected,(k,a,sign,actual,expected)
        print(f'k={k} n={n} A_faces={len(A)} X_faces={len(X)} '
              f'nonarc_triangles={len(extra)} chi_X={sum((-1)**(len(f)-1) for f in X)} '
              f'checked_dihedral={2*n} PASS')
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
