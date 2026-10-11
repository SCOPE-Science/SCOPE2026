import math
import numpy as np
from scipy.optimize import minimize
from math import comb

def predict(n,a,b):
    D=(n/2-a)*(b-n/2)
    if 4*D>=n:
        return n/2, n/4, n*(n-1)/4, list(range(a,b+1)),True
    d=b-a; A0=a*(n-a); A1=b*(n-b); delta=A1-A0
    if delta==0: p=.5
    else:
        B=n*delta-2*A0
        p=(B+math.sqrt(B*B+4*(n+1)*delta*A0))/(2*(n+1)*delta)
    mu=a+p*d; V=p*(1-p)*d*d; A=A0+p*delta
    return mu,V,A,[a,b],False

def objective(prob,ks,n):
    mu=np.dot(prob,ks)
    V=np.dot(prob,(ks-mu)**2)
    A=np.dot(prob,ks*(n-ks))
    if V<=0 or A<=0:return 1e6
    return -math.log(V)-(n-1)*math.log(A)

nchecks=0
max_gap=0.
for n in range(2,15):
    for a in range(n):
        for b in range(a+1,n+1):
            ks=np.arange(a,b+1,dtype=float)
            mu,V,A,contacts,sphere=predict(n,a,b)
            assert min(V,A)>0,(n,a,b,mu,V,A)
            L=objective(np.array([1.0]),np.array([0.0]),n) if False else -math.log(V)-(n-1)*math.log(A)
            qq=[((k-mu)**2/V+(n-1)*k*(n-k)/A)/n for k in ks]
            assert max(qq)<1+1e-9,(n,a,b,'containment',qq)
            if sphere: assert max(abs(q-1) for q in qq)<1e-10,(n,a,b,qq)
            elif b-a>1: assert max(qq[1:-1])<1-1e-8,(n,a,b,qq)
            # Check against optimized D-optimal orbit distribution, not the candidate formulas
            best=1e7
            for seed in range(3):
                x0=np.full(len(ks),1./len(ks))
                if seed: x0=np.random.default_rng(23*n+11*a+b+seed).dirichlet(np.ones(len(ks)))
                res=minimize(objective,x0,args=(ks,n),method='SLSQP',bounds=[(0,1)]*len(ks),constraints=[{'type':'eq','fun':lambda p: sum(p)-1}],options={'ftol':1e-12,'maxiter':800})
                best=min(best,res.fun)
            gap=abs(best-L)
            max_gap=max(max_gap,gap)
            assert best>=L-1e-6,(n,a,b,L,best,gap)
            nchecks+=1
print('VERIFIED',nchecks,'slab parameter triples; worst opt gap',max_gap)
