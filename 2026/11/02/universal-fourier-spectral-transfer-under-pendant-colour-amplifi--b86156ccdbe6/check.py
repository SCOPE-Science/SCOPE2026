#!/usr/bin/env python3
"""Independent small-case exact-enumeration checks for pendant-coloring Fourier Gram transfer."""
from itertools import product
from fractions import Fraction
import math
import numpy as np

checks=0

def verify(label,n,edges,q,s,full=True):
    global checks
    base=[x for x in product(range(q),repeat=n) if all(x[i]!=x[j] for i,j in edges)]
    assert base
    p=np.zeros((n,n),dtype=float)
    for x in base:
        for i in range(n):
            for j in range(n):
                p[i,j]+=(x[i]==x[j])
    p/=len(base)
    r=1/(q-1)
    C=(q*p-1)/(q-1)
    nleaves=n*s
    R=np.zeros((n,nleaves))
    for i in range(n):
        R[i,i*s:(i+1)*s]=1.
    upper=np.hstack([C,-r*C@R])
    lower=np.hstack([-r*R.T@C,(1-r*r)*np.eye(nleaves)+r*r*R.T@C@R])
    G=np.vstack([upper,lower])
    assert np.max(np.abs(G-G.T))<1e-12
    checks+=1
    vals=np.linalg.eigvalsh(C)
    positive_eigs=[]
    for c in vals:
        B=np.array([[c,-r*math.sqrt(s)*c],[-r*math.sqrt(s)*c,1-r*r+s*r*r*c]])
        positive_eigs.extend(np.linalg.eigvalsh(B))
    predicted=np.sort(positive_eigs+[1-r*r]*n*(s-1))
    actual=np.linalg.eigvalsh(G)
    assert np.max(np.abs(predicted-actual))<1e-9,(label,actual,predicted)
    checks+=1
    count=int(np.count_nonzero(np.abs(vals)<1e-9)); countnew=int(np.count_nonzero(np.abs(actual)<1e-9))
    assert count==countnew,(label,count,countnew)
    checks+=1
    if full:
        zz=np.exp(2j*np.pi*np.arange(q)/q)
        F=[]
        for x in base:
            options=[tuple(a for a in range(q) if a!=x[i//s]) for i in range(nleaves)]
            for L in product(*options):
                y=x+L
                F.append(np.array([zz[(a*t)%q] for a in range(1,q) for t in y],dtype=complex))
        F=np.array(F)
        gram=F.conj().T@F/len(F)
        pred=np.kron(np.eye(q-1),G)
        assert np.max(np.abs(gram-pred))<3e-10,(label,np.max(np.abs(gram-pred)))
        checks+=1
    if np.min(vals)>1e-7:
        lminus=lambda c: np.min(np.linalg.eigvalsh(np.array([[c,-r*math.sqrt(s)*c],[-r*math.sqrt(s)*c,1-r*r+s*r*r*c]])))
        lplus=lambda c: np.max(np.linalg.eigvalsh(np.array([[c,-r*math.sqrt(s)*c],[-r*math.sqrt(s)*c,1-r*r+s*r*r*c]])))
        assert abs(actual[0]-lminus(min(vals)))<1e-9
        assert abs(actual[-1]-lplus(max(vals)))<1e-9
        assert actual[-1]/actual[0] > max(vals)/min(vals)
        checks+=3
    print(label,'core',len(base),'new_graph_colors',len(base)*(q-1)**nleaves,'C spectrum',np.round(vals,7).tolist(),'G spectrum range',round(actual[0],8),round(actual[-1],8))

verify('K3 q3 s1',3,[(0,1),(1,2),(0,2)],3,1)
verify('K3 q4 s2',3,[(0,1),(1,2),(0,2)],4,2)
verify('P3 q3 s2',3,[(0,1),(1,2)],3,2)
verify('C4 q3 s1',4,[(0,1),(1,2),(2,3),(3,0)],3,1)
verify('edgeless 3 q4 s2',3,[],4,2)
verify('K4 q4 s1',4,[(i,j) for i in range(4) for j in range(i+1,4)],4,1)
# exact rational first moments for K_n: differences forced unequal -> C_ij=-1/(q-1)
for n in range(2,9):
 for q in range(max(n,3),max(n,3)+5):
  eigmin=(q-n)/(q-1)
  eigmax=q/(q-1)
  rr=1/(q-1)
  for s in [1,2,3,9,27,100]:
   def lam(c):
    tr=1-rr*rr+(1+s*rr*rr)*c
    det=(1-rr*rr)*c
    disc=max(0.,tr*tr-4*det)
    return ((tr-math.sqrt(disc))/2,(tr+math.sqrt(disc))/2)
   if eigmin>0:
    got=lam(eigmax)[1]/lam(eigmin)[0]
    assert got>eigmax/eigmin
    checks+=1
# test s^2 coefficient and strict increasing s
for r in [1/2,1/3,1/5]:
 for a,b in [(0.1,2.),(0.7,1.8),(1.,1.)]:
  hist=[]
  for s in [1,2,10,100,1000,100000]:
   def lam(c):
    tr=1-r*r+(1+s*r*r)*c
    discr=tr*tr-4*(1-r*r)*c
    hi=(tr+math.sqrt(discr))/2
    lo=(1-r*r)*c/hi
    return lo,hi
   cond=lam(b)[1]/lam(a)[0]
   hist.append(cond)
  assert all(hist[i+1]>hist[i] for i in range(len(hist)-1))
  coeff=b*r**4/(1-r*r)
  assert abs(hist[-1]/100000**2/coeff-1)<0.01
  checks+=2
print('ALL PASSED', checks,'assertion groups')
