"""Independent numerical checks of powered graph distances and critical inertia.
Requires Python 3, numpy. These are supplementary checks, not a proof.
"""
from itertools import combinations_with_replacement, product
import math
import numpy as np

def graph(s,rs):
    sizes=[s]+list(rs); N=sum(sizes)
    A=np.zeros((N,N),dtype=int); idx=[list(range(sum(sizes[:i]),sum(sizes[:i+1]))) for i in range(len(sizes))]
    for block in idx:
        for u in block:
            for v in block:
                if u!=v:A[u,v]=1
    for u in idx[0]:
        for block in idx[1:]:
            for v in block:A[u,v]=A[v,u]=1
    D=np.full((N,N),1000,dtype=int);np.fill_diagonal(D,0)
    D[A==1]=1
    for k in range(N):
        for i in range(N):
            for j in range(N):D[i,j]=min(D[i,j],D[i,k]+D[k,j])
    assert np.max(D)<=2
    return D,idx

def root(s,rs):
    def f(a):return (a-1-1/s)*sum(r/(r*(a-1)+1) for r in rs)-1
    lo=1+1/s;hi=2.
    while f(hi)<0:hi*=2
    for _ in range(65):
        mid=(lo+hi)/2
        if f(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

def max_nontrivial_eig(D,a):
    n=len(D);P=np.eye(n)-np.ones((n,n))/n
    M=np.where(D==2,a,np.where(D==1,1.,0.))
    return np.linalg.eigvalsh(P@M@P)[1:] # omit zero mode (not always smallest)

nchecks=0
for s in range(2,7):
    for m in range(2,6):
        for rs in combinations_with_replacement(range(1,5),m):
            if s+sum(rs)>21:continue
            a=root(s,rs);D,idx=graph(s,rs);n=len(D)
            u=np.ones(n)/math.sqrt(n)
            U=np.linalg.svd(np.eye(n)-np.outer(u,u))[0][:,:n-1]
            def ev(x):
                M=np.where(D==2,x,np.where(D==1,1.,0.));return np.linalg.eigvalsh(U.T@M@U)
            below=ev(1+(a-1)*.83);at=ev(a);above=ev(a+(a-1)*.23)
            assert max(below)<1e-8,(s,rs,'below',max(below))
            assert abs(at[-1])<2e-8 and at[-2]<-1e-8,(s,rs,'at',at[-2:])
            assert above[-1]>1e-8,(s,rs,'above',above[-1])
            assert abs((a-1-1/s)*sum(r/(r*(a-1)+1) for r in rs)-1)<1e-11
            # critical equality load with zero total
            z=np.zeros(n)
            for i,ri in enumerate(rs):
                z[idx[i+1]]=(a-1-1/s)/(ri*(a-1)+1)
            z[idx[0]]=-1/s
            assert abs(sum(z))<2e-12
            M=np.where(D==2,a,np.where(D==1,1.,0.))
            assert abs(z@M@z)<1e-8
            nchecks+=6
for s in range(2,8):
  for m in range(2,8):
    for r in range(1,7):
      a=root(s,[r]*m)
      exact=1+(m/s+1/r)/(m-1)
      assert abs(a-exact)<1e-11
      nchecks+=1
# partition majorization: if an upper sorted partition has prefix sums greater than another
for s in range(2,6):
 for m in range(2,6):
  for rs in combinations_with_replacement(range(1,6),m):
   for i in range(m):
    for j in range(i+1,m):
     if rs[j]-rs[i]>=2:
      improved=list(rs);improved[i]+=1;improved[j]-=1
      # more balanced partition -> smaller critical exponent
      assert root(s,improved)<root(s,rs)+1e-9
      nchecks+=1
print('PASS multicore supplementary checks:',nchecks)
