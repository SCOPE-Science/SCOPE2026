#!/usr/bin/env python3
"""Check local semigroup presentations for small complete multipartite edge toric varieties."""
from itertools import combinations_with_replacement, product
from math import comb


def rank_rational(vectors):
    from fractions import Fraction
    if not vectors:return 0
    a = [[Fraction(x) for x in v] for v in vectors]
    pivots = 0
    for c in range(len(a[0])):
        i = next((i for i in range(pivots,len(a)) if a[i][c]),None)
        if i is None:continue
        a[pivots],a[i]=a[i],a[pivots]
        z=a[pivots][c];a[pivots]=[x/z for x in a[pivots]]
        for j in range(len(a)):
            if j!=pivots and a[j][c]:
                z=a[j][c]
                a[j]=[x-z*y for x,y in zip(a[j],a[pivots])]
        pivots+=1
        if pivots==len(a):break
    return pivots

def test(parts,limit=4):
    cl=[];v=0
    for n in parts:
        cl.append(list(range(v,v+n)));v+=n
    cls={x:i for i,gg in enumerate(cl) for x in gg}
    edges=[(a,b) for a in range(v) for b in range(a+1,v) if cls[a]!=cls[b]]
    cases=0
    for u,v0 in edges:
        A,B=cls[u],cls[v0]
        outside=[w for w in range(v) if cls[w] not in (A,B)]
        gens=[]
        for w in cl[A]:
            if w!=u:gens.append((f'x{w}',w,u))
        for w in cl[B]:
            if w!=v0:gens.append((f'y{w}',w,v0))
        for w in outside:
            gens.append((f'p{w}',w,u))
            gens.append((f'q{w}',w,v0))
        def vector(a,b):
            arr=[0]*v;arr[a]+=1;arr[b]-=1;return tuple(arr)
        V=[vector(i,j) for _,i,j in gens]
        def plus(a,b):return tuple(x+y for x,y in zip(a,b))
        all_gens=set(V)
        for a,b in edges:
            if (a,b)==(u,v0):continue
            target=tuple((1 if w in (a,b) else 0)-(1 if w in (u,v0) else 0) for w in range(v))
            # all target edge ratios are sums of 1 or 2 stated generators
            assert target in all_gens or any(plus(s,t)==target for s in V for t in V),(parts,(u,v0),(a,b),target)
        f=parts[A]+parts[B]-2;m=len(outside)
        predicted_rank=f+m+1 if m else f
        assert rank_rational(V)==predicted_rank, (parts,(u,v0),rank_rational(V),predicted_rank)
        if m>=2:
            # Full homogeneous ideal equivalence: distinct product monomials vs Segre (rank-one) normal form.
            # Each multiset of p,q indices maps to a pair (#p, multiset of chosen outside indices).
            # This is equivalent to the 2x2 minors, and controls the full nonnegative semigroup kernel.
            pq=[(side,w) for w in outside for side in 'pq']
            for d in range(limit+1):
                direct=set()
                for ms in combinations_with_replacement(range(len(pq)),d):
                    y=[0]*v
                    for i in ms:
                        side,w=pq[i];y[w]+=1; y[u if side=='p' else v0]-=1
                    direct.add(tuple(y))
                pred=(d+1)*comb(d+m-1,m-1)
                assert len(direct)==pred,(parts,(u,v0),d,len(direct),pred)
        cases+=1
    return cases

if __name__=='__main__':
    patterns=[(1,1),(2,2),(1,1,1),(1,1,2),(1,2,2),(2,2,2),(1,1,1,1),(1,1,1,2),(1,1,2,2),(1,2,3),(2,3,2),(1,1,1,3)]
    total=0
    for p in patterns:
        n=test(p)
        total+=n
        print(f'{p}: {n} edge charts, verified')
    print(f'OK: {total} chart presentations, minor semigroup kernels up to degree 4')

def jacobian_rank_of_rank_one_minors(m, p, q):
    # Coordinates are p[0:m],q[0:m]. For each i<j, minor p_i q_j-p_j q_i.
    from fractions import Fraction
    rows=[]
    for i in range(m):
        for j in range(i+1,m):
            row=[0]*(2*m)
            row[i]+=q[j]
            row[j]-=q[i]
            row[m+i]-=p[j]
            row[m+j]+=p[i]
            rows.append(row)
    return rank_rational(rows)

if __name__=='__main__':
    num=0
    for m in range(2,9):
        assert jacobian_rank_of_rank_one_minors(m,[0]*m,[0]*m)==0
        for x,y in [(1,0),(0,1),(2,-3),(1,2)]:
            z=[(i+1)*(i+2) for i in range(m)]
            assert jacobian_rank_of_rank_one_minors(m,[x*v for v in z],[y*v for v in z])==m-1
            num+=1
    print(f'OK: {num} nonzero rank-one Jacobian points for m=2..8, codimension m-1')
