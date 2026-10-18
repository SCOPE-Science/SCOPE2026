"""Reproduce spectral and exact arithmetic checks for two-price two-block diffusion.
Usage: python verify.py. Requires Python >=3.10 and NumPy >=1.24.
"""
from fractions import Fraction as F
from itertools import combinations
import numpy as np

checks = 0

def ck(ok, msg='check'):
    global checks
    if not ok: raise AssertionError(msg)
    checks += 1

def th(p,q):
    return F(2*p*q, 2*p*q-p-q), F(2*p,p-1) if p>q else F(p,p-1)

def solve(p,q,t,B=F(1)):
    t=F(t); B=F(B); N=p+q
    lo,hi=th(p,q)
    if t<lo:
        z=B*N/(p*q+t*(p*(p-1)+q*(q-1))/2)
        a=b=c=z/N
    elif p>q and t<hi:
        z=B/(q+t*F((p-1)*(p-q),2*p))
        a=z/p; b=z*F(p-q,p*p);c=F(0)
    else:
        z=B/p; a=z/q; b=c=F(0)
    return z,a,b,c

def lap(p,q,a,b,c):
    n=p+q
    L=np.zeros((n,n),dtype=float)
    for i,j in combinations(range(n),2):
        w=b if j<p else c if i>=p else a
        w=float(w)
        L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
    return L

def edge_counts(p,q):
    return p*q, p*(p-1)//2,q*(q-1)//2

for p in range(2,9):
  for q in range(2,p+1):
    t0,t1=th(p,q)
    ck(t0>0 and t1>=t0,'threshold order')
    candidates=[t0/2,t0,F(t0+t1,2),t1,2*t1] if p>q else [t0/2,t0,2*t0]
    for t in candidates:
      for B in (F(1), F(17,5)):
        z,a,b,c=solve(p,q,t,B)
        # Boundaries can have several optima. The chosen endpoint is valid.
        E0,EA,EB=edge_counts(p,q)
        ck(E0*a+t*(EA*b+EB*c)==B,'exact budget')
        ck(a>=0 and b>=0 and c>=0,'nonnegative weights')
        ck(min((p+q)*a,q*a+p*b,p*a+q*c)==z,'exact spectral branches')
        ck(abs(np.linalg.eigvalsh(lap(p,q,a,b,c))[1]-float(z))<1e-9,'full matrix eigenvalue')
        # The aggregate Rayleigh bound for an arbitrary nonuniform feasible weight:
        # choose rational weights and normalize its actual expense to B.
        N=p+q
        rng=np.random.default_rng(10000+37*p+19*q+int(t*100))
        for k in range(4):
          raw=[F(int(x),1000) for x in rng.integers(1,400,size=N*(N-1)//2)]
          pairs=list(combinations(range(N),2))
          cost=sum((t if (i<p)==(j<p) else F(1))*w for (i,j),w in zip(pairs,raw))
          weights=[B*w/cost for w in raw]
          L=np.zeros((N,N),dtype=float); C0=CA=CB=F(0)
          for (i,j),w in zip(pairs,weights):
            if i<p and j<p:CA+=w
            elif i>=p and j>=p:CB+=w
            else:C0+=w
            wf=float(w)
            L[i,i]+=wf;L[j,j]+=wf;L[i,j]-=wf;L[j,i]-=wf
          l=np.linalg.eigvalsh(L)[1]
          bounds=[F(N,p*q)*C0,C0/F(p)+2*CA/F(p-1),C0/F(q)+2*CB/F(q-1)]
          ck(l<=float(min(bounds))+1e-9,'unrestricted Rayleigh upper bounds')
          ck(l<=float(z)+1e-9,'global optimum numerical stress')

# An explicit unequal-column, nonuniform global optimizer in the high-price regime.
p,q=3,2
B=F(1); U=B/p
cols=[F(11,60), F(9,60)]
ck(sum(cols)==U)
ck((p+2)*cols[0]*cols[1]>=U*U,'exact asymmetric certificate')
L=np.zeros((p+q,p+q))
for i in range(p):
 for j,u in enumerate(cols):
  k=p+j;w=float(u)
  L[i,i]+=w;L[k,k]+=w;L[i,k]-=w;L[k,i]-=w
ck(abs(np.linalg.eigvalsh(L)[1]-float(U))<1e-10,'asymmetric global optimum')
print(f'PASS: {checks} arithmetic and full-matrix checks')
