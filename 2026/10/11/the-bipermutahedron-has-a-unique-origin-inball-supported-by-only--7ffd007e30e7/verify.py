#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

def facet_data(n, states):
    # State 0: S only; 1: T only; 2: both.
    S={i for i,s in enumerate(states) if s in (0,2)}
    T={i for i,s in enumerate(states) if s in (1,2)}
    if not S or not T or (len(S)==n and len(T)==n):
        return None
    u=n-len(S)
    v=n-len(T)
    A=u*(n-u)+v*(n-v)
    slack=n*n-(u-v)*(u-v)
    assert A>0
    # Intrinsic squared distance = slack^2 / (A/n).
    d2=Fraction(n*slack*slack,A)
    return S,T,u,v,d2

for n in range(2,9):
    data=[]
    for states in product(range(3), repeat=n):
        q=facet_data(n,states)
        if q is not None:
            data.append(q)
    assert len(data)==3**n-3

    mind2=min(q[4] for q in data)
    minimizers=[q for q in data if q[4]==mind2]

    if n>=3:
        want=Fraction(n*(2*n-1)**2,n-1)
        assert mind2==want
        assert len(minimizers)==2*n
        for S,T,u,v,d2 in minimizers:
            assert (u,v) in ((n-1,0),(0,n-1))
            assert (len(S)==1 and len(T)==n) or (len(S)==n and len(T)==1)
    else:
        assert mind2==16
        assert len(minimizers)==2
        assert all((q[2],q[3])==(1,1) for q in minimizers)

# n=2 incenter segment.
# Coordinates are x=(a,-a), y=(b,-b).
# Radius 4 imposes:
# diagonal facets: 4 +/- (a-b) >= 4 -> a=b;
# coordinate facets: sqrt(2)*(3 +/- a) >= 4 and same for b.
# Therefore |a|=|b| <= 3-2*sqrt(2).
# Verify the endpoint algebraically through squared inequality:
# (3-|a|)^2 = 8 at |a| = 3-2sqrt(2).
# Let z=3-2sqrt(2); then (3-z)^2=(2sqrt(2))^2=8.
print("VERIFY_OK bipermutahedron-inradius n=2..8 all_bisubsets=yes")
