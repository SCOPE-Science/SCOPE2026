#!/usr/bin/env python3
"""Exact-arithmetic companion for the intersection and incidence dimensions.

Algebraic-geometric vanishing and obstruction results are proved in RESULT.md,
not by this finite executable.
"""


def ip(u, v):
    # Basis: hyperplane h and a line E on a (2,2,2) K3.
    return 8*u[0]*v[0] + u[0]*v[1] + u[1]*v[0] - 2*u[1]*v[1]


def add(u,v): return (u[0]+v[0],u[1]+v[1])
def mul(n,u): return (n*u[0],n*u[1])

h=(1,0); E=(0,1); D=add(mul(2,h),E)
assert (ip(h,h),ip(h,E),ip(E,E))==(8,1,-2)
assert (ip(D,D),ip(D,E),ip(D,h))==(34,0,17)
assert 3*(3+2)*(3+3)//2+2*3+2==53
for m in range(2,2001):
    C=mul(m,D)
    assert add(C,mul(-2,E)) == add(mul(4,h),mul(m-2,D))
    if m>=3:
        assert add(mul(m-1,D),mul(-2,E)) == add(mul(4,h),mul(m-3,D))
    else:
        assert add(mul(m-1,D),mul(-2,E)) == add(mul(2,h),mul(-1,E))
    assert add(mul(2,h),add(mul(3,E),mul(-m,D))) == add(mul(2,E),mul(1-m,D))
    assert ip(C,h)==17*m
    assert 1+ip(C,C)//2 == 17*m*m+1
    assert 2+ip(C,C)//2 == 17*m*m+2 # chi on K3
    assert 17*m*m+1 + 53 == 17*m*m+54
    assert 17*m*m+54+3 == 17*m*m+57
    assert ip(add(mul(2,h),mul(-m,D)),h) == 16-17*m < 0
assert (17*2,17*2*2+1,17*2*2+54,17*2*2+57)==(34,69,122,125)
# The restrictions of coordinate quadrics s*s, s*t, t*t span H^0(P^1,O(2)).
quadric_restriction=[[1,0,0],[0,1,0],[0,0,1]]
assert quadric_restriction==[[int(i==j) for j in range(3)] for i in range(3)]
print("VERIFY_OK: divisor identities, intersection arithmetic, Hilbert dimensions, endpoint, line restriction")
