"""Independent finite checks for two-orientation electrical design on cyclic tori.

Run: python verify.py
Requires: numpy, scipy. All tests use deterministic data.
These finite computations corroborate, but do not replace, the general proof.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.optimize import brentq

checks = 0

def check(test, message):
    global checks
    checks += 1
    if not bool(test):
        raise AssertionError(message)

def cycle_eigenvalues(n):
    return 4 * np.sin(np.pi * np.arange(n) / n) ** 2

def fourier_trace(m, n, x, y):
    a = cycle_eigenvalues(m)[:, None]
    b = cycle_eigenvalues(n)[None, :]
    D = x*a + y*b
    D[0, 0] = np.inf
    return float(np.sum(1/D))

def stationarity(m, n, tau):
    a = cycle_eigenvalues(m)[:, None]
    b = cycle_eigenvalues(n)[None, :]
    D = a+tau*b
    D[0, 0] = np.inf
    return float(np.sum((a-b)/D**2))

def optimal_tau(m, n):
    return brentq(lambda t: stationarity(m, n, t), 1e-12, 1e12,
                  xtol=1e-14, rtol=1e-13)

def graph_edges(m, n):
    edges = []
    for i in range(m):
        for j in range(n):
            v = i*n+j
            edges.append((v, ((i+1)%m)*n+j, 0))
            edges.append((v, i*n+(j+1)%n, 1))
    return edges

def full_trace(m, n, weights):
    N = m*n
    L = np.zeros((N, N))
    for (i, j, _), w in zip(graph_edges(m, n), weights):
        L[i, i] += w
        L[j, j] += w
        L[i, j] -= w
        L[j, i] -= w
    ev = np.linalg.eigvalsh(L)
    check(abs(ev[0]) < 3e-10, 'zero eigenvalue')
    check(ev[1] > 0, 'positive spectral gap')
    return float(np.sum(1/ev[1:]))

def direct_laplacian_eigenvalues(m,n,x,y):
    N=m*n
    L=np.zeros((N,N))
    for i,j,k in graph_edges(m,n):
        w=[x,y][k]
        L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
    return np.linalg.eigvalsh(L)

# Fourier spectrum, trace, and the nontrivial minimizer checked
# against the full, independently assembled weighted Laplacian.
for m,n in [(3,3),(4,3),(6,3),(5,4),(8,3)]:
    a=cycle_eigenvalues(m)
    b=cycle_eigenvalues(n)
    for x,y in [(0.3,0.7),(0.55,0.45),(1.5,2.5)]:
        A=np.sort((x*a[:,None]+y*b[None,:]).ravel())
        E=direct_laplacian_eigenvalues(m,n,x,y)
        for p,q in zip(A,E):check(abs(p-q)<1e-10,'Fourier eigenvalue')
        w=[x if k==0 else y for _,_,k in graph_edges(m,n)]
        F=full_trace(m,n,w)
        check(abs(F-fourier_trace(m,n,x,y))<1e-8,'Fourier trace')

rng=np.random.default_rng(246810)
for m,n in [(3,3),(4,3),(6,3),(5,4)]:
    t=optimal_tau(m,n)
    check(abs(stationarity(m,n,t))<1e-7,'stationarity')
    if m==n:check(abs(t-1)<1e-11,'axis exchange symmetry')
    x,y=1/(1+t),t/(1+t)
    optimum=fourier_trace(m,n,x,y)
    check(abs(full_trace(m,n,[x if k==0 else y for _,_,k in graph_edges(m,n)])-optimum)<1e-8,'full optimum')
    for lam in np.linspace(0.01,0.99,51):
        check(fourier_trace(m,n,lam,1-lam)+1e-7>=optimum,'scalar global')
    for sample in range(60):
        ws=rng.gamma(1.5,1,size=2*m*n)
        ws=ws/ws.sum()*(m*n)
        F=full_trace(m,n,ws)
        check(F+1e-6>=optimum,'asymmetric global competitor')

# Exact one-cycle Green kernel identity and its c-derivative.
for m in [3,4,7,18,60]:
    for c in [0.0008,0.02,0.3,1.1,5.0]:
        theta=2*math.asinh(math.sqrt(c)/2)
        coth=1/math.tanh(m*theta/2)
        val=m/math.sqrt(c*(c+4))*coth
        direct=float(sum(1/(u+c) for u in cycle_eigenvalues(m)))
        check(abs(val-direct)<1e-7*max(1,abs(direct)), 'cycle Green')

# Scaling tests are evidence for the proven asymptotic, not an infinite certificate.
for n in [3,4,7]:
    Sn=sum(1/math.sqrt(b) for b in cycle_eigenvalues(n)[1:])
    z=(3*Sn)**(2/3)
    old_ratio=0
    for m in [120,480,1920]:
        t=optimal_tau(m,n)
        ratio=t/(z*m**(-2/3))
        check(0.6<ratio<1.02,'asymptotic parameter range')
        check(ratio>old_ratio,'asymptotic convergence in test')
        old_ratio=ratio
        F=(1+t)*fourier_trace(m,n,1,t)
        # This is precisely the trace for x+y=1.
        C=(F-m*m/12)/(m**(4/3))
        check(abs(C-z/4)<0.18,'asymptotic cost constant')
        isotropic=fourier_trace(m,n,0.5,0.5)
        check(F<isotropic,'improvement on isotropic')

print(f'PASS: {checks} full-matrix, Fourier, Green-identity and finite asymptotic checks.')
