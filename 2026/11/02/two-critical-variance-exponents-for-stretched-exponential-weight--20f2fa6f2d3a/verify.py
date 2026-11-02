"""Reproduce finite exact identities and numerical asymptotic diagnostics.

This program is supplemental evidence; it does not establish the infinite-n limits.
Python 3 standard library only.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, lgamma, log

P = {2:F(2,5),3:F(1,3),4:F(3,7),5:F(1,6),6:F(2,9),7:F(1,4)}
weights={1:F(1)}
W=F(1)
for j,p in P.items():
    new_w = W*p/(1-p)
    weights[j]=new_w
    W += new_w

assert all(0 < p < 1 for p in P.values())

checks = 0
for n in range(2,8):
    ED=F(0)
    ED2=F(0)
    for choices in product(*(range(1,j) for j in range(2,n+1))):
        ds={1:0}
        mass=F(1)
        for j,parent in enumerate(choices,start=2):
            ds[j]=1+ds[parent]
            mass*=weights[parent]/sum(weights[i] for i in range(1,j))
        T=sum(ds.values())
        ED+=mass*T
        ED2+=mass*T*T
    v=F(0)
    predicted_mean=F(0)
    predicted_var=F(0)
    for j in range(2,n+1):
        p=P[j]
        predicted_mean += 1+sum(P[k] for k in range(2,j))
        predicted_var += (1+(n-j)*p)**2*v
        v=(1-p*p)*v+p*(1-p)
    assert ED==predicted_mean, ('mean',n)
    checks+=1
    assert ED2-ED*ED==predicted_var,('variance',n,ED2-ED*ED,predicted_var)
    checks+=1

# This recurrence is evaluated as a finite numerical identity, not as a CLT check.
def moment_sums(gamma,c,n):
    v=0.
    S=Q=R=0.
    for j in range(2,n+1):
        p=c*j**(-gamma)
        a=1-j*p
        S+=p*p*v
        Q+=p*a*v
        R+=a*a*v
        v=(1-p*p)*v+p*(1-p)
    return v,n*n*S+2*n*Q+R,S

def beta(a,b):return exp(lgamma(a)+lgamma(b)-lgamma(a+b))

def asymptotic(g,c,n):
    if g<.5:return c*beta(1-g,3)*n**(3-g)
    if g==.5:return 2*c**3/(1+2*c*c)*beta(.5,3)*n**2.5
    if g<2/3:return c**3/(1-g)*beta(2-3*g,3)*n**(4-3*g)
    if g==2/3:return 3*c**3*n*n*log(n)
    return None

print('Exact enumerated tree mean and path-length variance: %d equalities' % checks)
for g in [.25,.5,.60,2/3,.8]:
    c=.6
    n1=100_000;n2=500_000
    v1,var1,S1=moment_sums(g,c,n1)
    v2,var2,S2=moment_sums(g,c,n2)
    if g<=2/3:
        r1=var1/asymptotic(g,c,n1)
        r2=var2/asymptotic(g,c,n2)
        assert r1 > 0, (g, r1)
        assert r2 > r1, (g,r1,r2)
        assert r2 < 2, (g,r2)
        assert v2 > 0
        checks+=4
        print('gamma %.8f : variance/asymptotic @100k = %.6f, @500k = %.6f' % (g,r1,r2))
    else:
        assert S1 > 0
        assert S2 > S1
        assert S2 < 2
        assert var2/n2**2 > var1/n1**2
        checks+=4
        print('gamma %.8f : variance/n^2 @100k = %.6f, @500k = %.6f' % (g,var1/n1**2,var2/n2**2))
print('Total verification assertions: %d' % checks)
