#!/usr/bin/env python3
"""Reproducible finite checks of prime-torus actuator-placement formulas.
Uses independent real eigenspace testing and Fourier modal restrictions; mathematical
proof covers all primes, whereas tests only corroborate finite cases.
"""
import numpy as np
from math import cos,pi
from collections import defaultdict

def modal_groups(p,a,b):
    h=(p-1)//2
    lamb=[2-2*cos(2*pi*i/p) for i in range(h+1)]
    groups=[]
    for i in range(h+1):
        for j in range(h+1):
            ev=a*lamb[i]+b*lamb[j]
            modes=[(x,y) for x in ([0] if i==0 else [i,-i])
                         for y in ([0] if j==0 else [j,-j])]
            found=next((g for g in groups if abs(ev-g[0])<1e-9),None)
            if found is None:groups.append([ev,modes])
            else:found[1].extend(modes)
    return groups

def pbhranks(p,a,b,site):
    groups=modal_groups(p,a,b)
    for eig,modes in groups:
        Q=np.array([[np.exp(2j*pi*(x*k+y*l)/p) for k,l in modes] for x,y in site])
        sing=np.linalg.svd(Q,compute_uv=False)
        rank=int(sum(s>1e-8 for s in sing))
        if rank!=len(modes): return False,(eig,len(modes),rank)
    return True,(len(groups),max(len(v) for _,v in groups))

def laplacian(p,a,b):
    n=p*p; L=np.zeros((n,n),dtype=float)
    for x in range(p):
      for y in range(p):
        v=x*p+y
        for xx,yy,c in [((x+1)%p,y,a),(x,(y+1)%p,b)]:
          w=xx*p+yy
          L[v,v]+=c;L[w,w]+=c;L[v,w]-=c;L[w,v]-=c
    return L

def full_check(p,a,b,site):
    L=laplacian(p,a,b)
    ev,V=np.linalg.eigh(L)
    ix=np.array([x*p+y for x,y in site])
    groups=[]
    for k,e in enumerate(ev):
       if not groups or abs(e-ev[groups[-1][-1]])>1e-8:groups.append([k])
       else:groups[-1].append(k)
    for inds in groups:
       Q=V[ix,:][:,inds]
       rank=np.linalg.matrix_rank(Q,tol=1e-8)
       if rank!=len(inds):return False,(ev[inds[0]],len(inds),rank)
    return True,(len(groups),max(map(len,groups)))

def main():
    n=0
    for p in [5,7,11]:
      twox2=[(x,y) for x in range(2) for y in range(2)]
      twox4=[(x,y) for x in range(2) for y in range(4)]
      for a,b in [(1,2),(2,1),(2,3),(4,7),(1001,1000),(1,1001)]:
        ok,details=pbhranks(p,a,b,twox2)
        assert ok,(p,a,b,details)
        assert details[1]==4,(p,a,b,details)
        n+=2
        # Full matrix is independent of the analytic Fourier eigenvalue formula
        if p<=7:
          ok,det=full_check(p,a,b,twox2)
          assert ok and det[1]==4,(p,a,b,det)
          n+=2
      ok,details=pbhranks(p,1,1,twox4)
      assert ok and details[1]==8,(p,details)
      n+=2
      if p<=7:
          ok,det=full_check(p,1,1,twox4)
          assert ok and det[1]==8,(p,det)
          n+=2
      # PBH lower bound: fewer than maximum multiplicity cannot span that eigenspace
      assert max(len(v) for _,v in modal_groups(p,1,1))==8
      n+=1
      assert max(len(v) for _,v in modal_groups(p,4,7))==4
      n+=1
      # Random symmetric shifts preserve controllability because eigenspaces unchanged.
      for shift in [-3.0,0.0,2.5]:
          D=laplacian(p,4,7)+np.eye(p*p)*shift
          w=np.linalg.eigvalsh(D)
          base=np.linalg.eigvalsh(laplacian(p,4,7))
          assert np.max(np.abs(w-(base+shift)))<1e-8
          n+=1
    print('PASS:',n,'independent modal/full-matrix/multiplicity/shift checks; primes 5,7,11')
if __name__=='__main__':main()
