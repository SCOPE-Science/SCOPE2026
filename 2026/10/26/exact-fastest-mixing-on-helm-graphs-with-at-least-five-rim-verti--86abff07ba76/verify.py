#!/usr/bin/env python3
"""Independent exact-symbolic and dense-matrix checks for the helm-graph result."""
import math
import numpy as np
import sympy as sp

D, p = sp.symbols('D p', positive=True)
c = 1-D**2
t = 1+D
mu = sp.factor((c*(1-p)+t**2)/(1+t**2))
r = sp.factor(t*(1-c*(1-p))/(D*(1+t**2)))
q = sp.factor((1-p-r)/2)
B = sp.Matrix([[c*(1-p-r),r],[r,1-r]])
v = sp.Matrix([1,t])
assert sp.simplify(B*v-mu*v)==sp.zeros(2,1)
assert sp.simplify((v.T*sp.Matrix([[-c,1],[1,-1]])*v)[0])==0
assert sp.simplify((1-mu)-(D**2+p*c)/(1+t**2))==0
assert sp.simplify(mu-(1-p)-(p*t*t-(1-p)*D**2)/(1+t*t))==0
assert sp.simplify(sp.expand((p+r)*(1-r)-p*(1-r))-r*(1-r))==0
# Check the elementary inequalities invoked for the n=5 and n=6 cases.
D5=sp.sqrt((5-sp.sqrt(5))/4)
assert bool(D5>sp.Rational(4,5)) and bool(D5<sp.Rational(5,6))
assert sp.Rational(5,12)+sp.Rational(9,200)<sp.Rational(1,2)
assert sp.sqrt(2)/3<sp.Rational(1,2)
assert sp.sqrt(20)/14+1/(4*sp.sqrt(2))<sp.Rational(1,2)
# The discriminant of the positivity polynomial in n is negative.
disc=sp.factor((1/sp.sqrt(5)-1)**2-4*sp.Rational(1,20)*2)
assert disc<0

def params(n):
    co=math.cos(2*math.pi/n)
    delta=math.sqrt(1-co)
    h=1+delta
    a=co*(1-1/n)
    R=h*(1-a)/(delta*(1+h*h))
    Q=(1-1/n-R)/2
    M=(a+h*h)/(1+h*h)
    return 1/n,Q,R,M

def dense(n,p,q,r):
    N=2*n+1
    P=np.zeros((N,N),dtype=float)
    edges=[]
    for i in range(n):
        edges.append((0,1+i,p))
        edges.append((1+i,1+(i+1)%n,q))
        edges.append((1+i,n+1+i,r))
    for a,b,w in edges:
        P[a,b]+=w
        P[b,a]+=w
    for k in range(N):P[k,k]=1-P[k].sum()
    return P

for n in list(range(5,41))+[51,80,100,150]:
    p0,q0,r0,m=params(n)
    assert 0<p0<=1/n and q0>0 and 0<r0<.5
    assert m>=1-p0
    P=dense(n,p0,q0,r0)
    assert np.min(P)>-1e-12
    assert np.max(np.abs(P-P.T))<1e-12
    assert np.max(np.abs(P.sum(axis=1)-1))<1e-12
    ev=np.linalg.eigvalsh(P)
    spectral=max(abs(ev[0]),abs(ev[-2]))
    assert abs(spectral-m)<2e-10,(n,spectral,m)
    # Check the radial characteristic equation explicitly numerically.
    s=1-p0-2*r0
    disc=s*s+4*p0*(1-r0)
    lamrad=(s+math.sqrt(disc))/2
    assert lamrad<1-r0<m
    # At fixed parameters the largest nonconstant Fourier eigenvalue is m.
    C=math.cos(2*math.pi/n)
    M=np.array([[C*(1-p0-r0),r0],[r0,1-r0]])
    assert abs(np.linalg.eigvalsh(M)[-1]-m)<1e-10

# Feasible competitor stress tests; they are not the infinite proof.
rng=np.random.default_rng(20261020)
count=0
for n in [5,6,7,8,11,17,23,31]:
    opt=params(n)[-1]
    for j in range(100):
        pp=rng.uniform(0,1/n)
        rr=rng.uniform(0,1-pp)
        qq=rng.uniform(0,(1-pp-rr)/2)
        E=np.linalg.eigvalsh(dense(n,pp,qq,rr))
        f=max(abs(E[0]),abs(E[-2]))
        assert f+1e-10>=opt,(n,pp,qq,rr,opt,f)
        count+=1

for n in [500,1000,2000,5000]:
    p0,q0,r0,m=params(n)
    assert abs(n*(1-m)-.5)<0.02
    assert abs(r0-1/(2*math.sqrt(2)*math.pi))<.02
print(f'VERIFY_OK symbolic_eigen_lemmas 6; trig_boundaries 5; dense_graphs 40; feasible_comparisons {count}; asymptotic_samples 4')
