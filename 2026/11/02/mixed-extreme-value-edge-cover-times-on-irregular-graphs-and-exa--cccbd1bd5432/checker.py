#!/usr/bin/env python3
"""Independent finite checks for edge-coupon coverage of balanced spiders.
Reproduce: python3 checker.py (standard library and sympy)."""
from fractions import Fraction
from itertools import product
from math import comb, exp, log, sqrt
from collections import defaultdict
import sympy as S

Q = S.Symbol('q')

def spiders(k, ell):
    edges=[]
    for a in range(k):
        last=0
        for j in range(1,ell+1):
            v=1+a*ell+(j-1)
            edges.append((last,v));last=v
    return edges

def closed(k,ell):
    p=1-Q
    F=[S.Integer(1),S.Integer(1)]
    for j in range(2,ell):
        F.append(S.expand(p*F[-1]+p*Q*F[-2]))
    return S.expand((p*F[ell-1])**k-(Q*p*p*F[ell-3])**k)

def covered(edges,mask):
    verts={v for e in edges for v in e}
    seen={v for i,e in enumerate(edges) if mask>>i&1 for v in e}
    return verts == seen

def independent_formula(k,ell):
    edges=spiders(k,ell);m=len(edges);res=S.Integer(0)
    for mask in range(1<<m):
        if covered(edges,mask):
            z=mask.bit_count()
            res+=(1-Q)**z * Q**(m-z)
    return S.expand(res)

checks=0
for k,ell in [(2,3),(2,4),(2,5),(3,3),(3,4)]:
    edges=spiders(k,ell); m=len(edges)
    c=closed(k,ell)
    assert S.expand(c-independent_formula(k,ell))==0
    checks+=1
    coeff=S.Poly(c,Q)
    # Independent exact discrete edge-by-edge enumeration over visited masks.
    dp={0:1}
    for t in range(0,8):
        direct=Fraction(sum(v for mask,v in dp.items() if covered(edges,mask)),m**t)
        formula=sum((Fraction(int(a)) * Fraction(m-j,m)**t for (j,),a in coeff.terms()),Fraction())
        assert direct==formula,(k,ell,t,direct,formula)
        checks+=1
        nxt=defaultdict(int)
        for mask,ct in dp.items():
            for e in range(m):
                nxt[mask|(1<<e)]+=ct
        dp=nxt

# Verify recurrence by brute binary words for small lengths and several rational failure rates.
for n in range(0,12):
    for q in [Fraction(1,5),Fraction(2,7),Fraction(4,5)]:
        f=[Fraction(1),Fraction(1)]
        for j in range(2,max(n+1,2)):
            f.append((1-q)*f[-1]+q*(1-q)*f[-2])
        v=sum((q**(n-sum(bits))*(1-q)**sum(bits)
               for bits in product([0,1],repeat=n)
               if all(bits[j] or bits[j+1] for j in range(n-1))),Fraction(0))
        assert v==f[n],(n,q,v,f[n]);checks+=1

# Numerical trend checks: no numerical tests are used as proof of infinite limits.
def F_l_numeric(k,ell,x,regime='critical'):
    D=k*(ell-1)
    u=0.5*log(D)+x if regime=='critical' else log(k)+x
    q=exp(-u);p=1-q
    f0=f1=1.0
    f=[]
    for j in range(ell):
        if j==0:val=f0
        elif j==1:val=f1
        else:
            f0,f1=f1,p*f1+p*q*f0
            val=f1
        f.append(val)
    b=p*f[ell-1];a=q*p*p*f[ell-3]
    return b**k-a**k

for rho in [0.25,1.0,4.0]:
    for ell in [400,1000]:
        k=round(rho*ell)
        for x in [-1.0,0.0,1.0]:
            expected=exp(-sqrt(rho)*exp(-x)-exp(-2*x))
            obs=F_l_numeric(k,ell,x)
            assert abs(obs-expected)<0.08,(rho,ell,x,obs,expected)
            checks+=1
# Supercritical check
for k,ell in [(1600,40),(6400,40)]:
    for x in [-1.,0.,1.]:
        obs=F_l_numeric(k,ell,x,'super')
        assert abs(obs-exp(-exp(-x)))<0.06,(k,ell,x,obs)
        checks+=1
print('OK exact and numerical assertions:',checks)
