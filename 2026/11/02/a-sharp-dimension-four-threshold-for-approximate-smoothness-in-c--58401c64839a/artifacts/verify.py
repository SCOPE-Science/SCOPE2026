"""Self-contained finite rational checks for the cube-crosspolytope smoothness law.

Enumerates every signed two-support vertex and all exposed facet normals;
computes their pairwise distances by maximizing over the full polytope.
This checker corroborates examples only; the accompanying proof is infinite.
"""
from fractions import Fraction as Q
from itertools import combinations, product

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), Q(0))

def vertices(n,t):
    a=t-1
    out=set()
    for i,j in product(range(n), repeat=2):
        if i==j: continue
        for signs in product((-1,1),repeat=2):
            x=[Q(0)]*n; x[i]=Q(signs[0]); x[j]=signs[1]*a
            out.add(tuple(x))
    return sorted(out)

def normals(n,t):
    out=set()
    for i in range(n):
        for sign in (-1,1):
            x=[Q(0)]*n; x[i]=Q(sign); out.add(tuple(x))
    for signs in product((-1,1),repeat=n):
        out.add(tuple(Q(v)/t for v in signs))
    return sorted(out)

def measured(n,t):
    verts=vertices(n,t); fs=normals(n,t)
    assert all(max([abs(z) for z in x]+[Q(0)])==1 and sum(map(abs,x))==t for x in verts)
    for f in fs:
        assert max(dot(f,x) for x in verts)==1
    val=Q(0)
    for v in verts:
        active=[f for f in fs if dot(f,v)==1]
        for f,g in combinations(active,2):
            h=tuple(x-y for x,y in zip(f,g))
            dist=max(dot(h,x) for x in verts)
            val=max(val,dist)
    return val,len(verts),len(fs)

def expected(n,t):
    a=t-1
    return (1+a*a)/t if n==2 else Q(2)/t if n==3 else Q(2)

def main():
    count=0
    for n in (2,3,4,5):
        for t in [Q(9,8),Q(4,3),Q(3,2),Q(7,4),Q(15,8)]:
            val,nv,nf=measured(n,t)
            assert val==expected(n,t),(n,t,val,expected(n,t))
            count+=1
    print('VERIFY_OK',count,'full-polytope exact-rational cases')
if __name__=='__main__': main()
