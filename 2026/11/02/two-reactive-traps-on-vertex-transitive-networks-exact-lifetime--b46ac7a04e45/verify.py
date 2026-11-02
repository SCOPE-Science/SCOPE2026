#!/usr/bin/env python3
"""Numerical checks of the two-target resistance law using independent linear solves."""
import numpy as np

def test_graph(A, rng):
    n=len(A)
    L=np.diag(A.sum(axis=1))-A
    G=np.linalg.pinv(L,hermitian=True)
    assert np.max(np.abs(np.diag(G)-G[0,0]))<5e-10
    g=float(np.trace(G)/n)
    tests=0
    for _ in range(40):
        a,b=rng.choice(n,2,replace=False)
        d=float(G[a,a]-G[a,b])
        assert d>0
        K=float(np.exp(rng.uniform(-3,3)))
        f=float(rng.uniform(0.02,0.98))
        ka,kb=K*f,K*(1-f)
        M=L.copy();M[a,a]+=ka;M[b,b]+=kb
        actual=float(np.linalg.solve(M,np.ones(n)).mean())
        P=ka*kb
        pred=n*g+n*(1-d*d*P)/(K+2*d*P)
        assert np.isclose(actual,pred,rtol=2e-9,atol=3e-9),(n,a,b,actual,pred)
        M2=L.copy();M2[a,a]+=K/2;M2[b,b]+=K/2
        eq=float(np.linalg.solve(M2,np.ones(n)).mean())
        optimal=n/K+n*g-n*d/2
        assert np.isclose(eq,optimal,rtol=2e-9,atol=3e-9)
        assert eq<=actual+1e-8
        tests+=3
    return tests

def cycle(n):
    A=np.zeros((n,n))
    for i in range(n):
        A[i,(i+1)%n]=1;A[i,(i-1)%n]=1
    return A

def complete(n):return np.ones((n,n))-np.eye(n)

def hypercube(d):
    n=2**d;A=np.zeros((n,n))
    for i in range(n):
        for j in range(d):A[i,i^(1<<j)]=1
    return A

def torus(n,m):
    N=n*m;A=np.zeros((N,N))
    idx=lambda i,j:(i%n)*m+(j%m)
    for i in range(n):
        for j in range(m):
            for u,v in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:A[idx(i,j),idx(u,v)]+=1
    return A

def main():
    rng=np.random.default_rng(20261027)
    graphs=[cycle(n) for n in [4,5,7,9,12]] + [complete(n) for n in [4,7,11]] + [hypercube(d) for d in [2,3,4]] + [torus(3,3),torus(3,4),torus(4,4)]
    checks=sum(test_graph(g,rng) for g in graphs)
    A=torus(3,3);G=np.linalg.pinv(np.diag(A.sum(axis=1))-A,hermitian=True)
    assert np.isclose(G[0,0],2/9,atol=1e-12)
    assert np.isclose(2*(G[0,0]-G[0,1]),4/9,atol=1e-12)
    assert np.isclose(2*(G[0,0]-G[0,4]),5/9,atol=1e-12)
    print('PASS',checks+3,'independent numerical assertions')
if __name__=='__main__':main()
