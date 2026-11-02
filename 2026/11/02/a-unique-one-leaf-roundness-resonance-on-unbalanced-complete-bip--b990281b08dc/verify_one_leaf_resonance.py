"""Reproducible numerical/exact diagnostic checks for a one-leaf metric theorem.

Run: python verify_one_leaf_resonance.py
Optional dependency: numpy (for full-matrix spectra).
The universal assertions rely on the accompanying mathematical proof, not these tests.
"""
from fractions import Fraction as F
from math import log, log2, expm1, log1p, isclose
import random
import numpy as np


def p0(m, n):
    return log2(2 * m * n / (2 * m * n - m - n))


def delta(m, n, t, p=None):
    if p is None:
        p = p0(m, n)
    # Stable near large t and small exponent: powers of t cancel.
    return (t**p / m + (m-1) * (2.0**p) * expm1(p*log1p(t/2.0))/m
            - expm1(p*log1p(t)))


def positive_resonance(m, n):
    assert m > n >= 2
    # Ignore the trivial t=0 root.
    lo = 1.0e-14
    assert delta(m, n, lo) > 0
    hi = 1.0
    while delta(m, n, hi) > 0:
        hi *= 2.0
        assert hi < 1.0e12
    for _ in range(180):
        mid = (lo + hi) / 2.0
        if delta(m, n, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def metric(m,n,t, exact=False):
    N=m+n+1
    D=[[F(0) if exact else 0.0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if i==N-1:
                d=t if j==0 else (t+2 if j<m else t+1)
            else:
                d=2 if (i<m and j<m) or (m<=i<m+n and m<=j<m+n) else 1
            D[i][j]=D[j][i]=d
    return D


def formula_and_matrix(m,n,t,p,vec):
    D=metric(m,n,t)
    N=m+n+1
    direct=sum(vec[i]*vec[j]*(D[i][j]**p if i!=j else 0) for i in range(N) for j in range(N))
    h=vec[-1]
    c=vec[:-1].copy();c[0]+=h
    sig=sum(c[:m]); Abar=sig/m; Bbar=sum(c[m:])/n
    A=[v-Abar for v in c[:m]]; B=[v-Bbar for v in c[m:]]
    u=2**p; T=t**p; R=(t+2)**p-u; U=(t+1)**p-1
    radial=(2*(u-1)-u*(1/m+1/n))*sig*sig
    predicted=(radial-u*(sum(x*x for x in A)+sum(x*x for x in B))
               +2*h*(sig*((T+(m-1)*R)/m-U)+(T-R)*A[0])-2*T*h*h)
    return direct, predicted


def maxzero_eigs(m,n,t,p):
    D=np.asarray(metric(m,n,t), dtype=float)**p
    N=m+n+1
    E=np.zeros((N,N-1),dtype=float)
    for i in range(N-1):E[i,i]=1;E[-1,i]=-1
    Q,R=np.linalg.qr(E)
    return np.linalg.eigvalsh(Q.T @ D @ Q)


def exact_decomposition():
    rng=random.Random(20261031)
    checked=0
    for m in range(2,8):
      for n in range(2,8):
        for t in [F(1,3),F(1),F(7,4)]:
          for p in [1,2]:
            D=metric(m,n,t,True)
            for _ in range(6):
              vec=[F(rng.randint(-4,4)) for j in range(m+n)]
              vec.append(-sum(vec))
              h=vec[-1]; c=vec[:-1].copy(); c[0]+=h
              sig=sum(c[:m]); Abar=sig/m; Bbar=sum(c[m:])/n
              Af=[v-Abar for v in c[:m]]; Bf=[v-Bbar for v in c[m:]]
              u=F(2)**p;T=t**p;R=(t+2)**p-u;U=(t+1)**p-1
              radial=(2*(u-1)-u*(F(1,m)+F(1,n)))*sig*sig
              expr=(radial-u*(sum(x*x for x in Af)+sum(x*x for x in Bf))+
                   2*h*(sig*((T+(m-1)*R)/m-U)+(T-R)*Af[0])-2*T*h*h)
              q=sum(vec[i]*vec[j]*D[i][j]**p for i in range(m+n+1) for j in range(m+n+1))
              assert q==expr,(m,n,t,p,q,expr)
              checked+=1
    print('EXACT_RATIONAL_ZERO_SUM_DECOMPOSITION_OK',checked)


def spectral_phase():
    checked=0
    for m in range(2,13):
      for n in range(2,13):
        p=p0(m,n)
        if m==n==2:
            for t in [.1,1,3,100]:
                eig=maxzero_eigs(m,n,t,p)
                assert abs(eig[-1])<1e-8 and eig[-2]<-0.01
                checked+=1
        elif m>n:
            root=positive_resonance(m,n)
            for t in [root]:
                eig=maxzero_eigs(m,n,t,p)
                assert abs(eig[-1])<2e-8 and eig[-2]<-1e-5,(m,n,t,eig[-2:])
                checked+=1
            for t in [root*0.5,root*1.5]:
                eig=maxzero_eigs(m,n,t,p)
                assert eig[-1]>1e-12,(m,n,t,eig[-1])
                checked+=1
        else:
            for t in [0.1,1,10]:
                eig=maxzero_eigs(m,n,t,p)
                assert eig[-1]>1e-12,(m,n,t,eig[-1])
                checked+=1
    print('RESONANCE_AND_STRICT_DROP_FULL_MATRIX_OK',checked)


def asymptotics():
    for k in [1,2,4]:
        goal=2.0/(k*log(2))
        n=1000; t=positive_resonance(n+k,n)
        assert abs(t/n-goal)/goal<.04,(k,t/n,goal)
    print('NEAR_BALANCED_LINEAR_RESONANCE_SCALE_OK')
    for n in [2,3,5]:
        p=log2(2*n/(2*n-1))
        goal=(p*(1-2**(p-1)))**(-1/(1-p))
        m=2000;t=positive_resonance(m,n)
        val=t*m**(1/(1-p))
        assert abs(val-goal)/goal<.02,(n,val,goal)
    print('FIXED_SMALL_PART_SINGULAR_RESONANCE_SCALE_OK')


if __name__=='__main__':
    exact_decomposition()
    spectral_phase()
    asymptotics()
    print('ALL_ONE_LEAF_BICLIQUE_RESONANCE_CHECKS_OK')
