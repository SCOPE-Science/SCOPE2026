"""Exact checks for a singly reset linear Laplacian oscillator network.

Dependencies: Python 3.10+ and sympy; optional numpy for numerical diagnostics.
The analytical proof of the general theorem is in RESULT.md.
"""
from itertools import combinations
import sympy as s


def laplacian(n, edges):
    L=s.zeros(n)
    for i,j,w in edges:
        L[i,i]+=w; L[j,j]+=w
        L[i,j]-=w; L[j,i]-=w
    return L


def pinned_poisson(L, omega, r, k):
    n=L.rows; omega=s.Matrix(omega); Om=sum(omega)
    ix=[i for i in range(n) if i!=r]
    z=s.zeros(n,1)
    zs=(k*L.extract(ix,ix)).inv()*omega.extract(ix,[0])
    for i,entry in zip(ix,zs):z[i]=entry
    assert k*L*z==omega-Om*s.eye(n)[:,r]
    assert z[r]==0
    return z


def covariance(L,k,lam,Om,r):
    n=L.rows
    P=s.zeros(n);P[r,r]=1;Q=s.eye(n)-P
    ix=list(combinations(range(n),2))+[(i,i) for i in range(n)]
    xx=s.symbols('c:'+str(len(ix)))
    C=s.zeros(n)
    for (i,j),v in zip(ix,xx):C[i,j]=v;C[j,i]=v
    M=k*(L*C+C*L)+lam*(C-Q*C*Q)-Om**2/lam*P
    eq=[M[i,j] for i,j in ix]
    sol=s.solve(eq,xx,dict=True)
    assert len(sol)==1
    C=s.simplify(C.subs(sol[0]))
    assert M.subs(sol[0]).applyfunc(s.simplify)==s.zeros(n)
    return C


def test_graphs():
    examples=[(2,[(0,1,s.Rational(3,2))]),
              (3,[(0,1,1),(1,2,2)]),
              (3,[(0,1,2),(1,2,1),(0,2,3)]),
              (4,[(0,1,1),(0,2,2),(0,3,3)]),
              (4,[(0,1,2),(1,2,3),(2,3,4),(0,3,1)])]
    count=0
    for n,edges in examples:
        L=laplacian(n,edges)
        for r in range(n):
            k=s.Rational(5,3);lam=s.Rational(7,2)
            omega=s.Matrix([s.Rational(2*i+1, i+2) for i in range(n)])
            Om=sum(omega)
            z=pinned_poisson(L,omega,r,k)
            omega2=omega+s.Matrix([s.Rational(n-1 if i==r else -1,3) for i in range(n)])
            assert sum(omega2)==Om
            z2=pinned_poisson(L,omega2,r,k)
            assert k*L*(z2-z)==omega2-omega
            e=s.eye(n)[:,r];P=e*e.T
            mu=z+Om/lam*s.ones(n,1)
            assert k*L*mu+lam*P*mu==omega
            C=covariance(L,k,lam,Om,r)
            C2=covariance(L,k,lam,sum(omega2),r)
            assert C==C2
            for i in range(n):
                assert s.simplify(mu[i]-mu[r]-z[i])==0
            # Covariance must be positive semidefinite: exact principal minors.
            for sz in range(1,n+1):
                for I in combinations(range(n),sz):
                    assert C.extract(I,I).det()>=0
            count+=1
    print('PASS:',count,'rooted graph cases; anchored translation, moments and PSD.')


def test_pair():
    k,l,O=s.symbols('k l O',positive=True)
    L=laplacian(2,[(0,1,1)])
    C=covariance(L,k,l,O,0)
    den=l**2*(3*k+l)
    want=s.Matrix([[O**2*(k+l)/den,O**2*k/den],
                   [O**2*k/den,O**2*k/den]])
    assert s.simplify(C-want)==s.zeros(2)
    assert s.factor(C[0,0]+C[1,1]-2*C[0,1])==O**2/(l*(3*k+l))
    print('PASS: two-node symbolic covariance and exact relative-phase variance.')


def numerical_diagnostic():
    import math
    import numpy as np
    k=2.; lam=3.; w1=3.; w2=2.;Om=w1+w2
    rng=np.random.default_rng(17026)
    x1=x2=0.
    vals=[]
    for j in range(190000):
        t=rng.exponential(1/lam)
        mean=(x1+x2)/2+Om*t/2
        diff=(x1-x2)/2*math.exp(-2*k*t)+(w1-w2)/(4*k)*(1-math.exp(-2*k*t))
        x1,x2=mean+diff,mean-diff
        if j>=10000:vals.append((x1,x2))  # pre-reset; PASTA sampling
        x1=0.
    a=np.asarray(vals)
    actual_mean=a.mean(axis=0)
    actual_cov=np.cov(a,rowvar=False,bias=True)
    expected_mean=np.array([Om/lam,Om/lam+w2/k])
    den=lam**2*(3*k+lam)
    expected_cov=np.array([[Om**2*(k+lam)/den,Om**2*k/den],
                           [Om**2*k/den,Om**2*k/den]])
    assert np.max(np.abs(actual_mean-expected_mean))<0.04, (actual_mean,expected_mean)
    assert np.max(np.abs(actual_cov-expected_cov))<0.09, (actual_cov,expected_cov)
    print('PASS: Poisson pre-reset sample agrees with stationary mean/cov (180000 samples).')


if __name__=='__main__':
    test_graphs();test_pair();numerical_diagnostic()
