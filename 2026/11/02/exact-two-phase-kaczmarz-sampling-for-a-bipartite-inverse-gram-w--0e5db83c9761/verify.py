"""Standalone exact certificate and numerical cross-check for bipartite signed-precision sampling.

Run: python verify.py. Requires numpy and scipy for the independent eigenvalue
and optimization cross-checks; exact algebraic identities use only fractions.
"""
from fractions import Fraction as F
import math
import numpy as np


def model(p, q, w, v):
    n = p + q
    C = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(p):
        for j in range(p,n):
            C[i][j] = C[j][i] = w
    C[0][1] = C[1][0] = -v
    for i in range(n):
        C[i][i] = F(4) + sum(abs(C[i][j]) for j in range(n) if i != j)
    return C


def certificate(C, p, q, w, v):
    n = p+q
    z = min(F(1), w*q/(2*v))
    k = [F(0) for _ in range(n)]
    k[0] = k[1] = w*q*z-v*(2*z*z-1)
    for i in range(2,p): k[i] = w*q
    for i in range(p,n): k[i] = w*(p-2+2*z)
    d = [C[i][i] + k[i] for i in range(n)]
    T = sum(d)
    X = [[F(1) for _ in range(n)] for _ in range(n)]
    X[0][1] = X[1][0] = 2*z*z - 1
    for i in range(2,n):
        X[0][i] = X[i][0] = z
        X[1][i] = X[i][1] = z
    S = [[(d[i] if i==j else F(0))-C[i][j] for j in range(n)] for i in range(n)]
    SX = [[sum(S[i][k]*X[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    dual = sum(C[i][j]*X[i][j] for i in range(n) for j in range(n))
    assert all(x==0 for row in SX for x in row)
    assert T==dual and T>0 and all(d_i>0 for d_i in d)
    expected = sum(C[i][i] for i in range(n)) + 2*(w*q*(p-2+2*z)-v*(2*z*z-1))
    assert T == expected
    return d,T,S,X,z


def min_eig(M): return float(np.linalg.eigvalsh(np.asarray(M,dtype=float))[0])


def one_test(p,q,w,v):
    C=model(p,q,w,v)
    d,T,S,X,z=certificate(C,p,q,w,v)
    assert min_eig(C)>0
    assert min_eig(S)>-1e-8
    assert min_eig(X)>-1e-8
    a=np.array(C,dtype=float)
    G=np.linalg.inv(a)
    prob=np.array(d,dtype=float)/float(T)
    gamma=min_eig((np.sqrt(prob)[:,None]*G)*np.sqrt(prob)[None,:])
    assert abs(gamma-1/float(T)) < 1e-9
    return prob, gamma, a


def normalized_example(q,v0):
    # Symmetry-preserving row normalization for p=2; the inverse row Gram
    # retains exactly one positive cross-edge weight and one negative pair.
    p=2; n=p+q; w0=0.10
    C0=np.array(model(p,q,F(1,10),v0),dtype=float)
    G0=np.linalg.inv(C0)
    norm=np.sqrt(np.diag(G0))
    C=np.diag(norm)@C0@np.diag(norm)
    G=np.linalg.inv(C)
    assert np.max(np.abs(np.diag(G)-1))<1e-11
    w=float(C[0,2]);v=-float(C[0,1])
    assert np.max(abs(C[0,2:]-w))<1e-12
    assert np.max(abs(C[1,2:]-w))<1e-12
    assert np.max(abs(C[2:,2:]-np.diag(np.diag(C[2:,2:]))))<1e-12
    return C,G,w,v


def optimize_checks(C,G,p,q,w,v):
    n=p+q
    z=min(1.0,w*q/(2*v))
    k=np.zeros(n)
    k[:2]=w*q*z-v*(2*z*z-1)
    k[2:p]=w*q
    k[p:]=w*(p-2+2*z)
    d=np.diag(C)+k
    pstar=d/d.sum()
    gamma=1/d.sum()
    def f(pr):
        r=np.sqrt(np.maximum(pr,0))
        return -min_eig((r[:,None]*G)*r[None,:])
    rng=np.random.default_rng(9287+n)
    candidates=[np.ones(n)/n]+[rng.dirichlet(np.ones(n)) for _ in range(100)]
    for candidate in candidates:
        assert -f(candidate)<=gamma+5e-9
    # Random competitors give an independent finite-dimensional stress test;
    # the global certificate itself is the exact PSD primal-dual proof.
    for scale in [0.001,0.01,0.05,0.2]:
        for _ in range(20):
            perturb=rng.normal(0,scale,n)
            competitor=pstar*np.exp(perturb)
            competitor/=competitor.sum()
            assert -f(competitor)<=gamma+5e-9
    assert abs(-f(pstar)-gamma)<5e-10
    return gamma


def main():
    algebraic=0
    for p in range(2,7):
        for q in range(2,7):
            for w in [F(1,7),F(2,5),F(5,6)]:
                threshold=w*q/2
                for relative in [F(1,4),F(3,4),F(1),F(5,4),F(3),F(9)]:
                    one_test(p,q,w,threshold*relative)
                    algebraic+=1
    print('Exact primal-dual identities and spectral checks:',algebraic)
    for p,q in [(2,2),(2,4),(3,2),(3,4),(4,3)]:
        for relative in [F(1,2),F(1),F(3,2),F(4)]:
            w=F(1,9);v=w*q*relative/2
            prob,gamma,C=one_test(p,q,w,v)
            optimize_checks(C,np.linalg.inv(C),p,q,float(w),float(v))
    print('Random and perturbed sampling comparisons: 20 models')
    for v0 in [F(1,20),F(1,4),F(3,4)]:
        C,G,w,v=normalized_example(3,v0)
        optimize_checks(C,G,2,3,w,v)
    print('Unit-row-normalized model comparisons: 3')
    print('PASS')

if __name__ == '__main__':main()
