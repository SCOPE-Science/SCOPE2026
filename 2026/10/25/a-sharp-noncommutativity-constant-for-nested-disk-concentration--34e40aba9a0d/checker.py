#!/usr/bin/env python3
"""Numerical and symbolic checks for nested-disk Fock concentration commutators."""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import gammainc
from mpmath import hyper, mp

count=0

def check(cond, label):
    global count
    if not cond:
        raise AssertionError(label)
    count += 1

def close(a,b,label,tol=3e-10):
    check(abs(a-b) <= tol*max(1.0,abs(a),abs(b)),label)

def block(j,x):
    # j >= 1; angular sector k=j-1
    k=j-1
    E=math.exp(-x)*x**j/math.factorial(j)
    I=gammainc(j,x)
    return np.array([[I,E*math.sqrt(j)],[E*math.sqrt(j),I+(k-x)*E]])

def c(j,x,y):
    return 0.0 if x==y else math.exp(math.log(abs(y-x))+.5*math.log(j)-x-y+j*math.log(x*y)-2*math.lgamma(j+1))

s=sp.symbols('s',positive=True)
for k in range(12):
    deriv=sp.diff(s**(k+1)*sp.exp(-s),s)
    check(sp.simplify(deriv-s**k*(k+1-s)*sp.exp(-s))==0,'integration identity')
    check(sp.simplify(sp.diff((k+1-s)*s**(k+1)*sp.exp(-s),s) - 
       (s**k*(k+1-s)**2*sp.exp(-s)-s**(k+1)*sp.exp(-s)))==0,'radial identity')

pairs=[(0.4,1.3),(0.7,3.9),(1.7,4.1),(5.5,12.0),(3.0,3.8)]
for j in range(1,13):
    k=j-1
    for x,y in pairs:
        A=block(j,x);B=block(j,y)
        # Four Gaussian radial integrals compute the 2-by-2 blocks independently.
        t00=quad(lambda t: t**k*math.exp(-t)/math.factorial(k),0,x,epsabs=1e-12)[0]
        t01=quad(lambda t: t**k*(k+1-t)*math.exp(-t)/math.sqrt(math.factorial(k)*math.factorial(j)),0,x,epsabs=1e-12)[0]
        t11=quad(lambda t: t**k*(k+1-t)**2*math.exp(-t)/math.factorial(j),0,x,epsabs=1e-12)[0]
        close(A[0,0],t00,'direct matrix integral');close(A[0,1],t01,'direct matrix integral');close(A[1,1],t11,'direct matrix integral')
        C=A@B-B@A
        amp=c(j,x,y)
        close(C[0,1],math.copysign(amp,x-y),'commutator entry')
        close(C[1,0],-C[0,1],'skew symmetry')
        close(C[0,0],0,'zero diagonal');close(C[1,1],0,'zero diagonal')
        sig=np.linalg.svd(C,compute_uv=False)
        close(sig[0],amp,'singular value 1');close(sig[1],amp,'singular value 2')
        check(np.all(np.linalg.eigvalsh(A)>=-1e-11),'compression positive')
        check(np.all(np.linalg.eigvalsh(A)<=1+1e-11),'compression contractive')

L=1/(math.pi*math.sqrt(2*math.e))
for j in range(1,500):
    d=math.sqrt(2*j+1)
    x=(2*j+1-d)/2
    y=(2*j+1+d)/2
    logmax=0.5*math.log(j*(2*j+1))-(2*j+1)+j*math.log(j*(2*j+1)/2)-2*math.lgamma(j+1)
    val=math.exp(logmax)
    close(val,c(j,x,y),'critical radii')
    check(val<L,'strict constant')
    correction=(j+.5)*math.log1p(1/(2*j))-.5
    check(correction<=1/(8*j)+1e-12,'log inequality')
    check(2/(12*j+1)>1/(8*j),'Robbins comparison')
check(abs(math.exp(0.5*math.log(10000*20001)-20001+10000*math.log(10000*20001/2)-2*math.lgamma(10001))-L)<1e-5,'limit approach')

for j in range(1,30):
    threshold=math.sqrt(j*(j+1)**3)
    x=1.1; y=threshold/x
    close(c(j,x,y),c(j+1,x,y),'adjacent tie',tol=1e-9)
    check(c(j,x,y)>=c(j-1,x,y)-1e-12 if j>1 else True,'neighbor below')
    check(c(j+1,x,y)>=c(j+2,x,y)-1e-12,'neighbor above')

mp.dps=35
for x,y in pairs:
    q=x*y
    lhs=2*(x-y)**2*math.exp(-2*(x+y))*sum(j*q**(2*j)/(math.factorial(j)**4) for j in range(1,45))
    rhs=2*(x-y)**2*math.exp(-2*(x+y))*q*q*float(hyper([],[2,2,2],q*q))
    close(lhs,rhs,'Hilbert Schmidt hypergeometric identity')
    check(max(c(j,x,y) for j in range(1,45))<L,'operator norm universal bound')

print('PASS',count,'symbolic and quadrature assertions')
print('Sharp nonattained global bound',format(L,'.15f'))
print('First mode transition',math.sqrt(8))
print('Example norm for x=0.7,y=3.9',max(c(j,0.7,3.9) for j in range(1,35)))
