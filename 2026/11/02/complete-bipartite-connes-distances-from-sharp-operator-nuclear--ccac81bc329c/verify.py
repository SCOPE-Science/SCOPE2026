#!/usr/bin/env python3
"""Reproduce finite diagnostics for the exact complete-bipartite Connes metric.
Scientific proof uses analytic rank-two primal/dual certificates, not these tests.
Requires Python 3 and NumPy. Run: python3 verify.py
"""
import math
import numpy as np

def basis(n, i):
    e = np.zeros(n); e[i] = 1.
    u0 = np.ones(n) / math.sqrt(n)
    u1 = (e - np.ones(n)/n) / math.sqrt(1-1/n)
    assert abs(np.dot(u0,u1)) < 1e-13
    return u0,u1

def opnorm(m):
    return np.linalg.svd(m,compute_uv=False)[0]

def dual_certificate(p,q):
    u0,u1=basis(p,0)
    v0,v1=basis(q,0)
    alpha,beta=math.sqrt(p-1),math.sqrt(q-1)
    Y=(np.outer(u0,v0)+beta*np.outer(u0,v1)+alpha*np.outer(u1,v0)+np.outer(u1,v1))/math.sqrt(p*q)
    assert np.allclose(Y @ np.ones(q),np.eye(p)[0])
    assert np.allclose(np.ones(p) @ Y,np.eye(q)[0])
    return Y

def cross_certificate(p,q):
    u0,u1=basis(p,0);v0,v1=basis(q,0)
    a=u1/math.sqrt(q);b=-v1/math.sqrt(p)
    M=np.subtract.outer(a,b)
    v=(math.sqrt(p-1)+math.sqrt(q-1))/math.sqrt(p*q)
    Y=dual_certificate(p,q)
    assert math.isclose(opnorm(M),1,rel_tol=1e-12,abs_tol=1e-12)
    assert math.isclose(a[0]-b[0],v,rel_tol=1e-12,abs_tol=1e-12)
    assert math.isclose(sum(np.linalg.svd(Y,compute_uv=False)),v,rel_tol=1e-12,abs_tol=1e-12)
    assert math.isclose(np.sum(Y*M),v,rel_tol=1e-12,abs_tol=1e-12)
    return v

def within_certificate(p,q):
    a=np.zeros(p);a[0]=1/math.sqrt(2*q);a[1]=-a[0]
    M=np.subtract.outer(a,np.zeros(q))
    v=math.sqrt(2/q)
    assert math.isclose(opnorm(M),1,rel_tol=1e-12)
    assert math.isclose(a[0]-a[1],v,rel_tol=1e-12)
    return v

def main():
    pairs=0;random_tests=0
    rng=np.random.default_rng(23)
    for p in range(2,16):
      for q in range(2,16):
        cross_certificate(p,q);within_certificate(p,q)
        within_certificate(q,p)
        Y=dual_certificate(p,q)
        v=(math.sqrt(p-1)+math.sqrt(q-1))/math.sqrt(p*q)
        for _ in range(8):
          a=rng.normal(size=p);b=rng.normal(size=q)
          M=np.subtract.outer(a,b)
          assert abs(a[0]-b[0]) <= v*opnorm(M)+1e-10
          random_tests+=1
        pairs+=1
    print('PASS; (p,q) cases:',pairs,'random dual inequalities:',random_tests)
    print('K(2,2):',cross_certificate(2,2),'K(3,4):',cross_certificate(3,4),'K(9,9):',cross_certificate(9,9))
if __name__=='__main__':main()
