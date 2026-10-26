#!/usr/bin/env python3
"""Reproducible consistency checks for high-dimensional harmonic run-and-tumble limit.
No external files or online services are required.
"""
from fractions import Fraction
import math
import numpy as np

checks=0

def check(c, why):
    global checks
    if not bool(c):
        raise AssertionError(why)
    checks += 1

# Exact GEM(0,alpha) power-sum identities, checked without sympy.
for a in [Fraction(1, 4),Fraction(1, 2),Fraction(1),Fraction(2),Fraction(3),Fraction(9,2),Fraction(12)]:
    ev2 = Fraction(2)/((a+1)*(a+2))
    ew2 = a/(a+2)
    ev4 = Fraction(24)/((a+1)*(a+2)*(a+3)*(a+4))
    ew4 = a/(a+4)
    ev2w2 = 2*a/((a+2)*(a+3)*(a+4))
    s1=ev2/(1-ew2)
    t1=ev4/(1-ew4)
    s2=(ev4+2*ev2w2*s1)/(1-ew4)
    check(s1==1/(a+1),f'E S alpha {a}')
    check(t1==6/((a+1)*(a+2)*(a+3)),f'E T alpha {a}')
    check(s2==(a+6)/((a+1)*(a+2)*(a+3)),f'E S2 alpha {a}')
    check(s2-s1*s1==2*a/((a+1)**2*(a+2)*(a+3)),f'Var S alpha {a}')
    check(s2-t1==a/((a+1)*(a+2)*(a+3)),f'cross-weight alpha {a}')
    for d in (2,3,8,16,80):
        eq2=s1
        eq4=s2+2*(s2-t1)/d
        ey4=3*s2-6*t1/(d+2)
        kurt=ey4/(s1*s1)-3
        check(eq4-s1*s1 == (s2-s1*s1)+2*(s2-t1)/d, f'Var Q d={d}')
        check(kurt == 6*a/((a+2)*(a+3)) - 36*(a+1)/((d+2)*(a+2)*(a+3)),f'kurt d={d}')

# Independent vector realization: draw P from beta stick-breaking, then directions.
rng=np.random.default_rng(20481020)
def sample(alpha,d,n=7000,K=70):
    p=np.empty((n,K),float)
    remain=np.ones(n,float)
    for j in range(K):
        b=rng.beta(1,alpha,size=n)
        p[:,j]=remain*b
        remain*=1-b
    # Include last residual so weights sum precisely to 1 (truncation error controlled by its second moment).
    p[:,-1]+=remain
    s=(p*p).sum(axis=1)
    t=(p**4).sum(axis=1)
    q=np.empty(n)
    y=np.empty(n)
    block=200
    for first in range(0,n,block):
        stop=min(first+block,n)
        m=stop-first
        vectors=rng.normal(size=(m,K,d))
        vectors/=np.linalg.norm(vectors,axis=2)[:,:,None]
        x=np.einsum('mk,mkd->md',p[first:stop],vectors)
        q[first:stop]=np.einsum('md,md->m',x,x)
        y[first:stop]=math.sqrt(d)*x[:,0]
    return s,t,q,y

for a,d in [(0.5,4),(1.0,12),(3.0,40)]:
    s,t,q,y=sample(a,d)
    # Verify conditional mean-zero sphere cross-term and its finite-dimensional L2 identity.
    exact=2*a/(d*(a+1)*(a+2)*(a+3))
    empirical=np.mean((q-s)**2)
    check(abs(empirical-exact)<0.20*exact, f'radial L2 fluctuation {a},{d}: {empirical} vs {exact}')
    expected_s=1/(a+1)
    check(abs(np.mean(s)-expected_s)<0.035,f'GEM power sum {a}')
    check(abs(np.mean(q)-expected_s)<0.04,f'radius second moment {a},{d}')
    check(abs(np.mean(y*y)-expected_s)<0.06,f'coordinate second moment {a},{d}')

# Fixed finite weights: test the conditional central-limit variance and symmetry.
p=np.array([.47,.27,.17,.09]); p2=(p*p).sum(); p4=(p**4).sum()
for d in (8,64,256):
    n=4500
    z=rng.normal(size=(n,len(p),d))
    z/=np.linalg.norm(z,axis=2)[:,:,None]
    x=np.einsum('k,nkd->nd',p,z)
    fluc=math.sqrt(d)*(np.einsum('nd,nd->n',x,x)-p2)
    target=2*(p2*p2-p4)
    check(abs(np.mean(fluc))<0.09,f'conditional centering d={d}')
    check(abs(np.mean(fluc*fluc)-target)<0.18*target,f'conditional fluctuation variance d={d}')
print('PASS',checks,'assertions; exact GEM identities, finite-d moments and simulated independent spherical directions')
