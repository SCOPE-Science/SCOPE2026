#!/usr/bin/env python3
"""Exact rational arithmetic for a Poisson growing-ball circle comparison.

This script verifies the polynomial integral and rational inequality certificate.
The Poisson void identities and Taylor-remainder inequalities are proved in
RESULT.md; finite checks here are not substitutes for those arguments.
"""
from fractions import Fraction as Q

zero=Q(0)
def add(p,q):
    r=[zero]*max(len(p),len(q))
    for i,c in enumerate(p):r[i]+=c
    for i,c in enumerate(q):r[i]+=c
    return r

def neg(p):return [-c for c in p]
def sub(p,q):return add(p,neg(q))
def mul(p,q):
    r=[zero]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r

def scale(p,c):return [c*a for a in p]
def ev(p,x):return sum((c*x**i for i,c in enumerate(p)),zero)
def integral(p,lo,hi):return sum((c*(hi**(i+1)-lo**(i+1))/Q(i+1) for i,c in enumerate(p)),zero)

u2=[zero,zero,Q(1)]
Ishort=[zero,zero,Q(2)] # union of two disjoint radius-r arcs: integrated length 2u²
Ilong=[-Q(1,64),Q(1,4),Q(1)] # once radius r >=1/8, integrated length u²+u/4-1/64
A=Q(1,8); Z=Q(3,8); D=Q(1,2)
assert ev(Ishort,A)==ev(Ilong,A)==Q(1,32)
assert ev(Ilong,Z)==Q(7,32)
# derivative 4r before A, 2r+1/4 afterwards. At radius Z latter equals 1.
assert Q(4)*A == Q(2)*A+Q(1,4)
assert Q(2)*Z+Q(1,4) ==1
# Euler/alternating-Taylor bracketing: P3(x) <= exp(-x) <= Q2(x).
# These are symbolic polynomial substitution operations only.
def lowexp(x):return add(sub([Q(1)],x),sub(scale(mul(x,x),Q(1,2)),scale(mul(mul(x,x),x),Q(1,6))))
def hiexp(x):return add(sub([Q(1)],x),scale(mul(x,x),Q(1,2)))
P=lowexp(u2)
L=integral(P,zero,D)+integral(sub(P,hiexp(Ishort)),zero,A)+integral(sub(P,hiexp(Ilong)),A,Z)
assert L==Q(29716847,62914560), (L,str(L))
# Antipodal H mean is 5/4 - exp(-1/4). Since exp(-1/4)>=299/384,
# H mean <=181/384.
assert lowexp([Q(1,4)])[0]==Q(299,384)
anti_upper=Q(5,4)-Q(299,384)
assert anti_upper==Q(181,384)
gap=L-anti_upper
assert gap==Q(61807,62914560)>0
# Full support at epsilon=1/1024: difference bounded by
# (diameter 1/2)*(mean count in [tau1,tau1+1/2]=3/2)*epsilon.
mixture_penalty=Q(1,2)*Q(3,2)*Q(1,1024)
assert mixture_penalty==Q(3,4096)
final_gap=gap-mixture_penalty
assert final_gap==Q(15727,62914560)>0
print('Rational certificate PASS')
print('Haar after-first expected extra-time lower bound',L,float(L))
print('Antipodal after-first expected extra-time upper bound',anti_upper,float(anti_upper))
print('Haar minus antipodal certified gap',gap,float(gap))
print('Haar minus full-support mixture certified gap',final_gap,float(final_gap))
