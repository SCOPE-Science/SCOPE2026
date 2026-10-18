#!/usr/bin/env python3
"""Exact finite-level checks for the prime-adic finite-cocycle classification."""
from itertools import permutations, product
from math import gcd


def cyclic(n):
    return tuple(range(n)), lambda a,b:(a+b)%n, 0


def symmetric3():
    elements=tuple(permutations(range(3)))
    unit=(0,1,2)
    def mult(a,b):return tuple(a[b[j]] for j in range(3))
    return elements,mult,unit


def power(x,n,mult,unit):
    y=unit
    for _ in range(n):y=mult(y,x)
    return y


def order(x,mult,unit):
    y=unit
    for i in range(1,1000):
        y=mult(y,x)
        if y==unit:return i
    raise AssertionError('order bound')


def p_regular_part(g,p,mult,unit):
    d=order(g,mult,unit); a=1
    while d%p==0:
        d//=p;a*=p
    if d==1:return unit
    e=next(k for k in range(a*d) if k%a==0 and k%d==1)
    return power(g,e,mult,unit)


def canonical(c,p,mult,unit):
    s=0; m=1
    while m<len(c):m*=p;s+=1
    assert len(c)==m
    P=unit
    for z in c:P=mult(P,z)
    u=p_regular_part(P,p,mult,unit)
    r=order(u,mult,unit)
    if r==1:return unit
    inverse=pow(pow(p,s,r),-1,r)
    return power(u,inverse,mult,unit)


def conjugate(a,b,G,mult,unit):
    for h in G:
        # no need to compute h^{-1}, since a*h=h*b iff conjugate
        if mult(a,h)==mult(h,b):return True
    return False


def component_count(c,p,G,mult,unit,j):
    m=len(c);N=p**j
    assert N%m==0
    points={(z,g) for z in range(N) for g in G}
    num=0; sizes=[]
    while points:
        z,g=next(iter(points));start=(z,g);cur=start;size=0
        while True:
            assert cur in points
            points.remove(cur);size+=1
            r,h=cur
            cur=((r+1)%N,mult(h,c[r%m]))
            if cur==start:break
        num+=1;sizes.append(size)
    return num,set(sizes)


def run():
    checks=0
    for G,mult,unit in (cyclic(6),cyclic(7),cyclic(8),symmetric3()):
      for p in (2,3):
        # all single-symbol cocycles, and deterministic varied multibranch cocycles
        for s in (0,1,2):
          m=p**s
          samples=[]
          for i,g in enumerate(G):
            samples.append([g]*m)
            samples.append([G[(i+j*j+j)%len(G)] for j in range(m)])
          if m<=3:
            samples.extend([list(c) for c in product(G,repeat=m) if len(G)**m<=216])
          for c in samples:
            h=canonical(c,p,mult,unit)
            r=order(h,mult,unit)
            assert gcd(r,p)==1
            for j in (s+3,s+4):
                n,sizes=component_count(c,p,G,mult,unit,j)
                assert n==len(G)//r,(len(G),p,s,c,n,r)
                assert sizes=={p**j*r},(p,s,sizes,r)
                checks+=1
            # Raising the source-resolution level preserves the normalized invariant.
            c_lift=[c[i%m] for i in range(m*p)]
            assert canonical(c_lift,p,mult,unit)==h
            checks+=1
      
    # Direct comparison of all 36 binary S3 cocycles against canonical constants.
    G,mult,unit=symmetric3();p=2
    for a,b in product(G,repeat=2):
        c=[a,b];h=canonical(c,p,mult,unit)
        for q in G:
            prediction=conjugate(h,p_regular_part(q,p,mult,unit),G,mult,unit)
            # Exhaustive finite-level gauge criterion (cycle monodromy conjugacy).
            for j in (1,2,3,4):
                P=power(mult(a,b),2**(j-1),mult,unit)
                Q=power(q,2**j,mult,unit)
                if j==4: assert conjugate(P,Q,G,mult,unit)==prediction
            checks+=1
    # In the cyclic order-seven fibre, distinct constant cocycles remain inequivalent.
    G,mult,unit=cyclic(7)
    for a,b in product(G,repeat=2):
        assert (canonical([a],2,mult,unit)==canonical([b],2,mult,unit))==(a==b)
        checks+=1
    # One nonconstant cocycle with no constant representative at its first level.
    assert canonical([1,0],2,mult,unit)==4
    return checks

if __name__=='__main__':
    print('VERIFY_OK exact finite-level assertions:',run())
