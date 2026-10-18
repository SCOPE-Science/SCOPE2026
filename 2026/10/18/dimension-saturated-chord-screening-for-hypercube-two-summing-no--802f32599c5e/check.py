#!/usr/bin/env python3
"""Standalone numerical cross-checks for hypercube edge-gradient two-summing thresholds.
Uses only NumPy and SciPy. Analytical proof establishes all dimensions.
"""
from math import comb, sqrt
import numpy as np
from scipy.optimize import minimize

def edge_vectors(d):
    n = 1 << d
    edges = [(u,u^(1<<i)) for u in range(n) for i in range(d) if u < (u^(1<<i))]
    vectors=[]
    for u,v in edges:
        b=np.zeros(n); b[u]=1; b[v]=-1; vectors.append(b)
    return edges, np.asarray(vectors)

def r_formula(d,k):
    ans=0.0
    for j in range(1,d+1):
        count=sum(comb(k,z)*comb(d-k,j-z) for z in range(1,k+1,2) if 0<=j-z<=d-k)
        ans+=count / sqrt(2*j)
    return 4*ans/(2**d)

def objective(w,rows):
    L=(rows*np.sqrt(np.maximum(w,0))[:,None]).T @ (rows*np.sqrt(np.maximum(w,0))[:,None])
    eig=np.linalg.eigvalsh(L)
    return np.sqrt(np.maximum(eig[eig>1e-11],0)).sum()

def run():
    checks=0
    for d in range(3,7):
        edges,E=edge_vectors(d)
        lap=E.T@E
        lam,U=np.linalg.eigh(lap)
        H=(U[:,lam>1e-8]/np.sqrt(lam[lam>1e-8]))@U[:,lam>1e-8].T
        r=[]
        for k in range(1,d+1):
            b=np.zeros(1<<d); b[0]=1;b[(1<<k)-1]=-1
            rnum=b@H@b
            rform=r_formula(d,k)
            assert abs(rnum-rform)<1e-10,(d,k,rnum,rform)
            r.append(rform);checks+=1
        assert all(r[i+1]>r[i]+1e-10 for i in range(d-1))
        assert all(r[k-1]<k*r[0] for k in range(2,d+1))
        expected=sum(comb(d,j)*sqrt(2*j) for j in range(1,d+1))/sqrt(len(edges))
        assert abs(objective(np.ones(len(edges))/len(edges),E)-expected)<1e-10
        checks+=3
    # Optimizations for a few added chords, both sides of their joint thresholds.
    for d in [3,4]:
        edges,E=edge_vectors(d)
        m=len(edges)
        w0=np.r_[np.ones(m)/m, np.zeros(3)]
        target=[(0,3),(0,7),(1,6)] if d==3 else [(0,3),(0,7),(0,15)]
        for amp_factor in [.85,.99,1.01,1.15]:
            rows=[]
            for u,v in target:
                k=(u^v).bit_count()
                amp=amp_factor*sqrt(r_formula(d,1)/r_formula(d,k))
                b=np.zeros(1<<d);b[u]=amp;b[v]=-amp;rows.append(b)
            R=np.vstack([E,np.array(rows)])
            base=objective(w0,R)
            res=minimize(lambda w:-objective(w,R),w0,method='SLSQP',
                         bounds=[(0,1)]*len(R),constraints=[{'type':'eq','fun':lambda w:sum(w)-1}],
                         options={'maxiter':350,'ftol':2e-11})
            gain=-res.fun-base
            if amp_factor<1:
                assert abs(gain)<1e-6,(d,amp_factor,gain,res.message)
            else:
                assert gain>1e-8,(d,amp_factor,gain,res.message)
            checks+=1
    # Explicit dimension-asymptotic scaling and maximal pointwise amplification.
    for d in [20,40,80]:
        td=sqrt(r_formula(d,1)/r_formula(d,d))
        assert abs(d*(1-td)-.25)<.05,(d,td)
        assert d*td >d-1
        checks+=2
    print('PASS',checks,'independent spectral, derivative, optimization, and scaling checks')
if __name__=='__main__':run()
