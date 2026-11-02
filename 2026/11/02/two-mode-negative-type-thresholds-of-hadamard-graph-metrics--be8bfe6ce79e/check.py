#!/usr/bin/env python3
"""Reproducible independent finite checks of the distance-power spectrum.
Requires numpy and scipy; analytical theorem does not rely on finite tests.
"""
import collections, math
from fractions import Fraction as Q
import numpy as np
from scipy.linalg import hadamard
from scipy.optimize import brentq

def paley(q):
    assert q % 4 == 3
    residues={x*x % q for x in range(1,q)}
    def chi(x):
        x %= q
        return 0 if x==0 else (1 if x in residues else -1)
    Q=np.array([[chi(i-j) for j in range(q)] for i in range(q)],dtype=int)
    H=np.block([[np.ones((1,1),dtype=int),np.ones((1,q),dtype=int)],
                [np.ones((q,1),dtype=int),Q-np.eye(q,dtype=int)]])
    return H

def graph_data(H):
    k=len(H)
    assert np.array_equal(H@H.T,k*np.eye(k,dtype=int))
    N=4*k
    A=np.zeros((N,N),dtype=int)
    for i in range(k):
      for j in range(k):
       for s in (0,1):
        # Row sign + for s=0, - for s=1; column sign product.
        cs = s if H[i,j] == 1 else 1-s
        x=2*i+s;y=2*k+2*j+cs
        A[x,y]=A[y,x]=1
    assert np.all(A.sum(axis=0)==k)
    D=np.zeros((N,N),dtype=int)
    for v in range(N):
      q=collections.deque([v]);dist={v:0}
      while q:
       u=q.popleft()
       for w in np.flatnonzero(A[u]):
        if w not in dist:
         dist[w]=dist[u]+1;q.append(w)
      assert len(dist)==N
      D[v,:]=[dist[z] for z in range(N)]
    assert np.max(D)==4
    assert np.array_equal(D,D.T)
    return A,D

def distance_polynomials(k,theta):
    return np.array([1,theta,2*(theta*theta-k)/k,
      theta*(2*theta*theta-k*k-k)/(k*(k-1)),
      (k**3-2*k*k*theta*theta-k*k+2*theta**4)/(k*k*(k-1))],dtype=float)

def eig_formula(k,p):
    return {'sqrt': math.sqrt(k)*(1-3**p)-4**p,
    'zero':4**p-2*2**p,
    '-sqrt':math.sqrt(k)*(3**p-1)-4**p,
    '-k':k*(2*2**p-1-3**p)+4**p-2*2**p}

def roots(k):
    f=lambda p:eig_formula(k,p)['-k']
    g=lambda p:eig_formula(k,p)['-sqrt']
    if k==4:return (1.,1.)
    return brentq(f,.00000001,.9999,xtol=1e-13),brentq(g,.00000001,1.,xtol=1e-13)

if __name__=='__main__':
    # Exact rational bracketing certificate for the order-12 mode switch.
    boxes={2:(1265756,1265757),3:(1452851,1452852),4:(1602139,1602140)}
    for base,(l,u) in boxes.items():
      lo=Q(l,10**6);hi=Q(u,10**6)
      assert lo**50<base**17<hi**50
    xlo=Q(1265756,10**6); yhi=Q(1452852,10**6)
    zlo=Q(1602139,10**6);shi=Q(3464102,10**6)
    assert Q(3464101,10**6)**2<12<shi**2
    assert 22*xlo-12*yhi+zlo-12>0
    assert shi*(yhi-1)-zlo<0
    # Exact square-root enclosures prove the order-8 mode switch.
    a_lo=Q(1414213,10**6);a_hi=Q(1414214,10**6)
    b_lo=Q(1732050,10**6);b_hi=Q(1732051,10**6)
    assert a_lo*a_lo<2<a_hi*a_hi and b_lo*b_lo<3<b_hi*b_hi
    assert 14*a_hi-8*b_lo-6<0
    assert 2*a_lo*(b_lo-1)-2>0
    ncases=0
    for H in [hadamard(4),hadamard(8),paley(11),hadamard(16),paley(19)]:
      k=len(H)
      A,D=graph_data(H)
      ev=np.linalg.eigvalsh(A)
      expected=np.array([-k]+[-math.sqrt(k)]*k+[0.]*(2*k-2)+[math.sqrt(k)]*k+[k])
      assert np.max(np.abs(ev-expected))<1e-9
      rho,sig=roots(k)
      for p in [0.05,0.2,0.4,0.7,1., min(rho,sig)]:
       M=np.zeros_like(D,dtype=float)
       for j in range(1,5):M+=j**p*(D==j)
       # independently calculate all nontrivial eigenvalues by centered restriction
       J=np.eye(4*k)-np.ones((4*k,4*k))/(4*k)
       evpow=np.linalg.eigvalsh(-.5*J@M@J)
       expected_nontriv=[]
       terms=eig_formula(k,p)
       for name,mul in [('sqrt',k),('zero',2*k-2),('-sqrt',k),('-k',1)]:
         expected_nontriv += [-.5*terms[name]]*mul
       target=sorted(expected_nontriv+[0.])
       assert np.max(np.abs(evpow-np.array(target)))<1e-8
       ncases+=1
      if k>4:
       assert 0<min(rho,sig)<1
      print(f'order={k} roots_rho_sigma={rho:.12g},{sig:.12g} critical={min(rho,sig):.12g}')
    print(f'HADAMARD_NEGATIVE_TYPE_CHECK_OK cases={ncases}')
