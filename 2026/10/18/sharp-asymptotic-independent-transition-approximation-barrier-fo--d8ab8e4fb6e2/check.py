"""Independent finite verification of adjacent categorical change-count asymptotics.

Usage: python3 check.py. Only Python standard library is required.
Finite tests are not a proof of the asymptotic minimax statement.
"""
from fractions import Fraction
from collections import defaultdict
from itertools import product
from math import exp, erf, log, sqrt, pi

def moments_by_enumeration(probs, n):
    dist = defaultdict(Fraction)
    for seq in product(range(len(probs)), repeat=n):
        w = Fraction(1)
        for j in seq:
            w *= probs[j]
        k = sum(seq[i] != seq[i+1] for i in range(n-1))
        dist[k] += w
    mu = sum(k*v for k,v in dist.items())
    var = sum((k-mu)**2*v for k,v in dist.items())
    return mu,var

def run_pmf(probs,n):
    # DP over terminal letter and number of changes.
    state = {(j,0):v for j,v in enumerate(probs)}
    for length in range(2,n+1):
        nextstate = defaultdict(float)
        for (j,k),mass in state.items():
            for ell,p in enumerate(probs):
                nextstate[(ell,k+(ell!=j))] += mass*p
        state = nextstate
    d = [0.0]*n
    for (j,k),mass in state.items():d[k]+=mass
    return d

def binomial_pmf(m,p):
    if p==1: return [0.0]*m+[1.0]
    a=[(1-p)**m]
    for k in range(m): a.append(a[-1]*(m-k)/(k+1)*p/(1-p))
    return a

def kolmogorov(a,b):
    s=t=0.0; best=0.0
    for x,y in zip(a,b):
        s+=x;t+=y; best=max(best,abs(s-t))
    return best

def predicted_constant(probs):
    s2=sum(p*p for p in probs)
    s3=sum(p**3 for p in probs)
    q=1-s2; delta=s3-s2*s2
    tau2=q*(1-q); sig2=tau2+2*delta
    if abs(delta)<1e-15: return 0.0
    x=sqrt(tau2*sig2*log(sig2/tau2)/(sig2-tau2))
    return (erf(x/sqrt(2*tau2))-erf(x/sqrt(2*sig2)))/2

checks=0
for weights in ((Fraction(3,4),Fraction(1,4)),
                (Fraction(1,2),Fraction(1,3),Fraction(1,6)),
                (Fraction(1,3),)*3):
    q=1-sum(x*x for x in weights)
    delta=sum(x**3 for x in weights)-sum(x*x for x in weights)**2
    for n in (3,5,7):
        mu,var=moments_by_enumeration(weights,n)
        assert mu==(n-1)*q
        assert var==(n-1)*q*(1-q)+2*(n-2)*delta
        checks+=2
    if delta==0:
        assert all(w==weights[0] for w in weights)
        n=12
        p=run_pmf([float(v) for v in weights],n)
        b=binomial_pmf(n-1,float(q))
        assert kolmogorov(p,b)<1e-12
        checks+=1
    else:
        target=predicted_constant([float(w) for w in weights]); print('probabilities=',weights,'limit=',target)
        assert 0 < target < .5
        for n in (80,160,320):
            p=run_pmf([float(v) for v in weights],n)
            b=binomial_pmf(n-1,float(q))
            obs=kolmogorov(p,b)
            print('  n=',n,'observed_K=',round(obs,9))
            assert abs(obs-target)<.015
            checks+=1
print('PASS',checks,'independent finite tests')
