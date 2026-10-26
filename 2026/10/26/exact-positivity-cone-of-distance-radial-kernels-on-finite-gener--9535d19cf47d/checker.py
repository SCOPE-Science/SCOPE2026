#!/usr/bin/env python3
"""Exact spectral and concrete-geometry checks for radial kernels on finite generalized quadrangles.
This program verifies algebraic identities and one independent 30-vertex example;
the proof for arbitrary admissible orders is in RESULT.md.
"""
from itertools import product, combinations
from collections import deque
import sympy as S

s,t,r=S.symbols('s t r',positive=True)
f0,f1,f2,f3,f4=S.symbols('f0 f1 f2 f3 f4',real=True)

P=(s+1)*(s*t+1); L=(t+1)*(s*t+1)
h=s*t*(s+1)*(t+1)/(s+t)
assert S.simplify((S.factor(P-1-h))-(s**2*(s*t+1)/(s+t)))==0
assert S.simplify((S.factor(L-1-h))-(t**2*(s*t+1)/(s+t)))==0

A=f0+(s-1)*f2-s*f4
B=f0+(t-1)*f2-t*f4
C2=(s+t)*(f1-f3)**2
U=f0-(t+1)*f2+t*f4
V=f0-(s+1)*f2+s*f4
A0=f0+s*(t+1)*f2+s**2*t*f4
B0=f0+t*(s+1)*f2+s*t**2*f4
C02=(s+1)*(t+1)*(f1+s*t*f3)**2

fs={f0:1,f1:r,f2:r**2,f3:r**3,f4:r**4}
assert S.simplify((S.factor(A.subs(fs)))-((1-r**2)*(1+s*r**2)))==0
assert S.simplify((S.factor(B.subs(fs)))-((1-r**2)*(1+t*r**2)))==0
assert S.simplify((S.factor((A*B-C2).subs(fs)))-((1-r**2)**2*(1+s*t*r**4)))==0
assert S.simplify((S.factor(U.subs(fs)))-((1-r**2)*(1-t*r**2)))==0
assert S.simplify((S.factor(V.subs(fs)))-((1-r**2)*(1-s*r**2)))==0
assert S.simplify((S.factor(A0.subs(fs)))-((1+s*r**2)*(1+s*t*r**2)))==0
assert S.simplify((S.factor(B0.subs(fs)))-((1+t*r**2)*(1+s*t*r**2)))==0
assert S.simplify((S.factor((A0*B0-C02).subs(fs)))-((1+s*t*r**2)**2*(1-r**2)*(1-s*t*r**2)))==0
print('symbolic six-sector factorization: PASS')

# Independent construction of symplectic generalized quadrangle W(2).
pts=[p for p in product(range(2),repeat=4) if any(p)]
lookup={p:i for i,p in enumerate(pts)}
def sympl(a,b):
    return (a[0]*b[2]+a[2]*b[0]+a[1]*b[3]+a[3]*b[1])%2
lines=set()
for a,b in combinations(pts,2):
    if sympl(a,b)==0:
        c=tuple((x+y)%2 for x,y in zip(a,b))
        lines.add(frozenset([lookup[a],lookup[b],lookup[c]]))
lines=sorted(lines,key=lambda l:sorted(l))
assert len(pts)==len(lines)==15
M=S.zeros(15)
for j,ln in enumerate(lines):
    for i in ln:M[i,j]=1
assert all(sum(M[i,j] for j in range(15))==3 for i in range(15))
assert all(sum(M[i,j] for i in range(15))==3 for j in range(15))
# Direct graph distances, not inferred from geometry identities.
adj=[[] for _ in range(30)]
for i in range(15):
 for j in range(15):
    if M[i,j]:adj[i].append(15+j);adj[15+j].append(i)
dist=[]
for base in range(30):
  d=[-1]*30;d[base]=0;q=deque([base])
  while q:
    u=q.popleft()
    for v in adj[u]:
      if d[v]<0:d[v]=d[u]+1;q.append(v)
  assert set(d)==set(range(5))
  dist.append(d)
assert (M*M.T-3*S.eye(15)).eigenvals()=={6:1,1:9,-3:5}
print('W(2) incidence geometry, 30 shortest-path rows, singular spectra: PASS')

import numpy as np
for vals in [(1,S.Rational(1,2),S.Rational(1,4),S.Rational(1,8),S.Rational(1,16)),
             (1,S.Rational(2,3),S.Rational(4,9),S.Rational(8,27),S.Rational(16,81)),
             (2,-1,3,S.Rational(1,2),-2),
             (S.Rational(3,2),S.Rational(1,5),S.Rational(1,3),-S.Rational(2,7),0)]:
    K=np.array([[float(vals[dist[i][j]]) for j in range(30)] for i in range(30)])
    pvals={f0:vals[0],f1:vals[1],f2:vals[2],f3:vals[3],f4:vals[4],s:2,t:2}
    up=float(U.subs(pvals));vl=float(V.subs(pvals))
    ap=float(A.subs(pvals));bp=float(B.subs(pvals));cp2=float(C2.subs(pvals))
    a0=float(A0.subs(pvals));b0=float(B0.subs(pvals));c02=float(C02.subs(pvals))
    paired=np.linalg.eigvalsh([[ap,cp2**0.5],[cp2**0.5,bp]])
    main=np.linalg.eigvalsh([[a0,c02**0.5],[c02**0.5,b0]])
    pred=sorted([up]*5+[vl]*5+list(paired)*9+list(main))
    eigs=np.linalg.eigvalsh(K)
    assert np.allclose(pred,eigs,atol=2e-10,rtol=1e-11)
    expected_nonneg=all(z>=-1e-11 for z in [up,vl,ap,bp,ap*bp-cp2,a0,b0,a0*b0-c02])
    is_nonneg=min(eigs)>-1e-9
    assert expected_nonneg==is_nonneg
    if vals[1]==S.Rational(1,2):assert sum(abs(eigs)<1e-9)==1
    if vals[1]==S.Rational(2,3):assert not is_nonneg
    print('W(2) five-level radial profile:',vals,'PSD',bool(is_nonneg),'numerical rank',sum(abs(eigs)>1e-9))
print('all independent and symbolic checks: PASS')
