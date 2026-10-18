"""Standalone numerical checks of a Poisson resolvent on Dirichlet metric stars.
Usage: python check_star.py
Scientific checks only; finite sampling does not prove uniform inequalities.
"""
from math import sqrt, isclose
from fractions import Fraction
import random
import numpy as np

def exact_formula(lengths):
    L = sum(lengths)
    C = L / (2*sum(1/x for x in lengths))
    B = [x/2 - C/x for x in lengths]
    assert abs(sum(B)) <= 1.e-8*max(1., L)
    M = max(C + max(0.,b)**2/2 for b in B)
    return C, B, M

def independent_shooting(lengths, samples=501):
    # Determine unknown common central value by Kirchhoff flux balance.
    a = sum(lengths)/2
    b = sum(1/x for x in lengths)
    v = a/b
    allmax=0
    for x in lengths:
        y=np.linspace(0.,x,samples)
        val= -y*y/2 + (x/2 - v/x)*y + v
        allmax=max(allmax,float(np.max(val)))
    return allmax

def fe_check(lengths, nseg=10):
    # Linear FEM stiffness with Kirchhoff coupling; all leaves Dirichlet.
    # Each edge has nseg elements. Unknowns are center and arm interior nodes.
    k=len(lengths)
    N=1 + k*(nseg-1)
    A=np.zeros((N,N))
    rhs=np.zeros(N)
    for i,length in enumerate(lengths):
        h=length/nseg
        nodes=[0]+[1+i*(nseg-1)+j for j in range(nseg-1)]+[None]
        for j in range(nseg):
            a,b=nodes[j:j+2]
            for p,integral in ((a,h/2),(b,h/2)):
                if p is not None: rhs[p]+=integral
            if a is not None: A[a,a]+=1/h
            if b is not None: A[b,b]+=1/h
            if a is not None and b is not None:
                A[a,b]-=1/h
                A[b,a]-=1/h
    u=np.linalg.solve(A,rhs)
    return float(max(u)),float(u[0])

R=random.Random(20261017)
n_bounds=0
n_fem=0
for k in (3,4,5,7):
    L=3.7
    lo=L**2/(8*(k-1)**2)
    hi=L**2/8
    for j in range(250):
        ys=[10**R.uniform(-3,3) for _ in range(k)]
        lengths=[L*y/sum(ys) for y in ys]
        C,B,M=exact_formula(lengths)
        assert lo*(1+1.e-13) < M < hi*(1-1.e-13), (k,lengths,lo,M,hi)
        approximate=independent_shooting(lengths)
        assert 0 <= M-approximate < max(lengths)**2/(8*(501-1)**2)+2e-10, (M,approximate)
        n_bounds+=1
        if j < 8:
            fem,center=fe_check(lengths,10)
            assert abs(center-C)<1e-9, (center,C)
            assert 0 <= M-fem < max(lengths)**2/(8*10**2)+1e-10
            n_fem+=1
    for e in (1e-2,1e-4,1e-6):
        lengths=[e]+[(L-e)/(k-1)]*(k-1)
        M=exact_formula(lengths)[2]
        assert M>lo and M-lo<50*e*L
        lengths=[L-(k-1)*e]+[e]*(k-1)
        M=exact_formula(lengths)[2]
        assert M<hi and hi-M<50*e*L
print('PASS: random bounds and independent sampled shooting:',n_bounds)
print('PASS: independent finite-element Kirchhoff solves:',n_fem)
print('PASS: short-arm and long-arm sharp-boundary tests:',4*3*2)
for k in (3,4,5):
    L=3.
    equal=[L/k]*k
    lower=[.001]+[(L-.001)/(k-1)]*(k-1)
    upper=[L-(k-1)*.001]+[.001]*(k-1)
    print('k=',k,'inf=',L*L/(8*(k-1)**2),'eq=',exact_formula(equal)[2], 'near_inf=',exact_formula(lower)[2],'near_sup=',exact_formula(upper)[2], 'sup=',L*L/8)
