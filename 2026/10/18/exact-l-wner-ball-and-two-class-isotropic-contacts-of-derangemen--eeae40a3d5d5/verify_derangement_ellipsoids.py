"""Reproducible numerical and exact-arithmetic checks for derangement-polytope ellipsoids.

The theorem is established analytically; finite checks only guard against algebraic errors.
"""
from fractions import Fraction
from itertools import permutations
import numpy as np


def cycle_lengths(p):
    seen=set(); out=[]
    for i in range(len(p)):
        if i in seen: continue
        j=i; count=0
        while j not in seen:
            seen.add(j); count+=1; j=p[j]
        out.append(count)
    return sorted(out)


def projection(n):
    edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
    B=np.zeros((2*n,len(edges)))
    for col,(i,j) in enumerate(edges):
        B[i,col]=1.;B[n+j,col]=1.
    PH=np.eye(len(edges))-B.T @ np.linalg.pinv(B @ B.T) @ B
    return edges, PH


def check(n):
    N=n*(n-1);dim=n*n-3*n+1
    edges,PH=projection(n)
    assert np.linalg.norm(PH@PH-PH)<1e-8
    assert abs(np.trace(PH)-dim)<1e-8
    assert np.max(np.abs(np.diag(PH)-dim/N))<1e-8
    C=np.full(N, 1/(n-1))
    reps={"long":[],"short":[]}
    target_high=[2]*(n//2) if n%2==0 else [2]*((n-3)//2)+[3]
    target_high=sorted(target_high)
    for p in permutations(range(n)):
        typ=cycle_lengths(p)
        if typ==[n]: reps['long'].append(p)
        if typ==target_high: reps['short'].append(p)
    def covariance(arr):
        X=np.stack([np.array([float(j==p[i]) for i,j in edges])-C for p in arr])
        return (X.T@X)/len(X),X
    cov_long,x_long=covariance(reps['long'])
    if n==3:
        COV=cov_long;w=Fraction(0,1)
    else:
        cov_short,x_short=covariance(reps['short'])
        d=dim
        w=Fraction(n-3,d) if n%2==0 else Fraction(n,d)
        COV=(1-float(w))*cov_long+float(w)*cov_short
    R2=Fraction(n*(n-2),n-1)
    if n>=4:
        design_mean=(1-float(w))*x_long.mean(axis=0)+float(w)*x_short.mean(axis=0)
        assert np.max(np.abs(design_mean))<1e-10
    assert np.max(np.abs(COV-float(R2)/dim*PH))<1e-10,(n,np.max(np.abs(COV-float(R2)/dim*PH)))
    assert np.max(np.abs(np.linalg.norm(x_long,axis=1)**2-float(R2)))<1e-8
    return {'n':n,'dimension':dim,'R2':str(R2),
            'mixed_high_weight':str(w),'long_orbit_size':len(reps['long']),
            'high_orbit_size':len(reps['short']),
            'projector_residual':float(np.max(np.abs(COV-float(R2)/dim*PH)))}


if __name__=='__main__':
    for n in range(3,8): print(check(n))
    print('All projection, contact and isotropic two-orbit covariance tests passed.')
