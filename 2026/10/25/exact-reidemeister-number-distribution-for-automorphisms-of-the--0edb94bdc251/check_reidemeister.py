#!/usr/bin/env python3
"""Exact finite checks of an automorphism Reidemeister histogram for H_p.
Python 3 standard library only. No random choices.
"""
from collections import Counter
from itertools import product


def matrices(p):
    for a,b,c,d in product(range(p),repeat=4):
        D=(a*d-b*c)%p
        if D:
            yield (a,b,c,d,D)


def rankfixed(A,p):
    a,b,c,d,_=A
    a=(a-1)%p; d=(d-1)%p
    if a==b==c==d==0: return 2
    if (a*d-b*c)%p==0: return 1
    return 0


def prediction(p):
    return {
        1:p**3*(p+1)*(p-2)**2,
        p:p**3*(2*p*p-2*p-3),
        2*p-1:p*p*(p*p-1),
        p*p+p-1:p*p,
    }


def matrix_census(p):
    c=Counter()
    for A in matrices(p):
        det=A[-1]
        c[p**rankfixed(A,p)+(p-1)*(det==1)]+=p*p
    assert c==prediction(p), (p,c,prediction(p))
    assert sum(c.values())==p**3*(p-1)**2*(p+1)
    return dict(sorted(c.items()))


def group_orbit_count(p,A,t):
    """Count actual twisted orbits under all group actions, not fixed classes."""
    a,b,c,d,D=A
    inv2=pow(2,-1,p)
    elements=list(product(range(p),repeat=3))
    def prod(x,y):
        vx,vy,z=x; wx,wy,s=y
        return ((vx+wx)%p,(vy+wy)%p,(z+s+inv2*(vx*wy-vy*wx))%p)
    def phi(x):
        vx,vy,z=x
        return ((a*vx+b*vy)%p,(c*vx+d*vy)%p,(D*z+t[0]*vx+t[1]*vy)%p)
    def inv(x): return tuple((-t)%p for t in x)
    # Each action g acts by x -> g*x*phi(g)^-1; generate orbit as all images.
    left_right=[(g,inv(phi(g))) for g in elements]
    unseen=set(elements); count=0
    while unseen:
        x=next(iter(unseen))
        orbit={prod(prod(g,x),h) for g,h in left_right}
        assert len(orbit)<=len(elements)
        unseen.difference_update(orbit); count+=1
    return count


def orbit_census_three():
    p=3
    c=Counter()
    for A in matrices(p):
        for t in product(range(p), repeat=2):
            got=group_orbit_count(p,A,t)
            want=p**rankfixed(A,p)+(p-1)*(A[-1]==1)
            assert got==want,(A,t,got,want)
            c[got]+=1
    assert c==prediction(p),(c,prediction(p))
    return dict(sorted(c.items()))


if __name__=='__main__':
    for p in (3,5,7,11):
        print('matrix',p,matrix_census(p))
    print('group orbit BFS',3,orbit_census_three())
    print('VERIFY_OK')
