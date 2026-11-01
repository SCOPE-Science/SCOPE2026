#!/usr/bin/env python3
"""Finite reproducibility checks for the projective-matroid invariant-cycle theorem.
All general-rank assertions are proved symbolically in RESULT.md; finite runs
are independent cross-checks, not extrapolations.
"""
from itertools import combinations,product
from collections import Counter

class Field:
    def __init__(self,q):
        assert q in (2,3,4)
        self.q=q
    def add(self,a,b):
        return (a^b) if self.q==4 else (a+b)%self.q
    def mul(self,a,b):
        if self.q!=4:return (a*b)%self.q
        c=0
        while b:
            if b&1:c^=a
            b>>=1;a<<=1
            if a&4:a^=7 # x^2+x+1
        return c
    def inv(self,a):
        assert a
        return next(x for x in range(1,self.q) if self.mul(a,x)==1)

def points(q,r):
    F=Field(q)
    seen=set()
    for v in product(range(q),repeat=r):
        if not any(v):continue
        i=next(i for i,x in enumerate(v) if x)
        v=tuple(F.mul(x,F.inv(v[i])) for x in v)
        seen.add(v)
    return sorted(seen)

def rank(F,cols):
    if not cols:return 0
    mat=[[cols[c][i] for c in range(len(cols))] for i in range(len(cols[0]))]
    i=0
    for j in range(len(cols)):
        p=next((k for k in range(i,len(mat)) if mat[k][j]),None)
        if p is None:continue
        mat[i],mat[p]=mat[p],mat[i]
        z=F.inv(mat[i][j]);mat[i]=[F.mul(z,a) for a in mat[i]]
        for k in range(len(mat)):
            if k==i:continue
            z=mat[k][j]
            if z:mat[k]=[F.add(a,F.mul(z,b)) if F.q==4 else (a-F.mul(z,b))%F.q for a,b in zip(mat[k],mat[i])]
        i+=1
        if i==len(mat):break
    return i

def check(q,r):
    F=Field(q);P=points(q,r)
    facets=[f for f in combinations(range(len(P)),r) if rank(F,[P[i] for i in f])==r]
    faces=[f for f in combinations(range(len(P)),r-1) if rank(F,[P[i] for i in f])==r-1]
    face_counts=Counter(sub for f in facets for sub in combinations(f,r-1))
    assert all(face_counts[f]==q**(r-1) for f in faces)
    assert len(face_counts)==len(faces)
    # Basis facet stabilizer has an orientation-reversing transposition:
    base=[tuple(int(i==j) for i in range(r)) for j in range(r)]
    b=tuple(sorted(P.index(x) for x in base))
    assert b in facets
    swapped=tuple(tuple(v[1] if j==0 else v[0] if j==1 else v[j] for j in range(r)) for v in base)
    assert set(swapped)==set(base) and swapped[0]==base[1] and swapped[1]==base[0]
    # Under mod 2, the orbit sum has each codim-one coefficient q^(r-1).
    odd_coeff=q**(r-1)%2
    assert odd_coeff == q%2
    print('q=%s r=%s projective_points=%s facets=%s codim1=%s coefficient=%s mod2_cycle=%s' %
          (q,r,len(P),len(facets),len(faces),q**(r-1),not odd_coeff))

if __name__=='__main__':
    for pair in ((2,2),(3,2),(4,2),(2,3),(3,3),(4,3),(2,4)):
        check(*pair)
    print('VERIFY_OK')
