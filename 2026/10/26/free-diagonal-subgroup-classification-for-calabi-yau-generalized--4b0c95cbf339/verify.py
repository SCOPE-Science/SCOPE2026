#!/usr/bin/env python3
"""Exact finite checks for free diagonal subgroups of generalized Fermat complete intersections."""
from collections import Counter
from itertools import product, permutations
from math import comb, factorial


def gl_matrices(p, r):
    if r == 1:
        return [((a,),) for a in range(1, p)]
    if r == 2:
        return [((a, b), (c, d)) for a, b, c, d in product(range(p), repeat=4)
                if (a*d-b*c) % p]
    if (p, r) == (2, 3):
        # Three linearly independent columns, enumerated without a determinant library.
        out=[]
        vectors=list(product(range(2),repeat=3))
        for a,b,c in product(vectors,repeat=3):
            span={(0,0,0),a,b,tuple((x+y)%2 for x,y in zip(a,b))}
            if len(span)==4 and c not in span:
                out.append(tuple(tuple(col[i] for col in (a,b,c)) for i in range(3)))
        return out
    raise NotImplementedError


def gaussian_order(p, r):
    v=1
    for i in range(r):
        v *= p**r-p**i
    return v


def affine_permutations(p, r):
    vectors=list(product(range(p),repeat=r))
    idx={v:i for i,v in enumerate(vectors)}
    affine=[]
    for mat in gl_matrices(p,r):
        for b in vectors:
            affine.append(tuple(idx[tuple((sum(mat[i][j]*v[j] for j in range(r))+b[i])%p
                                              for i in range(r))] for v in vectors))
    assert len(affine)==p**r*gaussian_order(p,r)
    assert len(set(affine))==len(affine)
    return vectors,affine


def orbit_count_once(p,r):
    # At t=p^(r-1), every character occurs exactly once.
    alphabet=list(range(p**r))
    chars,aff=affine_permutations(p,r)
    seen=set(); orbits=0
    for word in permutations(alphabet):
        if word in seen:
            continue
        orbits+=1
        orbit={tuple(g[x] for x in word) for g in aff}
        assert len(orbit)==len(aff)
        seen.update(orbit)
    assert len(seen)==factorial(len(alphabet))
    return orbits


def fixed_point_free_character_array(p,r,t):
    chars=list(product(range(p),repeat=r))
    m=t//p**(r-1)
    word=chars*m
    for g in chars[1:]:
        histogram=Counter(sum(x*y for x,y in zip(alpha,g))%p for alpha in word)
        assert all(histogram[z]==t for z in range(p))


def main():
    assert orbit_count_once(3,2)==840
    assert orbit_count_once(2,3)==30
    assert orbit_count_once(2,2)==1
    # For cyclic groups at t=3, count balanced words modulo affine relabeling.
    assert factorial(9)//(factorial(3)**3*3*2)==280
    assert comb(6,3)//2==10
    fixed_point_free_character_array(3,2,3)
    fixed_point_free_character_array(2,3,4)
    fixed_point_free_character_array(2,1,3)
    # Smooth complete intersection of three cubics in projective eight-space.
    p,t=3,3; N=p*t; d=(p-1)*t-1
    chern=sum(comb(N,d-j)*(-p)**j*comb(t+j-1,j) for j in range(d+1))
    assert chern==-360
    euler=chern*p**t
    assert euler==-9720 and euler//9==-1080
    print('VERIFY_OK: AGL orbit counts 840/30/1; cyclic counts 280/10; free arrays and Euler -1080')

if __name__=='__main__':
    main()
