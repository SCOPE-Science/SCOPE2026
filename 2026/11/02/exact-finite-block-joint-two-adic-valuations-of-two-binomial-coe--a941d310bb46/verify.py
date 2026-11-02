#!/usr/bin/env python3
"""Exact finite-block carry-distribution checks, without third-party packages."""
from collections import defaultdict
from fractions import Fraction as Q
from math import comb


def population(L):
    d={(0,0,0):1}
    for _ in range(L):
        nd=defaultdict(int)
        for (t,x,y),v in d.items():
            for b in (0,1):
                c=(t+b)//2
                nt=b+c
                nd[(nt,x+b,y+c)]+=v
        d=nd
    joint=defaultdict(int)
    for (t,x,y),v in d.items():
        joint[(x,y+t//2)]+=v
    return dict(joint)


def brute(L):
    joint=defaultdict(int)
    for n in range(1<<L):
        x=n.bit_count()
        y=2*x-(3*n).bit_count()
        # factorial-valuation definition of v2(binomial(3n,n))
        def vfact(t):
            return t-t.bit_count()
        assert y==vfact(3*n)-vfact(n)-vfact(2*n)
        joint[(x,y)]+=1
    return dict(joint)


def moments(joint,L):
    def av(fn):return Q(sum(c*fn(x,y) for (x,y),c in joint.items()),1<<L)
    ex,ey=av(lambda x,y:x),av(lambda x,y:y)
    return ex,ey,av(lambda x,y:x*x)-ex*ex,av(lambda x,y:y*y)-ey*ey,av(lambda x,y:x*y)-ex*ey


def expected(L):
    z=(-1)**L
    tw=Q(1,2**L)
    return (
        Q(L,2),
        Q(L,2)-Q(2,3)+Q(3+z,6)*tw,
        Q(L,4),
        Q(11*L,12)-Q(14,9)+Q(5+z,3)*tw-Q(5+3*z,18)*tw*tw,
        Q(5*L,12)-Q(4,9)+Q(9+7*z,36)*tw,
    )

for L in range(0,16):
    j=population(L)
    assert sum(j.values())==(1<<L)
    assert moments(j,L)==expected(L),(L,moments(j,L),expected(L))
    if L<=14:
        assert j==brute(L),(L,j,brute(L))

# Hankel-minimality: evaluate at u=2,v=3 and verify nonzero 3-by-3 determinant.
def transfer_eval(L,u,v):
    arr=[1,0,0]
    for _ in range(L):
        arr=[arr[0]+arr[1],u*arr[0]+v*arr[2], u*v*arr[1]+u*v*arr[2]]
    return arr[0]+arr[1]+v*arr[2]
F=[transfer_eval(L,2,3) for L in range(5)]
def det3(M):
    a,b,c=M[0];d,e,f=M[1];g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
D=det3([[F[i+j] for j in range(3)] for i in range(3)])
assert D==-2304,(D,F)
print('VERIFY_OK complete_direct_dyadic_levels=0..14 moment_levels=0..15')
print('HANKEL_NONZERO u=2 v=3 det=-2304')
print('example_levels_1_to_5', [sorted(population(L).items()) for L in range(1,6)])
