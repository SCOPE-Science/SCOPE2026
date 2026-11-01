#!/usr/bin/env python3
"""Exact cubical-chain verification for two unordered particles on K_{4,4}.
Requires Python 3 with sympy and numpy. All computations are regenerated.
"""
from itertools import combinations
import numpy as np
import sympy as s
from collections import defaultdict
V=list(range(8)); E=[(a,b) for a in range(4) for b in range(4,8)]; eidx={x:i for i,x in enumerate(E)}
C0=list(combinations(V,2)); C1=[(v,e) for v in V for e in E if v not in e];C2=list(combinations(range(16),2)); C2=[(i,j) for i,j in C2 if len(set(E[i]+E[j]))==4]
i0={x:i for i,x in enumerate(C0)};i1={x:i for i,x in enumerate(C1)};i2={x:i for i,x in enumerate(C2)}
print(len(C0),len(C1),len(C2),flush=True)
d1=s.zeros(len(C0),len(C1));d2=s.zeros(len(C1),len(C2))
for ci,(v,e) in enumerate(C1):
 a,b=e;d1[i0[tuple(sorted((v,b)))],ci]=1;d1[i0[tuple(sorted((v,a)))],ci]=-1
for ci,(ei,ej) in enumerate(C2):
 a,b=E[ei];c,d=E[ej]
 # orientation ei then ej: boundary = [b,ej]-[a,ej] - [d,ei]+[c,ei]
 for cell,coef in [((b,E[ej]),1),((a,E[ej]),-1),((d,E[ei]),-1),((c,E[ei]),1)]:d2[i1[cell],ci]+=coef
print('chain',d1*d2==s.zeros(len(C0),len(C2)),flush=True)
r1,r2=d1.rank(),d2.rank();print('CHAIN_RANKS',r1,r2);assert (r1,r2)==(27,60)
# product torus for complementary K2,2 partitions
cycles=[]
for L in combinations(range(4),2):
 Lc=tuple(v for v in range(4) if v not in L)
 for R in combinations(range(4,8),2):
  Rc=tuple(v for v in range(4,8) if v not in R)
  if ((L,R)>(Lc,Rc)): continue
  a,b=L;c,d=R; aa,bb=Lc;cc,dd=Rc
  cyc1={eidx[(a,c)]:1,eidx[(b,c)]:-1,eidx[(b,d)]:1,eidx[(a,d)]:-1}
  cyc2={eidx[(aa,cc)]:1,eidx[(bb,cc)]:-1,eidx[(bb,dd)]:1,eidx[(aa,dd)]:-1}
  z=s.zeros(len(C2),1)
  for i,si in cyc1.items():
   for j,sj in cyc2.items():
    x,y=sorted((i,j));z[i2[(x,y)]]+=si*sj*(1 if i==x else -1)
  assert d2*z==s.zeros(len(C1),1)
  cycles.append((L,R,z))
print('torus count',len(cycles),flush=True)
T=s.Matrix.hstack(*(z for *_,z in cycles))
assert T.rank()==12;print('TORUS_RANK',12)


from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from sympy.matrices.normalforms import smith_normal_form
S=smith_normal_form(T,domain=ZZ);assert [abs(int(S[i,i])) for i in range(12)]==[1]*12
print('TORUS_INTEGRAL_LATTICE_SATURATED',12)
import itertools
from sympy import Rational
# choose twelve independent torus columns as rational basis
idx=list(T.rref()[1]);B=T[:,idx]
piv=list(B.T.rref()[1]); U=B[piv,:].inv()
assert B[piv,:]*U==s.eye(12)
def signed_action(p):
 # vertex permutation for whole K44, respecting or interchanging sides
 imap=[]
 for e in E:
  a,b=sorted((p[e[0]],p[e[1]])); imap.append((eidx[(a,b)],1 if p[e[0]]==a else -1))
 act=[]
 for ei,ej in C2:
  (ii,si),(jj,sj)=imap[ei],imap[ej]
  x,y=sorted((ii,jj));act.append((i2[(x,y)],si*sj*(1 if ii==x else -1)))
 return act
def traceH2(p):
 A=s.zeros(len(C2),12)
 for ci,(target,sign) in enumerate(signed_action(p)):
  for col in range(12):
   if B[ci,col]:A[target,col]+=sign*B[ci,col]
 co=U*A[piv,:]
 assert B*co==A
 return int(s.trace(co))
rep_types=[(0,1,2,3),(1,0,2,3),(1,0,3,2),(1,2,0,3),(1,2,3,0)]

from itertools import permutations

from math import comb
import numpy as np
Bnp=np.array(B.tolist(),dtype=np.int64);U_np=np.array(U.tolist(),dtype=np.int64)
row_index={v:i for i,v in enumerate(piv)}
def character_fast(p):
    act=signed_action(p)
    # only target pivot rows required
    tmp=np.zeros((12,12),dtype=np.int64)
    for i,(target,sign) in enumerate(act):
        if target in row_index:tmp[row_index[target],:]+=sign*Bnp[i,:]
    return int(np.trace(U_np@tmp))
def chi22(p):
    fix=sum(i==v for i,v in enumerate(p)); c2=sum(1 for i in range(4) for j in range(i+1,4) if p[i]==j and p[j]==i)
    return comb(fix,2)+c2-fix

def chi211(p):
    inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    return (-1)**inv*(sum(i==v for i,v in enumerate(p))-1)
from time import monotonic
start=monotonic();perms=list(permutations(range(4)))
for p in perms:
    for q in perms:
        direct=character_fast(tuple(p)+tuple(4+x for x in q))
        predicted=chi22(p)*chi211(q)+chi211(p)*chi22(q)
        assert direct==predicted, ('base',p,q,direct,predicted)
        swap=tuple(4+x for x in p)+tuple(q)
        direct=character_fast(swap)
        assert direct==0,('swap',p,q,direct)
print('ALL_1152_AUTOMORPHISM_CHARACTERS_OK')

S2=smith_normal_form(d2,domain=ZZ)
factors=[abs(int(S2[i,i])) for i in range(60)]
assert factors==[1]*59+[2],factors
print("H1_INTEGRAL_Z9_PLUS_Z2_OK")
print("VERIFY_OK")

# Independent signed Lefschetz cross-check via the one-particle graph cycle module.
for pp in perms:
    for qq in perms:
        for swap_sides in (False,True):
            g=(tuple(4+x for x in pp)+tuple(qq)) if swap_sides else (tuple(pp)+tuple(4+x for x in qq))
            e_images=[]
            for ei,(a,b) in enumerate(E):
                aa,bb=g[a],g[b];x,y=sorted((aa,bb))
                e_images.append((eidx[(x,y)],1 if aa==x else -1))
            trE=sum(sig for ei,(ii,sig) in enumerate(e_images) if ii==ei)
            trV=sum(g[i]==i for i in V)
            trC0=sum(tuple(sorted((g[a],g[b])))==(a,b) for a,b in C0)
            trC1=sum((g[v],E[e_images[eidx[e]][0]])==(v,e) and e_images[eidx[e]][1] for v,e in C1)
            trC2=sum(si*sj*(1 if ii<jj else -1) for ei,ej in C2 for ii,si in [e_images[ei]] for jj,sj in [e_images[ej]] if tuple(sorted((ii,jj)))==(ei,ej))
            independent=trC2-trC1+trC0+trE-trV
            assert independent==character_fast(g),(g,independent,character_fast(g))
print('ALL_1152_INDEPENDENT_LEFSCHETZ_CHECKS_OK')
