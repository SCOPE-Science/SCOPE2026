#!/usr/bin/env python3
"""Independent finite checks for robust alternating-price cycle conductance theorem.

Requires numpy, scipy, sympy; no external files. The infinite-family conclusion
relies on the written proof, not on these finite instances.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import minimize

checks = 0

def require(condition, msg):
    global checks
    assert condition, msg
    checks += 1

m = sp.symbols('m', integer=True, positive=True)
n = 2*m
u = m*(2*m*m+1)/3
v = 2*m*(m*m-1)/3
require(sp.simplify(u+v-n*(n*n-1)/6)==0,'path sum')
require(sp.simplify(u-v-m)==0,'odd-even gap')
for size in range(2,20):
    U=sp.Rational(size*(2*size*size+1),3)
    V=sp.Rational(2*size*(size*size-1),3)
    odd=sum(sp.Rational(k*(2*size-k)) for k in range(1,2*size,2))
    even=sum(sp.Rational(k*(2*size-k)) for k in range(2,2*size,2))
    require(odd==U and even==V,f'coeff parity m={size}')
    for price in [sp.Rational(1,4),sp.Rational(2,3),sp.Rational(9,10),sp.Rational(1),sp.Rational(11,10),sp.Rational(3,2),sp.Rational(4)]:
        t=float(price); budget=2.7; mf=float(size)
        uf=float(U); vf=float(V)
        if price<V/U:
            r=math.sqrt(uf*t/vf)
            target=mf*(math.sqrt(uf)+math.sqrt(vf*t))**2/budget
        elif price>U/V:
            r=math.sqrt(vf*t/uf)
            target=mf*(math.sqrt(vf)+math.sqrt(uf*t))**2/budget
        else:
            r=1.0
            target=mf*(1+t)*(uf+vf)/budget
        b=budget/(mf*(r+t)); a=r*b
        loss_a=uf/b+vf/a
        loss_b=uf/a+vf/b
        require(abs(max(loss_a,loss_b)-target)<1e-8*target,f'value m={size}, t={price}')
        require(abs(size*(a+t*b)-budget)<1e-12,f'budget m={size}')
        # The full list of edge failure losses agrees with the two-orbit formula.
        N=2*size
        weights=[a if i%2==0 else b for i in range(N)]
        L=[]
        for fail in range(N):
            sequence=[weights[(fail+k)%N] for k in range(1,N)]
            L.append(sum(k*(N-k)/sequence[k-1] for k in range(1,N)))
        require(max(abs(L[j]-(loss_a if j%2==0 else loss_b)) for j in range(N))<1e-8*target, f'loss m={size}')

# Unrestricted 2m-variable numerical optimizations for several dimensions.
for size in [2,3,4,5]:
    N=2*size
    B=10.0
    for t in [0.35,0.82,0.98,1.0,1.025,1.19,1.8,5.0]:
        U=size*(2*size*size+1)/3; V=2*size*(size*size-1)/3
        lo=V/U; hi=U/V
        if t<lo:r=math.sqrt(U*t/V)
        elif t>hi:r=math.sqrt(V*t/U)
        else:r=1.
        b=B/(size*(r+t)); a=r*b
        opt=np.array([a if j%2==0 else b for j in range(N)])
        costs=np.array([1 if j%2==0 else t for j in range(N)])
        coeff=np.zeros((N,N))
        for fail in range(N):
            for d in range(1,N):coeff[fail,(fail+d)%N]=d*(N-d)
        def loss(x):return np.max(coeff@ (1/x))
        require(abs(loss(opt)-max(U/b+V/a,U/a+V/b))<1e-9,'formula vs max')
        rng=np.random.default_rng(size*131+int(t*100))
        for j in range(60):
            trial=rng.uniform(0.01,5.0,N)
            trial=B*trial/np.dot(costs,trial)
            require(loss(trial)+1e-8>=loss(opt),'asymmetric competitor')
        con={'type':'eq','fun':lambda x:np.dot(costs,x)-B,'jac':lambda x: costs}
        sol=minimize(loss,opt*np.exp(np.random.default_rng(67).normal(0,0.12,N)),bounds=[(1e-4,None)]*N,constraints=[con],method='SLSQP',options={'maxiter':1200,'ftol':1e-11})
        if sol.success:require(loss(sol.x)+1e-6>=loss(opt),'numerical unconstrained minimizer')

# Direct Laplacian pseudoinverse (independent matrix construction) checks.
for size in [2,3,4,6]:
    N=2*size
    rng=np.random.default_rng(size)
    for trial in range(12):
        cond=rng.lognormal(size=N)
        fail=rng.integers(N)
        path_K=sum(d*(N-d)/cond[(fail+d)%N] for d in range(1,N))
        L=np.zeros((N,N))
        for j in range(N):
            if j==fail:continue
            w=cond[j];p=j;q=(j+1)%N
            L[p,p]+=w;L[q,q]+=w;L[p,q]-=w;L[q,p]-=w
        vals=np.linalg.eigvalsh(L)
        require(vals[1]>1e-11,'postfailure connected')
        matrix_K=N*sum(1/z for z in vals[1:])
        require(abs(path_K-matrix_K)<2e-8*matrix_K,'path cut vs Laplacian')

print('PASS',checks,'independent symbolic/numeric checks')
