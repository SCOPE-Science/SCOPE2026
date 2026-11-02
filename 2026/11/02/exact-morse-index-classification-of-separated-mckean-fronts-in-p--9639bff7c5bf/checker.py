"""Numerical cross-check for the finite Green-matrix Morse-index formula.
This script illustrates, but does not prove, the general spectral theorem.
Requires numpy and scipy.  Run with: python checker.py
"""
import itertools
import numpy as np
from scipy.optimize import brentq, root

alpha=0.25
L1=0.8
L2=1.6
L=L1+L2
a=0.5

def step(p,t):
    w=np.sqrt(p); c=np.cosh(t/w); s=np.sinh(t/w)
    return np.array([[c,s/w],[s*w,c]])
A=step(1/alpha,L2)@step(1.,L1)
vals,vecs=np.linalg.eig(A)
i_plus=int(np.argmax(vals));i_minus=1-i_plus
muplus=float(vals[i_plus]); muminus=float(vals[i_minus])
wplus=np.real(vecs[:,i_plus]/vecs[0,i_plus]);wminus=np.real(vecs[:,i_minus]/vecs[0,i_minus]);
W=wplus[1]-wminus[1]
assert W>0 and muplus>1 and muminus<1

def flow(s):
    if s<L1: return step(1.,s)
    return step(1/alpha,s-L1)@step(1.,L1)

def modes(x):
    k=int(np.floor(x/L)); s=x-k*L
    B=flow(s)
    return (muplus**k)*(B@wplus),(muminus**k)*(B@wminus)

def rates(x):
    up,um=modes(x)
    return up[1]/up[0],-um[1]/um[0]

def beta(x):
    rp,rm=rates(x)
    return rp/(rp+rm)

def green(x,y):
    lp=modes(min(x,y))[0][0]
    rp=modes(max(x,y))[1][0]
    return lp*rp/W

def vi(rho,x):
    if x <= rho:
        return 1.0-(1-beta(rho))*modes(x)[0][0]/modes(rho)[0][0]
    return beta(rho)*modes(x)[1][0]/modes(rho)[1][0]

def divi(rho,x):
    if x <= rho:
        z1=modes(x)[0]; zr=modes(rho)[0]
        p=1 if ((x%L)<L1) else 1/alpha
        return -(1-beta(rho))*(z1[1]/p)/zr[0]
    z1=modes(x)[1];zr=modes(rho)[1]
    p=1 if ((x%L)<L1) else 1/alpha
    return beta(rho)*(z1[1]/p)/zr[0]

def run_case(threshold, slots):
    number=len(slots)
    assert number % 2==1
    a_min,a_max=beta(L1),beta(0.)
    assert a_min < threshold < a_max
    phases = {}
    for level in (threshold,1.-threshold):
        phases[level]={
            'P':brentq(lambda t:beta(t)-level,0.,L1,xtol=1.e-13),
            'Q':brentq(lambda t:beta(t)-level,L1,L,xtol=1.e-13)
        }
    sigma=np.array([(-1)**i for i in range(number)])
    counts=[]
    for word in itertools.product('PQ',repeat=number):
        guess=np.array([slots[i]*L+phases[threshold if i%2==0 else 1.-threshold][w]
                        for i,w in enumerate(word)])
        def residual(rho):
            return np.array([sum(sigma[j]*vi(rho[j],rho[i])
                                 for j in range(number))-threshold for i in range(number)])
        sol=root(residual,guess,tol=1.e-10)
        rho=sol.x
        assert np.max(np.abs(residual(rho)))<1.e-8, (word,residual(rho))
        assert np.max(np.abs(rho-guess)) < 0.05, (word,rho-guess)
        slopes=np.array([sum(sigma[j]*divi(rho[j],rho[i])
                              for j in range(number)) for i in range(number)])
        assert np.all(-sigma*slopes>0), (word,slopes)
        weights=np.sqrt(np.abs(slopes))
        matrix=np.array([[green(rho[i],rho[j])/(weights[i]*weights[j])
                         for j in range(number)] for i in range(number)])
        eig=np.linalg.eigvalsh(matrix)
        idx=sum(v>1 for v in eig)
        assert idx==word.count('Q'), (word,eig,idx)
        assert np.min(abs(eig-1))>0.02, (word,eig)
        counts.append(idx)
    print('threshold=',threshold,'crossings=',number,
          'codes=',len(counts),'stable=',counts.count(0),
          'index_counts=',[counts.count(i) for i in range(number+1)])
    from math import comb
    assert [counts.count(i) for i in range(number+1)] == [comb(number,i) for i in range(number+1)]

run_case(0.5,[-4,0,4])
run_case(0.42,[-8,-4,0,4,8])
print('Green-matrix spectral indices agree for all tested words.')
