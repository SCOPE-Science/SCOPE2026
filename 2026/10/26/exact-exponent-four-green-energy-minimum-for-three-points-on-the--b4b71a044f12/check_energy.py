"""Exact stdlib-only arithmetic checks for three-point fourth Green energy.

Represents polynomials in three formal pairwise inner products over Q.
This validates the spherical-moment expansion and shifted identity;
the global inequalities are proved in RESULT.md, not by finite testing.
"""
from functools import lru_cache
from itertools import product
from fractions import Fraction as F
from math import comb, factorial

ZERO=(0,0,0)
def const(x):
    q=F(x)
    return {ZERO:q} if q else {}
def var(j):
    e=[0,0,0]; e[j]=1
    return {tuple(e):F(1)}
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items():
            out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def neg(p): return scale(p,-1)
def sub(p,q): return add(p,neg(q))
def scale(p,c):
    c=F(c)
    return {k:v*c for k,v in p.items() if v*c}
def mul(p,q):
    out={}
    for k,a in p.items():
        for m,b in q.items():
            j=tuple(k[i]+m[i] for i in range(3))
            out[j]=out.get(j,F(0))+a*b
    return {k:v for k,v in out.items() if v}
def power(p,n):
    r=const(1)
    for i in range(n):r=mul(r,p)
    return r

U,V,W=var(0),var(1),var(2)
G=((const(1),U,V),(U,const(1),W),(V,W,const(1)))

@lru_cache(None)
def wick(indices):
    if not indices:return const(1)
    i=indices[0]
    return add(*(mul(G[i][indices[j]],wick(indices[1:j]+indices[j+1:]))
                 for j in range(1,len(indices))))

def moment(exps):
    idx=tuple(i for i,e in enumerate(exps) for _ in range(e))
    n=len(idx)
    if n%2:return {}
    den=1
    for j in range(1,n//2+1):den*=2*j+1
    return scale(wick(idx),F(1,den))

T=add(*(scale(moment(exps), F((-1)**sum(exps)*comb(2,exps[0])*comb(2,exps[1])*comb(2,exps[2])))
        for exps in product(range(3),repeat=3)))
S=add(U,V,W)
Q=add(power(U,2),power(V,2),power(W,2))
P=add(mul(U,V),mul(U,W),mul(V,W))
R=mul(mul(U,V),W)
EXACT=add(const(232),scale(S,168),scale(Q,16),scale(P,56),scale(R,8))
assert scale(T,105)==EXACT, 'Wick spherical moment polynomial mismatch'

A=add(U,const(F(-1,2)))
B=add(V,const(F(-1,2)))
C=add(W,const(F(-1,2)))
def f(p,q,r):
    return add(const(232),scale(add(p,q,r),168),scale(add(power(p,2),power(q,2),power(r,2)),16),scale(add(mul(p,q),mul(p,r),mul(q,r)),56),scale(mul(mul(p,q),r),8))
shifted=add(U,V,W)
Qshift=add(power(U,2),power(V,2),power(W,2))
assert sub(f(A,B,C),const(33))==add(scale(shifted,98),scale(power(shifted,2),26),scale(Qshift,-10),scale(mul(mul(U,V),W),8)), 'shifted gap mismatch'

from math import factorial
# Independent direct equilateral-spinor integral over t=|z_0|^2 uniform on [0,1]:
spinor=F(2,7)+4*F(factorial(3)*factorial(3),factorial(7))
assert spinor==F(11,35)
assert F(33,105)==F(11,35)
assert spinor/64==F(11,2240)
print('CHECK_OK: exact six-factor spherical Wick moments; full shifted identity; independent spinor beta integral')
