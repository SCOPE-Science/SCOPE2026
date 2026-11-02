"""Standalone checks for the finite-state generosity-learning spectral cutoff theorem."""
from fractions import Fraction
from itertools import product
from math import comb, factorial, log, pi, sqrt, erf
from collections import Counter
import numpy as np
from scipy.sparse import csr_matrix


def single_Q(k,a,b):
    Q=np.zeros((k,k))
    for i in range(k):
        if i<k-1:
            Q[i,i+1]=a;Q[i,i]-=a
        if i>0:
            Q[i,i-1]=b;Q[i,i]-=b
    return Q

def pi_vector(k,a,b):
    ratio=a/b; z=sum(ratio**j for j in range(k))
    return np.array([ratio**j/z for j in range(k)])

def eig_formula(k,a,b):
    return np.array([0.]+[a+b-2*sqrt(a*b)*np.cos(j*pi/k) for j in range(1,k)])

def counts_states(m,k=3):
    if k!=3: raise ValueError
    return [(u,v,m-u-v) for u in range(m+1) for v in range(m+1-u)]

def count_P(m,a,b):
    states=counts_states(m)
    ix={z:i for i,z in enumerate(states)}
    rows=[];cols=[];values=[]
    for i,z in enumerate(states):
        stay=1.
        for j in range(2):
            if z[j]:
                y=list(z);y[j]-=1;y[j+1]+=1
                prob=a*z[j]/m
                rows.append(i);cols.append(ix[tuple(y)]);values.append(prob);stay-=prob
            if z[j+1]:
                y=list(z);y[j]+=1;y[j+1]-=1
                prob=b*z[j+1]/m
                rows.append(i);cols.append(ix[tuple(y)]);values.append(prob);stay-=prob
        rows.append(i);cols.append(i);values.append(stay)
    P=csr_matrix((values,(rows,cols)),shape=(len(states),len(states)))
    return states, P

def fixed_count_pi(states, p):
    from scipy.special import gammaln
    m=sum(states[0]); vals=np.array([np.exp(gammaln(m+1)-sum(gammaln(u+1) for u in z)+sum(z[j]*log(p[j]) for j in range(3))) for z in states])
    return vals

def finite_tv(m,a,b,c):
    states,P=count_P(m,a,b)
    lam=eig_formula(3,a,b)[1]
    t=int(round(m*(log(m)/(2*lam)+c)))
    dist=np.zeros(len(states));dist[states.index((m,0,0))]=1.
    for _ in range(t):
        dist=P.T @ dist
    stat=fixed_count_pi(states,pi_vector(3,a,b))
    return t, .5*np.sum(np.abs(dist-stat))

def main():
    for k in range(2,10):
        for a,b in [(.25,.25),(.13,.61),(.72,.07),(.4,.5)]:
            Q=single_Q(k,a,b); p=pi_vector(k,a,b)
            assert np.max(np.abs(p@Q))<1e-12
            SQ=np.diag(np.sqrt(p))@Q@np.diag(1/np.sqrt(p))
            assert np.max(np.abs(SQ-SQ.T))<1e-12
            eig=sorted(-np.linalg.eigvalsh(SQ))
            assert np.allclose(eig, sorted(eig_formula(k,a,b)),atol=1e-11,rtol=1e-11)
            theta=pi/k;q=sqrt(b/a)
            g=np.array([np.sin(j*theta)-q*np.sin((j-1)*theta) for j in range(1,k+1)])
            f=np.array([q**(j-1)*g[j-1] for j in range(1,k+1)])
            assert np.max(abs(Q@f+eig_formula(k,a,b)[1]*f))<1e-10
            assert abs(p@f)<1e-10
    print('PASS: exact spectral formula and first eigenvector, 32 parameter/dimension cases')
    for m in (2,3,4,7,10):
        states,P=count_P(m,.25,.25)
        st=fixed_count_pi(states,pi_vector(3,.25,.25))
        assert np.max(abs(P@np.ones(len(states))-1))<1e-12
        assert np.max(abs(st@P-st))<1e-12
        assert abs(sum(st)-1)<1e-12
    print('PASS: count-chain probabilities and multinomial stationarity for 5 sample populations')
    a=b=.25
    for c in (-3.,0.,3.):
        limit=2*(.5*(1+erf((sqrt(1.5)*np.exp(-a*c)/2)/sqrt(2))))-1
        print('gaussian profile c=',c,'limit=',round(limit,7))
        for m in [20,40,80]:
            t,tv=finite_tv(m,a,b,c)
            print(' m=',m,'t=',t,'tv=',round(tv,7))
    for a,b in ((.56,.14),(.14,.56)):
        k=3;q=sqrt(b/a); theta=pi/k
        u=np.array([q**(j-1)*(np.sin(j*theta)-q*np.sin((j-1)*theta)) for j in range(1,k+1)])
        pv=pi_vector(k,a,b)
        u=u/sqrt(sum(pv*u*u))
        lam=eig_formula(k,a,b)[1]
        profile=erf(abs(u[0])/2/sqrt(2))
        print('biased a,b=',a,b,'lambda=',round(lam,8),'endpoint amplitude=',round(u[0],8),'TV profile c=0=',round(profile,7))
        for m in (20,40,80):
            t,tv=finite_tv(m,a,b,0)
            print(' m=',m,'t=',t,'tv=',round(tv,7))
    print('PASS: all tests completed')

if __name__=='__main__':main()
