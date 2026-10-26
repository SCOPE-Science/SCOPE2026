#!/usr/bin/env python3
"""Independent matrix-superoperator checks for an edge-exchange dissipator.
Run: python3 edge_noise_verify.py (requires numpy)."""
import itertools
import numpy as np

def spectrum(n, edges):
    d = np.zeros(n)
    W = np.zeros((n,n))
    for (i,j),w in edges.items():
        d[i]+=w;d[j]+=w;W[i,j]=W[j,i]=w
    lap = np.diag(d)-W
    rates = list(np.linalg.eigvalsh(lap))
    for i in range(n):
        for j in range(i+1,n):
            rates += [(d[i]+d[j])/2-W[i,j],(d[i]+d[j])/2+W[i,j]]
    return np.sort(np.array(rates)), min(np.linalg.eigvalsh(lap)[1], min((d[i]+d[j])/2-W[i,j] for i in range(n) for j in range(i+1,n)))

def dense(n, edges):
    # Column-major (Fortran) vectorization: vec(V X V)=(V^T tensor V) vec(X).
    eye = np.eye(n); superop = np.zeros((n*n,n*n))
    for (i,j),w in edges.items():
        V = np.zeros((n,n));V[i,j]=V[j,i]=1
        S=V@V
        superop += w*(np.kron(V,V)-.5*(np.kron(eye,S)+np.kron(S,eye)))
    return np.sort(-np.linalg.eigvalsh(superop))

def main():
    rng = np.random.default_rng(4026)
    k=0
    for n in [3,4]:
        pairs=list(itertools.combinations(range(n),2))
        for mask in range(1<<len(pairs)):
            edges={p:float((mask>>z)&1) for z,p in enumerate(pairs)}
            r,g=spectrum(n,edges)
            assert np.allclose(r,dense(n,edges),atol=1e-10), (n,mask)
            k+=1
    for n in [3,4,5,6]:
        pairs=list(itertools.combinations(range(n),2))
        for _ in range(25 if n<=5 else 5):
            v=rng.random(len(pairs));v*=5/v.sum()
            edges=dict(zip(pairs,v))
            r,g=spectrum(n,edges)
            assert np.allclose(r,dense(n,edges),atol=1e-9),n
            B=sum(edges.values());target=(n-2)*B/len(pairs)
            assert g<=target+1e-9
            k+=1
    n=4;B=6.;pairs=list(itertools.combinations(range(n),2))
    for t in [-1.,-.5,0.,.4,1.]:
        edges={p:1. for p in pairs}
        edges[(0,1)]=1+t;edges[(2,3)]=1-t
        _,gap=spectrum(4,edges)
        assert abs(gap-B/3)<1e-10
        k+=1
    print(f'CHECKS_PASSED {k}')
if __name__=='__main__':main()
