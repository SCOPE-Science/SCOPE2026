"""Exact stationary occupation-moment checks for a two-site immigration/migration model.

Requires Python 3 with SymPy, NumPy and SciPy. The finite-state calculations are
corroborating tests; the theorem's unrestricted state-space proof is analytic.
"""
import math
import sympy as sp
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from scipy.optimize import brentq


def symbolic_certificate():
    a, d, h, r = sp.symbols('a d h r', positive=True)
    k = d + r
    D = r**2 + 3*(d+h)*r + 2*d**2 + 4*d*h
    m = a/k
    U = 2*a*a*(d+r+2*h)/(k*D)
    W = a*a*(2*d+r+4*h)/(k*D)
    excess = a*a*r*(k+h)/(k**2*D)
    covariance = a*a*h*r/(k**2*D)
    P = 2*d**3 + 4*d*d*h - (2*d*d+4*d*h)*r - (7*d+6*h)*r*r - 3*r**3
    checks = {
        'mean stationary balance':a-(d+r)*m,
        'factorial moment stationary balance':2*a*m + 2*h*W-(2*d+2*h+r)*U,
        'mixed moment stationary balance':2*a*m+2*h*U-2*(d+h+r)*W,
        'variance inflation formula':U-m*m-excess,
        'cross covariance formula':W-m*m-covariance,
        'injection independent ratio':covariance/excess-h/(k+h),
        'covariance reset derivative':sp.diff(covariance,r)-a*a*h*P/(k**3*D**2),
        'covariance hopping derivative':sp.diff(covariance,h)-a*a*r*(2*d+r)/(k*D**2),
        'optimum polynomial at death rate':P.subs(r,d) +10*d**3+6*d*d*h,
        'optimum polynomial at zero':P.subs(r,0)-2*d*d*(d+2*h),
        'limit r-to-zero':sp.limit(covariance,r,0),
        'limit r-to-infinity cubic scaling':sp.limit(r**3*covariance,r,sp.oo)-a*a*h,
        'large-hop saturation':sp.limit(covariance,h,sp.oo)-a*a*r/(k*k*(3*r+4*d)),
    }
    for name, test in checks.items():
        assert sp.cancel(test) == 0, (name, test)
    return len(checks)


def truncation_check(a, d, h, r, cutoff=14):
    states = [(n, m) for n in range(cutoff+1) for m in range(cutoff+1)]
    index = {st: i for i,st in enumerate(states)}
    dim = len(states)
    gen = lil_matrix((dim,dim),dtype=float)
    for i,(n,m) in enumerate(states):
        moves=[]
        if n<cutoff: moves.append(((n+1,m),a))
        if m<cutoff: moves.append(((n,m+1),a))
        if n>0:
            moves.append(((n-1,m),d*n))
            moves.append(((0,m),r))
            if m<cutoff:moves.append(((n-1,m+1),h*n))
        if m>0:
            moves.append(((n,m-1),d*m))
            moves.append(((n,0),r))
            if n<cutoff:moves.append(((n+1,m-1),h*m))
        for dest,rate in moves:
            if rate:
                gen[i,index[dest]] += rate
                gen[i,i] -= rate
    coeff=gen.tocsr().transpose().tolil()
    coeff[-1,:]=np.ones(dim)
    b=np.zeros(dim);b[-1]=1
    probs=spsolve(coeff.tocsc(),b)
    assert abs(probs.sum()-1)<1e-11
    assert min(probs)>-1e-12
    E1=sum(p*n for (n,m),p in zip(states,probs))
    E2=sum(p*m for (n,m),p in zip(states,probs))
    E11=sum(p*n*n for (n,m),p in zip(states,probs))
    E12=sum(p*n*m for (n,m),p in zip(states,probs))
    D=r*r+3*(d+h)*r+2*d*d+4*d*h
    mu=a/(d+r)
    v=mu + a*a*r*(d+r+h)/((d+r)**2*D)
    c=a*a*h*r/((d+r)**2*D)
    for got, expected in ((E1,mu),(E2,mu),(E11-E1**2,v),(E12-E1*E2,c)):
        assert abs(got-expected)<3e-9,(a,d,h,r,got,expected)
    return 4


def optimum_check(d,h):
    def P(r):return 2*d**3+4*d*d*h-(2*d*d+4*d*h)*r-(7*d+6*h)*r*r-3*r**3
    root=brentq(P,0,d)
    assert 0<root<d
    def C(r):
        D=r*r+3*(d+h)*r+2*d*d+4*d*h
        return h*r/((d+r)**2*D)
    for q in [root/2,root*0.9,root*1.1,1.5*root,2*root,4*root]:
        assert C(root)>C(q), (d,h,root,q)
    return 7


if __name__=='__main__':
    count=symbolic_certificate()
    for params in [(1,1,1,1),(2,3,1,2),(1,2,3,1),(3,1,2,4),(1,2,1,0)]:
        count+=truncation_check(*params)
    for d,h in [(1,1),(2,1),(1,4),(3,2),(2,5)]:
        count+=optimum_check(d,h)
    print('PASS:',count,'symbolic and independent numerical assertions')
