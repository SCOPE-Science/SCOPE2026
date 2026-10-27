"""Independent numerical replay and exact rational boundary certificates.

Run: python verify.py (requires numpy>=1.23).
Finite numerical tests illustrate, but do not prove, the universal theorem.
"""
from fractions import Fraction as F
from math import cos, pi, sqrt, isclose
import numpy as np

# Rational barriers used in the proof for n=10 and n=11.
assert F(119, 125)**2 > F(29, 32)
assert 1+324*F(119,125)**2 < F(86,5)**2
assert F(46,5)**2 < 85
assert F(19199,1000)**2 < F(5397041,14641)
assert F(10199,1000)**2 > 104
assert 12**3-13*12**2+20*12-10 > 0


def matrix(n,a,b):
    M=np.zeros((2*n+1,2*n+1))
    for i in range(n):
        s=1+i; t=1+n+i
        for u,v,w in [(0,s,a),(s,t,b),(s,1+n+(i-1)%n,b)]:
            M[u,v]+=w;M[v,u]+=w
    np.fill_diagonal(M,1-M.sum(axis=1))
    return M


def spectral(n,a,b):
    radial=np.array([[1-n*a,sqrt(n)*a,0],
          [sqrt(n)*a,1-a-2*b,2*b],[0,2*b,1-2*b]])
    r=list(np.linalg.eigvalsh(radial));r.pop(np.argmin([abs(x-1) for x in r]))
    vals=r[:]
    for k in range(1,n):
        cc=2*b*abs(cos(pi*k/n))
        m=np.array([[1-a-2*b,cc],[cc,1-2*b]])
        vals.extend(np.linalg.eigvalsh(m))
    return sorted(vals)


def mu(n,a,b):
    return max(map(abs,spectral(n,a,b)))

checked=0
for n in [3,4,5,6,7,8,9,10,11,12,13,20,30,100]:
    a=1/n;b=(1-a)/2
    M=matrix(n,a,b)
    assert np.max(abs(M-M.T))<1e-13
    assert np.max(abs(M.sum(axis=1)-1))<1e-13
    assert M.min()>-1e-13
    ev=np.linalg.eigvalsh(M)
    ev2=np.array(spectral(n,a,b)+[1.0])
    assert np.max(abs(ev-ev2))<1e-11,(n,ev,ev2)
    checked+=len(ev)
    pr=(1+sqrt(1+4*(n-1)**2*cos(pi/n)**2))/(2*n)
    rad=(n-1+sqrt((n-1)**2+4))/(2*n)
    if n>=11:
        assert pr>rad,(n,pr,rad)
        assert abs(mu(n,a,b)-pr)<1e-12
    elif n==10:
        assert pr<rad
        assert mu(n,a,b-1e-5)<mu(n,a,b)

for n in [11,12,15,30]:
    a0=1/n;b0=(1-a0)/2
    goal=mu(n,a0,b0)
    # Full two-variable orbit-invariant feasible region.
    for j in range(16):
        a=(j/15)/n
        for k in range(16):
            b=(1-a)*(k/15)/2
            assert mu(n,a,b)+1e-12>=goal,(n,a,b)
    # Nonuniform feasible matrices (edge weights constrained per vertex).
    rng=np.random.default_rng(12345+n)
    for _ in range(24):
        X=matrix(n,a0,b0)
        R=np.zeros_like(X)
        # Randomly reduce all existing edge weights, ensuring feasibility.
        ii,jj=np.triu_indices(2*n+1,1)
        for i,j in zip(ii,jj):
            if X[i,j]>0:
                w=float(X[i,j])*float(rng.uniform(.1,1))
                R[i,j]=R[j,i]=w
        np.fill_diagonal(R,1-R.sum(axis=1))
        assert R.min()>-1e-13
        evals=np.linalg.eigvalsh(R)
        assert max(abs(evals[:-1]))+1e-10>=goal

for n in [1000,10000]:
    a=1/n;c=cos(pi/n)
    optimal=(1+sqrt(1+4*(n-1)**2*c*c))/(2*n)
    m=(5-sqrt(1+16*c*c))/(2*n)
    met=1-1/(2*n)-2/3+sqrt(1/(4*n*n)+4*c*c/9)
    assert abs(n*(1-optimal)-0.5)<0.01
    assert abs(n*n*(met-optimal)-(pi*pi/6+1/16))<0.01
print('VERIFY_OK: 5 exact rational threshold inequalities; 14 spectral/dense comparisons; %d dense eigenvalues; 1024 orbit-feasible tests; 96 nonuniform tests; n=10 strict improvement; high-n asymptotics' % checked)
