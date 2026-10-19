"""Reproducibility checks for the two-row absolute-value iteration.

Run: python3 verify.py
Standard library only. Numerical tests are consistency checks, not substitutes for proof.
"""
from fractions import Fraction
import itertools
import math
import random

checks = 0

def check(condition, explanation):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(explanation)

def iterate(x, row, c):
    beta = 1.0 / (1.0-c)
    alpha = 1.0 - c
    b = beta if row == 0 else -beta
    return x - alpha * (x - b*abs(x))

def moment_matrix(s, p, c):
    a, b = 1+c, 1-c
    return [[p*a**s, p*b**s], [(1-p)*b**s, (1-p)*a**s]]

def spectral_radius(s,p,c):
    a,b = (1+c)**s,(1-c)**s
    return 0.5*(a+math.sqrt(a*a*(2*p-1)**2+4*p*(1-p)*b*b))

def p_limits(c):
    rad = -math.log1p(-c*c) / math.log((1+c)/(1-c))
    return (1-math.sqrt(rad))/2, (1+math.sqrt(rad))/2

# Algebra of the source update: row choice resets the sign.
for c in [0.015625, 0.2, 0.5, 0.9, 0.98]:
    for x in [-3.5, -0.125, 0.125, 2.25]:
        for row in [0,1]:
            y = iterate(x,row,c)
            expected = c*x+(1 if row==0 else -1)*abs(x)
            check(math.isclose(y,expected,rel_tol=1e-12,abs_tol=1e-12),'source update')
            check((y>0)==(row==0),'sign reset')
            factor = 1+c if ((x>0)==(row==0)) else 1-c
            check(math.isclose(abs(y),factor*abs(x),rel_tol=1e-12,abs_tol=1e-12),'factor')

# Exact rational fair-coin branch enumeration (no Monte Carlo sampling).
for c in [Fraction(1,4), Fraction(1,2), Fraction(3,4)]:
    for initial in [Fraction(-3,2),Fraction(7,5)]:
        for k in range(1,10):
            outcomes=[]
            for rows in itertools.product([-1,1], repeat=k):
                x=initial
                for sign in rows:
                    x=c*x+sign*abs(x)
                outcomes.append(x)
            signed=sum(outcomes, Fraction(0))/len(outcomes)
            first=sum((abs(x) for x in outcomes),Fraction(0))/len(outcomes)
            second=sum((x*x for x in outcomes),Fraction(0))/len(outcomes)
            check(signed==c**k*initial,'signed mean exact')
            check(first==abs(initial),'absolute mean exact')
            check(second==(1+c*c)**k*initial**2,'second moment exact')

# The two-state moment transfer reproduces exact independent-row enumeration.
for c in [0.12,0.5,0.9]:
    for p in [0.16,0.32,0.5,0.78,0.9]:
        for s in [0.3,1.0,2.0,2.7]:
            M=moment_matrix(s,p,c)
            for sign0 in [0,1]:
                vec=[float(sign0==0),float(sign0==1)]
                # sign0=0 represents positive, sign0=1 negative
                brute0 = 1.0 if sign0==0 else -1.0
                for k in range(1,8):
                    vec=[M[0][0]*vec[0]+M[0][1]*vec[1],M[1][0]*vec[0]+M[1][1]*vec[1]]
                    brute=0.0
                    for rows in itertools.product([0,1],repeat=k):
                        weight=1.0
                        x=brute0
                        for row in rows:
                            weight*=p if row==0 else (1-p)
                            x=(c*x+(1 if row==0 else -1)*abs(x))
                        brute+=weight*abs(x)**s
                    check(math.isclose(sum(vec),brute,rel_tol=1e-10,abs_tol=1e-10),'moment matrix enumeration')
            a,b=(1+c)**s,(1-c)**s
            lambda_ = spectral_radius(s,p,c)
            check(math.isclose(lambda_*lambda_-a*lambda_+p*(1-p)*(a*a-b*b),0,rel_tol=1e-9,abs_tol=1e-9),'characteristic equation')

# Sampling-window boundaries and strict Lyapunov signs.
for c in [0.001,0.01,0.1,0.3,0.5,0.8,0.99]:
    lo,hi=p_limits(c)
    check(0<lo<0.5<hi<1,'nonempty window')
    def gamma(p):
        return math.log1p(c)-2*p*(1-p)*math.log((1+c)/(1-c))
    check(abs(gamma(lo))<1e-12 and abs(gamma(hi))<1e-12,'critical zeros')
    check(gamma(.5)<0,'center stability')
    check(gamma(lo/2)>0,'outside divergence')
    check(gamma((lo+.5)/2)<0,'inside stability')
    for p in [.05,.19,.31,.5,.73,.88,.96]:
        r1=spectral_radius(1,p,c)
        check(r1>=1-1e-12,'first moment nondecay')
        check((abs(r1-1)<1e-11)==(p==.5),'unique first-moment balance')
        check(spectral_radius(2,p,c)>=1+c*c-1e-12,'second-moment gap')

# Sharp square-root collapse of admissible sampling bias.
for c in [1e-3, 1e-4, 1e-5, 1e-6]:
    lo,hi=p_limits(c)
    ratio=(hi-lo)/math.sqrt(c/2)
    check(abs(ratio-1)<0.004,'small-c width asymptotic')

# A representative stable biased parameter has a subunit fractional moment radius.
c,p=0.5,0.35
lo,hi=p_limits(c)
check(lo<p<hi,'biased stable example')
check(spectral_radius(0.1,p,c)<1,'fractional moment contraction')
check(spectral_radius(1,p,c)>1,'mean absolute growth')

print('PASS',checks,'deterministic assertions')
print('c=1/2 sampling-window:',p_limits(0.5))
print('c=1/2 fair signed, absolute, second-moment factors:',0.5,1.0,1.25)
print('c=1/2 fair logarithmic rate:',0.5*math.log(0.75))
