"""Reproduce exact resolvent and antipodal phase checks; run `python check.py`.
Finite checks supplement, and do not replace, the universal complex partial-fraction proof.
"""
from fractions import Fraction
from itertools import product
from math import atan, pi, sqrt, sin, cos, comb, factorial, log
from scipy.optimize import brentq
import numpy as np

checks=0

def verify(pred, tag):
    global checks
    assert pred,tag
    checks+=1

def f_binomial(d,t):
    return sum(Fraction((-1)**k*comb(d,k),1)/(1+4*t*k*k) for k in range(d+1))

def theta(d,a):
    return sum(atan(a/j) for j in range(1,d+1))

def f_phase(d,t):
    a=1/(2*sqrt(t))
    amp=1.0
    for j in range(1,d+1):
        amp*= j/sqrt(j*j+a*a)
    return amp*cos(theta(d,a))

# Recover exactly the full rational resolvent on small cubes, independently of Fourier expansion.
for d in range(2,7):
    vertices=list(product((0,1),repeat=d))
    pos={v:i for i,v in enumerate(vertices)}
    N=2**d
    L=np.eye(N)*d
    for i,v in enumerate(vertices):
        for j in range(d):
            w=list(v);w[j]^=1
            L[i,pos[tuple(w)]]=-1
    for t in [Fraction(1,20),Fraction(1,8),Fraction(1,3),Fraction(1,1),Fraction(3,1)]:
        R=np.linalg.inv(np.eye(N)+float(t)*(L@L))
        anti=R[0,-1]*N
        formula=float(f_binomial(d,t))
        verify(abs(anti-formula)<1e-10,('spectral',d,t))
        verify(abs(formula-f_phase(d,float(t)))<1e-10,('phase',d,t))
        verify(abs(R.sum(axis=1)-1).max()<1e-12,('stochastic row sums',d,t))

# The positive zeros are simple, with phase levels (m+1/2) pi.
for d in range(2,81):
    a_roots=[]
    for m in range(d//2):
        angle=(m+0.5)*pi
        a=brentq(lambda a:theta(d,a)-angle,1e-13,1e9,xtol=1e-12)
        a_roots.append(a)
        verify(abs(theta(d,a)-angle)<2e-8,('phase root',d,m))
        verify(a>0 and (m==0 or a>a_roots[m-1]),('root order',d,m))
        ti=1/(4*a*a)
        delta=min(ti/500, 1e-5)
        verify(f_phase(d,ti+delta)*f_phase(d,ti-delta)<0,('sign reversal',d,m))
    t_last=1/(4*a_roots[0]**2)
    H=sum(1/j for j in range(1,d+1))
    H3=sum(1/j**3 for j in range(1,d+1))
    approx=H**2/pi**2-H3/(6*H)
    if d>=15:
        verify(abs(t_last-approx)*H**3<1,('asymptotic scale',d))
    verify(f_phase(d,t_last*1.01)>0,('eventual antipodal positive',d))
    verify(f_phase(d,t_last*0.99)<0,('just before last threshold',d))

print('PASS:',checks,'direct matrix, rational spectral, phase and sign-transition checks')
