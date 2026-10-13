#!/usr/bin/env python3
"""Exact finite regression tests for chain-polytope Demazure root formulas.

All arithmetic is over the integers; the root cone inequalities are checked
against the primitive inward facet normals. The search box [-1,1]^d is a
finite regression domain, not a proof that no roots lie outside it.
"""
from itertools import product


def rays(a, b, c):
    n = a+b+c
    r = []
    for i in range(n):
        v = [0]*n
        v[i] = 1
        r.append(tuple(v))
    for i in range(a):
        for j in range(a,a+c):
            for k in range(a+c,n):
                v = [0]*n
                v[i] = v[j] = v[k] = -1
                r.append(tuple(v))
    return r


def predicted(a, b, c):
    n = a+b+c
    out = set()
    for i in range(n):
        m = [0]*n
        m[i] = -1
        out.add(tuple(m))
    if c==1:
        j = a
        for block in [list(range(a)),list(range(a+c,n))]:
            for flags in product((0,1),repeat=len(block)):
                m=[0]*n
                m[j]=-1
                for k,flag in zip(block,flags):
                    m[k]=flag
                out.add(tuple(m))
    return out


def exhaustive_box_roots(r):
    n=len(r[0]); roots=set()
    for m in product((-1,0,1),repeat=n):
        dots=[sum(t*z for t,z in zip(v,m)) for v in r]
        if dots.count(-1)==1 and all(x>=0 for x in dots if x!=-1):
            roots.add(m)
    return roots


def bracket(m,n,r):
    rho=next((i for i,v in enumerate(r) if sum(t*z for t,z in zip(v,m))==-1),None)
    sigma=next((i for i,v in enumerate(r) if sum(t*z for t,z in zip(v,n))==-1),None)
    if rho==sigma: return None
    x=sum(t*z for t,z in zip(r[rho],n))
    y=sum(t*z for t,z in zip(r[sigma],m))
    if x==0 and y==0:return None
    s=tuple(u+v for u,v in zip(m,n))
    return (s,x,y)


def lower_central_class(roots,r):
    base=set(roots)
    level=set(base)
    for step in range(1,len(r)+4):
        next_level=set()
        for m in base:
            for n in level:
                v=bracket(m,n,r)
                if v is not None:
                    s,x,y=v
                    assert s in base,(step,m,n,s,x,y)
                    next_level.add(s)
        if not next_level:
            return step
        level=next_level
    raise AssertionError('nilpotency bound exceeded')


def main():
    cases=[(2,2,1),(2,3,1),(3,2,1),(3,3,1),(2,4,1),(4,3,1),
           (2,2,2),(2,3,2),(3,3,2),(2,2,3),(3,2,3)]
    checked=0
    for a,b,c in cases:
        r=rays(a,b,c)
        got=exhaustive_box_roots(r)
        exp=predicted(a,b,c)
        assert got==exp,(a,b,c,sorted(got-exp),sorted(exp-got))
        d=a+b+c
        assert len(exp)==(a+b+2**a+2**b-1 if c==1 else d)
        cls=lower_central_class(got,r)
        want=max(a,b)+1 if c==1 else 1
        assert cls==want,(a,b,c,cls,want)
        checked+=3**d
        print('PASS',a,b,c,'dimension',d,'rays',len(r),
              'roots',len(got),'nilpotency_class',cls)
    print('ALL PASS',len(cases),'parameter triples,',checked,'bounded integer vectors')

if __name__=='__main__':
    main()
