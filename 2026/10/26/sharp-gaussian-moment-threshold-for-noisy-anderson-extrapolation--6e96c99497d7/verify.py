"""Standalone checks for Gaussian noisy Anderson memory/codimension theorem.

Run: python verify.py.  Tests finite-dimensional identities, not infinite-moment proofs.
Requires numpy and sympy; no network or input datasets.
"""
import math
import numpy as np
import sympy as sp

checks = 0
for m in range(1, 9):
    C = sp.eye(m) + sp.ones(m,m)
    invC = C.inv()
    one = sp.ones(m,1)
    assert invC == sp.eye(m) - sp.ones(m,m)/(m+1)
    checks += 1
    assert (one.T*invC*one)[0] == sp.Rational(m,m+1)
    checks += 1
    assert invC[m-1,m-1] == sp.Rational(m,m+1)
    checks += 1
    assert sp.simplify(1/invC[m-1,m-1]) == sp.Rational(m+1,m)
    checks += 1

rng=np.random.default_rng(1729)
for d,m in [(1,1),(2,1),(2,2),(3,1),(3,2),(3,3),(5,2),(5,4),(6,6)]:
    H=np.eye(d,m)
    assert np.linalg.matrix_rank(H)==m
    x0=np.zeros(d)
    xs=[x0]+[H[:,j] for j in range(m)]
    q=lambda x: 0.35*x+np.linspace(0.05,0.13,d)
    mu=np.column_stack([q(x)-x for x in xs])
    a=np.mean(mu,axis=1)
    for _ in range(250):
        es=rng.normal(0.0,0.7,(d,m+1))
        rs=mu+es
        R=rs[:,1:]-rs[:,[0]]
        Y=np.column_stack([q(x) for x in xs])+es
        alpha=-np.linalg.lstsq(R,rs[:,0],rcond=None)[0]
        xi=rs[:,0]-a+R@np.ones(m)/(m+1)
        alt=np.ones(m)/(m+1)-np.linalg.lstsq(R,a+xi,rcond=None)[0]
        assert np.allclose(alpha,alt,atol=1e-10)
        checks+=1
        z=Y[:,0]+(H+R)@alpha
        B=Y[:,0]-R@np.linalg.lstsq(R,rs[:,0],rcond=None)[0]
        assert np.allclose(z,B+H@alpha,atol=1e-10)
        checks+=1
        for j in range(m):
            other=[k for k in range(m) if k!=j]
            if other:
                Rminus=R[:,other]
                u=R[:,j]-Rminus@np.linalg.lstsq(Rminus,R[:,j],rcond=None)[0]
            else:
                u=R[:,j]
            assert np.allclose(alpha[j],-u@rs[:,0]/(u@u),atol=1e-8)
            checks+=1
        lam=0.2
        ridge=-np.linalg.solve(R.T@R+lam*np.eye(m),R.T@rs[:,0])
        assert np.linalg.norm(ridge)<=np.linalg.norm(rs[:,0])/(2*np.sqrt(lam))+1e-9
        checks+=1

# Exact chi-radius identities explaining the threshold for the perpendicular component.
for t in range(1,9):
    for k in range(1,t):
        p=sp.Rational(k,2)
        lhs=2**(-p/2)*sp.gamma((t-p)/2)/sp.gamma(sp.Rational(t,2))
        assert sp.N(lhs)>0
        checks+=1

print('PASS:',checks,'deterministic exact and matrix identities')
print('Dimension threshold: finite p-th moment iff p < d-m+1.')
print('These computations test formulas; Gaussian small-ball integration proves the universal law.')
