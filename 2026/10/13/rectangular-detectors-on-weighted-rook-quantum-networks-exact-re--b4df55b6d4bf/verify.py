"""Finite checks for absorption on weighted Cartesian complete-graph products."""
import numpy as np
from scipy.linalg import expm

def analytic(m,n,r,s,res):
 a0=min(r,m-1);b0=min(s,n-1)
 rank=(a0+1)*(b0+1)-int(res and r<m and s<n)
 C=np.empty((m,n),float)
 for x in range(m):
  for y in range(n):
   c=(1. if x<r else 1/(m-r))*(1. if y<s else 1/(n-s))
   if res and r<m and s<n:
    v=(1 if x<r else -r/(m-r))-(1 if y<s else -s/(n-s))
    c-=v*v/(m*n*(r/(m-r)+s/(n-s)))
   C[x,y]=c
 return rank,C

def numeric(m,n,r,s,res):
 a,b=(n,m) if res else (1,np.sqrt(2))
 A=np.ones((m,m))-np.eye(m); B=np.ones((n,n))-np.eye(n)
 H=a*np.kron(A,np.eye(n))+b*np.kron(np.eye(m),B)
 D=np.array([i*n+j for i in range(r) for j in range(s)])
 vals,U=np.linalg.eigh(H)
 groups=[]
 for k,v in enumerate(vals):
  if not groups or abs(v-vals[groups[-1][0]])>1e-7:groups.append([k])
  else:groups[-1].append(k)
 bright=np.zeros((m*n,m*n))
 rank=0
 for ks in groups:
  E=U[:,ks];F=E[D,:].conj().T
  S=np.linalg.svd(F,full_matrices=False)
  # Orthonormal basis for detector projections in eigenspace
  uu,ss,vv=S
  q=int((ss>1e-8).sum());rank+=q
  if q:Z=E@uu[:,:q];bright+=Z@Z.conj().T
 return rank,np.diag(bright).reshape((m,n)),H,D,bright

tests=0
for m in range(2,7):
 for n in range(2,7):
  for r in range(1,m+1):
   for s in range(1,n+1):
    for res in [False,True]:
     rank,C=analytic(m,n,r,s,res)
     R,Cnum,*_=numeric(m,n,r,s,res)
     assert R==rank,(m,n,r,s,res,rank,R)
     assert np.max(abs(C-Cnum))<2e-10,(m,n,r,s,res,np.max(abs(C-Cnum)))
     tests+=1
# Dynamics with independently chosen sink rates, two distinct source positions.
loss_checks=0
for m,n,r,s,res in [(2,2,1,1,True),(2,3,1,2,True),(3,3,1,1,False),(3,4,2,3,True),(4,4,2,2,True),(2,4,2,3,False)]:
 R,C,H,D,B=numeric(m,n,r,s,res)
 W=np.zeros((m*n,m*n))
 for t,k in enumerate(D):W[k,k]=0.8+0.17*t
 M=-1j*H-W
 for source in [0,m*n-1]:
  z=expm(1000*M)[:,source]
  survival=float(np.real(np.vdot(z,z)))
  expected=1-C.reshape(-1)[source]
  assert abs(survival-expected)<4e-5,(m,n,r,s,res,source,survival,expected)
  loss_checks+=1
print('VERIFY_OK spectral_rank_and_sitewise_cases='+str(tests)+' direct_loss_cases='+str(loss_checks))
