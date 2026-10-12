#!/usr/bin/env python3
"""Exact arithmetic checks for the Fermat cubic's type-nine prime spectrum.
Python 3.10+, standard library only. Finite verification is not a proof for all primes.
"""
from collections import Counter

def primes_below(n):
    for p in range(2,n):
        if all(p % d for d in range(2,int(p**0.5)+1)):
            yield p

def P_add(P,Q,p):
    if P is None: return Q
    if Q is None: return P
    x,y=P; u,v=Q
    if x==u:
        if (y+v)%p == 0: return None
        slope = (3*x*x*pow(2*y,-1,p))%p
    else:
        slope = ((v-y)*pow(u-x,-1,p))%p
    xx = (slope*slope-x-u)%p
    return xx, (slope*(x-xx)-y)%p

def P_mul(P,n,p):
    R=None
    while n:
        if n&1: R=P_add(R,P,p)
        P=P_add(P,P,p)
        n//=2
    return R

def curve_data(p):
    roots={}
    for y in range(p): roots.setdefault((y*y)%p,[]).append(y)
    n3,n9=1,1
    for x in range(p):
        for y in roots.get((x*x*x-432)%p,()):
            P=(x,y)
            if P_mul(P,9,p) is None:
                n9+=1
                if P_mul(P,3,p) is None: n3+=1
    return n9-n3

def predicted(p):
    if p%9==1:
        return 72 if pow(3,(p-1)//3,p)==1 else 18
    if p%9==8: return 6
    return 0

# Arithmetic in Z[a,b]/(a^3-3,b^6+b^3+1); reduced basis a^i*b^j,
# 0<=i<3, 0<=j<6, sufficient for verifying the stated point identities.
from functools import lru_cache
@lru_cache(None)
def b_reduce(j):
    if j<6: return {j:1}
    res={}
    for e,c in b_reduce(j-3).items(): res[e]=res.get(e,0)-c
    for e,c in b_reduce(j-6).items(): res[e]=res.get(e,0)-c
    return {e:c for e,c in res.items() if c}
def add(A,B):
    out=A.copy()
    for ij,c in B.items():out[ij]=out.get(ij,0)+c
    return {ij:c for ij,c in out.items() if c}
def neg(A):return {ij:-c for ij,c in A.items()}
def sc(A,n):return {ij:n*c for ij,c in A.items() if n*c}
def mul(A,B):
    out={}
    for (i,j),v in A.items():
        for (k,l),w in B.items():
            n=v*w*(3**((i+k)//3))
            for q,c in b_reduce(j+l).items():
                key=((i+k)%3,q)
                out[key]=out.get(key,0)+n*c
    return {ij:v for ij,v in out.items() if v}
def power(A,n):
    R={(0,0):1}
    while n:
        if n&1:R=mul(R,A)
        A=mul(A,A);n//=2
    return R
one={(0,0):1};a={(1,0):1};b={(0,1):1};c3=sc(one,3)
# T4 from Merta--Zieba, arXiv:2406.13802v1, Section 2.
f=add(add(power(b,4),sc(power(b,3),2)),add(neg(b),one))
y=mul(mul(a,b),f)
z=neg(mul(power(a,2),mul(add(add(power(b,2),b),one),add(add(power(b,3),neg(b)),one))))
assert f, 'The alpha coefficient does not vanish'
assert add(add(power(c3,3),power(y,3)),power(z,3))=={}, 'not on Fermat cubic'
q=add(add(power(c3,9),sc(mul(power(c3,6),power(y,3)),6)),
      add(sc(mul(power(c3,3),power(y,6)),3),neg(power(y,9))))
assert q=={}, 'the published degree-nine type-nine factor failed'

cm_kernel=Counter()
for ra in range(3):
    for sa in range(3):
        fixed=0
        for rx in range(9):
            for sx in range(9):
                u=3*(ra*rx-sa*sx)
                v=3*(ra*sx+sa*rx-sa*sx)
                fixed+=(u%9==0 and v%9==0)
        trace=(2*ra-sa)%3
        assert (trace==0)==(fixed in (27,81))
        cm_kernel[fixed]+=1
assert cm_kernel==Counter({9:6,27:2,81:1})

seen=Counter()
for p in primes_below(1100):
    if p<5:continue
    actual=curve_data(p)
    expected=predicted(p)
    assert actual==expected, (p,actual,expected)
    seen[actual]+=1
assert all(seen[v]>0 for v in (0,6,18,72)),seen
print('VERIFY_OK symbolic_T4_on_cubic_and_degree9_factor; primes_5_to_1099='+str(sum(seen.values()))+
      '; observations='+str(sorted(seen.items())))
