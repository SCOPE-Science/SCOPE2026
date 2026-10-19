#!/usr/bin/env python3
"""Reproduce finite stopping laws and numeric Gumbel comparisons for fresh Gaussian block tests.
This code implements the stated spectral-flat matrix model only; infinite limits use proof.
Dependencies: Python 3, NumPy, SciPy.
"""
import math
import numpy as np
from scipy.stats import chi2
from scipy.optimize import brentq

rng=np.random.default_rng(20261015)
checks=0

def exact_p(n,q,b):
    grid=np.arange(n, -1, -b,dtype=int)
    p=np.ones(grid.size)
    keep=grid>0
    p[keep]=chi2.cdf(b*q, b*grid[keep]);
    return grid,p

def stopping_pmf(n,q,b):
    grid,p=exact_p(n,q,b)
    masses=[]; survive=1.
    for prob in p:
        masses.append(survive*prob)
        survive*=1-prob
    assert np.isclose(sum(masses),1,atol=1e-10)
    return grid,np.asarray(masses)

for n,b,q in [(4,1,2),(8,2,4),(12,3,6),(24,4,12),(50,1,30)]:
    m,p=stopping_pmf(n,q,b)
    assert abs(p.sum()-1)<1e-12
    for i in range(len(m)):
        # Independent-event survival characterizes the complete stopping law.
        assert np.isclose(p[i],(1-exact_p(n,q,b)[1][:i]).prod()*exact_p(n,q,b)[1][i],atol=1e-12)
        checks+=1
    count=120000
    # Draw one independent Gaussian block statistic per possible remaining rank,
    # stopping on the first successful test.
    draws=np.stack([rng.chisquare(df=int(b*z),size=count)/b if z else np.zeros(count) for z in m])
    observed=np.argmax(draws<=q,axis=0)
    means=((m[observed]-np.dot(m,p))**2).mean()
    assert abs(m[observed].mean()-np.dot(m,p))<4*math.sqrt(means/count)
    for i in range(len(m)):
        # conservative 6-sigma plus discretization tolerance
        f=np.mean(observed==i)
        se=math.sqrt(p[i]*(1-p[i])/count)
        assert abs(f-p[i])<7*se+1e-4,(n,b,q,i,f,p[i])
        checks+=1
print('FINITE',checks,'chi-square/product and Monte Carlo comparisons passed')

# Actual QR/orthogonal updates; tests are normalized Gaussian block sketches.
for n,b in [(8,1),(12,2),(16,4)]:
  for rep in range(32):
    Q=np.empty((n,0))
    T=None
    q=n//2
    for step in range(n//b+1):
      P=np.eye(n)-Q@Q.T
      Omega=rng.standard_normal((n,b))/math.sqrt(b)
      Y=P@Omega
      assert np.isclose(np.linalg.norm(P,'fro')**2,n-Q.shape[1],atol=1e-8)
      checks+=1
      if np.linalg.norm(Y,'fro')**2 <= q or Q.shape[1]==n:
        T=Q.shape[1]
        break
      nextQ,_=np.linalg.qr(Y)
      Q=np.column_stack((Q,nextQ[:,:b]))
      assert np.allclose(Q.T@Q,np.eye(Q.shape[1]),atol=1e-9)
      checks+=1
    assert T is not None
print('MATRIX',checks,'projector rank/Q orthogonality checks passed')

def beta(q,b):
    rhs=math.log(q/(math.pi*b**3))
    return brentq(lambda z:z*z+4*math.log(z)-rhs, 1e-6,100)

def finite_gumbel_cdf(n,q,b,x):
    z=beta(q,b)
    cutoff=q+math.sqrt(2*q/b)*(z+x/z)
    # threshold for M < cutoff, which means no success at ranks >= cutoff.
    start=int(math.ceil(cutoff/b))*b
    dims=np.arange(start,n+1,b,dtype=np.int64)
    if not len(dims):return 1.
    p=chi2.cdf(b*q,b*dims)
    return math.exp(np.log1p(-p).sum())

for q in [1000,10000,100000,1000000]:
 b=1; n=2*q
 z=beta(q,b)
 for x in [-1,0,1]:
    actual=finite_gumbel_cdf(n,q,b,x)
    target=math.exp(-math.exp(-x))
    assert 0 <= actual<=1 and 0<=target<=1
    checks+=1
    print('ASYMPT',q,b,x,'beta=',round(z,4),'finite_CDF=',round(actual,6),'limit=',round(target,6),'absdiff=',round(actual-target,6))
 grid,pmf=stopping_pmf(n,q,b)
 print('EARLY_PROB',q,'=',float(pmf[grid>q].sum()))
for n,q in [(1024,800),(4096,3072)]:
 for b in [1,2,4,8,16,32]:
    ranks,pmf=stopping_pmf(n,q,b)
    risk=float(pmf[ranks>q].sum())
    assert -1e-10<=risk<=1+1e-10
    checks+=1
    print('FAILURE_EXACT',n,q,b,format(risk,'.10f'))
print('TOTAL',checks,'checks passed')
