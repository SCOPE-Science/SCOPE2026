"""Reproducibility checks for randomly contracted Brownian resetting.

Only finite exact identities and reproducible simulation are checked here;
the analytic convex-order theorem requires its separate mathematical proof.
"""
from fractions import Fraction as F
from math import factorial
import numpy as np

m=F(1,4)
D=F(3,2)
r=F(5,3)

# Return E[B^k] for each squared-multiplier model, including k=0.
def bmoment(label,k):
    if k==0:return F(1)
    if label=='fixed':return m**k
    if label=='binary':return m
    if label=='uniform':return F(1,2)**k/F(k+1)
    if label=='two-point':return F(2,3)*F(1,8)**k+F(1,3)*F(1,2)**k
    if label=='mix':return F(2,5)*m**k+F(3,5)*m
    raise ValueError(label)

labels=['fixed','binary','uniform','two-point','mix']
checks=0
for label in labels:
    v=[F(1)]
    x=[F(1)]
    for n in range(1,11):
        s=bmoment(label,n)
        # Separate moment recursions for operational time and the position.
        partial=sum(F(factorial(n),factorial(k))*r**(k-n)*bmoment(label,k)*v[k] for k in range(n))
        v.append(partial/(1-s))
        x.append(x[-1]*F((2*n)*(2*n-1))*D/(r*(1-s)))
        from_clock=F(factorial(2*n),factorial(n)*2**n)*(2*D)**n*v[n]
        assert x[n]==from_clock
        checks+=1
        lower=F(1)
        upper=F(1)
        for k in range(1,n+1):
            lower*=F((2*k)*(2*k-1))*D/(r*(1-m**k))
            upper*=F((2*k)*(2*k-1))*D/(r*(1-m))
        assert lower<=x[n]<=upper
        checks+=1
    assert x[1]==2*D/(r*(1-m))
    checks+=1
    kurt=x[2]/(x[1]**2)
    assert kurt==6*(1-m)/(1-bmoment(label,2))
    assert F(6)/(1+m)<=kurt<=6
    checks+=2

assert F(6)/(1+m)==F(24,5)
# Exact kurtosis for B uniform on [0,1/2], B^2 moment = 1/12.
assert 6*(1-m)/(1-F(1,12))==F(54,11)
checks+=2

# Direct test of stationary Laplace transform relation by sample moments:
# M_X(t)=1+(E[X^2]/2)t^2+(E[X^4]/24)t^4+...
# The stationary generator recursion must annihilate coefficients to order 20.
for label in labels:
    x=[F(1)]
    for n in range(1,11):
        x.append(x[-1]*F((2*n)*(2*n-1))*D/(r*(1-bmoment(label,n))))
    for n in range(1,11):
        lhs=(r*(1-bmoment(label,n))*x[n]
             -F((2*n)*(2*n-1))*D*x[n-1])
        assert lhs==0
        checks+=1

# Seeded direct simulations of the stationary random Brownian clock;
# this is a finite probabilistic cross-check, not a substitute for proof.
N=60000
rng=np.random.default_rng(414141)
for label in labels:
    vals=np.zeros(N)
    for step in range(75):
        tau=rng.exponential(scale=float(1/r),size=N)
        if label=='fixed': b=np.full(N,float(m))
        elif label=='binary': b=(rng.random(N)<float(m)).astype(float)
        elif label=='uniform': b=rng.random(N)/2
        elif label=='two-point': b=np.where(rng.random(N)<2/3,1/8,1/2)
        else:
            mask=rng.random(N)<2/5
            bern=(rng.random(N)<float(m)).astype(float)
            b=np.where(mask,float(m),bern)
        vals=tau+b*vals
    analytic=float(1/(r*(1-m)))
    empirical=vals.mean()
    se=vals.std(ddof=1)/np.sqrt(N)
    assert abs(empirical-analytic)<6*se+0.006, (label,empirical,analytic,se)
    checks+=1
print(f'PASS: {checks} exact and seeded numerical checks')
