"""Independent finite consistency checks for multidimensional lattice heat sign cutoff.

This diagnostic samples finitely many dimensions/times and does not establish
universal positivity, uniqueness, or asymptotics.
"""
import math
import numpy as np
from scipy.special import ive
from scipy.optimize import brentq


def ratio(t):
    return float(ive(1, 2*t)/ive(0, 2*t))


def score(m,t):
    m=abs(m)
    p=ive(np.array([max(m-1,0),m,m+1]),2*t)
    if m==0:
        return 2*(ratio(t)-1)
    return float((p[0]+p[2])/p[1]-2)


def phase(d,t):
    return score(1,t)+(d-1)*score(0,t)


def tau(d):
    return brentq(lambda t: phase(d,t),1.e-8,5.)

assertions=0
for d in range(1,9):
    rt=tau(d)
    assert abs(phase(d,rt))<2.e-8;assertions+=1
    for t in [rt/4,rt/2,rt*.999,rt,rt*1.001,rt*2]:
        assert (phase(d,t) >= -1e-8) == (t <= rt); assertions+=1
        scores=[score(m,t) for m in range(8)]
        assert all(a<b+1e-11 for a,b in zip(scores,scores[1:]));assertions+=1
        for x in np.ndindex(*(5,)*min(d,3)):
            if not any(x):
                continue
            ss=sum(score(xi,t) for xi in x) + (d-len(x))*score(0,t)
            assert ss+1e-10>=phase(d,t);assertions+=1
    p0=math.exp(-2*d*rt)*float(ive(0,2*rt)*math.exp(2*rt))**d # redundant scaled
    formula=4*d*p0*(1-ratio(rt))
    assert formula>0;assertions+=1
for d in [20,50,100,200,500]:
    rt=tau(d)
    approx=1/(2*d)+1/(4*d*d)+1/(8*d**3)
    assert abs(rt-approx) < 0.2/d**4;assertions+=1
    assert abs(d*rt-0.5)<0.02;assertions+=1
print('PASS:',assertions,'finite consistency assertions')
print('threshold samples:',[(d,tau(d)) for d in (1,2,3,5,10,50,100)])
