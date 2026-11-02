"""Reproducibility checks for a near-critical Zipf-disaster renewal theorem.
Finite calculations corroborate but do not prove the limiting distribution.
"""
from fractions import Fraction
from math import exp, log
import numpy as np

def renewal_float(N, c):
    beta=1+c/log(N)
    t=np.arange(1,N+2,dtype=float)
    tails=np.power(t,-beta)
    f=np.zeros(N+1,dtype=float)
    f[1:]=tails[:N]-tails[1:]
    u=np.empty(N+1,dtype=float)
    u[0]=1.
    for j in range(1,N+1):
        u[j]=np.dot(f[1:j+1],u[j-1::-1])
    ages=np.arange(0,N+1,dtype=float)
    weights=u[::-1]*np.power(ages+1,-beta)
    return beta,u,weights

def h(c):
    return (1-exp(-c))/c if c else 1.

def expected_cdf(c, theta):
    if c==0: return theta
    return (1-exp(-c*theta))/(1-exp(-c))

nchecks=0
for N in (8,14,25):
    ff=[Fraction(0)] + [Fraction(1,k)-Fraction(1,k+1) for k in range(1,N+1)]
    u=[Fraction(1)]
    for j in range(1,N+1):
        u.append(sum(ff[s]*u[j-s] for s in range(1,j+1)))
    w=[u[N-k]/Fraction(k+1) for k in range(N+1)]
    assert sum(w)==1; nchecks+=1
    assert all(u[j+1]<=u[j] for j in range(N));nchecks+=1
    # Entire finite-time mass law agrees with the reset recurrence.
    state=[Fraction(1)]
    for j in range(1,N+1):
        nextstate=[Fraction(0)]*(j+1)
        for k,mass in enumerate(state):
            p=Fraction(k+1,k+2)
            nextstate[0]+=mass*(1-p)
            nextstate[k+1]+=mass*p
        state=nextstate
    assert state==w;nchecks+=1
for c in (-2.,0.,2.):
    for N in (1200,3600):
        beta,u,w=renewal_float(N,c)
        assert 0.0<beta;nchecks+=1
        assert abs(np.sum(w)-1.)<2e-11;nchecks+=1
        assert np.min(u)>0 and np.max(np.diff(u))<2e-12;nchecks+=1
        scaled=u[N]*log(N)*h(c)
        assert .75 < scaled < 1.28,(N,c,scaled);nchecks+=1
        for theta in (.3,.7):
            observed=np.sum(w[:int(N**theta)+1])
            expected=expected_cdf(c,theta)
            # Finite-size convergence is logarithmically slow; this is only a sanity test.
            assert abs(observed-expected)<.21,(N,c,theta,observed,expected);nchecks+=1
        print('N=',N,'c=',c,'beta=',round(beta,8),'renewal_scaled=',round(scaled,6),
              'cdf_0.3=',round(sum(w[:int(N**.3)+1]),6),'cdf_0.7=',round(sum(w[:int(N**.7)+1]),6))
for k in (10,100,1000,10000):
    for t in (0.2,1.,2.5):
        r=int(t*(k+1))
        cond=((k+1)/(k+r+1))**1
        target=(1+t)**(-1)
        assert abs(cond-target)<=1/(k+1), (k,t,cond,target);nchecks+=1
print('PASS:',nchecks,'assertions, including exact rational finite laws and triangular-family numerics')
