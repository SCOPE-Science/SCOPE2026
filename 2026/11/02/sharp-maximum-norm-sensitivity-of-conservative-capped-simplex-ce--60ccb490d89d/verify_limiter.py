#!/usr/bin/env python3
"""Checks for the sharp fixed-mass uniform capped-simplex sensitivity theorem.

This verifies finite-dimensional algebra and numerical examples only;
the general theorem rests on the written proof, not on finite sampling.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from random import Random


def clipped_projection(values, mass):
    """Independent bisection implementation of KKT projection in doubles."""
    lo, hi = min(values)-2, max(values)+2
    for _ in range(100):
        mid = (lo+hi)/2
        total = sum(min(1.0, max(0.0, x-mid)) for x in values)
        if total > mass:
            lo = mid
        else:
            hi = mid
    t = (lo+hi)/2
    return [min(1.0, max(0.0, x-t)) for x in values]


def formula(n):
    return F(2)-F(2, n//2+1)


def local_predicted(n,k):
    b=n-k
    if k <=1:
        return F(0)
    return F(1)+F(min(b,k-2),k)


def local_exact(n,k):
    """Enumerates all vertices of cube intersect the zero-sum hyperplane."""
    if k == 1:
        return F(0)
    best=F(0)
    if n % 2 == 0:
        for plus in combinations(range(n), n//2):
            ps=set(plus)
            v=[1 if j in ps else -1 for j in range(n)]
            val=F(v[0])-sum(map(F,v[:k]))/k
            best=max(best,abs(val))
    else:
        for zero in range(n):
            remaining=[i for i in range(n) if i!=zero]
            for plus in combinations(remaining,(n-1)//2):
                ps=set(plus)
                v=[0 if j==zero else (1 if j in ps else -1) for j in range(n)]
                val=F(v[0])-sum(map(F,v[:k]))/k
                best=max(best,abs(val))
    return best


def exact_mass_witness(n,mass):
    """Exact rational pair in a single strict active-set region."""
    k=n//2+1
    b=n-k
    if b==0:
        return
    mass=F(mass)
    assert 0<mass<n
    lower = mass<k
    if lower:
        a=mass/k
        z=[a]*k+[F(0)]*b
    else:
        a=(mass-b)/k
        z=[a]*k+[F(1)]*b
    assert 0<a<1
    eta=min(a,1-a,F(1,10))/20
    step=eta/100
    if lower:
        x=[a+eta]*k+[-k*eta/b]*b
    else:
        x=[a-eta]*k+[1+k*eta/b]*b
    v=[F(1)]+[-F(1)]*(k-1)+[F(k-2,b)]*b
    assert sum(v)==0 and max(abs(t) for t in v)==1
    y=[xi+step*vi for xi,vi in zip(x,v)]
    assert sum(x)==mass and sum(y)==mass
    lamx=sum(x[:k])/k-a
    lamy=sum(y[:k])/k-a
    px=[max(F(0),min(F(1),xi-lamx)) for xi in x]
    py=[max(F(0),min(F(1),xi-lamy)) for xi in y]
    assert px==z
    assert sum(py)==mass
    assert all(0<q<1 for q in py[:k])
    assert all(q in (0,1) for q in py[k:])
    for i in range(k,n):
        if lower:
            assert x[i]-lamx<0 and y[i]-lamy<0
        else:
            assert x[i]-lamx>1 and y[i]-lamy>1
    observed=max(abs(a-b) for a,b in zip(px,py))/step
    assert observed == formula(n),(n,mass,observed,formula(n))
    qpx=clipped_projection([float(q) for q in x],float(mass))
    qpy=clipped_projection([float(q) for q in y],float(mass))
    assert max(abs(u-float(vv)) for u,vv in zip(qpx,px))<1e-9
    assert max(abs(u-float(vv)) for u,vv in zip(qpy,py))<1e-9


def main():
    count=0
    for n in range(2,11):
        exact=[]
        for k in range(1,n+1):
            obtained=local_exact(n,k)
            expected=local_predicted(n,k)
            assert obtained==expected,(n,k,obtained,expected)
            exact.append(obtained)
            count+=1
        assert max(exact)==formula(n),(n,exact,formula(n))
        count+=1
    for n in range(3,33):
        for mass in (F(1,9),F(n,2),F(n)-F(1,9)):
            exact_mass_witness(n,mass)
            count+=1
    rng=Random(20261028)
    for n in range(2,21):
        for _ in range(125):
            mass=rng.uniform(.03,n-.03)
            x=[rng.uniform(-2,2) for _ in range(n)]
            y=[rng.uniform(-2,2) for _ in range(n)]
            x=[v+(mass-sum(x))/n for v in x]
            y=[v+(mass-sum(y))/n for v in y]
            px=clipped_projection(x,mass)
            py=clipped_projection(y,mass)
            assert abs(sum(px)-mass)<1e-9
            assert abs(sum(py)-mass)<1e-9
            den=max(abs(a-b) for a,b in zip(x,y))
            num=max(abs(a-b) for a,b in zip(px,py))
            assert num<=float(formula(n))*den+2e-8,(n,num,den)
            count+=1
    print(f"PASS: {count} exact active-set/vertex and floating-point projection tests")
    print('Exact threshold: n<=3 factor 1; n=4 factor 4/3; n=10 factor 5/3.')
    print('Finite computations do not establish the all-dimension theorem.')


if __name__=='__main__':
    main()
