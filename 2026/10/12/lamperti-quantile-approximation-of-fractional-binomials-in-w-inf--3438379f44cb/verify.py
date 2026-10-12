#!/usr/bin/env python3
"""Finite numerical checks of the displayed Bernoulli-quantile construction.

Uses the Python standard library only. No asymptotic theorem is inferred from these samples.
"""
import math
from math import comb

def parameter(alpha, v):
    z = (2.0/alpha)*math.atanh(
        math.tan(math.pi*alpha*(v-0.5)) /
        math.tan(math.pi*alpha/2.0))
    return 1.0/(1.0+math.exp(-z))

def cgf_approx(alpha, t, samples=20000):
    h = 1.0/samples
    return alpha*h*sum(math.log1p(parameter(alpha,(j+0.5)*h)*math.expm1(t)) for j in range(samples))

for alpha in (0.4,2.0/3.0,0.85):
    ps=[parameter(alpha,(j+0.5)/999) for j in range(999)]
    assert 0<ps[0]<0.5<ps[-1]<1
    assert all(ps[j]<ps[j+1] for j in range(998))
    assert max(abs(ps[j]+ps[-j-1]-1) for j in range(999))<1e-13
    for t in (-3.,-1.,0.,1.,3.):
        lhs=cgf_approx(alpha,t)
        rhs=math.log1p(math.exp(alpha*t))-math.log(2)
        assert abs(lhs-rhs)<3e-5,(alpha,t,lhs,rhs)

def poisson_binomial(probs):
    a=[1.0]
    for p in probs:
        b=[0.0]*(len(a)+1)
        for j,v in enumerate(a):
            b[j]+=v*(1-p)
            b[j+1]+=v*p
        a=b
    return a

def quantile_distance(n):
    # For U=(2/3)Bin(3n,1/2), V=sum(2n independent Bernoullis).
    alpha=2.0/3.0
    probs=[parameter(alpha,(j+0.5)/(2*n)) for j in range(2*n)]
    vpmf=poisson_binomial(probs)
    upmf=[comb(3*n,j)/2.0**(3*n) for j in range(3*n+1)]
    vc=[];uc=[];sv=su=0.0
    for z in vpmf: sv+=z;vc.append(sv)
    for z in upmf: su+=z;uc.append(su)
    assert abs(sum(vpmf)-1)<1e-12
    assert abs(sum(upmf)-1)<1e-12
    assert abs(sum(probs)-n)<1e-12
    # Determine the monotone quantile displacement on each CDF breakpoint interval.
    points=sorted(set([0.0,1.0]+[min(1.,max(0.,x)) for x in vc[:-1]+uc[:-1]]))
    ans=0.0
    for q0,q1 in zip(points,points[1:]):
        if q1<=q0: continue
        q=(q0+q1)/2
        j=next(j for j,x in enumerate(vc) if x>=q)
        k=next(k for k,x in enumerate(uc) if x>=q)
        ans=max(ans,abs(j-alpha*k))
    return ans

values={n:quantile_distance(n) for n in (1,2,3,5,8,12)}
assert all(0<=v<=1.4 for v in values.values()),values
print('VERIFY_OK alpha=0.666666666667 n12_distance=%.12f mixture_checks=15' % values[12])
