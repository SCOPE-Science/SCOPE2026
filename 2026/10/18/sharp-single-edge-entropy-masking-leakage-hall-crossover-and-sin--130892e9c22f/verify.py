"""Reproduce exact and numerical consequences of a single-cost-cell entropic transport theorem.
Run: python verify.py  (requires numpy >= 1.20)
Finite checks supplement, but do not substitute for, the analytic proof in RESULT.md.
"""
import math
from fractions import Fraction
from random import Random
import numpy as np

assertions=0

def ck(flag):
    global assertions
    assertions += 1
    if not bool(flag):
        raise AssertionError('check %d failed' % assertions)

def mass(p,q,t):
    d=p+q-1.0
    if t==1:
        return p*q
    b=1.0-p-q+t*(p+q)
    disc=math.sqrt(b*b+4.0*(1-t)*t*p*q)
    return 2.0*t*p*q/(b+disc) if b >= 0 else (-b+disc)/(2.0*(1-t))

def plan(r,c,t):
    p,q=float(r[0]),float(c[0])
    x=mass(p,q,t)
    P=np.empty((len(r),len(c)))
    P[0,0]=x
    P[0,1:]=(p-x)*c[1:]/(1-q)
    P[1:,0]=(q-x)*r[1:]/(1-p)
    P[1:,1:]=(1-p-q+x)*np.outer(r[1:],c[1:])/((1-p)*(1-q))
    return P,x

def jacobian(r,c,P):
    return (P.T/r)@P/c[:,None]

for a,b in [(1,2),(1,5),(2,5),(17,29),(1,100)]:
    t=Fraction(a*a,b*b)
    x=Fraction(a,2*(a+b))
    y=Fraction(1,2)-x
    ck(x*x==t*y*y)
    ck(2*x==Fraction(a,a+b))
    lam=Fraction((b-a)**2,(b+a)**2)
    ck((x-Fraction(1,4))**2/Fraction(1,16)==lam)

rng=Random(540193)
for k in range(650):
    m,n=rng.randint(2,7),rng.randint(2,7)
    r=np.array([0.2+rng.random() for i in range(m)])
    c=np.array([0.2+rng.random() for j in range(n)])
    r/=r.sum();c/=c.sum()
    t=10**(-rng.uniform(0.02,5.0))
    P,x=plan(r,c,t)
    ck(np.min(P)>0)
    ck(np.max(abs(P.sum(axis=1)-r))<5e-12)
    ck(np.max(abs(P.sum(axis=0)-c))<5e-12)
    ck(abs(x*(1-r[0]-c[0]+x)-t*(r[0]-x)*(c[0]-x))<5e-13)
    ck(abs(P[0,0]*P[1,1]/(P[0,1]*P[1,0])-t)<2e-8)
    lam=(x-r[0]*c[0])**2/(r[0]*(1-r[0])*c[0]*(1-c[0]))
    sing=np.linalg.svd(P/np.sqrt(np.outer(r,c)),compute_uv=False)
    ck(abs(sing[0]-1)<4e-12)
    ck(abs(sing[1]**2-lam)<4e-12)
    ck(np.max(sing[2:])<4e-12 if min(m,n)>2 else True)
    J=jacobian(r,c,P)
    eig=np.linalg.eigvals(J)
    ck(abs(np.sort(abs(eig))[-1]-1)<2e-11)
    ck(abs(np.sort(abs(eig))[-2]-lam)<2e-11)
    ck(lam<=((1-math.sqrt(t))/(1+math.sqrt(t)))**2+5e-12)
    if r[0]+c[0]<=1:
        hard,_=plan(r,c,1e-100)
        hard[0,0]=0
        hard[0,1:]=r[0]*c[1:]/(1-c[0])
        hard[1:,0]=c[0]*r[1:]/(1-r[0])
        hard[1:,1:]=(1-r[0]-c[0])*np.outer(r[1:],c[1:])/((1-r[0])*(1-c[0]))
        ck(abs(np.sum(abs(P-hard))/2-2*x)<1e-10)
        ck(x<=math.sqrt(t)/(2*(1+math.sqrt(t)))+5e-12)
    if k<25:
        # Reconstruct fixed-point column scalings, then differentiate a full row/column sweep.
        K=np.ones((m,n)); K[0,0]=t
        v=P[0,:]/K[0,:]
        G=np.zeros((n,n))
        h=1e-6
        def sweep(v):
            u=r/(K@v)
            return np.log(c/(K.T@u))
        for j in range(n):
            a=np.zeros(n);a[j]=h
            G[:,j]=(sweep(v*np.exp(a))-sweep(v*np.exp(-a)))/(2*h)
        ck(np.max(abs(G-J))<1e-8)

for t in [1.0,0.25,0.01,1e-4,1e-8]:
    p=q=.5
    x=mass(p,q,t)
    a=math.sqrt(t)
    ck(abs(x-a/(2*(1+a)))<1e-12)
    ck(abs(2*x-a/(1+a))<1e-12)
    ck(abs(((x-p*q)**2/(p*(1-p)*q*(1-q)))-((1-a)/(1+a))**2)<1e-12)
for kappa in [0.05,0.1,0.3,0.7]:
    for t in [0.001,.03,.5,.999999]:
        s=1-kappa
        A=kappa+t*s
        exact=t*s*s/(2*(A+math.sqrt(A*A+t*(1-t)*s*s)))
        ck(abs(mass(s/2,s/2,t)-exact)<1e-12)
for u in [0,0.2,1,5]:
    t=1e-10
    s=1-u*math.sqrt(t)
    x=mass(s/2,s/2,t)
    pred=(math.sqrt(u*u+1)-u)/2
    ck(abs(x/math.sqrt(t)-pred)<0.0001)
print('PASS:',assertions,'deterministic exact-rational and numerical checks')
