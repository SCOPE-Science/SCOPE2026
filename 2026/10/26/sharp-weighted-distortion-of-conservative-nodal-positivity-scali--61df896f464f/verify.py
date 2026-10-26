from fractions import Fraction as F
from math import sqrt
import random

def projector(u,w,m):
    # exact weighted projection by sorting candidates
    for k in range(1,len(u)+1):
        active=sorted(range(len(u)), key=lambda j:u[j], reverse=True)[:k]
        tau=(sum(w[j]*u[j] for j in active)-m)/sum(w[j] for j in active)
        z=[max(F(0),u[j]-tau) for j in range(len(u))]
        if sum(w[j]*z[j] for j in range(len(u)))==m:
            return z
    raise AssertionError('No root found')

def norms(u,w): return sum(wj*uj*uj for wj,uj in zip(w,u))

def check(w,u):
    m=sum(a*b for a,b in zip(w,u)); assert m>0
    amin=min(u)
    if amin>=0:return None
    theta=m/(m-amin)
    r=[m+theta*(x-m) for x in u]
    z=projector(u,w,m)
    nd=norms([x-y for x,y in zip(u,r)],w)
    opt=norms([x-y for x,y in zip(u,z)],w)
    assert opt>0
    sw=sorted(w)
    C2=((1-sw[0])*(1-sw[1]))/(sw[0]*sw[1])
    assert nd<=C2*opt, (w,u,nd/opt,C2)
    return float(nd/opt),float(C2)

rng=random.Random(13)
N=0
for n in range(2,9):
 for rep in range(300):
    w0=[rng.randint(1,17) for _ in range(n)]
    w=[F(v,sum(w0)) for v in w0]
    raw=[F(rng.randint(-30,30),10) for _ in range(n)]
    mean=sum(a*b for a,b in zip(w,raw))
    u=[x-mean+1 for x in raw]
    ans=check(w,u)
    N+=1
    if ans is not None: assert ans[0] <= ans[1]+1e-12
    order=sorted(range(n),key=lambda j:w[j]);i,j=order[:2]
    eps=F(1,10**8);delta=F(1,10**4)
    x=[delta]*n
    x[i]=-eps
    x[j]=(1-w[i]*x[i]-sum(w[k]*x[k] for k in range(n) if k not in (i,j)))/w[j]
    result=check(w,x)
    if result is not None and n>=3:
       assert result[0]/result[1]>0.94, (n,w,result)

for n in range(2,11):
 # LGL endpoints weights and sum; compute using scipy Legendre
 from numpy.polynomial.legendre import Legendre
 import numpy as np
 x=np.r_[-1.0,Legendre.basis(n-1).deriv().roots(),1.0]
 P=Legendre.basis(n-1)(x)
 ww=1/(n*(n-1)*P**2)
 assert abs(sum(ww)-1)<1e-12
 assert abs(min(ww)-1/(n*(n-1)))<1e-12
 C=n*(n-1)-1
 print('LGL',n,'ratio constant',C)
print('PASS: exact-rational sampled and sharp-sequence checks',N,'plus 9 LGL quadratures')
