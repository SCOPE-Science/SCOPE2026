"""Reproducible checks for sparse multiway threshold-witness collisions.

Run: python verify.py (requires NumPy for the Monte Carlo cross-check).
All assertions are finite checks; the infinite-dimensional claims use analytic proofs.
"""
import itertools
import math
from fractions import Fraction
from functools import lru_cache
import numpy as np

CHECKS=0

def check(x, msg=''):
    global CHECKS
    if not bool(x):
        raise AssertionError(msg)
    CHECKS += 1

def hall(mask_list, quotas):
    r=len(mask_list)
    for subset in range(1,1<<r):
        union=0
        demand=0
        for i in range(r):
            if subset & (1<<i):
                union|=mask_list[i]
                demand+=quotas[i]
        if union.bit_count() < demand:
            return False
    return True

def brute(mask_list,quotas):
    @lru_cache(None)
    def dfs(i,used):
        if i==len(mask_list):
            return True
        avail=mask_list[i] & ~used
        if avail.bit_count() < quotas[i]:
            return False
        bits=[j for j in range(8) if avail & (1<<j)]
        for sub in itertools.combinations(bits,quotas[i]):
            m=sum(1<<j for j in sub)
            if dfs(i+1,used|m):return True
        return False
    return dfs(0,0)

def exact_defect(n,r,quotas):
    numerator=0
    totalevent=0
    allbits=0
    for masks in itertools.product(range(1<<n),repeat=r):
        wt=2**sum(m.bit_count() for m in masks) * 3**(n*r-sum(m.bit_count() for m in masks))
        allbits+=wt
        if all(m.bit_count()>=k for m,k in zip(masks,quotas)):
            totalevent+=wt
            if not hall(masks,quotas):
                numerator+=wt
    den=5**(n*r)
    check(allbits==den, 'probability normalization')
    one=Fraction(0)
    for m in range(1<<n):
        if m.bit_count()>=quotas[0]:
            one+=Fraction(2**m.bit_count()*3**(n-m.bit_count()),5**n)
    expected=Fraction(1)
    for k in quotas:
        q=Fraction(sum(math.comb(n,j)*2**j*3**(n-j) for j in range(k,n+1)),5**n)
        expected*=q
    check(Fraction(totalevent,den)==expected, 'factorization')
    check(0<=numerator<=totalevent,'nonnegative defect')
    return Fraction(numerator,den)

# Exhaustive witness-versus-Hall verification, independent implementations.
for n,r,quotas in [
    (2,2,(1,1)),(3,2,(2,1)),(4,2,(3,2)),
    (3,3,(1,1,1)),(4,3,(1,2,1)),(4,3,(2,2,2)),
    (4,3,(3,1,2))]:
    for masks in itertools.product(range(1<<n),repeat=r):
        check(hall(masks,quotas)==brute(masks,quotas), 'Hall matching equivalence')

for n,r,k in [(4,3,(2,2,2)),(5,2,(2,3))]:
    x=exact_defect(n,r,k)
    check(x>0,'positive finite defect')
    print('Exact defect:',n,r,k,str(x),'=',float(x))

# Analytic one-dimensional Gaussian integral for r=2, a=b=0.
def normcdf(x):
    return 0.5*(1+math.erf(x/math.sqrt(2)))
def normpdf(x):
    return math.exp(-x*x/2)/math.sqrt(2*math.pi)
def gauss_pair_defect(t,n=4000):
    h=t/n
    def f(x):return normpdf(x)*(normcdf(t-x)-0.5)
    return h/3*(f(0)+f(t)+4*sum(f((2*j-1)*h) for j in range(1,n//2+1))
                +2*sum(f(2*j*h) for j in range(1,n//2)))

for t in (0.2,0.5,1.0,2.0,5.0):
    x=gauss_pair_defect(t)
    check(0<x<0.25,'positive bounded pair defect')
    print('Gaussian pair defect:',t,'%.12f'%x)
check(abs(gauss_pair_defect(1.0)-0.0677300307008491)<1e-11,'analytic calibration')

# Quantitative finite-n to Gaussian-limit comparisons for r=2,3.
# Each coordinate has independent r-bit pattern with the exact Bernoulli product law.
rng=np.random.default_rng(20261027)
for r,a in [(2,(0.,0.)),(3,(0.,0.,0.))]:
    n=100000
    p=n**(-1/3)
    s=math.sqrt(n*p*(1-p))
    quota=math.ceil(n*p)
    patterns=np.arange(1<<r,dtype=np.int64)
    pr=np.array([p**int(v).bit_count()*(1-p)**(r-int(v).bit_count()) for v in patterns])
    M=45000
    table=rng.multinomial(n,pr,size=M)
    totals=np.column_stack([table[:,(patterns&(1<<i))!=0].sum(axis=1) for i in range(r)])
    all_ok=np.all(totals>=quota,axis=1)
    disjoint=all_ok.copy()
    for J in range(1,1<<r):
        indices=[i for i in range(r) if (J>>i)&1]
        union=table[:,(patterns & J)!=0].sum(axis=1)
        disjoint &= union>=len(indices)*quota
    finite=float(np.mean(all_ok & ~disjoint))
    K=900000
    Z=rng.standard_normal((K,r))
    E=Z+np.array(a)[None,:]
    gaussian=np.all(E>=0,axis=1)
    for J in range(3,1<<r):
        if J.bit_count()<2:continue
        ids=[i for i in range(r) if (J>>i)&1]
        gaussian &= E[:,ids].sum(axis=1)>=math.comb(len(ids),2)
    limit=1-float(np.mean(gaussian))-float(1-np.mean(np.all(E>=0,axis=1)))
    check(abs(finite-limit)<0.02,'finite-n Gaussian Hall polytope')
    if r==2:
        check(abs(limit-gauss_pair_defect(1.0))<0.004,'r2 limit versus analytic integral')
    print('Finite-vs-Gaussian:',r,'finite=%.6f'%finite,'Gaussian=%.6f'%limit)

print('PASS',CHECKS,'assertions')
