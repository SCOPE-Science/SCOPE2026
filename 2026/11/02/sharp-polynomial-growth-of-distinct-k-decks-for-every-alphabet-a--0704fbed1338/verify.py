#!/usr/bin/env python3
"""Standalone exact checks of a positive-word construction for subsequence decks.

All arithmetic is integral or exact rational. The finite computations provide
checks of the construction, not a substitute for its all-parameter proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb


def signature(word, k):
    """Noncommutative coefficients through degree k, indexed by strings."""
    out = {'': 1}
    for letter in word:
        for subword, multiplicity in list(out.items()):
            if len(subword) < k:
                next_subword = subword + letter
                out[next_subword] = out.get(next_subword, 0) + multiplicity
    return out


def mobius(d):
    primes = 0
    p = 2
    while p * p <= d:
        if d % p == 0:
            d //= p
            if d % p == 0:
                return 0
            primes += 1
        p += 1
    if d > 1:
        primes += 1
    return (-1) ** primes


def witt(q, j):
    return sum(mobius(d) * q ** (j // d) for d in range(1, j+1) if j % d == 0) // j


def insert_if_independent(vector, pivots):
    """Exact rational incremental row-echelon test."""
    v = [Fraction(a) for a in vector]
    for p in sorted(pivots):
        if v[p]:
            multiple = v[p]
            v = [a - multiple * b for a,b in zip(v,pivots[p])]
    new_pivot = next((p for p,a in enumerate(v) if a), None)
    if new_pivot is None:
        return False
    scalar = v[new_pivot]
    pivots[new_pivot] = [a / scalar for a in v]
    return True


def pairs(q, k):
    letters = [str(i) for i in range(q)]
    result = {1: [(a, letters[-1]) for a in letters[:-1]]}
    if k >= 2:
        result[2] = [(a+b, b+a) for a,b in combinations(letters,2)]
    for j in range(3, k+1):
        monomials = [''.join(t) for t in product(letters,repeat=j)]
        pivots = {}
        chosen = []
        for u,v in result[j-1]:
            for a in letters:
                x = u+a+v
                y = v+a+u
                sx,sy = signature(x,j),signature(y,j)
                assert len(x) == len(y)
                assert all(sx.get(t,0) == sy.get(t,0)
                           for t in sx.keys() | sy.keys() if len(t)<j)
                vec = [sx.get(t,0)-sy.get(t,0) for t in monomials]
                if insert_if_independent(vec,pivots):
                    chosen.append((x,y))
        result[j] = chosen
    for j in range(1,k+1):
        assert len(result[j]) == (q-1 if j==1 else witt(q,j)), (q,j,len(result[j]))
        for u,v in result[j]:
            assert len(u)==len(v)
            su,sv=signature(u,j),signature(v,j)
            assert all(su.get(t,0)==sv.get(t,0) for t in su.keys()|sv.keys() if len(t)<j)
            assert any(su.get(t,0)!=sv.get(t,0) for t in su.keys()|sv.keys() if len(t)==j)
            # Uniform letter expansion multiplies the leading difference by m**j.
            for m in (2,3):
                um=''.join(c*m for c in u)
                vm=''.join(c*m for c in v)
                tm,tn=signature(um,j),signature(vm,j)
                for t in su.keys()|sv.keys()|tm.keys()|tn.keys():
                    if len(t)<j:
                        assert tm.get(t,0)==tn.get(t,0)
                    elif len(t)==j:
                        assert tm.get(t,0)-tn.get(t,0)==m**j*(su.get(t,0)-sv.get(t,0))
    return result


def test(q,k,R):
    chosen = pairs(q,k)
    blocks=[]
    for j in range(1,k+1):
        for u,v in chosen[j]:
            for r in range(R):
                m=2**r
                U=''.join(a*m for a in u)
                V=''.join(a*m for a in v)
                blocks.append((j,U,V,2**j-1))
    exponent=sum(j*len(chosen[j]) for j in range(1,k+1))
    total=2**(R*exponent)
    length=sum(B*len(U) for j,U,V,B in blocks)
    print(f'basis q={q} k={k}: '+','.join(f'd{j}={len(chosen[j])}' for j in chosen))
    print(f'code q={q} k={k} R={R} length={length} count={total} exponent={exponent}')
    if total <= 1000:
        observed=set()
        alphabet=[str(i) for i in range(q)]
        targets=[''.join(p) for p in product(alphabet,repeat=k)]
        for digits in product(*(range(B+1) for j,U,V,B in blocks)):
            word=''.join(V*d+U*(B-d) for (j,U,V,B),d in zip(blocks,digits))
            assert len(word)==length
            deck=signature(word,k)
            key=tuple(deck.get(t,0) for t in targets)
            assert key not in observed, (q,k,R,'k-deck collision')
            observed.add(key)
            # Exact identity recovering all lower deck entries from the k-deck.
            if len(observed)<=5:
                for j in range(1,k):
                    for p in product(alphabet,repeat=j):
                        a=''.join(p)
                        lhs=sum(deck.get(t,0)*signature(t,j).get(a,0) for t in targets)
                        rhs=comb(length-j,k-j)*deck.get(a,0)
                        assert lhs==rhs
        assert len(observed)==total
        print(f'exhaustive distinct fixed-length decks: {len(observed)} PASS')
    else:
        print('large code: basis and scaling verified; no exhaustive enumeration asserted')


def main():
    for test_case in [(2,2,2),(2,3,1),(3,2,1),(3,3,1),(2,4,1),(4,3,1)]:
        test(*test_case)
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':
    main()
