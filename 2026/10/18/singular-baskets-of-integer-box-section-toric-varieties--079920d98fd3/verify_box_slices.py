#!/usr/bin/env python3
"""Independent finite checks for local singularity baskets of integer box sections.
This program does not certify the unbounded theorem: its finite enumerations
are cross-checks of the accompanying lattice proof.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter
from math import comb
from itertools import combinations as subset_combinations


def grid_vertices(caps,level):
    """Enumerate box-edge/hyperplane intersections independently of subset-sum classification."""
    n=len(caps); out=set()
    for free in range(n):
        remaining=[j for j in range(n) if j!=free]
        for up in product((0,1),repeat=n-1):
            pt=[F(0)]*n
            for i,v in zip(remaining,up):
                pt[i]=F(caps[i]*v)
            pt[free]=F(level)-sum(pt)
            if 0<=pt[free]<=caps[free]:out.add(tuple(pt))
    return out

def basket(caps,k):
    n=len(caps); counts=Counter(); allbound=[]
    for up in product((0,1),repeat=n):
        S=tuple(i for i in range(n) if up[i]); total=sum(caps[i] for i in S)
        if total==k:
            allbound.append(S)
            if 2<=len(S)<=n-2:
                counts[(len(S),n-len(S),comb(n-2,len(S)-1))]+=1
    return counts,allbound

def enumerate_monomials(s,l,d):
    """Degree d monomials in rank-one s x l matrix coordinate ring.
    Compare two enumerations: products of edge monomials vs balanced exponent arrays."""
    outputs={(tuple([0]*s),tuple([0]*l))}
    for _ in range(d):
        outputs={(tuple(a[i]+(i==p) for i in range(s)),tuple(b[j]+(j==q) for j in range(l)))
                 for a,b in outputs for p in range(s) for q in range(l)}
    return len(outputs),comb(s+d-1,d)*comb(l+d-1,d)

def determinant(rows):
    """Exact integer determinant by the permutation expansion (small checker matrices)."""
    from itertools import permutations
    d=len(rows)
    ans=0
    for perm in permutations(range(d)):
        inversions=sum(perm[i]>perm[j] for i in range(d) for j in range(i+1,d))
        term=-1 if inversions%2 else 1
        for i in range(d):term*=rows[i][perm[i]]
        ans+=term
    return ans


def check_integral_fan_faces(n, S):
    """Compute the lattice saturation index of every proper cone face.
    A normal ray is the signed coordinate class in Z^n/Z(1,...,1).
    For 2 <= |S| <= n-2 proper faces omit a ray from each sign class.
    The columns are independent, and gcd of maximal minors must be 1.
    """
    indices=set(range(n)); Q=indices.difference(S)
    ray=[]
    for i in range(n):
        signed=-1 if i in S else 1
        col=([1 if j==i else 0 for j in range(n-1)] if i<n-1 else [-1]*(n-1))
        ray.append([signed*v for v in col])
    for mask in product((0,1),repeat=n):
        T={i for i in range(n) if mask[i]}
        if S.issubset(T) or Q.issubset(T):
            continue
        if not T:continue
        rays=[ray[i] for i in sorted(T)]
        r=len(T)
        minors=[abs(determinant([[ray[j] for ray in rays] for j in rows]))
                for rows in subset_combinations(range(n-1),r)]
        assert 1 in minors,(n,S,T,minors)


def run():
    samples=[((1,1,1,2,2,3),3),((1,1,1,1,1),2),((2,2,3,3,4),5),
             ((1,2,4,8,16,32),13),((2,3,3,4,4,5),8),((1,1,2,3),3)]
    for caps,k in samples:
        n=len(caps)
        verts=grid_vertices(caps,F(k)); count,allbound=basket(caps,k)
        assert len(allbound)<=len(verts)
        assert {tuple(F(caps[i] if i in S else 0) for i in range(n)) for S in allbound}<=verts
        for p in verts:
            free=[i for i,x in enumerate(p) if x!=0 and x!=caps[i]]
            assert len(free)<=1
            if not free:
                S=tuple(i for i,x in enumerate(p) if x==caps[i])
                assert S in allbound
        for S in allbound:
            if 2<=len(S)<=n-2:
                check_integral_fan_faces(n,set(S))
        eps=F(1,100)
        for sign in (-1,1):
            near=grid_vertices(caps,F(k)+sign*eps)
            for S in allbound:
                if 2<=len(S)<=n-2:
                    wall=tuple(F(caps[i] if i in S else 0) for i in range(n))
                    close=[p for p in near if sum(abs(p[i]-wall[i]) for i in range(n))==eps]
                    assert len(close)==(n-len(S) if sign>0 else len(S)),(caps,k,S,sign,close)
        print('CAPS',caps,'LEVEL',k,'TORUS_FIXED',len(verts),'SINGULAR',sum(count.values()),'BASKET',dict(count))
    for s in range(2,5):
        for l in range(2,5):
            for degree in range(5):
                a,b=enumerate_monomials(s,l,degree)
                assert a==b,(s,l,degree,a,b)
    print('BALANCED_SEMIGROUP_DEGREES_OK')
    print('VERIFY_OK')

if __name__=='__main__':run()
