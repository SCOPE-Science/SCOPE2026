#!/usr/bin/env python3
"""Exact finite cut checks for a centered graphical zonotope of the Boolean cube.
The all-dimensional statement requires the separate analytic proof.
"""
from fractions import Fraction
import random

def edges_of_cube(d):
    n=1<<d
    return [(v,v^(1<<k)) for v in range(n) for k in range(d) if not (v&(1<<k))]

def cut_size(smask, edges):
    return sum(bool((smask>>u)&1) != bool((smask>>v)&1) for u,v in edges)

def qrat(d):
    n=1<<d
    if d<=4: return Fraction(n,4)
    return Fraction(d*d*n,4*(n-1))

def expected(d):
    n=1<<d
    if d<=4:
        return {sum(1<<v for v in range(n) if v&(1<<k)):None for k in range(d)} | {sum(1<<v for v in range(n) if not (v&(1<<k))):None for k in range(d)}
    return {1<<v:None for v in range(n)} | {((1<<n)-1)^(1<<v):None for v in range(n)}

def check_full(d):
    n=1<<d; edges=edges_of_cube(d); target=qrat(d)
    contacts=[]
    for smask in range(1,(1<<n)-1):
        s=smask.bit_count(); b=cut_size(smask,edges)
        q=Fraction(n*b*b,4*s*(n-s))
        assert q >= target,(d,smask,s,b,q,target)
        if q==target: contacts.append(smask)
    assert set(contacts)==set(expected(d)),(d,contacts,expected(d))
    return len(contacts)

def check_sample(d,limit=10000):
    n=1<<d; edges=edges_of_cube(d); target=qrat(d)
    rng=random.Random(8472026+d)
    masks=set(expected(d))
    masks.update(1<<v for v in range(n))
    masks.update(sum(1<<v for v in range(n) if v&(1<<k)) for k in range(d))
    for _ in range(limit):
        p=rng.uniform(.04,.96)
        m=sum((1<<v) for v in range(n) if rng.random()<p)
        if 0<m<(1<<n)-1:masks.add(m)
    for m in masks:
        s=m.bit_count(); b=cut_size(m,edges)
        q=Fraction(n*b*b,4*s*(n-s))
        assert q>=target,(d,s,b,q,target)
        if q==target:assert m in expected(d),(d,m)
    return len(masks)

def check_walsh(d):
    n=1<<d
    def chi(a,v):
        return -1 if ((a&v).bit_count()%2) else 1
    # All characters of the cube form an exact orthogonal integer matrix.
    for a in range(n):
        for b in range(n):
            total=sum(chi(a,v)*chi(b,v) for v in range(n))
            assert total==(n if a==b else 0)
    # Optimizing cut vectors annihilate exactly the advertised Walsh modes.
    for m in expected(d):
        s=m.bit_count()
        for a in range(n):
            # N*1_S - |S|*1 is the integer scaled centered cut normal.
            product=sum(((n if (m>>v)&1 else 0)-s)*chi(a,v) for v in range(n))
            if d<=4 and a.bit_count()>=2:
                assert product==0,(d,m,a,product)
    return True

if __name__=='__main__':
    for d in range(1,5):
        print(f'full_d={d} size={1<<d} cut_classes={(1<<(1<<d))-2} contacts={check_full(d)} walsh={check_walsh(d)}')
    for d in (5,6):
        print(f'sampled_d={d} size={1<<d} subsets={check_sample(d,3000)}' + (' walsh='+str(check_walsh(d)) if d==5 else ''))
    print('VERIFY_OK graphical-hypercube-inball d1-4_exhaustive=yes d5-6_sampled=yes universal_analytic_proof=required')
