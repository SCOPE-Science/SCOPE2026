#!/usr/bin/env python3
"""Exact finite checks for normal-fan cones of path stable-set polytopes.
Run with Python >=3.9; standard library only. Checks n=3,...,7.
This supplements, but does not replace, the all-n graphic-matroid argument.
"""
from itertools import combinations
from fractions import Fraction

def rank(rows):
    if not rows: return 0
    a=[[Fraction(v) for v in row] for row in rows]
    m=len(a); n=len(a[0]); r=0
    for c in range(n):
        pivot=next((q for q in range(r,m) if a[q][c]), None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        scale=a[r][c]
        a[r]=[z/scale for z in a[r]]
        for q in range(r+1,m):
            if a[q][c]:
                mul=a[q][c]
                a[q]=[z-mul*w for z,w in zip(a[q],a[r])]
        r+=1
        if r==m: break
    return r

def run(n):
    verts=[bits for bits in range(1<<n) if not (bits&(bits<<1)) & ((1<<n)-1)]
    fib=[0,1]
    for _ in range(n+1): fib.append(fib[-1]+fib[-2])
    assert len(verts)==fib[n+2]
    full=(1<<len(verts))-1
    facet=[]
    for i in range(n):
        ray=[0]*n;ray[i]=-1
        facet.append((('Z',i),ray,sum((1<<j) for j,bits in enumerate(verts) if not (bits>>i)&1)))
    for i in range(n-1):
        ray=[0]*n;ray[i]=ray[i+1]=1
        facet.append((('E',i),ray,sum((1<<j) for j,bits in enumerate(verts) if ((bits>>i)&1)+((bits>>(i+1))&1)==1)))
    faces={full}
    for _,_,fm in facet:
        faces|={f&fm for f in tuple(faces) if f&fm}
    assert all(f for f in faces)
    # all intersections of facets are included by sequential closure
    masks=[]
    for c in range(1,n-1):
        target=(1<<len(verts))-1
        for ix in (c-1,c,c+1):
            if ix==c: target &= facet[n+ix-1][2] & facet[n+ix][2]  # both incident path edges
            else: target &= facet[ix][2]  # zero at neighboring positions
        assert target
        masks.append(target)
    bad=[];dims={}; total_non_simple=0
    rk_cache={}
    for f in faces:
        active=tuple(i for i,(_,_,fm) in enumerate(facet) if f&fm==f)
        if active not in rk_cache:
            rk_cache[active]=rank([facet[i][1] for i in active])
        codim=rk_cache[active]
        non_simple=(len(active)>codim)
        expected=any(f&m==f for m in masks)
        assert non_simple==expected, ('wrong singular classification',n,f,active)
        if non_simple:
            total_non_simple+=1
            dims[n-codim]=dims.get(n-codim,0)+1
            bad.append(f)
    maximal=[f for f in bad if not any(f!=g and (f&g)==f for g in bad)]
    assert set(maximal)==set(masks), ('components',n,len(maximal),len(masks))
    # Nerve of irreducible singular components = independence complex of P_(n-2).
    for r in range(len(masks)+1):
        for chosen in combinations(range(len(masks)),r):
            meet=full
            for j in chosen: meet&=masks[j]
            assert bool(meet)==all(j+1 not in chosen for j in chosen)
    return len(verts),len(faces),len(maximal),total_non_simple,dims

if __name__=='__main__':
    for n in range(3,8):
        print(n,run(n))
    # Transverse cone normal rays have primitive square circuit and unit minors.
    r0=(-1,0,0);r1=(0,0,-1);r2=(1,1,0);r3=(0,1,1)
    assert tuple(x+y for x,y in zip(r0,r2))==tuple(x+y for x,y in zip(r1,r3))
    rays=(r0,r1,r2,r3)
    def det3(A):
        a,b,c=A;return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
    assert all(abs(det3(p))==1 for p in combinations(rays,3))
    print('VERIFY_OK')
