"""Reproduce exact and numerical fastest-mixing checks for complete split graphs.

Run: python verify.py  (dependencies: numpy and scipy).
The exhaustive assertions cover the displayed finite ranges, not all graph orders.
"""
from fractions import Fraction as Q
from math import isclose
import numpy as np
from scipy.optimize import linprog


def candidate(r, m):
    assert r >= 2 and m >= 2
    if m <= 2*r:
        a = Q(2, m + 2*r)
        b_lo = max(Q(0), Q(2 * (r - m), r * (m + 2*r)))
        b_hi = Q(2*r - m, (r-1) * (m+2*r))
        mu = Q(m, m + 2*r)
    else:
        a, b_lo, b_hi, mu = Q(1,m), Q(0), Q(0), Q(m-r,m)
    return a, b_lo, b_hi, mu


def spectrum(r, m, a, b):
    return [Q(1), 1-r*a, 1-m*a-r*b, 1-(m+r)*a]


def matrix(r,m,a,b):
    n=r+m
    p=np.zeros((n,n),float)
    for i in range(r):
        for j in range(r):
            if i != j: p[i,j]=float(b)
        for j in range(r,n): p[i,j]=p[j,i]=float(a)
    for i in range(n): p[i,i]=1-sum(p[i,j] for j in range(n) if j!=i)
    return p

checks_exact = 0
checks_dense = 0
checks_lp = 0
checks_nonuniform = 0
for r in range(2,19):
    for m in range(2,35):
        a, lo, hi, mu = candidate(r,m)
        assert Q(0) <= lo <= hi
        assert m*a+(r-1)*hi <= 1
        assert r*a <= 1
        for b in (lo, (lo+hi)/2, hi):
            assert b >= 0 and 1 - m*a - (r-1)*b >= 0
            assert max(abs(x) for x in spectrum(r,m,a,b)[1:]) == mu
            checks_exact += 1
        # The capacity bound and balancing eigenvalues give the exact optimum.
        a_bal = Q(2,m+2*r)
        assert a == min(a_bal,Q(1,m))
        if m < r: assert lo > 0
        if r <= m < 2*r: assert lo == 0 and hi > 0
        if m >= 2*r: assert hi == 0
        if r <= 8 and m <= 12:
            p=matrix(r,m,a,(lo+hi)/2)
            eigen=np.linalg.eigvalsh(p)
            assert min(p.ravel()) >= -1e-12
            assert np.allclose(p.sum(axis=1), 1, atol=1e-12)
            target=sorted([1.0]+[float(1-r*a)]*(m-1)+[float(1-m*a-r*(lo+hi)/2)]*(r-1)+[float(1-(m+r)*a)])
            assert np.allclose(eigen,target,atol=3e-12)
            assert abs(max(abs(eigen[0]),abs(eigen[-2]))-float(mu))<1e-12
            checks_dense += 1
        if r <= 12 and m <= 20:
            # Minimize s with the exact invariant spectral affine inequalities.
            E=np.array([[-r,0],[-m,-r],[-m-r,0]],float)
            A=[];rhs=[]
            for x,y in E:
                A.extend(([x,y,-1],[-x,-y,-1]));rhs.extend([-1,1])
            A.extend(([m,r-1,0],[r,0,0])); rhs.extend([1,1])
            res=linprog([0,0,1],A_ub=A,b_ub=rhs,bounds=[(0,None)]*3,method='highs')
            assert res.success and isclose(res.fun,float(mu),abs_tol=1e-9)
            checks_lp+=1
            # Randomized non-invariant symmetric weights with row capacities respected.
            if r<=6 and m<=8:
                rng=np.random.default_rng(137+r*100+m)
                for _ in range(12):
                    p0=matrix(r,m,a,(lo+hi)/2)
                    q=np.zeros_like(p0)
                    for i in range(r+m):
                        for j in range(i+1,r+m):
                            if p0[i,j]>1e-14:
                                q[i,j]=q[j,i]=p0[i,j]*rng.uniform(.2,1.0)
                    for i in range(r+m):q[i,i]=1-sum(q[i,j] for j in range(r+m) if j!=i)
                    eig=np.linalg.eigvalsh(q)
                    assert max(abs(eig[0]),abs(eig[-2])) + 1e-10>=float(mu)
                    checks_nonuniform += 1
print('VERIFY_OK',f'exact_rational_cases={checks_exact}',f'dense_spectra={checks_dense}',f'linear_programs={checks_lp}',f'nonuniform_feasible_checks={checks_nonuniform}')
