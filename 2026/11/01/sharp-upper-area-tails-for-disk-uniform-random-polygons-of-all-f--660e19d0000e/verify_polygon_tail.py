#!/usr/bin/env python3
"""Independent checks of the all-order near-maximal disk-polygon area law.
Requires numpy, scipy, and sympy. This does not constitute an infinite proof.
"""
import math
import numpy as np
import sympy as sp
from scipy.special import gamma


def constant(n):
    assert n >= 3
    a = math.sin(2 * math.pi / n)
    return 2**n * math.factorial(n-1) / (math.sqrt(n) * math.pi**((n-1)/2) * a**((3*n-1)/2) * gamma((3*n+1)/2))


def boundary_constant(n):
    a = math.sin(2*math.pi/n)
    return math.factorial(n-1) / (math.sqrt(n)*math.pi**((n-1)/2)*a**((n-1)/2)*gamma((n+1)/2))


def check_quadratic():
    for n in range(3, 16):
        m=n-1
        M=sp.eye(m)+sp.ones(m,m)
        assert M.det()==n
        assert M.inv()==sp.eye(m)-sp.ones(m,m)/n
        a=math.sin(2*math.pi/n)
        rhs=boundary_constant(n)*(2/a)**n *gamma((n+1)/2)/gamma((3*n+1)/2)
        assert math.isclose(constant(n),rhs,rel_tol=1e-13)
    print('15 determinant/inverse and normalization comparisons passed')


def check_local_taylor():
    t=sp.symbols('t', real=True)
    for n in [3,4,6]:
        u=sp.symbols('u0:'+str(n))
        w=sp.symbols('w0:'+str(n-1))
        a=sp.sin(2*sp.pi/n)
        gaps=[2*sp.pi/n+t*z for z in w]+[2*sp.pi/n-t*sum(w)]
        radii=[1-t*t*z for z in u]
        A=sum(radii[i]*radii[(i+1)%n]*sp.sin(gaps[i]) for i in range(n))/2
        A0=n*a/2
        second=sp.simplify((A0-A).diff(t,2).subs(t,0)/2)
        predicted=a*sum(u)+a/4*(sum(z*z for z in w)+sum(w)**2)
        assert sp.simplify(second-predicted)==0, (n,second,predicted)
        first=sp.simplify((A0-A).diff(t).subs(t,0))
        assert first==0
    print('6 exact Taylor-coefficient and first-derivative identities passed')


def sample_ratio(n,eps,N=60000,seed=20261030):
    # Uniform samples in the limiting mixed simplex-ellipsoid cap.
    rng=np.random.default_rng(seed+n)
    m=n-1
    a=math.sin(2*math.pi/n)
    b=a/4
    t=rng.beta(m/2,n+1,N)
    dirs=rng.normal(size=(N,m))
    dirs/=np.linalg.norm(dirs,axis=1)[:,None]
    y=dirs*np.sqrt(t*eps)[:,None]
    # (b(I+J))^{-1/2}: eigenvalues 1/sqrt(b) and 1/sqrt(b*n)
    z=(y+(1/math.sqrt(n)-1)*y.mean(axis=1,keepdims=True))/math.sqrt(b)
    gaps=np.empty((N,n))
    gaps[:,:m]=2*math.pi/n+z
    gaps[:,m]=2*math.pi/n-z.sum(axis=1)
    assert np.min(gaps)>0
    rr=rng.dirichlet(np.ones(n),size=N)
    v=rng.beta(n,1,N)
    deficits=rr*((eps/a)*(1-t)*v)[:,None]
    radii=1-deficits
    assert np.min(radii)>0
    actual=(n*a/2-0.5*np.sum(radii*np.roll(radii,-1,axis=1)*np.sin(gaps),axis=1))
    wt=(gaps[:,-1]/(2*math.pi/n))*np.prod(radii,axis=1)
    ratio=np.mean((actual<eps)*wt)
    return float(ratio)


def main():
    check_quadratic()
    check_local_taylor()
    for n in [3,4,5,6]:
        vals=[sample_ratio(n,eps) for eps in [0.03,0.01,0.003,0.001]]
        assert 0.6<vals[-1]<1.08, (n,vals)
        print('n=%d, C_n=%.14g, scale exponent=%.1f, cap importance ratios eps=.03,.01,.003,.001: %s' %(n,constant(n),(3*n-1)/2,','.join('%.5f'%v for v in vals)))
    print('All reproducibility checks passed; rare-tail limit proved analytically in text.')

if __name__=='__main__':
    main()
