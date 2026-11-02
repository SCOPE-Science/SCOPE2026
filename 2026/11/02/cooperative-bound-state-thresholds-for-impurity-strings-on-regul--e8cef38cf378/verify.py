#!/usr/bin/env python3
"""Reproduction of finite impurity-array spectral tests on regular trees.
Scientific claims and derivations are in RESULT.md; these numerical tests are supplementary.
Requires numpy and scipy. All tests are deterministic and use only local computations.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.sparse import lil_matrix, eye
from scipy.sparse.linalg import spsolve

checks = 0
worst = 0.0

def near(a, b, tol=3e-10):
    global checks, worst
    err = abs(a-b)/max(1,abs(a),abs(b))
    worst = max(worst,err)
    assert err < tol, (a,b,err)
    checks+=1

def free_green(q, lam, dist):
    branch=(lam-math.sqrt(lam*lam-4*(q-1)))/(2*(q-1))
    onsite=1/(lam-q*branch)
    return onsite*branch**dist

def calc_theta_roots(p,r):
    def phi(t):
        return math.atan2(math.sin(t),math.cos(t)-r)
    def quant(t,j):
        return (p-1)*t+2*phi(t)-j*math.pi
    return np.array([brentq(lambda t:quant(t,j), 1e-13, math.pi-1e-13, xtol=1e-13) for j in range(1,p+1)])

for q in (3,4,5,7):
    c=math.sqrt(q-1)/(q-2)
    for d in (1,2,3):
        r=(q-1)**(-d/2)
        for p in (1,2,3,4,5,8,12,20):
            js=np.arange(p)
            C=r**np.abs(js[:,None]-js[None,:])
            eig=np.linalg.eigvalsh(C)[::-1]
            th=calc_theta_roots(p,r)
            predicted=(1-r*r)/(1+r*r-2*r*np.cos(th))
            for u,v in zip(eig,predicted): near(u,v)
            first=1/(c*eig[0]); last=1/(c*eig[-1])
            for kappa in (.1,.3,.7,1.3,3.2,6.0):
                direct=int(np.count_nonzero(kappa*c*eig > 1+1e-11))
                angles=int(np.count_nonzero(kappa>1/(c*predicted)+1e-11))
                assert direct==angles
                checks+=1
            if p>1:
                inv=np.linalg.inv(C)
                tr=np.diag(np.full(p,1+r*r))
                tr[0,0]=tr[-1,-1]=1
                tr+=np.diag(np.full(p-1,-r),1)+np.diag(np.full(p-1,-r),-1)
                near(np.linalg.norm((1-r*r)*inv-tr),0,tol=3e-10)
            if p>=8:
                low=(1-r)/(c*(1+r)); high=(1+r)/(c*(1-r))
                assert low<first and last<high
                checks+=2

# Independent finite-tree Dirichlet-resolvent comparisons, not an infinite-volume proof.
def tree_ball(q,R):
    # Generations of a rooted regular tree; all boundary branches omitted.
    edges=[]; parents=[-1]; depth=[0]; frontier=[0]
    for layer in range(1,R+1):
        new=[]
        for par in frontier:
            children=q if par==0 else q-1
            for _ in range(children):
                k=len(parents)
                parents.append(par);depth.append(layer)
                edges.append((par,k));new.append(k)
        frontier=new
    A=lil_matrix((len(parents),len(parents)),dtype=float)
    for a,b in edges:A[a,b]=A[b,a]=1.0
    return A.tocsr(),parents,depth

for q in (3,4):
    A,parents,depth=tree_ball(q,7 if q==3 else 5)
    # Choose a straight branch path from root.
    chain=[0]
    for d in range(3):
        v=next(j for j,p in enumerate(parents) if p==chain[-1])
        chain.append(v)
    for e_offset in (1.0,2.0,5.0):
        lam=2*math.sqrt(q-1)+e_offset
        I=eye(A.shape[0],format='csr')
        b=np.zeros(A.shape[0]);b[0]=1
        x=spsolve(lam*I-A,b)
        for d in range(4):
            # Finite tree only approximates free resolvent; compare with loose
            # tolerance and convergence at a more distant spectral point.
            exact=free_green(q,lam,d)
            err=abs(x[chain[d]]-exact)/exact
            assert err < .14,(q,lam,d,err)
            checks+=1

# Large-size density, critical finite-p shifts, and exact finite-p thresholds.
for q,d in ((3,1),(4,2),(7,1)):
    c=math.sqrt(q-1)/(q-2); r=(q-1)**(-d/2)
    low=(1-r)/(c*(1+r)); high=(1+r)/(c*(1-r))
    p=600
    j=np.arange(p)
    # Work with an explicit tridiagonal inverse to avoid dense 600x600 eigenproblem.
    from scipy.linalg import eigh_tridiagonal
    diag=np.full(p,1+r*r);diag[0]=diag[-1]=1
    off=np.full(p-1,-r)
    D=eigh_tridiagonal(diag,off,eigvals_only=True)
    eig=(1-r*r)/D
    first=1/(c*eig[0]);last=1/(c*eig[-1])
    first_const=(first-low)*p*p/(low*r*math.pi**2/(1-r)**2)
    last_const=(high-last)*p*p/(high*r*math.pi**2/(1+r)**2)
    assert abs(first_const-1)<.025,(q,d,first_const)
    assert abs(last_const-1)<.025,(q,d,last_const)
    checks+=2
    for fraction in (.1,.25,.5,.75,.9):
        kappa=low+fraction*(high-low)
        t=(1+r*r-kappa*c*(1-r*r))/(2*r)
        frac=math.acos(max(-1,min(1,t)))/math.pi
        empirical=float(np.count_nonzero(kappa*c*eig>1))/p
        assert abs(frac-empirical)<.005,(q,d,frac,empirical)
        checks+=1

print(f'PASS {checks} numeric comparisons; max normalized equality error {worst:.3g}; finite-ball tests are approximate')
