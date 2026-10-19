"""Independent finite numerical checks for the stated analytic dynamical calculation.
These checks are not substitutes for the all-size proof in RESULT.md.
"""
import math
from fractions import Fraction
c=(1+math.sqrt(13))/6
kap=2*math.pi/math.acos(c)
A=math.pi*math.sqrt(1-c*c)*(26*c-7)/(12*(4-11*c)*(1-c))
assert 9.03118<kap<9.03120
assert -2.106<A<-2.105
# Exact rational polynomial identity behind the continuum first-mode threshold.
for x in [Fraction(-1,2),Fraction(0),Fraction(1,2),Fraction(3,4),Fraction(1)]:
    lhs=(4*x*x-1)/3-x/2-x*(2*x*x-1)/2
    rhs=(1-x)*(3*x*x-x-1)/3
    assert lhs==rhs

def mode(m,n,ell):
    return sum(math.cos(6*math.pi*r/n)*(1-math.cos(2*math.pi*ell*r/n)) for r in range(1,m+1))

def real_threshold(m):
    lo=9*m
    hi=9.1*m
    assert mode(m,lo,1)<0<mode(m,hi,1)
    for _ in range(48):
        mid=(lo+hi)/2
        if mode(m,mid,1)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

checks=5
for m in (100,200,500):
    root=real_threshold(m)
    M=m+.5
    assert abs(root-(kap*M+A/M))<0.0003
    for n in (math.floor(root),math.ceil(root)):
        if 9*m<=n<=9.1*m:
            sign=mode(m,n,1)
            assert (sign<0)==(n<root)
            for ell in range(2,n//2+1):
                assert mode(m,n,ell)>0
                checks+=1
            checks+=1
print(f'VERIFY_OK; finite mode checks={checks}; kappa={kap:.12f}; A={A:.12f}')
