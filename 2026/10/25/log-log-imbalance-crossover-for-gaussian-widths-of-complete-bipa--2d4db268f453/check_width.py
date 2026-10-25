#!/usr/bin/env python3
"""Independent finite support checks and limiting-functional numerical diagnostics.
Run: python check_biclique_width.py
Requires only Python standard library.
"""
import math,random,itertools,statistics
random.seed(1729)

def subset_width(v,which):
    n=len(v); ans=0.0
    for mask in range(1,1<<n):
        bits=[j for j in range(n) if mask>>j&1]
        if which=='all' or (which=='biclique' and (len(bits)==1 or (min(bits)<which_p and max(bits)>=which_p))):
            d=[v[j] for j in bits]
            ans+=max(d)-min(d)
    return ans

def H(v):
    z=sorted(v,reverse=True);m=len(z)
    return sum(2.0**(-j)*(z[j-1]-z[m-j]) for j in range(1,m+1))

cases=0
for p in range(1,5):
    for q in range(p,6):
        if p+q>8:continue
        which_p=p
        for i in range(40):
            v=[random.gauss(0,1) for _ in range(p+q)]
            lhs=subset_width(v,'biclique')/2**(p+q)
            rhs=H(v)-2**(-p)*H(v[p:])-2**(-q)*H(v[:p])
            assert math.isclose(lhs,rhs,rel_tol=4e-12,abs_tol=1e-12),(p,q,lhs,rhs)
            cases+=1
print('EXACT_SUPPORT_PASS',cases,'sampled vectors with exhaustive subset supports, dimensions 2..8')

# Poisson extreme points are -log of the arrival times of a unit-rate Poisson process.
M=60000;K=38
sample=[]
for j in range(M):
    ga=0.0;gb=0.0;s=0.0;t=0.0
    for r in range(1,K+1):
        ga+=random.expovariate(1.0)
        gb+=random.expovariate(1.0)
        s-=2.0**(-r)*math.log(ga)
        t-=2.0**(-r)*math.log(gb)
    sample.append(s+t)
mean=statistics.mean(sample);var=statistics.variance(sample)
# exact E=2(Euler gamma - log 2); var = 2(zeta(2)-2Li_2(1/2)+Li_2(1/4))
# numerical Li2 via absolutely convergent series
li=lambda z:sum(z**k/k**2 for k in range(1,1000))
mean_target=2*(0.5772156649015328606065120900824-math.log(2))
var_target=2*(math.pi**2/6-2*li(.5)+li(.25))
assert abs(mean-mean_target)<0.035,(mean,mean_target)
assert abs(var-var_target)<0.07,(var,var_target)
print('POISSON_MOMENT_PASS','samples',M,'truncation',K,'mean',round(mean,5),'exact',round(mean_target,5),'variance',round(var,5),'exact',round(var_target,5))
