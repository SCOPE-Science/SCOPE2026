"""Reproducibility checks for a Hardy composition--differentiation edge law.

Requires Python 3, NumPy, and SciPy for the numerical eigenvalue tests.
Exact finite-dimensional quadratic-form identities use Python fractions.
Finite checks are diagnostics; the asymptotic theorem is analytical.
"""
from fractions import Fraction
import math
import itertools


def weights_rational(N, d, r):
    out=[]
    for n in range(N):
        t=math.factorial(n+d)//math.factorial(n)
        out.append(t*r**n)
    return out


def check_finite_identity():
    assertions=0
    for N,d,m,a in itertools.product((5, 7, 9),(1,2),(1,2,3),
                                      (Fraction(1,2),Fraction(1),Fraction(3,2))):
        r=Fraction(2,3)
        w=weights_rational(N,d,r)
        for variant in range(17):
            f=[Fraction(((variant+3)*i*i+2*i+variant)%13-6,variant+5) for i in range(N)]
            h=[w[i]*f[i] for i in range(N)]
            # (I+a S^m) h lives on N+m coordinates.
            g=[Fraction(0) for _ in range(N+m)]
            for i,v in enumerate(h):
                g[i]+=v
                g[i+m]+=a*v
            norm=sum(t*t for t in g)
            gradient=[Fraction(0) for _ in range(N+m)]
            for i,v in enumerate(h):
                gradient[i]+=v
                gradient[i+m]-=v
            deficit=sum(t*t for t in gradient)
            rhs=(1+a)**2*sum(t*t for t in h)-a*deficit
            assert norm==rhs
            assertions+=1
    return assertions


def numeric_norm(eps,d,m,a):
    import numpy as np
    from scipy.linalg import eigh_tridiagonal
    nmax=int(d/eps+24/math.sqrt(eps)+30*m)
    n=np.arange(nmax,dtype=float)
    b=np.ones(nmax)
    for j in range(1,d+1):
        b*=eps*(n+j)
    b*=np.exp(-eps*n)
    tops=[]
    for residue in range(m):
        v=b[residue::m]
        diagonal=(1+a*a)*v*v
        subdiagonal=a*v[:-1]*v[1:]
        if len(v)>1:
            top=eigh_tridiagonal(diagonal,subdiagonal,
                select='i',select_range=(len(v)-1,len(v)-1),
                eigvals_only=True)[0]
            tops.append(float(top))
    return math.sqrt(max(tops))


def check_first_order():
    assertions=0
    cases=((1,1,1.),(2,2,1.),(3,1,2.),(1,3,0.25),(4,2,2.))
    for d,m,a in cases:
        leading=(1+a)*(d/math.e)**d
        coefficient=(d+1)/2-m*math.sqrt(a)/(2*(1+a)*math.sqrt(d))
        previous=None
        for eps in (.02,.01,.005,.0025):
            measured=numeric_norm(eps,d,m,a)
            normalized=(measured/leading-1)/eps
            error=abs(normalized-coefficient)
            # A diagnostic tolerance, not a mathematical error bound.
            assert error < 0.12
            if previous is not None:
                assert error < previous
                assertions+=1
            previous=error
            assertions+=1
    return assertions

if __name__=='__main__':
    exact=check_finite_identity()
    numeric=check_first_order()
    print(f'exact finite quadratic-form identities: {exact} passed')
    print(f'finite-section asymptotic diagnostics: {numeric} passed')
    print(f'total: {exact+numeric} passed')
